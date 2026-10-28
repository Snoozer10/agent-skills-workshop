# Task-based naming

Read before assigning new branches, worktree aliases, commits, tickets, PRs or operational comment headings. The orchestrator chooses one naming agreement and passes it to every delegate.

## 1. Establish the agreement

Use **task purpose**, not agent/vendor identity: feat, fix, docs and similar meaningful types. Actor prefixes such as codex/, antigravity/ or claude/ are outside this naming policy. Keep actor identity in owner/provenance fields and actual Git authorship.

Inspect applicable human instructions, repository naming guidance, issue forms and existing commit/PR validation or release configuration. Adopt compatible task-based conventions already in use; use the defaults below when none exists. An actor-based default yields to this agreement. A binding higher-priority or mechanically enforced namespace is a concrete constraint: propose a supported alternative and hold only the affected action rather than silently publishing a disallowed name or bypassing enforcement. An ordinary default is not a reason to ask again.

Record allowed types/aliases, artifact formats, domain scopes, existing issue-ID convention, collision handling and relevant automated checks in the existing charter/capsule. This is a decision record, not permission to install hooks, change repository rules or retitle published work.

**Done:** the integration owner and delegates have the same approved formats and understand any actual enforcement conflict.

## 2. Classify the outcome

Choose the smallest accurate type from the accepted task and final change. Use repository-approved aliases consistently; the following are defaults, not a universal external standard:

| Type | Meaning |
|---|---|
| feat | New user/application capability |
| fix | Correct defective behavior |
| refactor | Restructure while preserving behavior |
| docs | Documentation, specification or guidance |
| test | Tests/fixtures as the deliverable |
| perf | Performance improvement |
| build | Build, dependency or packaging mechanics |
| ci | CI pipeline or automation |
| style | Formatting without behavior change |
| chore | Other maintenance; describe its actual purpose |
| revert | Intentional reversal of an earlier change |

A feature may include tests without becoming a test task; a bug fix stays fix. A documentation-only proposal is not the implementation it proposes. For mixed work, name the coherent deliverable; split independently valuable scopes only when their ownership/acceptance warrants it. Revise an unmerged PR's proposed title when its final purpose changes, within publication authority.

Commit types other than feat/fix are an agreed convention; [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) does not mandate this entire taxonomy.

## 3. Apply the format for the artifact

| Artifact | Default format / rule |
|---|---|
| Branch | type/existing-id-short-slug; omit the ID when no tracker item exists |
| Worktree alias/folder | type-existing-id-short-slug; record actual path separately |
| Commit | type(optional-domain-scope): imperative summary |
| Bounded issue / PR title | type(optional-domain-scope): concrete outcome |
| Campaign / decision parent | Campaign: objective or Decision: question, rather than a misleading implementation type |
| Operational comment | Plan, Progress, Review, Verification, Blocked or Handoff heading, followed by task link and accurate content |

Use short lowercase hyphenated branch/folder slugs; use the repository's real domain terms for scopes. Domain scopes identify affected subsystems rather than the agent doing the work. A normal conversational reply needs no forced machine-style prefix.

Commit/PR syntax is not branch syntax. Add a breaking marker/footer only for a real breaking change and follow the repository's release rules. Do not change SemVer/release tooling to accommodate the profile. Issue labels/statuses remain separate tracker fields; creating labels, closing issues or publishing comments still requires the relevant grant. Related references need not be closing directives.

**One illustrative task** (synthetic issue #123):

- Branch: fix/123-empty-input
- Worktree alias: fix-123-empty-input
- Commit: fix(parser): handle empty input without crashing
- Issue/PR: fix(parser): handle empty input without crashing
- Comment heading: Verification — #123; body identifies the candidate, checks actually run and remaining limits.
- Owner metadata: actual integration actor and reviewer, with truthful provenance.

These are naming examples, not claims that an issue or verification exists.

## 4. Validate and preserve identity

Validate each proposed Git branch with [git check-ref-format --branch](https://git-scm.com/docs/git-check-ref-format), using a safely passed argument. This checks Git syntax, not task semantics. Inspect known local/remote refs and target-filesystem case collisions and reuse a suitable existing task branch. If necessary, use a meaningful slice suffix; avoid actor-based uniqueness and fabricated issue numbers. Unknown remote state remains a qualification gap, not proof of uniqueness.

For concurrent slices, name the scope (for example fix/123-empty-input and fix/123-error-location), assign one owner each and keep the established parent issue. Do not create duplicate tickets just to obtain branch names.

Check commit/squash/PR titles against existing configured validation when applicable. Review naming against the actual diff and task; a valid prefix does not prove acceptance. Operational comments must distinguish proposed, verified, integrated and blocked facts.

Apply this agreement to **new names**. Preserve existing branches, published PR/issue identities, commit history, author attribution and immutable receipt paths. Rename/retitle/rewrite only when separately authorized, accounting for consumers and automation. Provider-owned opaque IDs remain exact; an optional semantic alias does not replace their physical identity.

**Done:** proposed artifacts match task purpose and the naming agreement, pass applicable checks, and preserve existing identities. Record the selected names in the assignment/return.
