# Baseline validation

Validated on 18 October 2026 on Windows with Python 3.12.10, Git Bash, Node, and Codex CLI 0.162.1.

This report concerns the reusable baseline. It is not acceptance evidence for any future product built from it.

## Observed results

| Check | Result |
|---|---|
| Complete catalog | 121 entries: Matt 38, Addy 25, Pstack 58 |
| Official skill-creator quick_validate.py | 121 passed; zero failures |
| Codex UI metadata and invocation policies | 80 explicit-only, 41 automatic-or-explicit; source policies preserved |
| Bundled structural/integrity validator | Passed: entrypoints, unique names, catalog consistency, real Markdown resource links, required documents and licenses |
| Preserved upstream snapshots | 578 SHA-256 checks passed; original Git blob hashes also verified when fetched |
| Native explicit loader | All five requested main entrypoint bodies attached successfully; no missing attachments |
| Bundled shell helpers | Six Bash syntax checks passed |
| Bundled JavaScript helper | One Node syntax check passed |
| Modified worktree-audit helper | Executed successfully on a Git worktree whose path contains spaces; full path preserved, local refs unchanged, no remote fetch/PR lookup/private transcript scan |
| Package portability | Passed: archive CRC check and extracted-folder validator; 121 skills and 578 source snapshots verified after relocation |

The native loader test explicitly requested pstack-create-verification-skill, pstack-blast-radius, pstack-interrogate, matt-grill-with-docs, and addy-spec-driven-development. Four explicit-only skills were absent from startup model context as expected, then all five bodies loaded via native explicit mentions. A separate CLI shell-inspection attempt was restricted by local execution policy; the explicit-loader check required no shell calls. File validation was performed from the main session.

## Practical forward tests

### pstack-create-verification-skill

An independent evaluator received a small runnable Field Notes CLI and the skill, without an intended solution. It generated:
- A valid Codex verify-field-notes skill.
- Launch/doctor/drive/evidence/cleanup instructions and executable helper.
- A map covering create, search and delete.
- A proved create/list/persistence journey.

Doctor, the official validator, and prove-add exited 0. The harness executed the actual CLI through help, empty list, add and a fresh-process list; an independent file read confirmed persistence. Owned scratch data was removed and proof survived cleanup. AC-01 was proved; AC-02 and AC-03 were mapped and explicitly unverified. Fixture product sources were unchanged.

### pstack-blast-radius

An independent evaluator assessed a timestamp-support change against the specified baseline, including an untracked consumer. Its executable probes found:
- Alerts crash when timezone information is stripped and naive/aware times are subtracted.
- Exports exit successfully while silently losing timezone information.

Three baseline checks passed and twelve current safety checks failed across Z, positive-offset and negative-offset inputs. These failures are the intended detection outcome of the assessment, not a failing skill implementation. Real CLI runs confirmed the crash and the export violation. Product hashes remained unchanged.

### pstack-interrogate

A separate coordinator applied the skill and sent the same raw fixture, specification and reviewer guidance to two fresh-context reviewers. Neither reviewer received the other's findings or the author's preferred answer. They independently identified the alert and export failures; the lead verified and merged them under the parser root cause and returned request changes.

The panel selected inherited-model delegates. Exact runtime model identity and diversity were unobservable, so this validates independent-context review, not a cross-family model panel. Six product-file hashes matched before and after. No product fixes were applied.

## Independent compatibility audit

The source/dependency audit found and prompted corrections to model-role JSON consumption, namespaced helper paths, Codex skill-generation and reflection paths, setup/help text, Bun bootstrap prerequisites, spaced worktree paths, and the three dormant Benny procedures. The final manual Benny preflight consumes a shared project configuration, validates required fields against the bundled source example, and requires confirmed source coordinates and actual tools before proceeding.

## Limits

- The full catalog received structural/resource/policy validation. All 121 workflows were not behaviorally exercised.
- The three Pstack workflows above received practical controlled tests. The five named entrypoints received a native explicit-loader check; this is not an execution test of Matt's full interview or Addy's full build lifecycle.
- No browser/device/production deployment, external tracker/Slack operation, unattended automation, formal proof system, external-model CLI, or Bun-dependent orchestration was exercised.
- Claude-only hooks do not enforce Codex permissions. Source Bash helpers require compatible Bash unless an appropriate alternative is implemented and tested.
- Seven Matt in-progress skills remain experimental. Three Pstack dormant-pack procedures remain conditional integrations.
- Original snapshots and licenses are preserved. Local adaptations are unofficial; platform and source changes require revalidation.

Historical proof records are under [validation-evidence](validation-evidence/). Machine-specific paths are replaced by symbolic roots in these shareable copies; original execution records were inspected before copying.

## Getting-started guide update — 19 October 2026

Added GETTING-STARTED.md with the IoT Incident Console example, fourteen numbered messages, an optional blast-radius prompt, and a resume prompt. The README links to the guide.

Checked all sixteen prompt blocks, all referenced namespaced skills against the catalog, and local links in the guide and README. Re-ran the structural/source-integrity validator and ZIP extraction validation when packaging this documentation update. No skill behavior was changed, and the practical forward-test results above remain historical results from 18 October 2026.
