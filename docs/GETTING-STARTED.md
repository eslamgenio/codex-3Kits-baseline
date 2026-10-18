# Getting started: build an IoT Incident Console

Use this worked example to start a complex project from the baseline. The IoT Incident Console is a proposed local web application where engineers register devices, import simulated readings, investigate alerts, and acknowledge incidents. It has not been implemented by this guide.

- **Matt** clarifies requirements and terminology.
- **Addy** specifies, plans, implements, and tests.
- **Pstack** verifies real behavior and challenges consequential changes.

Send each numbered prompt as a separate message. Wait for the response and review the requested checkpoint before continuing. The `$...` lines identify the intended skills; select the matching namespaced skill in your Codex picker when available. These prompts authorize actions only when you send them in your new project chat.

## 1. Create the project folder

Extract or copy the complete baseline into a new, empty folder, for example a folder named `IoTIncidentConsole` under your Documents/Projects directory. Include hidden `.agents/` and `.gitignore` files.

Open the folder that directly contains `AGENTS.md`, `README.md`, and `.agents` in Codex, then start a chat there. You do not need to reinstall the skill packs. For this Windows example, use PowerShell-compatible commands.

### Message 1 — Check the starting point

```text
Read AGENTS.md, README.md, PROJECT.md, and docs/WORKFLOW.md.

Confirm that this is an unconfigured copy of the project baseline and that the main Matt, Addy, and Pstack entrypoints are present.

Run the bundled structural validator if its Python and PyYAML prerequisites are available. Report missing prerequisites without installing anything yet.

Initialize a local Git repository if one does not exist, and create one initial commit containing the baseline. This authorizes that local baseline commit only. Do not configure a remote or push. If Git identity is missing, tell me what information you need.

Do not implement application code.
```

Expected result: the baseline is inspected, available validation results are reported, and a local starting revision is recorded. Any missing prerequisite or Git identity is stated explicitly.

## 2. Discover the product and agree on requirements

### Message 2 — Discover the product

```text
$matt-grill-with-docs

I want to build an IoT Incident Console for engineers investigating device issues.

My initial idea is a local web application that can:
- Register devices with unique identifiers.
- Import simulated timestamped readings from CSV.
- Identify readings that violate agreed thresholds.
- Display incidents and let an engineer acknowledge them.
- Export an investigation history.

For the first version, use fictional data and local execution. Real device connections, external notifications, cloud deployment, and production authentication are outside scope.

I know Python and prefer a straightforward implementation with modest dependencies. Recommend a suitable stack after understanding the requirements.

Treat these as starting proposals. Interview me about ambiguities, failure cases, data rules, and useful acceptance criteria. Ask one question at a time and recommend an answer when helpful.

Maintain the glossary and justified architectural decisions. Record agreed project context in PROJECT.md.

Finish with the agreed requirements and unresolved questions. Do not implement.
```

Answer the interview questions. For example: Does importing the same CSV twice duplicate readings? Which timezone formats are accepted? Does acknowledging an incident require a comment? These answers should become testable requirements.

### Message 3 — Separate the capabilities

```text
$addy-spec-driven-development

Use our agreed requirements to propose a capability map before writing detailed specifications.

Possible capabilities are devices, telemetry, incidents, and reporting. Validate those boundaries rather than accepting them automatically.

For each capability, show its responsibility, dependencies, and observable outcome. Recommend the smallest useful first capability and the implementation order.

Keep UI, API, and persistence work within complete user-facing slices where appropriate.

Save the proposed map using the baseline conventions. Stop for my approval before detailed specifications or implementation.
```

An illustrative map might look like this. Use the actual approved map if the interview produces different boundaries.

| Module | Observable outcome | Depends on |
|---|---|---|
| `devices` | Engineer can register and list devices | — |
| `telemetry` | Engineer can import and inspect readings | `devices` |
| `incidents` | Engineer can investigate and acknowledge incidents | `telemetry` |
| `reporting` | Engineer can export investigation history | `incidents` |

### Message 4 — Specify the first capability

Send this after reviewing and accepting the proposed map.

