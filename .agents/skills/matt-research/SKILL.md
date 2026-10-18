---
name: matt-research
description: Investigate a question against high-trust primary sources and capture
  the findings as a Markdown file in the repo. Use when the user wants a topic researched,
  docs or API facts gathered, or reading legwork delegated to a background agent.
metadata:
  upstream: matt/research
  source-commit: 49dd158d1076134a641b33efb035946536778336
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

Spin up a **background agent** to do the research, so you keep working while it reads.

Its job:

1. Investigate the question against **primary sources** (official docs, source code, specs, first-party APIs), not a secondary write-up of them. Follow every claim back to the source that owns it.
2. Write the findings to a single Markdown file, citing each claim's source.
3. Save it where the repo already keeps such notes; match the existing convention, and if there is none, put it somewhere sensible and say where.


## Provenance

Adapted from [matt/research](../../../vendor/matt/skills/engineering/research/SKILL.upstream.md) at `49dd158d1076134a641b33efb035946536778336`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
