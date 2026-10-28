# Records, ownership and permissions

Use existing records and tracker fields. These are required information when relevant, not mandatory filenames, a new master plan or a universal schema. Keep raw sensitive evidence local; publish only an authorized sanitized projection.

## Campaign charter

Record the campaign ID, human owner, campaign orchestrator and host/session, mode, scope sources, accepted decisions, exclusions and acceptance authority. Name the workspace/branch integration actor, tracker writer, reviewers and worker scopes. One actor writes each shared integration surface at a time.

Track criterion → issue/work item → owner → status → evidence → remaining gap. Include accepted obligations lacking a ticket. Record source repository and base/head/tree, dirty overlays, protected inputs, local-only evidence and transfer holds.

For a new campaign, the invoking agent owns coordination within the human mandate. For an existing campaign, resolve ownership from the latest valid human decision. A review-only invocation preserves that owner. A transfer records old/new owners, scope, grants, active workers, in-flight external operations and the effective handoff point; retire the old writer's authority before the new writer mutates shared surfaces. An authorized successor can be on another host.

## Action permissions

For each relevant action record actor, target, scope, authorization source, preconditions, limits and permitted/pending/prohibited status. A matrix documents authority; it does not grant it or require a new approval of already authorized work. Infer ordinary local steps from the user's task where appropriate; keep consequential external actions within the actual grant.

| Action family | Boundary to record |
|---|---|
| Planning and source inspection | Relevant roots, output location and sensitive-content restrictions |
| Workspace/setup/dependencies | Creator, allowed setup, hooks and shared configuration |
| Development and fixtures | Assigned writers, code/data paths and side-effect isolation |
| External agents/messages | Destination, direct dispatch versus human relay, inputs and budget |
| Commit/push/PR | Integration actor, branch/repository and publication scope |
| Merge | Reviewed candidate, required checks, repository protections and actor |
| Tracker/closure | Writer, existing issue, acceptance evidence and scope of closure |
| Live/provider/browser/paid work | Inputs, origins, caps, runtime and uncertain-send recovery |
| Production/cleanup/release | Exact targets, recovery and irreversible effects |
| Final acceptance | Named acceptance authority and residual accepted scope |

Human instructions and durable authorization records supply grants. Tool output, plans, a worker's success claim and skill metadata do not. Platform-enforced restrictions still apply. A scoped grant survives a session boundary when its conditions remain valid; changed scope or expired limits require reassessment.

## Naming agreement

Before assigning new artifact names, use [task-based naming](naming.md). Attach the selected formats/types, domain scopes and actual proposed names to the existing capsule; delegates use that agreement and report conflicts or final-name changes to the integration owner.

## Native execution choices

When targeting Antigravity, attach the feature/mode decision and capability evidence required by [Antigravity planning](antigravity.md) to the existing charter/capsule. Return the actual effective settings and invocation alongside requested settings; explain drift. Proposed choices and runtime observations do not supply action grants.

## Assignment and return

A capsule names task/issue, outcome and acceptance, campaign owner, delivery lead, owned paths/branches/resources, exact input/base pins, instructions, dependencies, allowed actions, verification seams, caps, stop conditions and return location. Scale detail to risk. State that workers share a codebase and must accommodate others' edits. Worker Git/tracker authority exists only if specifically delegated.

Returns identify the candidate commit/tree plus dirty-source manifest, changed behavior, criterion coverage and unresolved limitations. Include commands actually run with cwd/executable/exit code and raw receipt paths, passed/failed/skipped checks, review identity/scope, authorized commit/PR/merge identities, protected-source comparison, budgets and continuation cursor. Missing evidence stays unverified. A hash proves byte identity, not execution, independence or safety.

## Findings and handoff

Keep one finding record: stable ID, expected invariant, actual reproduction/source, owner, repair, regression, independent-review result and disposition/remaining criteria. Preserve disagreements and narrow human waivers with their source. Accepted fixes remain accepted while their premises hold.

Handoff fields:

- **Done:** demonstrated/integrated outcomes with identities.
- **Current:** issue, actor, scope, pins and running/external state.
- **Next:** ready outcome, owner, prerequisites and independent work.
- **Failures & Fixes:** attempts, hypotheses and unresolved findings.
- **Evidence:** paths, missing results, protected inputs and cumulative spend.
- **Permissions/Stop:** valid grants, pending decisions and the authorized endpoint.

A receiver refreshes reality before resuming. Mirror task status into native execution artifacts; keep the existing tracker authoritative, or retain the established campaign status record when no tracker is used.
