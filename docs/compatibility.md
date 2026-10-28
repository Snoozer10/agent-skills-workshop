# Compatibility

The common format is a self-contained SKILL.md package with relative resources. A shared format does not standardize tools, delegation, permissions, context injection or automatic activation.

| Layer | Owner |
| --- | --- |
| Task intent, criteria and safety invariants | Skill entrypoint |
| Conditional platform procedure | Skill's focused reference |
| Discovery, installation and configuration recipe | adapters/ |
| Tested host/version and remaining limits | Catalog plus retained test evidence |

Maintain one authoritative source per instruction. Do not fork four whole skills to change installation paths. Generate host variants only when demonstrated incompatibility requires them; record transformations and test their output.

## Current state

campaign-orchestrator preserves Claude frontmatter extensions and Codex agents/openai.yaml. The repository validator accepts these as explicit host extensions; this is not a universal host-compatibility certificate.

antigravity-multiagent remains an exact Antigravity-specific import. It is not qualified for native execution in Codex, Claude or OpenCode. Its project-specific examples and API/model claims remain review work.

See [adapter recipes](../adapters/README.md) before choosing a destination. Antigravity App/IDE and CLI documentation currently name different global roots. Check the actual installed surface/version; do not infer discovery from file presence.

## Verification matrix

For each skill/host, record: source revision; host/surface/version; destination and duplicate precedence; discovery; explicit invocation; automatic activation behavior; required tool availability; representative execution; limitations.

Use unverified, verified, unavailable or unsupported precisely. Manual-only intent must be preserved. Where the host lacks a qualified enforcement control, disclose that limitation instead of silently enabling automatic use.

Official references, consulted 2026-10-28:
- [Agent Skills format](https://agentskills.io/specification)
- [Claude skill controls](https://code.claude.com/docs/en/skills)
- [Antigravity skills](https://antigravity.google/docs/skills)
- [OpenCode skills and permissions](https://opencode.ai/docs/skills/)
- Codex control evidence: the locally installed official skill-creator documentation and the imported agents/openai.yaml; runtime verification remains pending.
