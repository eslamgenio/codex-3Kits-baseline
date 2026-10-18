---
name: pstack-principle-migrate-callers-then-delete-legacy-apis
description: Apply when introducing a new internal API while old callers still exist.
  Migrate callers and delete the old API in the same wave instead of preserving compatibility
  layers.
metadata:
  upstream: pstack/principle-migrate-callers-then-delete-legacy-apis
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

# Migrate Callers Then Delete Legacy APIs

- Update tests to assert the new contract, and delete tests that only protect pre-refactor implementation details

**When this applies:**
- No external users depend on backward compatibility
- The project can absorb coordinated breaking changes
- The new API is part of a simplification or refactor initiative


## Provenance

Adapted from [pstack/principle-migrate-callers-then-delete-legacy-apis](../../../vendor/pstack/skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
