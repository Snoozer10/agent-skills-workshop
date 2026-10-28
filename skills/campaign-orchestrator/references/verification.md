# Review, correction and integration

Read for review/closeout or before corrective acceptance and integration. Apply only checks relevant to the accepted slice and its risks.

## Establish the candidate

Read accepted criteria, exceptions, actual changes and meaningful tests. Record exact base/head/tree plus hashes for relevant uncommitted inputs. Report/test source must match the candidate. Review can inspect existing sources; checks that might write require an isolated approved surface.

Report **Standards** against applicable repository contracts and **Specification** against each criterion separately. Identify reviewer and reviewed source. Self-checks remain self-checks. If independent review is required but unavailable, use an authorized eligible alternative or return review-ready with the gap. Optional advisory review is not a new gate.

## Verify behavior

Start with the original counterexample, then vary inputs and interruption points around the same invariant. Exercise the public seam and necessary consumers. A helper-level happy path or a literal canary repair does not establish the downstream requirement.

Reuse valid evidence. Rerun checks when source/environment/input changes or a concrete failure/gap justifies it. Distinguish fixtures, local process/library integration, live external execution and human editorial acceptance. Record skipped checks and approved substitutions honestly; an offline waiver does not create live evidence.

| Relevant risk | Evidence to seek |
|---|---|
| Sensitive diagnostics | Unlabelled/nested private content and credential tails absent from displayed/new summaries; required original exceptions and raw history preserved |
| Observation/non-mutation | Real isolated I/O, sidecars/close effects, races and transient or attempted writes; final hash equality alone is insufficient |
| Evidence-derived records | Physical identity/digests, examined ranges, suitable modality, rationale/contradictions and owner overrides; immutable versions and validated pointers |
| Archive/recovery | Ownership/live-use classification, interrupted operations, reused IDs, conflicts, retries and physical-state restoration without overwritten receipts |
| Shared authority/cutover | Isolated competing processes/checkouts, stale holders/fences, incompatible clients and damaged authorities; complete declared recovery set before real cutover |
| Compatibility/packaging | Real public imports/launchers, consumer behavior and built resources for the changed surface |
| Documentation/skill discovery | Candidate-tree paths/anchors; public readback after integration; fresh-host discovery/invocation only when authorized and supported |

These branches are diagnostic choices, not a mandatory suite for every campaign.

## Correct and integrate

Maintain the existing finding record. Classify severity by observed impact. A disputed finding needs a concrete reproduction and visible differing interpretations. Independently recheck required invariants and affected consumers after repair; acceptance applies only to demonstrated criteria.

Freeze review source. A new candidate or shared-file drift triggers review of its delta and affected integration, while still-valid evidence remains usable. Before integration refresh exact head, changed files, required checks, unresolved blockers and authorization. Check new artifact names against the assigned [naming agreement](naming.md) and actual diff. Stage/commit only assigned changes. Follow repository protections and eligible-review rules; an internal audit does not impersonate a platform approval.

Merge only within the recorded grant. Read back the resulting default-branch tree and relevant public routes, record merge identity and update the bounded handoff. Keep publication or integration pending when authorization is absent.

## Closeout

Account for every accepted obligation, including uncovered requirements with no child issue. Separate complete, partial, failed, deferred/waived and unverified outcomes. A merged PR or closed child list is not final acceptance. Recommend closure only for fully demonstrated scopes, through the named acceptance authority. Keep recovery evidence and useful workspaces unless their exact disposal is authorized.