```text
I approve the capability map.

Use addy-spec-driven-development to specify the first capability in the approved dependency order.

Use its stable module ID in the specification filename. Include scope, exclusions, user journeys, validation and failure behavior, relevant interfaces, testing strategy, and observable acceptance criteria with stable identifiers.

In PROJECT.md, record the active module and its canonical specification path so future sessions can identify the current work.

Surface unresolved decisions instead of silently choosing product behavior.

Save the specification and stop for approval before planning.
```

For the device module, useful criteria might include rejecting duplicate device IDs and retaining registered devices after restarting the app. Check that the specification states the expected behavior precisely.

### Message 5 — Establish the quality bar

```text
$addy-constraint-driven-development

Propose a practical quality bar for this project, using the agreed requirements and first module specification.

Consider input validation, deterministic tests, persistence, failure handling, relevant accessibility checks, and later timestamp-sensitive behavior.

Explain which checks should block acceptance and which can remain advisory. Recommend numerical thresholds only where they have a useful measurement method.

Do not introduce arbitrary coverage targets or install tooling yet.

Show me the proposed constraints for approval. Record agreed standards in CONSTRAINTS.md, and identify enforcement work that belongs in implementation.
```

Review the proposed standards and answer any remaining questions. Continue when the specification and constraints accurately reflect what you want.

## 3. Plan and build one capability

### Message 6 — Approve and plan

```text
I approve the active module specification and the agreed quality constraints.

$addy-planning-and-task-breakdown

Create the implementation plan for the active module only.

Break it into small, dependency-ordered slices that each deliver observable behavior. Include the relevant UI, API, persistence, and tests within each slice where appropriate.

For every task, identify:
- Acceptance criteria covered.
- Likely files affected.
- Actual verification commands or required tooling.
- Dependencies and review checkpoints.

Record the current Git baseline and pre-existing local changes.

Save tasks/plan.md and tasks/todo.md using the baseline conventions. Preserve unrelated unfinished work. Stop before implementation.
```

### Message 7 — Implement through the first checkpoint

Send this after reviewing the plan and task breakdown.

```text
I approve the plan and task breakdown.

$addy-incremental-implementation
$addy-test-driven-development

Implement the active module through the next agreed checkpoint, using relevant specialist skills.

Work one slice at a time and verify each slice before proceeding. Use the repository’s actual commands and the agreed constraints.

Continue through approved tasks without asking permission between routine steps. Pause at the checkpoint, a genuine blocker, or a decision outside the approved scope.

At the checkpoint, explain:
- What I can now do in the application.
- How I can try it.
- Which acceptance criteria were exercised.
- Which checks passed and what remains unverified.

Leave commits, pushes, PRs, and deployment for separate instructions.
```

Try the working slice yourself. For the device module, a practical checkpoint could be:

1. Open the app.
2. Register a fictional device.
3. Confirm it appears in the list.
4. Try the same identifier again.
5. Restart the app and confirm persistence.

### Message 8 — Continue after trying the checkpoint

```text
Checkpoint approved.

Continue through the next agreed checkpoint under the same scope and verification rules. Keep the task records accurate and surface any requirement that needs reconciliation.
```

Repeat Message 8 after successful checkpoints until the active module is implemented. If behavior is wrong, describe the observed result and expected result instead of approving it.

## 4. Establish and run reusable application verification

Run the generator once the application has a runnable user-facing slice. Reuse the generated skill for later checks; keep its feature map current as modules are added.

### Message 9 — Create reusable application verification

```text
$pstack-create-verification-skill

The application now has a runnable user-facing slice.

Create a project-local verification skill named verify-iot-incident-console using our existing tooling.

Include startup, readiness checks, application interaction, evidence capture, and cleanup. Map implemented journeys to their acceptance criteria. Keep planned but unimplemented features separate.

Prove one implemented journey end to end through the real user surface. Preserve evidence after cleanup.

Report exactly what was proved and which journeys remain unverified.
```

### Message 10 — Verify the completed module

