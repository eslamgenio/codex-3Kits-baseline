---
name: pstack-principle-laziness-protocol
description: Apply when refactoring, evaluating diff size, or tempted to add abstractions,
  layers, or signal threading. Bias toward deletion and the smallest change that solves
  the problem.
metadata:
  upstream: pstack/principle-laziness-protocol
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

# Laziness Protocol

- **Consolidate decisions.** Do not repeat the same choice in several places. Put it behind one source of truth and pass the result as a simple flag.
- **Minimize the diff.** Make the smallest change that solves the problem. Fewer lines beat "elegant" boilerplate.


## Provenance

Adapted from [pstack/principle-laziness-protocol](../../../vendor/pstack/skills/principle-laziness-protocol/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
