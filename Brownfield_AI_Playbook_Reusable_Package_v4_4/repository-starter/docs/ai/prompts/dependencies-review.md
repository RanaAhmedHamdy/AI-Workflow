# Common rules

- Work on exactly one requested document.
- Graphify is a discovery aid, not architecture authority.
- Verify every material claim against current source, tests, build files, or reviewed project documents.
- Apply `docs/ai/GRAPHIFY_USAGE.md` and `docs/ai/graphify-context-overrides.tsv`.
- Do not edit production code, tests, AGENTS.md, existing product documents, Graphify installation files, or `graphify-out/`.
- Do not mark the target document reviewed during creation.
- Record provenance, inspected revision, commands run, exclusions, and Needs verification.
- Repository-relative paths only; never use `file://` links.
- You may use bounded research subagents. Subagents must not edit files. One main agent synthesizes and writes the target document.

# Task: Review DEPENDENCIES.md

Review only:

`docs/wiki/project/DEPENDENCIES.md`

Do not edit it.

Check:
- declared versus resolved version confusion;
- dependencies listed without source evidence;
- missing major plugins or libraries;
- transitive dependencies presented as direct;
- unused dependency claims without verification;
- future technologies presented as current;
- stale paths and weak provenance.

Return blocking findings, non-blocking findings, smallest revision scope, and promotion recommendation.
