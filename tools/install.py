"""Preview/install a catalog skill, or restore a trusted local receipt."""
from __future__ import annotations
import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import uuid
from common import Problem, manifest, read_catalog, safe_path

ROOT = Path(__file__).resolve().parents[1]

def write_record(path, data):
    pending = path.with_suffix(".pending")
    with pending.open("w", encoding="utf-8", newline="\n") as stream:
        json.dump(data, stream, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(pending, path)

def read_record(path):
    return json.loads(safe_path(path).read_text(encoding="utf-8"))

def disjoint(a, b):
    if a == b or a in b.parents or b in a.parents:
        raise Problem(f"overlapping source, state or discovery roots: {a}, {b}")

@contextmanager
def writer_lock(state, target):
    locks = safe_path(state / "locks")
    locks.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha256(str(target).casefold().encode()).hexdigest()
    path = locks / f"{key}.lock"
    try:
        with path.open("x", encoding="utf-8") as stream:
            stream.write(f"pid={os.getpid()}\ntarget={target}\n")
    except FileExistsError as exc:
        raise Problem(f"writer lock exists; reconcile live/stale owner: {path}") from exc
    try:
        yield
    finally:
        path.unlink()

def check_layout(root, target_root, state):
    source_root = safe_path(root / "skills")
    for a, b in ((source_root, target_root), (source_root, state), (state, target_root)):
        disjoint(a, b)

def install(root, name, target_root, state, *, apply=False, adopt=False, previous_receipt=None):
    root = safe_path(root)
    from validate import validate
    validate(root)
    entry = read_catalog(root)[name]
    source = root / entry["path"]
    wanted = manifest(source)
    if not wanted or "SKILL.md" not in wanted:
        raise Problem("source package is incomplete")
    target_root, state = safe_path(target_root), safe_path(state)
    check_layout(root, target_root, state)
    target = target_root / name
    before = manifest(target)
    if before is not None:
        if previous_receipt:
            prior = read_record(previous_receipt)
            if (prior.get("status") != "installed" or safe_path(prior["target"]) != target
                    or before != prior["candidate"]):
                raise Problem("previous receipt does not describe the current installation")
        elif not (adopt and before == wanted):
            raise Problem("unmanaged or modified destination; exact adoption or previous receipt required")
    plan = {"operation": "install", "target": str(target), "before": before,
            "candidate": wanted, "apply": apply}
    if not apply:
        return plan
    state.mkdir(parents=True, exist_ok=True)
    with writer_lock(state, target):
        if manifest(source) != wanted or manifest(target) != before:
            raise Problem("source or target changed after preview")
        ident = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex
        receipt_dir = state / ident
        receipt_dir.mkdir()
        candidate = receipt_dir / "candidate"
        shutil.copytree(source, candidate)
        if manifest(candidate) != wanted or manifest(source) != wanted:
            raise Problem(f"candidate copy/source changed; retained: {receipt_dir}")
        receipt = receipt_dir / "receipt.json"
        record = {**plan, "schema_version": 1, "status": "prepared"}
        write_record(receipt, record)
        target_root.mkdir(parents=True, exist_ok=True)
        if target_root.stat().st_dev != receipt_dir.stat().st_dev:
            raise Problem(f"state and target must share a filesystem; retained: {receipt}")
        if manifest(target) != before:
            raise Problem("target changed before replacement")
        if before is not None:
            os.replace(target, receipt_dir / "previous")
        record["status"] = "previous-preserved"
        write_record(receipt, record)
        os.replace(candidate, target)
        if manifest(target) != wanted:
            raise Problem("installed package hash mismatch")
        record["status"] = "installed"
        write_record(receipt, record)
        return {**record, "receipt": str(receipt)}

def restore(receipt, *, apply=False):
    receipt = safe_path(receipt)
    record = read_record(receipt)
    if record.get("schema_version") != 1:
        raise Problem("unsupported receipt schema")
    folder = receipt.parent
    state = safe_path(folder.parent)
    target = safe_path(record["target"])
    disjoint(state, target.parent)
    before, wanted = record["before"], record["candidate"]
    current = manifest(target)
    previous = folder / "previous"
    if current == before and manifest(previous) is None:
        if apply:
            with writer_lock(state, target):
                if manifest(target) != before:
                    raise Problem("target changed before marking restored")
                record["status"] = "restored"
                write_record(receipt, record)
        return {"operation": "restore", "target": str(target), "already_original": True}
    if current is not None and current != wanted:
        raise Problem("installed content drift; restoration refused")
    if before is not None and manifest(previous) != before:
        raise Problem("preserved original missing or changed")
    if before is None and manifest(previous) is not None:
        raise Problem("unexpected preserved original")
    plan = {"operation": "restore", "target": str(target), "apply": apply}
    if not apply:
        return plan
    with writer_lock(state, target):
        if manifest(target) != current or (before is not None and manifest(previous) != before):
            raise Problem("state changed before restoration")
        removed = folder / "removed"
        if current is not None:
            if removed.exists():
                raise Problem("previous removal evidence exists; reconcile receipt")
            os.replace(target, removed)
        if before is not None:
            os.replace(previous, target)
        if manifest(target) != before:
            raise Problem("restored state hash mismatch")
        record["status"] = "restored"
        write_record(receipt, record)
    return {**plan, "status": "restored"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    put = commands.add_parser("install")
    put.add_argument("--skill", required=True)
    put.add_argument("--target-root", type=Path, required=True)
    put.add_argument("--state-root", type=Path, default=ROOT / ".runtime" / "installs")
    put.add_argument("--adopt-existing", action="store_true")
    put.add_argument("--previous-receipt", type=Path)
    put.add_argument("--apply", action="store_true")
    back = commands.add_parser("restore")
    back.add_argument("--receipt", type=Path, required=True)
    back.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "install":
            result = install(ROOT, args.skill, args.target_root, args.state_root,
                             apply=args.apply, adopt=args.adopt_existing,
                             previous_receipt=args.previous_receipt)
        else:
            result = restore(args.receipt, apply=args.apply)
        print(json.dumps(result, indent=2))
    except (Problem, OSError, KeyError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
