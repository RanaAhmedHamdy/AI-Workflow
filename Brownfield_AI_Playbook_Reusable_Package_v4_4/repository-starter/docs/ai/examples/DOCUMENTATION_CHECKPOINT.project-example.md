# Documentation workflow checkpoint

**Status:** Active
**Purpose:** Record completed documentation phases and the next authorized documentation task.
**Authority:** Workflow state only. This file does not override `AGENTS.md`, source code, tests, reviewed project documentation, or explicit human decisions.

## Completed foundation documents

The following project-level documents have been generated:

* `docs/wiki/project/MODULES.md`
* `docs/wiki/project/FEATURE_MAP.md`
* `docs/wiki/testing/TESTING_MAP.md`
* `docs/wiki/project/DEPENDENCIES.md`
* `docs/wiki/project/PROJECT_OVERVIEW.md`
* `docs/wiki/project/ARCHITECTURE.md`

Before relying on any of these documents as reviewed context, confirm that its status is `Reviewed` or `Reviewed orientation`.

## Completed feature documents

The following feature documents have been generated:

* `docs/wiki/features/GUIDED_LESSON.md`
* `docs/wiki/features/TODAY.md`
* `docs/wiki/features/LESSONS_MAP.md`
* `docs/wiki/features/LESSON_OVERVIEW.md`
* `docs/wiki/features/ACTIVITIES_LIST.md`
* `docs/wiki/features/ACTIVITY_DETAIL.md`
* `docs/wiki/features/PARENT_SCRIPTS.md`
* `docs/wiki/features/NOTEBOOK.md`
* `docs/wiki/features/ACTIVITY_COMPLETION.md`
* `docs/wiki/features/LESSON_COMPLETED.md`
* `docs/wiki/features/PROGRESS.md`
* `docs/wiki/features/PARENT_SETTINGS.md`
* `docs/wiki/features/UNLOCK_BUNDLES.md`
* `docs/wiki/features/WELCOME.md`
* `docs/wiki/features/NAVIGATION.md`

## Feature documentation re-review batch

This bounded batch was explicitly authorized to re-review all existing feature
pages sequentially. The shared test command was
`./gradlew test --console=plain`; it completed successfully in 34 seconds with
`65 actionable tasks: 65 up-to-date`. Both unit-test variants were
`UP-TO-DATE`, so the invocation did not freshly execute test methods.

