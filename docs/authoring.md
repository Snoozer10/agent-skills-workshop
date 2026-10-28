# Authoring and evaluation

## Create or improve

Start with a realistic user request and observable completion condition. Reuse a skill when its responsibility fits; split only when a different invocation or conditional branch warrants it.

A package needs SKILL.md with name and description. Keep essential decisions in the entrypoint and conditional detail in linked references. Add scripts or assets only when they materially support the workflow.

Use [templates/skill/SKILL.md](../templates/skill/SKILL.md) as a starting point outside the catalog. Choose activation explicitly rather than copying another skill's settings. Keep tools, models, paths and permissions conditional on the actual host.

Register a new maintained skill in catalog.yaml with its maintenance role and origin. Use [authoring-tools guidance](authoring-tools.md) for external helpers; their use does not register a maintained output. Tag its purpose independently of host support. Version behavior changes and preserve historical import evidence.

## Evidence levels

- Structural: metadata, names, resources, local links and host-control consistency.
- Behavioral: realistic requests, ambiguous activation, scope/permission pressure, recovery and refusal of unsupported claims.
- Host integration: discovery, explicit invocation and actual supported execution on a recorded host/surface/version.
- Live outcome: separately authorized external execution with receipts and limits.

Passing one level does not establish another. Store sanitized reusable scenarios in tests/scenarios/. Keep raw private evaluation receipts in ignored .runtime/attempts/ or an approved external evidence location.

For consequential changes, compare a no-skill or previous-version baseline with the candidate using the same task and inputs. Use independent fresh contexts when permitted. Record the actual outputs, source version, environment, budgets and unresolved findings. A checklist walkthrough is not a runtime agent evaluation.

## Review and release

Run the README checks, then review instruction quality and accepted behavior separately. Reuse valid evidence; repeat affected checks when the candidate changes.

Inspect the distribution file list for private data, provenance and licensing before publishing. Integration and installation are separate actions. Use the installer dry run and retain its receipt for recovery.
