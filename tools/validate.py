"""Validate package structure, local destinations and declared host controls."""
from __future__ import annotations
import argparse
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
from common import Problem, frontmatter, load_yaml, manifest, read_catalog, read_authoring_tools

LINK = re.compile(r"(?<!!)\[[^\]\n]+\]\(([^)\n]+)\)")
ALLOWED = {
    "name", "description", "license", "compatibility", "metadata", "allowed-tools",
    # Recognized host extensions, not a universal portability certificate.
    "disable-model-invocation", "user-invocable",
}

def local_links(page, boundary):
    errors = []
    # Inline links outside fenced examples; no anchor/network validation claim.
    fence = chr(96) * 3
    text = re.sub(r"(?ms)^" + fence + r".*?^" + fence + r"[^\n]*", "", page.read_text(encoding="utf-8"))
    for raw in LINK.findall(text):
        target = raw.split('"', 1)[0].strip().strip("<>")
        parts = urlsplit(target)
        if parts.scheme or parts.netloc or not parts.path:
            continue
        decoded = unquote(parts.path)
        dest = page.parent / decoded
        try:
            dest.resolve().relative_to(boundary.resolve())
        except ValueError:
            errors.append(f"{page}: link escapes boundary: {target}")
            continue
        if not dest.exists():
            errors.append(f"{page}: missing local link: {target}")
            continue
        # Preserve authored case: Path.resolve() may normalize it on Windows.
        import os
        authored = Path(os.path.abspath(dest)).relative_to(Path(os.path.abspath(boundary)))
        cursor = boundary
        for component in authored.parts:
            if component not in {p.name for p in cursor.iterdir()}:
                errors.append(f"{page}: wrong-case local link: {target}")
                break
            cursor /= component
    return errors

def validate(root):
    root = Path(root)
    catalog = read_catalog(root)
    helpers = read_authoring_tools(root)
    if set(catalog) & set(helpers):
        raise Problem("maintained skills and external helpers share an identity")
    actual = {p.name for p in (root / "skills").iterdir() if p.is_dir()}
    if actual != set(catalog):
        raise Problem("catalog and skill directories differ")
    errors = []
    for name, entry in catalog.items():
        package = root / entry["path"]
        manifest(package)
        fm = frontmatter(package / "SKILL.md")
        if set(fm) - ALLOWED:
            errors.append(f"{name}: undeclared frontmatter extension")
        if fm.get("name") != name:
            errors.append(f"{name}: frontmatter name mismatch")
        desc = fm.get("description")
        if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
            errors.append(f"{name}: invalid description")
        version = fm.get("metadata", {}).get("version", "unversioned")
        if version != entry["version"]:
            errors.append(f"{name}: catalog version mismatch")
        for page in package.rglob("*.md"):
            errors.extend(local_links(page, package))
        if entry["activation"] == "explicit-only-intent":
            if fm.get("disable-model-invocation") is not True:
                errors.append(f"{name}: missing Claude explicit-only control")
            metadata = package / "agents" / "openai.yaml"
            if metadata.exists():
                data = load_yaml(metadata.read_text(encoding="utf-8"))
                if data.get("policy", {}).get("allow_implicit_invocation") is not False:
                    errors.append(f"{name}: missing Codex explicit-only control")
    for folder in ("docs", "adapters"):
        for page in (root / folder).rglob("*.md"):
            errors.extend(local_links(page, root))
    for name in ("README.md", "AGENTS.md", "CONTRIBUTING.md"):
        errors.extend(local_links(root / name, root))
    runtime_contract = root / ".runtime" / "AGENTS.md"
    if runtime_contract.exists():
        errors.extend(local_links(runtime_contract, root))
    if errors:
        raise Problem("\n".join(errors))
    return {"skills": len(catalog), "authoring_tools": len(helpers),
            "checks": "catalog ownership/origin, helper provenance, frontmatter, package files, local link destinations/case, declared controls",
            "not_proven": "anchors, remote URLs, host discovery, behavioral or live-agent execution"}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        print(validate(args.root))
    except (Problem, OSError, TypeError, AttributeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
