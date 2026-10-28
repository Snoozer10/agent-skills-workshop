# Platform adapters

Primary documentation checked on 2026-10-28. Verify the installed host/version before relying on any interface. Protocol portability does not imply identical discovery, permissions or isolation.

## Explicit invocation

- **Codex:** agents/openai.yaml sets policy.allow_implicit_invocation to false. Invoke with $campaign-orchestrator. Confirm discovery in the actual session.
- **Claude Code:** disable-model-invocation: true and user-invocable: true retain manual use. Personal discovery normally uses ~/.claude/skills; use direct-path instructions if the canonical installation is not discovered. [Official skills documentation](https://code.claude.com/docs/en/skills).
- **Antigravity:** documents manual and automatic invocation. Global roots differ: CLI ~/.gemini/antigravity-cli/skills; App/IDE ~/.gemini/config/skills; workspace .agents/skills. The referenced docs do not establish a universal manual-only switch. Preserve the entrypoint's direct-human guard and verify native enforcement before claiming it. [Official skills documentation](https://antigravity.google/docs/skills).

The canonical ~/.agents/skills location alone does not prove cross-host discovery. Create bindings/copies only when requested; preserve provenance and avoid changing active hosts. Native metadata may be ignored by other runtimes.

Portable explicit request: “Read [absolute installed path]/SKILL.md and use campaign-orchestrator in plan mode for [goal].” For an existing campaign name its owner and whether this request preserves or transfers that role. This names a mode; it does not grant execution.

## Antigravity feature selection

For planning/setup, Teamwork or Boost choice, integrity settings, native CLI entry, headless transport and resumption, read [Antigravity planning](antigravity.md) before making recommendations. It owns the capability/decision procedure; this file owns discovery and host controls.

## Isolation and permissions

The App documents New Worktree mode for Git folders, while non-Git folders can remain shared. Project permissions inherit global settings. Verify paths/resources using [delivery](delivery.md); Teamwork folders alone prove no isolation. Avoid assuming an equivalent CLI worktree flag. [Official projects documentation](https://antigravity.google/docs/projects).

Platform restrictions apply alongside human grants; a prompt cannot bypass enforcement. Check installed permission controls rather than inventing settings. [Official permissions documentation](https://antigravity.google/docs/permissions).

Codex policy authority: the installed official skill-creator references/openai_yaml.md. Read that source when changing metadata.

No host session was launched for this revision. Metadata and document checks do not prove runtime discovery or universal user-only enforcement.
