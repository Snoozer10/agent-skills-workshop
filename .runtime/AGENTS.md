# Runtime records

This directory owns local work attempts, exact preimages, check outputs and installation receipts. The root workshop contract still applies.

- Before continuing a task, inspect its existing attempt and next action. Reuse verified work and retain failed evidence.
- Use attempts/<unique-task-id>/ for bounded task records; keep purpose, input identity, checks, remaining work and next action together.
- Use installs/ for new installer receipts. Retain each receipt and preserved original while recovery may be needed.
- authoring-tools.local.yaml maps external helper IDs to this machine's locations. It is local configuration, not proof of host discovery or permission to invoke a helper.
- Keep runtime payloads ignored. This AGENTS.md is the only tracked file in this directory.
- Preserve existing .local/ evidence and receipts where they already live. No automatic migration, cleanup or deletion follows from creating .runtime/.
- Runtime records do not override accepted requirements, tracker status or user grants. Do not store credentials, production databases or generated media here.
