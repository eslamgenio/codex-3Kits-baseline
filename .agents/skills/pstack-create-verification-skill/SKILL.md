---
name: pstack-create-verification-skill
description: Generate a project-local verification skill that drives your app the
  way a user does — any language, framework, or platform. Use for $pstack-create-verification-skill,
  "make a control skill for this repo", or when a project has no scripted way to prove
  UI/CLI/service behavior.
metadata:
  upstream: pstack/create-verification-skill
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

# Create a Codex project verification skill

Generate a repository-specific skill that drives the real application and preserves proof for the next Codex session.

## Inspect the repository

Find the actual user surfaces, documented launch commands, existing tests or interaction harnesses, prerequisites, and ways to observe side effects. Prefer existing tooling. Determine how to isolate instances, data, ports, and profiles. Use Windows/PowerShell commands on Windows unless a working Bash environment is an explicit prerequisite.

If the checkout cannot start, report the precise blocker. Fix it only within the user's authorized implementation scope. An unexplored broken baseline is not a basis for verification instructions.

## Generate the recipe

Create `.agents/skills/verify-<app>/SKILL.md` with valid name and description frontmatter. Reuse a suitable existing skill instead of duplicating it. Its description identifies the app and surface. Include these sections with observed commands and selectors:

- **Launch:** setup from disposable empty state, including required migrations and seed data; exact readiness criteria and ownership of any started process. A short-lived CLI needs a command invocation, not a fabricated server.
- **Doctor:** a read-only check of the expected build, instance, data location, and usable prerequisites. Run before driving, and after surprising failures.
- **Drive:** real user entry points through the available UI, CLI, API, or library public interface. Prefer stable handles to coordinates.
- **Evidence:** commands/actions, stdout/stderr or UI captures, exit status, resulting state, and relevant persisted effects. Store proof separately from disposable data; identify the environment and feature.
- **Cleanup:** tear down only instances and scratch state created by this run. Keep evidence. Do not kill by process name or remove a user's data.
- **Helpers:** include only useful executable helpers, document their invocation, and execute them before delivery.

For an unavailable browser, device, PTY, credential, or service, identify the missing capability and report that path as unverified. A lower-level test may be supplemental evidence; it is not proof that an unavailable user surface works. Observe what dry-run modes actually do.

## Map features

Read [the feature-map examples](references/feature-map-example/README.md) for format only; their Notes commands and Unix paths are illustrations.

Create `features/README.md` and individual feature files, initially covering the main 3-5 observable features or all features of a smaller app. Each file describes:
1. Sub-features.
2. How to get to it (user POV), including distinct entry points.
3. Driving it with the actual harness: preconditions, exact action, expected observable result.
4. Gotchas.

Connect journeys to existing acceptance criteria when available. Missing seed data or an unreachable prerequisite is a reported failure or coverage gap, not permission to weaken the journey.

## Prove the generated skill

Execute its instructions for ONE mapped feature: launch, doctor, drive, capture proof, cleanup, then confirm proof still exists. One proved journey is the generator's completion condition, not complete acceptance coverage. Fix and retry the generated harness within scope if necessary, cleaning each failed attempt. Inspect the artifacts rather than trusting a delegate's completion message.

Mark the output **proven** only after this execution succeeds; otherwise **draft/blocked**, with the exact failing step. Separate local/stand-in proof from unverified target environments. State which mapped journeys remain unverified.

The user can later invoke `pstack-maintain-verification-skill` to maintain the map. Because that workflow is explicit-only, offer it rather than silently launching it.


## Provenance

Adapted from [pstack/create-verification-skill](../../../vendor/pstack/skills/create-verification-skill/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
