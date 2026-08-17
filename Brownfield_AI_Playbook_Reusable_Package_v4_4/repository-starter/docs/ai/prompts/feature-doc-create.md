# Feature documentation creation prompt

Document exactly one existing feature. This is a documentation-only task and is designed to run directly with any repository-aware AI coding agent; no runner is required.

## Resolve the selected feature

1. Read `docs/ai/feature-docs.tsv`.
2. Read `docs/ai/DOCUMENTATION_CHECKPOINT.md` when present.
3. If the checkpoint authorizes exactly one feature-document path, use that row from the manifest.
4. Otherwise select the first manifest row, in numeric order, whose output page does not exist or is not `Reviewed`, but only when the checkpoint contains no conflicting authorization.
5. If the manifest is missing, the selected row cannot be resolved, or repository state/checkpoint makes more than one target plausible, stop without editing and report what must be resolved.
6. Record the selected feature ID, display name, output path, and current Git revision before writing.

Do not select more than one feature.

## Read first

1. `AGENTS.md`
2. `docs/ai/GRAPHIFY_USAGE.md`
3. `docs/ai/DOCUMENTATION_CHECKPOINT.md` when present
4. `docs/ai/feature-docs.tsv`
5. `docs/wiki/project/PROJECT_OVERVIEW.md`
6. `docs/wiki/project/MODULES.md`
7. `docs/wiki/project/FEATURE_MAP.md`
8. `docs/wiki/project/DEPENDENCIES.md`
9. `docs/wiki/project/ARCHITECTURE.md`
10. `docs/wiki/testing/TESTING_MAP.md`
11. Relevant authoritative product/design/context documents configured by the repository
12. One existing reviewed feature page, when available, for structure and evidence style

## Task

Create or revise only the selected manifest output path. Document that feature's current implementation.

Use Graphify only for bounded discovery. Verify every material claim against current source, tests, build files, or reviewed documentation. Absence of a Graphify relationship is not evidence of absence.

Inspect only the files identified for the feature by `FEATURE_MAP.md`, plus directly related routes/navigation, UI/screen files, state owners, repositories, models/helpers, persistence, tests, and build configuration needed to verify a material claim. Expand scope only when required to verify a dependency, and state why.

Cover at minimum:
- status, reviewed/inspected revision, and scope;
- product contract and current implemented behavior;
- entry routes and navigation wiring;
- UI/screen composition and state ownership;
- constructor dependencies;
- repository/data/persistence flow;
- active, partial, placeholder, or deferred behavior;
- important transitions;
- tests and the exact evidence they provide;
- protected boundaries;
- known gaps and `Needs verification`;
- related documentation and provenance.

Clearly distinguish verified source facts, product/owner intent, executed test evidence, static-inspection limits, recommendations, and `Needs verification`. Do not claim a declaration, annotation, dependency, or test existence proves runtime behavior.

## Editing boundaries

Do not modify source, tests, build configuration, resources, generated Graphify files, `AGENTS.md`, product/context authority, another feature page, the checkpoint, or Git history/remotes. Creation owns only the selected feature page; review owns checkpoint advancement.

Set the selected page to `Draft`. If it already exists as `Draft`, revise only that page using current evidence and supplied review findings.

## Completion

- verify the selected output path matches the manifest;
- show `git diff -- <selected-output-path>`;
- summarize selected manifest row, evidence inspected, and remaining verification items;
- state that the next task is a fresh run of `docs/ai/prompts/feature-doc-review.md`;
- stop after this one feature page.
