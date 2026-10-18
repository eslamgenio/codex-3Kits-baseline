---
name: pstack-setup-pstack
description: Configure which models pstack uses per role and at what reasoning budget.
  Detects your available models and writes an always-applied rule that overrides the
  skill defaults. Use for $pstack-setup-pstack, "configure pstack models", "pstack
  budget", or changing pstack's model choices.
metadata:
  upstream: pstack/setup-pstack
  source-commit: 0148b78c56c72a1b8412055913c79f767095b217
---

## Codex adapter

Read [../../CODEX-COMPATIBILITY.md](../../CODEX-COMPATIBILITY.md) before executing this workflow. Resolve family-local skill names through the catalog; use only tools exposed in this session. This adapter and the project's AGENTS.md govern host-specific operations in the upstream workflow.

### Capability and behavior adjustment

Use project-local .agents/pstack-models.json with schema_version=1 and roles mapping role names to lists of verified model IDs or inherit-parent. Role names include interrogate.reviewers, arena.runners, architect.runners, swarm.workers, code, and judgment. Show proposed choices and ask before saving; preserve unrelated settings. Do not write Cursor rules or infer account entitlements from model names. Missing role entries inherit the parent model.

# Configure project-local Pstack models for Codex

Configure only this project's `.agents/pstack-models.json`. The file is optional; an absent file or role uses inherited-model delegates.

1. Inspect the delegation capabilities actually exposed in the current session. Model IDs are usable only when the session confirms they are accepted. Never infer entitlements from Cursor defaults or the parent model's name. If selectable model IDs cannot be confirmed, offer inherited-model delegates and identify diversity as unknown or same-model.
2. Read any existing JSON and preserve unrelated keys and role choices. If malformed, report it and show the repair before writing.
3. Ask for the desired budget and review diversity only where those choices can actually be represented by the available tool. A label such as high is a preference, not proof that a runtime supports that reasoning option. Describe the actual supported mapping.
4. Show the proposed configuration, model availability, expected panel sizes, and any limitations; wait for approval before writing.
5. Save valid JSON, read it back, and validate schema_version=1, roles as an object, and role values as nonempty lists of confirmed model IDs or `inherit-parent`. Report the saved path and capabilities; do not claim a model invocation succeeded merely because the JSON is valid.

Example with no presumed external model access:

```json
{
  "schema_version": 1,
  "roles": {
    "interrogate.reviewers": ["inherit-parent", "inherit-parent"],
    "arena.runners": ["inherit-parent", "inherit-parent"],
    "arena.cross_judge_pool": ["inherit-parent"],
    "architect.runners": ["inherit-parent", "inherit-parent"],
    "swarm.workers": ["inherit-parent"],
    "code": ["inherit-parent"],
    "judgment": ["inherit-parent"]
  }
}
```

The example gives two independent reviewers but no guaranteed model diversity. Use the role-name mapping in the common adapter for every consumer. Reasoning/speed values are optional per-role fields only if the actual runtime supports them; do not encode them into invented model slugs.

Offer the explicitly invoked `pstack-create-verification-skill` only when a reusable app-driving recipe is missing. Do not generate one as a configuration side effect.


## Provenance

Adapted from [pstack/setup-pstack](../../../vendor/pstack/skills/setup-pstack/SKILL.upstream.md) at `0148b78c56c72a1b8412055913c79f767095b217`. The snapshot is reference material; the active instructions are this file and its Codex adapter. See the bundled source manifest and license.
