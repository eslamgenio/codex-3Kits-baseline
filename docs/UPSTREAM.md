# Upstream provenance and adaptation

Pinned on 18 October 2026:

| Library | Commit | Skills |
|---|---|---|
| Matt Pocock | 49dd158d1076134a641b33efb035946536778336 | 38 |
| Addy Osmani | aeac41d4d005999432bb7312f7ff06383a91d59d | 25 |
| Pstack | 0148b78c56c72a1b8412055913c79f767095b217 | 58 |

Sources:
- https://github.com/mattpocock/skills
- https://github.com/addyosmani/agent-skills
- https://github.com/cursor/plugins/tree/main/pstack

All tracked regular source files from Matt/Addy and the Pstack subtree are preserved in vendor/. File bytes are unchanged; instruction filenames SKILL.md, AGENTS.md and CLAUDE.md become *.upstream.md. Tracked source symlinks are preserved as inert text containing their target, not live links. The catalog records SHA-256 hashes for snapshot integrity. The fetch process additionally checked each original Git blob hash against the pinned source tree.

Matt includes 20 engineering, 7 productivity, 4 miscellaneous and 7 in-progress skills. Only the first 27 are promoted by its primary plugin; the extra entries are included because this baseline requests the complete repository skill set. Addy's root references and all skill-local resources are retained.

Active skills use matt-, addy-, and pstack- prefixes. Cross-skill mentions and resolvable local resource links are mapped to the namespaced catalog. Host-only frontmatter is translated into Codex metadata, preserving explicit-only invocation. Original content remains available for comparison.

The three requested Pstack workflows have self-contained Codex implementations. The rest use the upstream procedure with an explicit shared Codex adapter and, where necessary, a per-skill capability adjustment. This is a compatibility layer, not evidence that every external integration or optional workflow has executed.

The baseline does not install Claude hooks, Cursor rules, external MCP servers, model CLIs, accounts, auto-update hooks, automations, CI, or a product stack. It does not convert upstream Bash into universally portable PowerShell.

Licenses are copied under licenses/. Pstack copyright 2026 Lauren Tan; other notices are preserved verbatim in their respective MIT license files. Adapted files include source provenance. This is an unofficial local adaptation.

Pstack's 58 entries comprise 55 normal skill-root entries and three dormant Benny pack procedures, imported as clearly marked conditional Codex skills. They do not activate background automation.

Active helper adjustments preserve source snapshots: worktree-audit.sh retains spaced paths and uses local metadata without fetching remote refs, querying PR APIs or scanning private Cursor transcripts. Node/Bun helper prerequisites and first-run installation behavior are disclosed. Concrete helper paths are mapped to the namespaced installation.

Native Codex explicit invocation was exercised for the five main discovery/specification/verification/review entrypoints. Explicit-only entries can be absent from startup context while still loading successfully through native explicit mentions.
