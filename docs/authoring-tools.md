# Maintained skills, authoring helpers and installations

These are separate roles, not mutually exclusive filesystem locations.

| Record | Responsibility |
| --- | --- |
| catalog.yaml | Maintained, installable skill source under skills/ |
| authoring-tools.yaml | External tools that help author or evaluate source |
| Runtime installation receipt | Actual deployed copy, bytes and recovery state |

## Maintained source

A catalog entry declares role: maintained-skill and maintenance: first-party. This identifies workshop maintenance responsibility, not a legal conclusion about copyright.

origin distinguishes created-in-repository, imported-existing and upstream-derived. Imported skills name an existing origin_record; adaptations identify an upstream source. Creating a skill outside this repository does not make it an external helper.

Both initial skills are first-party maintained imports. Their historical import receipt remains unchanged. Their current source can evolve through reviewed revisions.

## External helpers

The three registered helpers remain externally authored. Their source identities, recorded versions and entrypoint fingerprints support reproducibility; an entrypoint fingerprint does not cover the full plugin or establish behavior.

Helpers are optional at the repository level. Select them according to the actual task, current human invocation and host availability. They do not become runtime dependencies or get bundled into every maintained skill.

Their instructions cannot expand user grants or override host restrictions. Where a helper requests unavailable execution, disclose the limitation and the resulting evaluation gap. Do not claim that file presence establishes invocation or that a checklist establishes behavioral proof.

Machine locations can be recorded in ignored .runtime/authoring-tools.local.yaml. Resolve against the recorded source identity and disclose version/hash drift before relying on changed guidance. That map is not read or executed by the installer; no helper is automatically launched or installed.

CI validates the portable manifest without requiring this workstation's plugin cache. A missing optional helper does not block structural checks.

## Adding another helper

Add its external identity, purpose, when-to-use condition, source distribution/version and SHA-256 of the observed entrypoint to authoring-tools.yaml. Keep personal absolute paths local. Preserve upstream authorship and licensing when copying or adapting actual content.

The installer selects installable outputs only from catalog.yaml. It validates helper metadata but never resolves or deploys those helpers. Selecting an external helper ID fails without writing a destination. Adding a helper record does not create an installable output, tool permission or invocation grant.
