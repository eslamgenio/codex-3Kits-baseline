# Codex complex-project baseline

A reusable starting point for complex projects using Matt Pocock's discovery skills, Addy Osmani's engineering workflow, and Pstack's verification and review workflows.

This package includes **121 namespaced skills**: Matt 38, Addy 25, and Pstack 58, pinned to the source commits in [UPSTREAM.md](docs/UPSTREAM.md). All upstream skill folders and their resources are included. Seven Matt skills are experimental, and three Pstack skills come from its dormant Benny automation pack; Claude integrations, Bash scripts and external services retain explicit capability requirements. Inclusion is not proof that every optional integration works on your machine.

## Start a new project

For a complete worked example, follow the [Getting-started guide: IoT Incident Console](docs/GETTING-STARTED.md). It includes the exact prompts, approval checkpoints, and a module-by-module walkthrough.

1. Extract or copy the complete baseline into a new, empty project folder, including hidden .agents/ and .gitignore.
2. Open that folder in Codex. Do not install another copy of the same packs into it.
3. Read [AGENTS.md](AGENTS.md) and [the workflow prompts](docs/WORKFLOW.md).
4. Start with the prompt below. The baseline chooses no framework, database, application structure, or deployment provider for you.
5. Review the specification and plan, then authorize implementation.

For an existing repository, reconcile its README.md, AGENTS.md, ignore rules, and skill folders before copying. Preserve its current instructions and project documentation. This baseline is designed primarily for a new project.

### First prompt

$matt-grill-with-docs

Use this skill for the new project.

I want to build: [describe the product, its users, and the problem].

Read this baseline's instructions and inspect what actually exists. Clarify scope, user journeys, failure behavior, data, permissions, integrations, and quality expectations. Maintain the glossary and justified ADRs. Record agreed project context in PROJECT.md.

Finish with agreed requirements and open questions. Stop before implementation.

## What is ready

- Namespaced Codex skill entrypoints, UI metadata, and preserved invocation policies.
- Shared Codex tool/capability mapping and per-skill adjustments where needed.
- Full original source snapshots, licenses and SHA-256 hashes.
- An implementation workflow and copyable prompts.
- Three substantially adapted Pstack skills: create-verification-skill, blast-radius and interrogate.

[VALIDATION.md](docs/VALIDATION.md) records what was actually tested and what remains unverified. Structural compatibility across the catalog does not establish behavioral quality for all 121 workflows.

## Prerequisites

- Codex with local skill support. In CLI/IDE, mention a skill with $name or use the available picker; app interfaces may use a picker/mention instead.
- Git for versioned diffs, history and worktree workflows.
- The actual application's own language/toolchain, selected during specification.
- Optional browser/device/MCP tools, credentials, Bash, solvers, trackers, or hosting only for workflows requiring them. The catalog identifies important dependencies.
- To run the baseline validator: Python 3 and PyYAML. This is tooling for the baseline; it does not require your product to use Python.

On Windows, after installing those validation prerequisites:

    py -3 tools/validate_baseline.py

The validator checks structure, dependency links, catalog consistency, source snapshot integrity, and invocation policy. It does not execute your application or all optional integrations.

## Layout

- AGENTS.md: project execution instructions.
- PROJECT.md: project-specific context to establish during discovery.
- .agents/skills/: active, namespaced Codex skills.
- .agents/CODEX-COMPATIBILITY.md: host tool and capability adaptations.
- .agents/skill-catalog.json: complete machine-readable inventory and source hashes.
- docs/WORKFLOW.md: exact staged prompts.
- docs/GETTING-STARTED.md: practical IoT example with exact prompts from setup through module acceptance and resuming work.
- docs/SKILLS.md: full skill inventory and capability notes.
- docs/UPSTREAM.md: provenance, licensing and adaptation details.
- docs/VALIDATION.md: observed checks and practical evaluation results.
- vendor/: reference-only upstream snapshots.
- licenses/: upstream MIT licenses.
- tools/: baseline structural validator.

## Updates

Use a new pinned baseline release and review its changes. Do not overwrite local skill customizations or unfinished project records automatically. The bundled source hashes identify the starting versions; this package has no auto-updater, background agent, external account connection, or enabled CI pipeline.

Local adaptations are unofficial and are not endorsed by the upstream authors or OpenAI.
