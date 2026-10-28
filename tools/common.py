"""Small shared checks; no agent execution or host configuration."""
from __future__ import annotations
import hashlib
import os
from pathlib import Path
import re
import stat
import yaml

class Problem(ValueError):
    pass

class UniqueLoader(yaml.SafeLoader):
    pass

def unique_mapping(loader, node, deep=False):
    result = {}
    for key, value in node.value:
        k = loader.construct_object(key, deep=deep)
        if k in result:
            raise Problem(f"duplicate YAML key: {k}")
        result[k] = loader.construct_object(value, deep=deep)
    return result

UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)

def load_yaml(text):
    try:
        return yaml.load(text, Loader=UniqueLoader)
    except yaml.YAMLError as exc:
        raise Problem(f"invalid YAML: {exc}") from exc

def safe_path(path):
    """Reject links/junctions in existing path components before resolving."""
    path = Path(os.path.abspath(path))
    for part in [*reversed(path.parents), path]:
        if part.is_symlink():
            raise Problem(f"linked path: {part}")
        if part.exists():
            attrs = getattr(part.lstat(), "st_file_attributes", 0)
            if attrs & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0):
                raise Problem(f"reparse path: {part}")
    return path

def manifest(path):
    path = safe_path(path)
    if not path.exists():
        return None
    if not path.is_dir():
        raise Problem(f"package is not a directory: {path}")
    result, folded = {}, set()
    for folder, directories, files in os.walk(path, followlinks=False):
        for name in directories + files:
            entry = safe_path(Path(folder) / name)
            rel = entry.relative_to(path).as_posix()
            if rel.casefold() in folded:
                raise Problem(f"case collision: {rel}")
            folded.add(rel.casefold())
            if not entry.is_file() and not entry.is_dir():
                raise Problem(f"special file: {entry}")
        for name in files:
            entry = Path(folder) / name
            result[entry.relative_to(path).as_posix()] = hashlib.sha256(entry.read_bytes()).hexdigest()
    return dict(sorted(result.items()))

def frontmatter(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise Problem(f"missing YAML frontmatter: {path}")
    try:
        end = lines.index("---", 1)
    except ValueError as exc:
        raise Problem(f"unterminated YAML frontmatter: {path}") from exc
    data = load_yaml("\n".join(lines[1:end]))
    if not isinstance(data, dict):
        raise Problem(f"frontmatter must be a mapping: {path}")
    return data

NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")

def read_catalog(root):
    data = load_yaml((Path(root) / "catalog.yaml").read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise Problem("unsupported catalog schema")
    entries = data.get("skills")
    if not isinstance(entries, list) or not entries:
        raise Problem("catalog skills must be a nonempty list")
    result = {}
    for entry in entries:
        if not isinstance(entry, dict):
            raise Problem("catalog entry must be a mapping")
        name = entry.get("name", "")
        if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64:
            raise Problem("invalid skill name")
        if name in result or entry.get("path") != f"skills/{name}":
            raise Problem(f"duplicate name or noncanonical path: {name}")
        if entry.get("role") != "maintained-skill" or entry.get("maintenance") != "first-party":
            raise Problem(f"catalog accepts first-party maintained outputs only: {name}")
        origin = entry.get("origin")
        if origin not in {"created-in-repository", "imported-existing", "upstream-derived"}:
            raise Problem(f"invalid source origin: {name}")
        if origin == "imported-existing":
            record = entry.get("origin_record")
            if not isinstance(record, str) or not record:
                raise Problem(f"imported source needs a historical origin record: {name}")
            record_path = Path(root) / record
            try:
                record_path.resolve().relative_to(Path(root).resolve())
            except ValueError as exc:
                raise Problem(f"origin record escapes repository: {name}") from exc
            if Path(record).is_absolute() or not record_path.is_file():
                raise Problem(f"missing relative origin record: {name}")
        if origin == "upstream-derived":
            upstream = entry.get("upstream")
            if not isinstance(upstream, dict) or not isinstance(upstream.get("source"), str) or not upstream["source"]:
                raise Problem(f"derived source needs upstream attribution: {name}")
        for field in ("version", "activation", "qualification"):
            if not isinstance(entry.get(field), str) or not entry[field]:
                raise Problem(f"missing {field}: {name}")
        for field in ("categories", "hosts", "limitations"):
            if not isinstance(entry.get(field), list) or not all(isinstance(v, str) and v for v in entry[field]):
                raise Problem(f"invalid {field}: {name}")
        result[name] = entry
    return result


def read_authoring_tools(root):
    data = load_yaml((Path(root) / "authoring-tools.yaml").read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        raise Problem("unsupported authoring-tools schema")
    entries = data.get("tools")
    if not isinstance(entries, list):
        raise Problem("authoring tools must be a list")
    result = {}
    for entry in entries:
        if not isinstance(entry, dict):
            raise Problem("authoring tool must be a mapping")
        identity = entry.get("id", "")
        if not isinstance(identity, str) or not re.fullmatch(r"[a-z0-9]+(?:[-:][a-z0-9]+)*", identity):
            raise Problem("invalid authoring tool identity")
        if identity in result:
            raise Problem(f"duplicate authoring tool: {identity}")
        if set(entry) - {"id", "role", "required", "purpose", "when_to_use", "source"}:
            raise Problem(f"unexpected helper fields; keep machine paths local: {identity}")
        if entry.get("role") != "authoring-helper" or entry.get("required") is not False:
            raise Problem(f"repository helpers must be explicitly optional: {identity}")
        for field in ("purpose", "when_to_use"):
            if not isinstance(entry.get(field), str) or not entry[field].strip():
                raise Problem(f"missing helper {field}: {identity}")
        source = entry.get("source")
        if not isinstance(source, dict) or set(source) != {
            "distribution", "version", "entrypoint_sha256"
        }:
            raise Problem(f"invalid helper source identity: {identity}")
        for field in ("distribution", "version"):
            if not isinstance(source.get(field), str) or not source[field].strip():
                raise Problem(f"missing helper source {field}: {identity}")
        if not re.fullmatch(r"[a-f0-9]{64}", str(source.get("entrypoint_sha256", ""))):
            raise Problem(f"invalid helper entrypoint fingerprint: {identity}")
        result[identity] = entry
    return result
