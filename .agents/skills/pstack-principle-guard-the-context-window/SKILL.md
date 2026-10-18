---
name: pstack-principle-guard-the-context-window
description: 'Apply when context is filling up: large outputs, long files, repeated
  reads, fan-out planning. Route bulk to subagents; keep summaries in the main thread,
  not raw payloads.'
metadata:
  upstream: pstack/principle-guard-the-context-window
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

### Capability and behavior adjustment

Delegate only when the actual Codex session offers permitted subagents; otherwise reduce and summarize context without claiming fresh-agent coverage.

# Guard the Context Window

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

**Pattern:**
- **Size phases and cap scope.** Limit files per phase, set turn budgets, account for mechanism costs.


## Provenance

Adapted from [pstack/principle-guard-the-context-window](../../../vendor/pstack/skills/principle-guard-the-context-window/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
