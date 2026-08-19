# Common rules

- Work on exactly one requested document.
- Graphify is a discovery aid, not architecture authority.
- Verify every material claim against current source, tests, build files, or reviewed project documents.
- Apply `docs/ai/GRAPHIFY_USAGE.md`. Graphify output is optional.
- If `docs/ai/graphify-context-overrides.tsv` exists, apply only directly relevant verified rows.
- Do not edit production code, tests, AGENTS.md, existing product documents, Graphify installation files, or `graphify-out/`.
- Do not mark the target document reviewed during creation.
- Record provenance, inspected revision, commands run, exclusions, and Needs verification.
- Repository-relative paths only; never use `file://` links.
- You may use bounded research subagents. Subagents must not edit files. One main agent synthesizes and writes the target document.

# Task: Create ARCHITECTURE.md

Create only:

`docs/wiki/project/ARCHITECTURE.md`

Prerequisites:
- MODULES.md reviewed;
- FEATURE_MAP.md reviewed;
- TESTING_MAP.md reviewed;
- DEPENDENCIES.md reviewed;
- PROJECT_OVERVIEW.md reviewed.

Use current source plus those reviewed maps.

Include:
- architecture goals and constraints;
- major layers and ownership;
- data/content flow;
- state ownership;
- repository abstraction;
- persistence boundaries;
- DI boundaries;
- navigation model;
- Route/Screen organization;
- testing seams;
- cross-feature contracts;
- known exceptions;
- active versus future architecture;
- protected boundaries;
- Needs verification;
- provenance.

Rules:
- Describe current architecture first.
- Label approved direction separately from implemented evidence.
- Do not infer runtime Hilt behavior from provider declarations alone.
- Do not invent backend, Room, billing, login, camera, sharing, or cloud architecture.
- Do not turn this into a redesign proposal.
- If the target already exists as `Draft`, revise only that file using current evidence and supplied review findings.
- Set status to Draft.
- Show the final diff.
