# Antigravity planning and delivery

Read **before planning Antigravity work, selecting native features, preparing setup/relay instructions, resuming its delivery, or reviewing its execution choices**. Apply the campaign's current mode and owner. This is a decision guide, not an automatic launch script.

## 1. Qualify the capabilities needed

Consult the current [CLI feature overview](https://antigravity.google/docs/features?tab=cli#antigravity-cli-features), [slash catalog](https://antigravity.google/docs/slash-commands/) and the relevant feature pages below. Read only task-relevant branches; facts here were checked on 2026-10-28 and can change.

Record surface (CLI/App/IDE), executable/version, intended project/conversation, supported invocation and required plan/entitlement. Separate **documented**, **locally observed**, **unverified** and **unavailable** capability claims from **proposed** and **authorized** actions. An executable's presence proves neither paid-feature access nor a successful invocation.

Use existing metadata and safe inspection first. A version/help probe can start a process; run it only within the setup grant. Account access, credentials, installation, global configuration and service activation stay outside passive discovery. Missing runtime access permits a qualified plan, not a claim of tested readiness.

**Done:** each selected feature has a reason, current source, availability evidence/gap and permitted fallback. Consult its dedicated official page for a feature absent from this guide; do not extrapolate from a similar command.

## 2. Choose the smallest useful workflow

| Task shape | Candidate | Decision boundary |
|---|---|---|
| Understood local task | Ordinary prompt / scoped worker | Extra orchestration should add demonstrable value |
| Unsettled requirements | /plan; targeted /grill-me | Resolve missing decisions, preserve accepted ones |
| Bounded hard bug or algorithm | /boost | Immediate work, not a planning-only shortcut |
| Sustained dependent milestones | /teamwork-preview | Phase 1 artifact, then execution within the approved grant |
| Explicitly desired continuous autonomy | /goal | Bounded outcome, budget and stop policy remain necessary |

Before proposing Boost, read [its workflow comparison and safety sections](https://antigravity.google/docs/boost/). Before proposing Teamwork, read [its phases, usage, roles, execution paths and integrity sections](https://antigravity.google/docs/teamwork/). Both currently require paid plans. State why the choice is useful and why a simpler route is insufficient.

For analysis-only Boost, specify read-only investigation and its return. Submitting any Boost request still requires authorized dispatch/budget. During an existing Teamwork attempt, assign a focused investigation through its lead; a separate overlapping Boost run needs a justified scope and compatible ownership. A native feature does not grant more files, spend or publication authority.

## 3. Set integrity separately from permissions and proof

Teamwork's [integrity modes](https://antigravity.google/docs/teamwork/#integrity-modes) regulate permitted implementation shortcuts:

| Mode | Documented constraint |
|---|---|
| development | Reuse and libraries permitted; rejects fabricated/facade results |
| demo | Additionally restricts copied core, external core delegation and test-source reverse engineering |
| benchmark | Independent implementation from scratch; standard library only |

For maintenance of an existing dependency-based project, propose development with explicit acceptance/independent verification. This is a scope-fit recommendation, not weaker proof. Choose demo/benchmark only when their restrictions match the user's purpose; incompatible restrictions require a scope decision, not a silent rewrite.

Record separately: workflow, integrity, CLI execution/permission mode, model/effort, evidence depth, cost limits and allowed actions. [CLI modes](https://antigravity.google/docs/cli/modes) control edit/command oversight; they are not integrity settings. The human supplies grants; the orchestrator allocates work inside them. Map integrity in the Phase 1 artifact rather than inventing a CLI flag. Preserve existing settings unless change is authorized.

**Done:** selected mode, allowed reuse, excluded shortcuts and required proof are explicit and mutually compatible.

## 4. Prepare the native entry and Phase 1 return

For interactive CLI, supply the slash command as text for the **Antigravity TUI prompt**, not PowerShell. Use the [CLI reference](https://antigravity.google/docs/cli/reference/) for actual startup flags and local support. For Teamwork the entry is /teamwork-preview followed by the bounded brief. Explain where to submit it; do not assume a shell subcommand or direct control tool exists.

The relay includes real brief/input paths, verified source/base, qualified workspace or proposed target with setup holds, campaign and delivery owners, accepted criteria, protected data, exclusions, action grants, caps, stop point and required return. Reuse the accepted capsule in [records](contracts.md), including its [naming agreement](naming.md), not a competing master plan. Explicitly name Phase 1 only when execution is pending.

Require Phase 1 to return: reconciled scope and actual blockers; proposed workspace and observed transfer findings/qualification holds; feature and integrity choices with rationale; milestone ownership/dependencies; criterion-to-check plan; permission gaps; and one identified prompt artifact. Review that artifact against accepted requirements before Phase 2. A valid execution grant can be reused; a planning-only grant ends at the artifact. Native approval controls still apply.

When no delivery workspace exists, propose its path and the bounded creation/transfer procedure from [delivery](delivery.md). Phase 1 can leave setup unperformed. Execute qualification only under the setup grant, before dependent imports or writes; a plan is not proof of isolation.

Teamwork's Critic, Challenger, Auditor and Success Auditor cover review, adversarial testing, integrity checks and final verification; its orchestrators may hand off to successors. Request the needed independent outcomes and receipts; do not assume every role ran or claim fixed native team composition. Native success claims still undergo the campaign's [verification](verification.md).

**Done:** relay is self-contained and the next actor/action is clear; no execution occurs merely because a plan or artifact exists.

## 5. Select transport, inspect and resume deliberately

[Headless CLI](https://antigravity.google/docs/cli/headless) offers print/JSON output and streaming input. TUI support does not prove headless protocol support: some CLI-handled slash commands cannot be sent through streaming input, and interactive controls/approvals are not generally interchangeable. Verify the exact feature/transport and permitted error handling before scripting. A blocked approval is not a reason to widen permissions. Prefer the human relay when direct control cannot be qualified.

Use [CLI controls](https://antigravity.google/docs/cli/reference/) selectively: /agents and /tasks for activity, /artifact and /diff for review, /context and /usage or /credits for limits, /skills for discovery. Inspect model/effort and permission settings as needed; mutation requires the relevant grant. Check commands in the installed interface rather than copying this list as a runnable script.

For /resume or a conversation-ID startup, confirm intended session, effective project and workspace; resumption can restore that conversation's project. [Project behavior](https://antigravity.google/docs/projects) must be reconciled with the pinned campaign, not inferred from the shell cwd. Recheck running workers and cumulative budgets before another attempt.

Remote control, schedules, plugins, new rules, added directories and broadened permissions are separate persistent/external actions. Consider them only when the task calls for them; obtain missing grants rather than treating “use CLI features” as blanket approval.

**Done:** record actual invocation/target, observed effective mode, receipts and unresolved host limits. Preserve the [delivery recovery](delivery.md) and campaign ownership rules.
