---
name: pstack-blast-radius
description: Find what a change could break somewhere else before it ships, beyond
  the diff, and prove the one fact it's safe because of by running real code instead
  of writing it up. Use for 'blast radius of X', 'what could this break', or reviewing
  a small diff you don't trust.
metadata:
  upstream: pstack/blast-radius
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

# Prove a change's blast radius

Assess what could break beyond the changed files, and execute the facts on which safety depends. This is an assessment, not permission to fix product code.

## Establish scope

Use the user's requested base revision, patch, files, or before/after artifact. In Git, identify the real default/base branch from existing metadata rather than assuming main. Include relevant committed, staged, unstaged, and untracked changes. Preserve pre-existing unrelated work and state any scope exclusions. If no reliable baseline exists, state that limitation or request the missing artifact.

Read the changed code, its consumers, relevant contracts, dependency versions/local patches, and useful commit rationale. Explain the existing path directly; the separate how/why skills are optional, not hard dependencies.

## Find the safety facts

Identify the one or two concrete invariants on which safety depends. Follow effects that symbol searches miss: serialized data, database state, cross-language consumers, wire formats, timing, teardown, flags, retries, and remote boundaries. Use real consumers and source locations; label external consumers that cannot be inspected.

For each material fact, distinguish:
1. An assertion.
2. A source citation.
3. A traced execution argument.
4. An executed check against the real code.
5. A reproduction on the running application's user surface.

## Execute the important checks

Write the smallest useful probe or test against the exact current code and installed dependency version. Put new probes in an isolated scratch location unless the user requested a permanent regression test. Use temporary data. Record the command, exit code, observations, and evidence location.

A failing probe is evidence of a risk, not proof of safety. A passing check establishes only the conditions it exercised. If execution is blocked, report the fact as unproven and name the blocker; do not replace missing evidence with a convincing explanation.

For broad work, independent review can help if delegation is available and permitted. Report actual model diversity. Same-model reviews do not become cross-model evidence by assigning different roles. Product edits, dependency installs, remote writes, commits, and PRs require task authorization.

## Return

- What changed and the scope examined.
- The safety facts, their evidence levels, and their proved, disproved, or unproven status.
- Confirmed risks with actual file/line references, execution paths, likely impact, and qualitative likelihood grounded in the observed conditions.
- Risks checked and cleared, with the limits of those checks.
- The cheapest useful regression check before acceptance.
- Execution blockers and external areas not inspected.

Keep the report actionable. Avoid fabricated callers, numerical probabilities, or claims of complete safety.


## Provenance

Adapted from [pstack/blast-radius](../../../vendor/pstack/skills/blast-radius/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
