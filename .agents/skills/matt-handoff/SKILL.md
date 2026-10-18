---
name: matt-handoff
description: Compact the current conversation into a handoff document for another
  agent to pick up.
metadata:
  upstream: matt/handoff
  source-commit: 49dd158d1076134a641b33efb035946536778336
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save to the temporary directory of the user's OS (`$TMPDIR`, else `/tmp`; `%TEMP%` on Windows) - not the current workspace.

Include a "suggested skills" section in the document, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.


## Provenance

Adapted from [matt/handoff](../../../vendor/matt/skills/productivity/handoff/SKILL.upstream.md) at `49dd158d1076134a641b33efb035946536778336`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
