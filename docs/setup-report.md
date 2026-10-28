# Initial setup report

Date: 2026-10-28. Scope: agent-skills-workshop only.

## Delivered

- Cloned the existing empty private remote into the user-created local folder.
- Imported campaign-orchestrator v1.3.0 (9 files) and antigravity-multiagent (1 file) byte-for-byte.
- Recorded historical source paths, sizes and SHA-256 values in [the import receipt](imports/2026-10-28.json).
- Added a shallow catalog, source ownership, authoring guidance, host adapter recipes and a starter template.
- Added Python structural validation and an explicit installer with preview, drift protection, retained preimages and interrupted-operation restoration.
- Configured Windows/Linux GitHub Actions with read-only repository permissions. Action revisions were resolved from the official repositories' v7 tags during setup.

## Observed checks

Using the repository-local Python 3.11 environment with pinned PyYAML 6.0.3:

- `python tools/validate.py`: passed for both skills. Checks catalog, metadata, relative inline-link destinations/case and declared activation controls.
- `python -m unittest discover -s tests -p "test_*.py" -v -f`: 28 tests passed, none skipped.
- `python tools/install.py --help`: passed.
- Public CLI fixture: preview left files unchanged; install copied exact package bytes; restore removed the first-time installation from discovery while retaining evidence.
- Fault-injection fixtures: interrupted install and interrupted restore recovered the previous bytes.
- Both source installations still matched their imported copies after setup.
- Full staged whitespace check: one inherited trailing blank line at the end of antigravity-multiagent/SKILL.md (line 147). Preserved for byte-exact import; no content correction authorized in this setup batch. Authored-file whitespace check passed.

Raw local commands and outputs are retained under ignored `.local/setup/`. The structural validator intentionally does not claim anchor validation, remote-link availability, host discovery or behavioral-agent proof.

## Review and remaining qualification

Standards: source and deployment are separated; skill packages retain their original bytes and invocation controls; private evaluation state and the local Python environment are ignored. Installer recovery uses retained directory moves and rejects drift. It is recoverable, not a continuously atomic directory exchange.

Specification: the agreed initial repository structure, faithful imports, catalog, compatibility guidance, focused validation and reversible installation are present.

The Antigravity-specific package still needs an audit of native API/model claims, project-specific examples and activation policy. The campaign package's independent behavioral evaluation and each host's discovery/invocation trial remain unrun. These are recorded limitations, not passed checks.

No live agent, global installation or unrelated project/worktree was modified. No commit, push, issue publication or remote CI run belongs to this local setup result. The reviewed local index is prepared for an initial commit; publishing remains a separate next action.

Licensing and external provenance review remain prerequisites for public distribution.
