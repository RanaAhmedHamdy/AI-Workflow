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

# Task: Review ARCHITECTURE.md

Review only:

`docs/wiki/project/ARCHITECTURE.md`

Do not edit it.

Check:
- current versus planned architecture confusion;
- dependency direction errors;
- unsupported runtime claims;
- duplicated feature details;
- Graphify omissions treated as absent dependencies;
- missing exceptions and protected boundaries;
- missing testing seams;
- accidental redesign recommendations;
- weak provenance or unresolved verification.

Return blocking findings, non-blocking findings, smallest revision scope, and promotion recommendation.
