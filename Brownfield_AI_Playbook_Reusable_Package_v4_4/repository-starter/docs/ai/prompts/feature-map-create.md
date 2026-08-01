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

# Task: Create FEATURE_MAP.md

Create only:

`docs/wiki/project/FEATURE_MAP.md`

Use:
- current source and tests;
- `docs/wiki/project/MODULES.md`;
- product requirements, roadmap, content schema, and design system;
- Graphify query results;
- Graphify usage and override files.

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

Cover at least:
Welcome/guest entry, Today, Lessons Map, Lesson Overview, Activities List,
Activity Detail, Guided Lesson, Parent Scripts, Notebook, Progress and badges,
Parent Settings, Unlock Bundles, Activity Completion, Lesson Completed,
Share Success preview, and main bottom navigation.

Rules:
- Do not describe planned behavior as implemented.
- Distinguish UI-only placeholders from functional capabilities.
- Confirm constructor dependencies directly.
- Confirm route/screen mappings directly.
- Confirm tests from actual test files.
- Keep this a map, not a duplicate PRD.
- Set status to Draft.
- Show the final diff.
