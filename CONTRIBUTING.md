# Contributing

1. Read [AGENTS.md](AGENTS.md) and [docs/authoring.md](docs/authoring.md).
2. Choose one observable outcome and identify affected skills, resources and hosts.
3. Use a task branch such as `docs/authoring-guide`, `fix/manual-activation` or `feat/evidence-review`. Reuse an existing issue identifier when one exists; do not create issues just to name branches.
4. Preserve source provenance and invocation settings. Keep host-specific mechanisms in the relevant reference or adapter.
5. Run the README checks and relevant behavioral scenarios. Record unrun checks plainly.
6. Review Standards (clarity, maintainability, permissions) and Specification (accepted behavior) separately.
7. Commit only the reviewed scope. Publish, merge and install only within the user's current grant.

Use independent agent evaluation where it adds confidence and is permitted. Self-review and deterministic tests must not be presented as independent agent review.

Versions belong to individual skills. Bump a skill's declared version and catalog entry together when changing its behavior; imported unversioned packages remain marked unversioned until a reviewed revision establishes a version.

Before registering a maintained skill or an external helper, follow [ownership and helper guidance](docs/authoring-tools.md). Store local attempt evidence under [.runtime/](docs/runtime.md).

## Licensing and public evidence

Contribute material you have permission to distribute under the applicable terms. Record the upstream source, revision and required notices for adaptations; using an authoring helper does not transfer ownership of its contents. See [third-party notices](THIRD_PARTY_NOTICES.md).

Keep examples and fixtures portable and sanitized. Review commit metadata, history and workflow output before publishing private work. Preserve honest experimental and compatibility labels until supporting evidence exists.
