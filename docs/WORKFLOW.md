# Copyable Codex workflow

Use one feature at a time. Mention the named skill through the available picker or type its name explicitly. Prerequisites and conditional capabilities are in the catalog. The first seven stages are the normal path; use optional checkpoints when they address a real risk.

## 1. Discover

Use $matt-grill-with-docs for this feature: [describe the feature, intended users and problem].
Inspect the repository before asking answerable questions. Clarify user journeys, scope, failure behavior, data rules, permissions and quality needs. Maintain the glossary and justified ADRs. Finish with agreements and open questions. Do not implement.

## 2. Specify

Use $addy-spec-driven-development to turn our agreements into the canonical specification.
Reuse existing conventions. Give observable acceptance criteria stable IDs. Record exclusions, failure cases, constraints and unresolved questions. For a multi-capability initiative, propose the capability map before module specs. Stop at the skill's approval gates before planning or code.

After reviewing: I approve the specification. Proceed to planning.

## 3. Plan

Use $addy-planning-and-task-breakdown for the approved spec.
Create dependency-ordered slices with acceptance criteria, files, verification and checkpoints. Record the Git baseline and pre-existing changes. Save tasks/plan.md and tasks/todo.md unless the project uses another tracker. Preserve unrelated unfinished work. Stop before implementation.

After reviewing: I approve the plan and task breakdown.

## 4. Build

Use $addy-incremental-implementation and $addy-test-driven-development plus relevant specialist skills.
Implement the approved plan one verified slice at a time through the next agreed checkpoint. Continue between approved tasks without repeated permission. Pause for the checkpoint, blockers or out-of-scope product decisions. Do not weaken checks. Report criteria exercised and unverified areas. Keep Git/publication operations within my explicit authorization.

After a checkpoint: Checkpoint approved. Continue under the same scope through the next checkpoint.

## 5. Establish and run verification

Use $pstack-create-verification-skill once the app runs.
Reuse existing tooling, generate a Codex project verification skill, map journeys to acceptance criteria, and prove one journey end to end. Preserve evidence and state remaining coverage.

Then: Use the generated verify-* skill to exercise every journey affected by this feature, including failure paths. Report criteria as verified, failed or unverified with evidence and blockers.

## 6. Review

Use $addy-code-review-and-quality on all feature changes since the recorded baseline, including scoped committed and uncommitted work. Compare against the specification and standards. Return prioritized findings without edits.

For a consequential change: Use $pstack-interrogate on the same scope. Use independent reviewers, report actual model diversity, and synthesize Act On, Consider, Noted and Dismissed findings. Do not apply fixes.

## 7. Resolve and hand over

Use Addy's implementation/testing skills to fix confirmed Act On findings. Present trade-offs for Consider findings before expanding scope. Rerun affected checks and journeys; review material new changes.
Update task records and report acceptance status, evidence, remaining issues, unverified areas, and whether work is local or deployed.

## Optional quality bar

Use $addy-constraint-driven-development if no agreed quality bar exists. Propose relevant thresholds and enforcement, record my choices, and put missing checks in the plan. Reuse existing standards.

## Optional design checkpoint

Use $pstack-architect with checkpoint on [the unresolved architectural decision].
Compare structural alternatives and show interfaces, ownership and trade-offs. Record the recommended design in a document. Stop before implementation. After approval, let Addy update the plan and build.

## Optional impact check

Use $pstack-blast-radius on this feature's complete changes.
Trace downstream consumers and non-obvious contracts. Execute the facts safety depends on. Report proved, disproved and unproven assumptions with evidence. Return risks and useful regression checks without product edits.

## Optional recurring mistakes

Use $pstack-correct to identify repeated mistake classes supported by actual project history. Within the approved scope, prevent recurrence through architecture, types, lint/CI or meaningful tests before adding prose rules. Prove checks detect past mistakes.

## Optional verification maintenance

Use $pstack-maintain-verification-skill to check our saved map against source and live behavior. Fix drift only in the verification skill and owned harness. Report product regressions separately and preserve evidence. Publish only if authorized.

## Resume in a new chat

Read AGENTS.md, PROJECT.md, the active specification, tasks/plan.md and tasks/todo.md. Inspect current changes and verification evidence. Summarize the current state and next ready task, then continue within the previously recorded approved scope. Surface any missing approval or genuinely unresolved product decision.
