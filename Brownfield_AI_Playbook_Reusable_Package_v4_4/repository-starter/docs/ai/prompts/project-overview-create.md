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

# Task: Create PROJECT_OVERVIEW.md

Create only:

`docs/wiki/project/PROJECT_OVERVIEW.md`

Use reviewed:
- MODULES.md
- FEATURE_MAP.md
- TESTING_MAP.md
- DEPENDENCIES.md
and current authoritative product/design documents.

Include:
- product and users;
- current implemented scope;
- platforms and technology;
- major capabilities;
- system boundaries;
- current maturity;
- active versus placeholder areas;
- protected boundaries;
- known risks and uncertainty;
- links to authoritative detailed pages.

Rules:
- Summarize; do not duplicate full PRD, design system, or architecture.
- Separate product intent from implemented evidence.
- Do not promote unresolved behavior to fact.
- If the target already exists as `Draft`, revise only that file using current evidence and supplied review findings.
- Set status to Draft.
- Show the final diff.
