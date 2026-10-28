# Agent Skills Workshop

Create, evaluate and maintain agent skills from one reviewed source repository.

## Start here

- [Setup report](docs/setup-report.md): completed checks and remaining qualification.
- [Catalog](catalog.yaml): skill categories, declared versions and validation limits.
- [Authoring helpers and ownership](docs/authoring-tools.md): external tools versus maintained outputs.
- [Local runtime](docs/runtime.md): attempts, evidence and recovery receipts.
- [Authoring](docs/authoring.md): the development and review workflow.
- [Compatibility](docs/compatibility.md): portable instructions versus host-specific behavior.
- [Installation and recovery](docs/installation.md): explicit, reversible deployment.
- [Contributing](CONTRIBUTING.md): branch conventions and focused checks.

## Current collection

| Skill | Purpose | Current qualification |
| --- | --- | --- |
| [campaign-orchestrator](skills/campaign-orchestrator/SKILL.md) | Campaign ownership, coordination, delivery and acceptance | Imported v1.3.0; host behavior and independent agent evaluation remain unverified |
| [antigravity-multiagent](skills/antigravity-multiagent/SKILL.md) | Antigravity-native delegation guidance | Exact unversioned import; API/model claims and project-specific examples need audit |

The [initial import receipt](docs/imports/2026-10-28.json) preserves source identities and per-file SHA-256 values. Existing installed skills were copied, not moved or updated.

## Local checks

Requires Python 3.11 or later. In PowerShell, from this repository:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe tools/validate.py
.\.venv\Scripts\python.exe -m unittest discover -s tests -p "test_*.py" -v -f
```

Structural validation does not prove skill behavior or host discovery. Agent evaluations can consume quota and require a separate bounded execution scope.

## Source and installation

Edit maintained source under `skills/`. External authoring helpers are registered separately in `authoring-tools.yaml` and are not installable outputs. [Adapter recipes](adapters/README.md) describe how to select host destinations. Installation starts with a dry run and never changes host configuration automatically.

This repository is a skill collection with small maintenance tools. It does not launch agents, coordinate a live campaign, or grant publication permissions.

## Distribution

Repository visibility was verified private at setup. Licensing and third-party provenance need review before public distribution. No blanket license has been assigned to imported material.
