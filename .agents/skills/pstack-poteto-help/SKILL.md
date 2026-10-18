---
name: pstack-poteto-help
description: Guides users through pstack setup, $pstack-poteto-mode, and picking the
  skill, playbook, or principle for a task. Type $pstack-poteto-help with a question.
metadata:
  upstream: pstack/poteto-help
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

# Pstack help for this Codex baseline

Answer the user's actual workflow question using the installed skill catalog and the baseline README, workflow prompts, and Codex compatibility contract.

For setup, inspect the installed namespaced skills and capability notes. This baseline is project-local: it does not require Cursor /add-plugin, a Cursor custom mode, .mdc rules, or Claude settings. Explain the available skill mention/picker rather than inventing slash commands.

For model configuration, point to explicitly invoked `pstack-setup-pstack` and optional `.agents/pstack-models.json`. Identify actual model/delegation availability and limitations.

For ordinary projects, explain that Addy owns implementation, Matt supports discovery and domain language, and Pstack adds selected verification/review procedures. `pstack-poteto-mode` is an explicitly selected alternative orchestrator, not an additional global boss.

Find the smallest suitable skill or playbook for the user's task. Read its active Codex entrypoint before advising. Give one copyable prompt with the namespaced name, inputs, expected outcome, and any required tool or external-service prerequisite. For an unavailable capability, explain the limit and a concrete supported alternative without pretending equivalence.

Treat the baseline's source snapshots as provenance. Do not instruct the user to install another copy of the same packs or modify global configuration just to ask for help.


## Provenance

Adapted from [pstack/poteto-help](../../../vendor/pstack/skills/poteto-help/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
