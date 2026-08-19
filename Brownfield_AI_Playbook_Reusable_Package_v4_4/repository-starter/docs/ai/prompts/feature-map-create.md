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

# Task: Create FEATURE_MAP.md

Create only:

`docs/wiki/project/FEATURE_MAP.md`

Use:
- current source and tests;
- `docs/wiki/project/MODULES.md`;
- product requirements, roadmap, content schema, and design system;
- Graphify query results when usable output exists;
- `docs/ai/GRAPHIFY_USAGE.md` and any existing directly relevant override rows.

For each current feature, include:
- feature name;
- product requirement source;
- status: implemented, partial, placeholder, deferred, or Needs verification;
- entry routes;
- Route composables;
- Screen composables;
- ViewModels;
- repositories and persistence;
- domain/helper logic;
- important source paths;
- relevant tests;
- protected boundaries;
- known gaps;
- Needs verification;
- related wiki pages.

Coverage rule:
- derive the feature inventory from current repository/product evidence rather than from example-project feature names;
- include every materially implemented, partial, placeholder, or explicitly deferred user-facing feature that is in scope for the receiving repository;
- if product authority and source disagree about whether a feature exists, record the discrepancy as `Needs verification` instead of inventing a status.

Rules:
- Do not describe planned behavior as implemented.
- Distinguish UI-only placeholders from functional capabilities.
- Confirm constructor dependencies directly.
- Confirm route/screen mappings directly.
- Confirm tests from actual test files.
- Keep this a map, not a duplicate PRD.
- If the target already exists as `Draft`, revise only that file using current evidence and supplied review findings.
- Set status to Draft.
- Show the final diff.