```text
Use the generated verify-iot-incident-console skill to exercise every implemented journey affected by the active module, including relevant failure paths.

Report each acceptance criterion as verified, failed, or unverified, with evidence and reasons.

Distinguish product failures from verification-harness problems. Do not weaken expectations to obtain a pass.

If the required user surface cannot be driven with available tools, identify the missing capability. Do not describe API-only checks as proof that the browser UI works.
```

Creating the verification skill proves one journey. Message 10 requests the wider module verification.

## 5. Review, resolve, and accept the module

### Message 11 — Review the completed module

```text
$addy-code-review-and-quality

Review the active module against its approved specification, CONSTRAINTS.md, and repository standards.

Cover its complete changes since the recorded module baseline, including relevant committed, staged, unstaged, and new files. Exclude unrelated pre-existing work.

Look for correctness problems, missing acceptance criteria, weak tests, unnecessary complexity, and integration gaps.

Return prioritized findings with source references and supporting reasoning. Do not apply fixes during this pass.
```

### Message 12 — Add independent scrutiny when warranted

Use this for a meaningful change that warrants independent review.

```text
$pstack-interrogate

Adversarially review the same complete module changes against the approved specification and constraints.

Use independent reviewers where available. Report the actual reviewer configuration and whether model diversity is confirmed, unknown, or unavailable.

Focus on missed failure paths, hidden assumptions, and interactions with existing behavior.

Synthesize Act On, Consider, Noted, and Dismissed findings. Identify additional findings beyond the earlier review. Do not apply fixes.
```

### Optional message — Check a consequential shared change

Blast-radius becomes useful when you reach telemetry: timestamp handling can affect incident ordering, age calculations, and exports. Use this before accepting a change with wider consequences.

```text
$pstack-blast-radius

Assess the complete changes for the active module, including its effects on existing consumers.

For timestamp-related changes, inspect ingestion, persistence, incident ordering, age calculations, and exports where those consumers exist.

Identify the facts on which safety depends and execute focused checks against the real code.

Separate proved, disproved, and unproven assumptions. Include evidence, affected source locations, and useful regression checks.

Do not fix product code during this assessment.
```

### Message 13 — Resolve and verify

```text
Use Addy’s implementation and testing skills to resolve confirmed Act On findings.

Confirm each issue against the code and specification before changing anything. Present the trade-off before expanding scope for Consider findings.

Make focused fixes and add meaningful regression protection. Rerun affected checks and application journeys. Obtain focused review of material new changes.

Update the task records and return:
- Acceptance criteria and verification status.
- Checks executed and evidence locations.
- Findings resolved and remaining issues.
- Blocked or unverified areas.
- Whether the work is local or deployed.

Do not mark required failed or unverified criteria complete.
```

### Message 14 — Accept this module and prepare the next

Send this after checking the results and accepting the completed module.

```text
I accept the completed module based on the reported evidence.

Create a local commit containing its scoped implementation and related project records. Do not push.

Update PROJECT.md with the completed module and the next capability in the approved map.

Use addy-spec-driven-development to specify that next capability, reusing the established terminology, interfaces, constraints, and verification approach.

Stop at specification approval before planning or implementation.
```

Repeat the specify → plan → build → verify → review → accept cycle for each capability. Reuse the application verification skill and extend its feature map as the product grows. The [general workflow](WORKFLOW.md) includes optional design, recurring-mistake, and verification-maintenance prompts.

## 6. Resume in a new chat

### Resume message

```text
Read AGENTS.md, PROJECT.md, the active module specification, CONSTRAINTS.md, tasks/plan.md, and tasks/todo.md.

Inspect the current working changes and relevant verification evidence.

Summarize:
- What is already implemented and verified.
- What the active approved scope is.
- The next ready task.
- Any blocker or genuinely unresolved decision.

Continue within the recorded approved scope. Respect the agreed checkpoints and do not restart discovery or planning without a reason.
```

## 7. Separate local completion from deployment

Deployment is a separate stage. Completing this example locally establishes a verified local application. Production authentication, infrastructure, operational safeguards, and release readiness need their own agreed scope and verification.

For the baseline’s historical checks and their limits, see [VALIDATION.md](VALIDATION.md). Those results do not establish that your new application works.
