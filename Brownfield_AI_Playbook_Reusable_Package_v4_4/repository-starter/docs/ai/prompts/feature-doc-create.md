\
# Feature documentation creation prompt

You are documenting one existing Android feature. This is a documentation-only task.

## Inputs supplied by the runner

- Feature ID: `{{FEATURE_ID}}`
- Feature name: `{{FEATURE_NAME}}`
- Output file: `{{OUTPUT_PATH}}`
- Current Git revision: `{{GIT_REVISION}}`

## Read first

1. `AGENTS.md`
2. `docs/ai/GRAPHIFY_USAGE.md`
3. `docs/ai/DOCUMENTATION_CHECKPOINT.md`
4. `docs/wiki/project/PROJECT_OVERVIEW.md`
5. `docs/wiki/project/MODULES.md`
6. `docs/wiki/project/FEATURE_MAP.md`
7. `docs/wiki/project/DEPENDENCIES.md`
8. `docs/wiki/project/ARCHITECTURE.md`
9. `docs/wiki/testing/TESTING_MAP.md`
10. Relevant authoritative files under `ai-context/`, especially:
   - `PRODUCT_REQUIREMENTS.md`
   - `CONTENT_SCHEMA.md`
   - `DESIGN_SYSTEM.md`
   - `ROADMAP.md`

Read an existing reviewed feature page such as
`docs/wiki/features/GUIDED_LESSON.md` for structure and evidence style.

## Task

Create or update only:

`{{OUTPUT_PATH}}`

Document the current implementation of **{{FEATURE_NAME}}**.

Use Graphify only for bounded discovery. Verify every material claim against
current source, tests, build files, or reviewed documentation. Absence of a
Graphify relationship is not evidence of absence.

## Allowed inspection

Inspect only the files identified for this feature by `FEATURE_MAP.md`, plus
directly related:

- routes and route parsing;
- Route and Screen composables;
- ViewModels and UI-state models;
- repositories and implementations;
- domain/data models and derivation helpers;
- persistence keys and data stores;
- navigation callbacks and destinations;
- unit or instrumented tests;
- build configuration only when necessary to verify a claim.

Expand scope only when required to verify a material dependency. State the
reason in the final summary.

## Required document sections

Use sections that fit the feature, covering at minimum:

1. Status, reviewed revision, and scope
2. Product contract
3. Entry routes and navigation wiring
4. Route composable
5. Screen composable
6. ViewModel, state ownership, and constructor dependencies
7. Repository/data/persistence flow
8. Active implementation behavior
9. Placeholder, partial, or deferred behavior
10. Navigation matrix or important transitions
11. Tests and exact evidence they provide
12. Protected boundaries
13. Known gaps
14. Needs verification
15. Related documentation
16. Provenance and inspected revision

Clearly distinguish:

- verified current-source facts;
- product or owner intent;
- executed test evidence;
- static inspection limitations;
- recommendations;
- Needs verification.

Do not present a declaration, annotation, dependency, or test existence as
runtime proof. Do not claim a test proves more than its assertions.

## Editing boundaries

Do not modify:

- Kotlin, Java, XML, Gradle, resources, tests, or generated Graphify files;
- `AGENTS.md`;
- `ai-context/`;
- any other feature document;
- Git history, branches, remotes, commits, or tags.

Do not create an ADR, skill, hook, test, or source fix.

Do not change `docs/ai/DOCUMENTATION_CHECKPOINT.md` during creation. The
review pass owns checkpoint advancement.

## Completion

Before finishing:

- verify the output path is correct;
- ensure the page contains no invented implementation;
- ensure uncertain claims are marked `Needs verification`;
- show `git diff -- {{OUTPUT_PATH}}`;
- summarize inspected files, resulting document, and remaining verification
  items.

Stop after this one feature page.
