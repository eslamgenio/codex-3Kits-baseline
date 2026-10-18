---
name: pstack-interrogate
description: Use for "pstack-interrogate", "adversarial review", "multi-model review",
  "challenge this", "stress test this code", "find blind spots", or "tear this apart".
  Multiple LLM reviewers challenge changes from independent angles.
metadata:
  upstream: pstack/interrogate
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

# Interrogate a change with independent Codex reviewers

Produce an adversarial review and a synthesized verdict. Reviewers and the lead remain read-only with respect to product files; return findings rather than automatically applying fixes.

## Scope and intent

Determine the user's actual review boundary and state intent in one paragraph from the request, specification, and available change history. Ask only if the intent or baseline cannot be established.

Include all relevant committed, staged, unstaged, and new files for that boundary. Use the actual base branch/revision. An empty committed diff does not prove an unchanged working tree. Give reviewers the same code snapshot, contract, and surrounding source needed to understand it. Preserve unrelated pre-existing work.

## Form the panel

Use the session's actual delegation API, not Cursor Task fields or installed Claude/Grok defaults. Use two fresh reviewers by default when available and permitted. The coordinator stays responsible for synthesis; reviewers do not recursively create panels.

If `.agents/pstack-models.json` exists at the project root, read its `interrogate.reviewers` role. Values may only be model identifiers verified accepted by this session or `inherit-parent`. If no usable configuration exists, use inherited-model reviewers; do not modify configuration as a review side effect.

Report capability honestly:
- Different model families actually selected: a cross-family panel.
- Different model IDs in one family: a within-family panel.
- Inherited or identical model choices: independent-context, same-model panel.
- Runtime cannot confirm model identity: model diversity unknown.
- No delegation: single-context degraded review, explicitly not an independent panel.

Do not install or invoke external model CLIs, spend through an extra account, create external PRs, or bypass a rejected model choice. If a requested model fails, disclose the failure and continue only with a supported selection allowed by the task, or report blocked when the user requires that exact panel.

## Review independently

Read these resources before dispatch:
- [reviewer prompt](references/reviewer-prompt.md)
- [rubric](references/rubric.md)
- [code-quality lens](references/code-quality-review.md)

Fill the same template for every reviewer with the stated intent, scope, and contract. Instruct them to return severity, location, concrete execution path/evidence, and optional remedy. They may inspect surrounding source using available tools. The code-quality resource's language about restructuring is a proposal lens, not authorization to edit.

Give each reviewer a fresh context containing only the task and raw artifacts needed for review. Do not supply another reviewer's findings or the author's preferred conclusions. Clearly instruct reviewers to leave product files unchanged. Existing safe read-only tests can support a finding; any tool needing unavailable credentials or writes is a reported limitation.

## Synthesize with lead judgment

Read [lead judgment](references/lead-judgment.md). Verify claims against actual code, consumers, and constraints. Merge duplicate findings, retain the reviewer attribution, and resolve disagreement where evidence permits. A serious issue raised by one reviewer still deserves examination; agreement is a signal, not proof. An empty review is valid.

Return:
1. Intent and full scope.
2. Reviewers, actual model selections/unknown identity, independence and missing capabilities.
3. **Act On:** confirmed correctness, security, or material maintainability issues.
4. **Consider:** legitimate changes requiring a trade-off.
5. **Noted:** valid context without an immediate action.
6. **Dismissed:** incorrect or irrelevant findings, with reasons.
7. Agreement map and unresolved disagreements.
8. Tests/checks actually executed, unverified areas, and confirmation that product files were not edited.

If work changes while the panel runs, identify the reviewed snapshot and re-review material differences before issuing a verdict on the new version.


## Provenance

Adapted from [pstack/interrogate](../../../vendor/pstack/skills/interrogate/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
