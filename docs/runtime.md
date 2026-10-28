# Local runtime workspace

.runtime/ stores local attempts and installer receipts. Only [.runtime/AGENTS.md](../.runtime/AGENTS.md) is tracked; payloads and machine paths are ignored.

## Current uses

- attempts/<unique-task-id>/: purpose, exact preimages, candidate identity, raw checks, outcome and next action.
- installs/: new installation receipts, preserved original packages and recovery state.
- authoring-tools.local.yaml: optional machine-specific resolutions for IDs in [authoring-tools.yaml](../authoring-tools.yaml).

Choose an existing applicable attempt before creating a new one. A record should explain what is complete, what failed, what remains and how to resume; no universal packet schema or generated index is required.

The installer defaults new state to .runtime/installs/. Existing .local/ setup evidence remains historical and existing receipts remain usable by their exact paths. Nothing is moved or removed automatically.

Ignored data is not backed up by Git. Retain recovery receipts and preimages in an appropriate separate backup when their loss matters. Keep secrets and production state outside the workshop.

Classification and retention notes are not permission to clean up. Inspect ownership, references and restoration needs before proposing any retirement.
