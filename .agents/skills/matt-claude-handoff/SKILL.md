---
name: matt-claude-handoff
description: Experimental upstream workflow. Hand the current conversation off to
  a fresh background agent that picks up the work immediately.
metadata:
  upstream: matt/claude-handoff
  source-commit: 49dd158d1076134a641b33efb035946536778336
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

### Capability and behavior adjustment

Claude background launching is unavailable as a native Codex feature. Create the handoff artifact and use an authorized Codex background/delegation facility only if exposed; otherwise stop at the saved handoff. Never execute claude --bg as a Codex fallback.

Write a handoff summary of the current conversation so a fresh agent can continue the work. Save it to the temporary directory of the user's OS, then launch a background agent seeded with it as its prompt: `claude --bg --name "<descriptive name>" -- "$(cat <summary file>)"`. Passing the file keeps the shell from running backticks or expanding `$` in the summary. It starts in the current working directory and returns immediately; the user manages it with `claude agents`.

Always pass `-n`/`--name` with a descriptive name (e.g. `--name "Fix login bug"`); it sets the display name shown in the job list, session picker, and terminal title.

Include a "suggested skills" section in the summary, naming which skills the next agent should call the Skill tool for.

Do not duplicate content already captured in other artifacts (specs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

Redact any sensitive information, such as API keys, passwords, or personally identifiable information, since the summary becomes the agent's prompt.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the summary accordingly.


## Provenance

Adapted from [matt/claude-handoff](../../../vendor/matt/skills/in-progress/claude-handoff/SKILL.upstream.md) at `49dd158d1076134a641b33efb035946536778336`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
