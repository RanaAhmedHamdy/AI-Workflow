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

# Task: Review TESTING_MAP.md

Review only:

`docs/wiki/testing/TESTING_MAP.md`

Do not edit it.

Check:
- tests claimed to pass without execution evidence;
- overclaims about what unit tests prove;
- missing actual test files;
- roadmap intentions confused with implemented coverage;
- missing device/UI/runtime gaps;
- persistence and migration overclaims;
- weak provenance;
- stale commands or paths.

Return blocking findings, non-blocking findings, smallest revision scope, and promotion recommendation.
