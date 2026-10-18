---
name: pstack-principle-attack-the-premise
description: Apply when two or more fixes that share one premise have failed the same
  gate. Write the premise down and test it directly before you write another fix that
  assumes it.
metadata:
  upstream: pstack/principle-attack-the-premise
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

# Attack the Premise

When two or more fixes that share one premise have failed the same gate, suspect the premise, not the fixes.

**Why:** Each failed fix is evidence against the belief it assumed. A third fix on the same premise spends effort where the evidence already says the cause is not.

**Pattern:**
- **Write the premise down.** The premise is the one sentence that every failed fix assumed.
- **Test the premise before the next fix.** Find an observation that would come out differently if the premise were false, and make it. Look at how the failures are distributed, not only at how large they are. Make the check rerunnable per [Build the Lever](../pstack-principle-build-the-lever/SKILL.md).
- **Follow the evidence.** If it contradicts the premise, the cause is elsewhere. Look for what the failures have in common that the premise did not predict. If it confirms the premise, ask the next "pstack-why" per [Fix Root Causes](../pstack-principle-fix-root-causes/SKILL.md). The earlier fixes may have treated a consequence instead of the cause.
- **Remove the condition instead of compensating for it**, per the [Laziness Protocol](../pstack-principle-laziness-protocol/SKILL.md). If the evidence shows that one part always lands on the losing side, change what puts it there. A mechanism that cleans up after it leaves the cause in place and adds work on every run.

**Stop:** Do not start the next fix before the premise is written down and tested.

This principle is distinct from [Redesign from First Principles](../pstack-principle-redesign-from-first-principles/SKILL.md), which rebuilds a design around a new requirement. It questions a fact the current design assumes.


## Provenance

Adapted from [pstack/principle-attack-the-premise](../../../vendor/pstack/skills/principle-attack-the-premise/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
