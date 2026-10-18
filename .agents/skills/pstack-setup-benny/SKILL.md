---
name: pstack-setup-benny
description: Configure Benny and prepare its triage and repro automations. Use when
  installing Benny or changing its Slack, tracker, repository, routing, control, model,
  or budget settings.
metadata:
  upstream: pstack/setup-benny
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

### Capability and behavior adjustment

Dormant automation-pack extra. Native Cursor hosting is unavailable; the Codex adaptation produces project-local bounded manual configuration and reports unattended scheduling blocked unless an authorized scheduler is actually exposed.

# Set up a bounded issue-triage workflow for Codex

This is an adaptation of a dormant Pstack automation pack, not native Cursor hosting.

Inspect the project's intended issue sources, tracker, application verification recipe, repository boundaries, credentials and available tools. Ask only for decisions that cannot be observed. Keep secret values outside committed configuration.

Use the nested configuration shape in `vendor/pstack/automations/benny/templates/configuration.example.yaml` from the project root, translating actual tool IDs and project paths rather than copying placeholders. Preserve schema_version=1. Validate the fields needed by each selected operation: source channel and triage identity/actions, repository/default branch, tracker/routing, verdict markers, budgets, and control/feature-map/environment for reproduction. Report incomplete configuration as draft; do not label it operational. Both manual consumers load the same JSON and require confirmed immutable source coordinates.

By default, produce a project-local configuration/design at `.agents/benny-config.json` and a short operating recipe for manually invoking `pstack-triage-issue-reports` and `pstack-reproduce-and-fix-issues`. Include source/target IDs only after confirmed by the user or authorized evidence. Record unresolved capabilities instead of placeholders that look operational.

If the user explicitly requests scheduling, use only an actually exposed authorized Codex automation service. Prepare the complete schedule, task scope, notification policy, credentials handoff and stopping conditions before requesting any required approval. Without that service, report unattended operation blocked; the bounded manual workflow remains available.

Do not create .cursor/settings.json, Cursor automations, Slack messages, tracker records, webhooks, or network exposure as an implied setup step. Those operations require their own task authorization. The source pack remains bundled as reference material; no live automation pack is copied or enabled by this skill.

Report what was configured, what can run manually, what prerequisites remain, and whether any schedule was actually created.


## Provenance

Adapted from [pstack/setup-benny](../../../vendor/pstack/automations/benny/skills/setup-benny/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
