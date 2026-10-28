# Workspace qualification and bounded delivery

Read for start/resume work that creates or uses a development workspace, dispatches workers or runs side-effecting verification. Planning proposes this boundary; read-only review does not require a new checkout.

## 1. Reuse or qualify the workspace

Inspect the relevant source without changing it: repository/root, base commit/tree, dirty/untracked inputs and applicable instructions. Inspect hidden index flags, hooks, imports, runtime paths and other shared resources where they can conceal changes or escape the intended boundary.

Prefer a suitable existing isolated workspace, then verified native isolation, then an authorized clean worktree or dedicated clone. Resolve actual top-level, Git/common/index paths, worktree metadata, links/junctions and non-Git folders. A worktree shares Git administration; a clone is not a process/data sandbox. Verify effective cwd and use explicit repository targets. A tool's silent cwd fallback fails qualification.

Transfer only allowlisted development inputs. Choose materialization that enforces exclusions before checkout hooks or imports run; reject native isolation that automatically copies protected inputs. Keep dirty overlays separate from the committed base and preserve exact preimages/hashes. Label local-only evidence and unresolved transfer holds. Production databases, credentials, authentication profiles and generated media remain outside transfer unless expressly included. Tracked operational data still requires this classification. Preserve the source checkout, rejected attempts and recovery state.

Use checks whose imports, hooks and fixtures stay within the verified boundary. If an untracked required input cannot be transferred safely, mark the affected task blocked and continue independent authorized work.

**Completion:** receipt identifies source/candidate, overlays, exclusions, effective paths and safe verification surfaces before dependent writes. Drift pauses affected work until its specific cause is understood.

## 2. Assign ready slices

Use real dependencies, not issue numbering or an old prompt sequence. Check current owners and in-flight attempts before dispatch. Parallel work needs disjoint write ownership and compatible shared resources; serialize shared contracts/indexes or designate one writer.

Use the capsule in [records](contracts.md). A subordinate native team lead can coordinate workers inside its scope; campaign ownership remains with the recorded orchestrator. Workers accommodate existing edits and return changes plus receipts. Assign Git/tracker mutations separately when permitted.

Verify installed interfaces and target sessions before invoking a tool. External dispatch requires the actual grant and applicable caps. When dispatch is unavailable, prepare one self-contained human-relay prompt with source pins, scope, allowed actions, checks and expected return. Sending a prompt or starting another session is a separate action.

**Completion:** returned candidate and meaningful checks cover the slice, with unresolved limits and next action identified. Refresh the return against current source before accepting it.

## 3. Recover without duplicating effects

Before a retry or resume, inspect running processes, assignments, locks and receipts. An unknown send, job, push or merge result is uncertain, not failed: reconcile its external identity/state before repeating it. Preserve cumulative budgets across attempts.

Apply the repository's retry brake. If none exists, stop after two unchanged failures without a new hypothesis. Preserve failed evidence and report the smallest missing input or recovery action. Changed hypotheses may justify a bounded new attempt within existing authorization.

**Completion:** one known attempt owns each live operation; recovery preserves original evidence and unrelated work.

## 4. Return at the authorized boundary

Use [verification](verification.md) for review/integration. Routine delivery may proceed through approved milestones without waiting for an optional external adviser. A required eligible reviewer or repository check remains required.

For example: a user appoints one agent as campaign lead and another as independent reviewer. The lead dispatches one scoped repair, reads its candidate receipts, obtains the required review and integrates only if permitted. A later review request to the second agent returns findings to the same lead; it neither starts a duplicate repair nor transfers ownership.
