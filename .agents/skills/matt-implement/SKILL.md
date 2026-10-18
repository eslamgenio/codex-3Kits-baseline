---
name: matt-implement
description: Implement a piece of work based on a spec or set of tickets.
metadata:
  upstream: matt/implement
  source-commit: 49dd158d1076134a641b33efb035946536778336
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

Implement the work described by the user in the spec or tickets.

If the user passes a ticket reference, fetch it from the issue tracker and state its title before starting. If the reference is ambiguous, ask.

Call the Skill tool with "matt-tdd" where possible, at pre-agreed seams.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, call the Skill tool with "matt-code-review" to review the work.

Commit your work to the current branch.


## Provenance

Adapted from [matt/implement](../../../vendor/matt/skills/engineering/implement/SKILL.upstream.md) at `49dd158d1076134a641b33efb035946536778336`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