| Feature page | Result | Reviewed revision | Unresolved blocker |
|---|---|---|---|
| `docs/wiki/features/GUIDED_LESSON.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/TODAY.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/LESSONS_MAP.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/LESSON_OVERVIEW.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/ACTIVITIES_LIST.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/ACTIVITY_DETAIL.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/PARENT_SCRIPTS.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/NOTEBOOK.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/ACTIVITY_COMPLETION.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/LESSON_COMPLETED.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/PROGRESS.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/PARENT_SETTINGS.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/UNLOCK_BUNDLES.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/WELCOME.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |
| `docs/wiki/features/NAVIGATION.md` | Reviewed | `0edffddfc8f1451aace500a9c55b4e4e019832c8` | — |

## Current phase

Phase 7 Interface Localization & RTL Verification, and Curriculum Localization Seam complete. The P3.5-Q10 interface localization, RTL support, in-app English/Arabic switcher, dedicated settings DataStore persistence (`settings_preferences`), unit tests (146 debug and 146 release unit tests, 0 failures/errors), connected instrumentation tests (5/5 passed on Android 11 API 30 AVD), debug APK build, and project-owner manual test verification are complete. Its durable records `docs/review/PHASE_7_LOCALIZATION_RTL_VERIFICATION.md` and `docs/review/PHASE_7_CURRICULUM_LOCALIZATION_SEAM_VERIFICATION.md` have status `Reviewed` following explicit verification and review on 2026-07-30.

P3.5-Q01 Batch 1 and Batch 2 are implemented with pre-Batch-3 corrections. Batch 1 now exposes the exact production `NavigationBackStackSaver` to focused JVM tests and covers a detail route plus parent Back across Activity recreation; actual process death remains `Needs verification`. Batch 2 uses `widthIn(max = 720.dp)` before `fillMaxWidth()` and has controlled 1024dp-parent/720dp-content/152dp-margin tests plus Compact/Medium/Expanded navigation tests in explicit light and dark themes. Fresh verification passed 149/149 debug and 149/149 release JVM tests, `assembleDebug`, and 14/14 connected tests on API 30 AVD `Medium_Phone_API_30_android11`.

## Next authorized task

Stand ready for the next project-owner workflow directive (P3.5-Q01 Batch 3: Adaptive Insets, IME & Orientation Reflow — Notebook, Landscape & Large Text). Batch 3 has not started.

Further source modifications beyond the completed pre-Batch-3 correction scope, curriculum translation, editorial review, or release actions remain prohibited until authorized.

The Phase 3.4 architecture coverage review has final result
`Pass with routed Needs verification`. Its durable record was separately
reviewed at revision `9127c9a7bb5c700a8f673d69efc222b10fcf7a27`, approved
without blocking correction, and promoted to Reviewed.

## Planned feature-page sequence

Complete. The re-review table above is the current feature inventory and
supersedes the earlier planned sequence.

## Cross-feature architecture phase

After at least the Guided Lesson, Today, Notebook, and Progress feature pages have been reviewed, create these architecture maps one at a time:

1. `docs/wiki/architecture/DATA_FLOW.md`
2. `docs/wiki/architecture/STATE_MANAGEMENT.md`
3. `docs/wiki/architecture/PERSISTENCE_AND_CACHE.md`
4. `docs/wiki/architecture/NAVIGATION.md`
5. `docs/wiki/architecture/DEPENDENCY_INJECTION.md`
6. `docs/wiki/architecture/ERROR_HANDLING.md`
7. `docs/wiki/architecture/DESIGN_SYSTEM_AND_UI_COMPONENTS.md`
8. `docs/wiki/architecture/UI_ADAPTATION_AND_ACCESSIBILITY.md`
9. `docs/wiki/architecture/CONFIGURATION_AND_ENVIRONMENTS.md`
10. `docs/wiki/architecture/SECURITY_BOUNDARIES.md`
11. `docs/wiki/architecture/BUILD_AND_RELEASE.md`
12. `docs/wiki/architecture/CODE_STYLE_AND_CONVENTIONS.md`
13. `docs/wiki/testing/TESTABILITY_ROADMAP.md`

Do not create architecture maps merely to complete a list. Each map must be justified by reviewed feature evidence and current source.

`docs/ai/architecture-docs.tsv` is the canonical order and prompt-routing
manifest for this phase. Each entry has a focused scope specification under
`docs/ai/architecture-specs/`. `scripts/run-architecture-doc.sh` may render the
authorized create, read-only review, or promotion prompt for one map at a time;
it does not invoke Codex or advance workflow state.

`docs/ai/architecture-coverage-routing.tsv` maps every canonical checklist
concern to an existing or planned current home. It is planning/routing input,
not a completed Phase 3.4 classification.

Each map follows three separate passes:

1. create it as Draft;
2. perform a read-only documentation review;
3. promote it only after that review recommends promotion without blocking
   corrections.

Checklist concerns that have an adequate current home or are not observed must
be classified during Phase 3.4 rather than converted into empty documents.

The Phase 3.4 architecture coverage gate was performed after the applicable
architecture maps were drafted and separately reviewed. Its durable record is
`docs/review/PHASE_3_4_ARCHITECTURE_COVERAGE.md`, now Reviewed after a separate
read-only documentation review approved it without blocking correction.

## Decision and verification phase

After the feature and architecture pages reveal unresolved choices, record only decisions that unblock concrete work.

Decision records should include:

* decision;
* decided by;
* date;
* evidence or link;
* current scope;
* tests or fixes authorized now;
* remaining Needs verification;
* documentation affected.

Do not invent decisions from existing implementation.

## No-edit implementation audit

After the relevant feature page and architecture maps are reviewed, perform a no-edit audit of one bounded feature.

Classify findings as:

* Aligned and covered
* Aligned but uncovered
* Partially aligned
* Contradicts contract
* Not implemented
* Needs runtime or backend verification
* Deferred or inactive path
* No safe seam

Recommend exactly one next implementation or testing action.

## Skills phase

Create project-specific skills only after repeated verified workflows are clear.

Likely candidates:

* `guided-lesson-changes`
* `lesson-content-validation`
* `viewmodel-repository-changes`
* `datastore-persistence-changes`
* `compose-resource-and-layout-review`

Core reusable skills may include:

* `protected-boundary-preflight`
* `documentation-review`
* `documentation-impact-assessment`
* `characterization-tests`
* `pr-review`

Skills must describe verified project procedures. They must not become another copy of architecture documentation.

## Workflow rules

* Work on one document or one bounded audit at a time.
* Use one main writer; research subagents must remain read-only.
* Run a separate no-edit review after each document is created.
* Do not automatically mark a page reviewed.
* Do not automatically continue to the next phase.
* Do not edit `graphify-out/graph.json` manually.
* Do not treat Graphify as architecture authority.
* Do not claim runtime behavior from static inspection alone.
* Keep temporary audit output outside durable documentation unless its findings are approved for capture.

## Resume instruction for Codex

Before continuing documentation work:

1. Read `AGENTS.md`.
2. Read `docs/ai/GRAPHIFY_USAGE.md`.
3. Read this checkpoint.
4. Confirm the completed foundation files and their statuses.
5. Run only the next authorized task.
6. Stop after showing the resulting diff.

## Resume instruction for future conversations

The foundation maps and feature re-review batch are complete.
`docs/wiki/architecture/DATA_FLOW.md`, `docs/wiki/architecture/STATE_MANAGEMENT.md`,
`docs/wiki/architecture/PERSISTENCE_AND_CACHE.md`, `docs/wiki/architecture/NAVIGATION.md`,
`docs/wiki/architecture/DEPENDENCY_INJECTION.md`, and
`docs/wiki/architecture/ERROR_HANDLING.md`, and
`docs/wiki/architecture/DESIGN_SYSTEM_AND_UI_COMPONENTS.md`, and
`docs/wiki/architecture/UI_ADAPTATION_AND_ACCESSIBILITY.md`, and
`docs/wiki/architecture/CONFIGURATION_AND_ENVIRONMENTS.md`, and
`docs/wiki/architecture/SECURITY_BOUNDARIES.md`, and
`docs/wiki/architecture/BUILD_AND_RELEASE.md`, and
`docs/wiki/architecture/CODE_STYLE_AND_CONVENTIONS.md` have been promoted to
Reviewed. `docs/wiki/testing/TESTABILITY_ROADMAP.md` has also been promoted to
Reviewed. All planned Phase 3 architecture maps are now Reviewed.

The Phase 3.4 architecture coverage review has been performed. Its durable
record is `docs/review/PHASE_3_4_ARCHITECTURE_COVERAGE.md`, with status
Reviewed and result `Pass with routed Needs verification`.

Phase 3.5 owner-question capture has begun with the first bounded
progress/notebook data, backup and direct device-transfer, retention,
privacy-wording, and state-restoration bundle. Its decision packet is
`docs/review/PHASE_3_5_VERIFICATION_QUESTIONS.md`. The project owner answered
all four questions on 2026-07-29. Only the Q03/Q12 backup configuration and
truthful-copy implementation scope was authorized and completed; Q02/Q04 route
to later Phase 3.6 audits.

`docs/review/PHASE_3_5_VERIFICATION_QUESTIONS.md` was separately reviewed at
revision `62a7e3b8b4366a9ee79e16d45e07ca2e18e2db5a`, approved without blocking
correction, and promoted to Reviewed.

`docs/review/PHASE_3_5_VERIFICATION_QUESTIONS_BUNDLE_2.md` was separately re-reviewed on 2026-07-29, approved without blocking corrections, and promoted to Reviewed.

`docs/review/PHASE_3_5_VERIFICATION_QUESTIONS_BUNDLE_3.md` was separately reviewed on 2026-07-29, approved without blocking corrections, and promoted to Reviewed. All 15 Phase 3.5 owner questions now have binding Reviewed decision records across Bundles 1, 2, and 3.

The Phase 7 system-following dark mode implementation, focused Compose integration tests (`ThemeCompositionTest`), unit tests, debug build, and runtime verification on Android 11 AVD (`sdk_gphone_arm64`) are complete. Its durable record `docs/review/PHASE_7_DARK_MODE_VERIFICATION.md` has status `Reviewed` following explicit owner review and promotion.

The P3.5-Q01 Batch 1 (Window Size Class Seam & Saver-backed Activity-recreation restoration seam) and Batch 2 (Adaptive Navigation & Layout Shell for explicit Medium/Expanded classes with controlled 720dp max-width behavior) implementations and pre-Batch-3 corrections are complete. Fresh evidence is 149/149 debug and 149/149 release JVM tests, successful debug APK assembly, and 14/14 connected tests on one Compact-width API 30 phone AVD. Actual process death, named Medium/Expanded running-app inspection, real resize/multi-window, foldable posture, ChromeOS, and non-touch input remain `Needs verification`.

The exact next authorized implementation task is P3.5-Q01 Batch 3: Adaptive Insets, IME & Orientation Reflow — Notebook, Landscape & Large Text.
