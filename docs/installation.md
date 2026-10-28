# Installation and recovery

Use Python 3.11+ with requirements-dev.txt installed. Examples below use `python` for that interpreter.

## Preview

```powershell
python tools/install.py install --skill campaign-orchestrator --target-root "$HOME/.agents/skills"
```

Default operation is read-only. It reports source hashes, destination state and any adoption/drift conflict. The tool copies the source package unchanged; it does not convert host metadata or verify host discovery.

## Apply

Add `--apply` after reviewing the preview. State defaults to this repository's ignored `.runtime/installs/`. Use one state directory and one writer per destination. The state directory must be outside discovery roots and on the same filesystem as the destination for directory moves.

An existing unmanaged installation is protected. `--adopt-existing` allows adoption only if its bytes exactly match the source package. For subsequent updates, supply `--previous-receipt PATH/receipt.json`; the target must still match that receipt's installed manifest. Drift requires review, not an overwrite flag.

Apply preserves any existing package in a unique receipt directory before replacing it. The receipt retains candidate identity, original bytes and hashes, physical target and operation phase. Installation is a recoverable two-move operation: a process crash may temporarily leave the destination absent. This is not a continuously atomic directory exchange.

## Restore

```powershell
python tools/install.py restore --receipt PATH/receipt.json
python tools/install.py restore --receipt PATH/receipt.json --apply
```

Restore previews first, rejects intervening edits, verifies preserved bytes and moves the previous package back. A first-time installation is removed from discovery by moving it into retained receipt evidence. Nothing is recursively deleted by the tool.

A repeated restore is safe when the recorded original state is already present. Interrupted install/restore receipts can recover the old state, subject to drift checks. Receipt storage is trusted local administrative evidence; do not use untrusted receipts.

A stale lock after process death requires confirming that no writer remains before manually removing that specific lock. Never clear a live writer's lock. Keep receipts until the installed revision and recovery obligation are retired deliberately.

Existing .local/ receipts remain at their recorded paths and can still be restored explicitly. No migration or cleanup is performed. See [runtime guidance](runtime.md).

## Limits

Links/junctions and special files in packages or traversed control paths are rejected. File bytes and paths are preserved; ACLs, alternate data streams and empty directories are not part of the manifest guarantee. Installation does not launch an agent, change configuration, resolve duplicate skills or grant permissions.
