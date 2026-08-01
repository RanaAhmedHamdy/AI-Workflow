# Data Flow map specification

## Checklist coverage

- Data flow and external integrations
- API/backend contracts
- Domain and feature ownership boundaries
- Project-specific lesson identity and variable-activity contracts

Application/module structure remains owned by the reviewed project
`ARCHITECTURE.md` and `MODULES.md`; link instead of duplicating them.

## Discovery question

How do lesson content, progress, notebook notes, completion state, route
arguments, and placeholder purchase/settings data move through repositories,
ViewModels, Routes, Screens, DataStore, and Hilt?

## Required evidence

- `data/LessonOrder.kt`, `data/LessonContentDays.kt`, and `data/FakeCampData.kt`
- repository interfaces and implementations
- `di/RepositoryModule.kt` and qualifiers
- guided completion and Today selection logic
- relevant ViewModels and Route composables
- route parsing and transport
- reviewed Guided Lesson, Today, Notebook, Progress, Parent Settings,
  Completion, Navigation, Architecture, and Testing pages
- relevant repository, DataStore, selector, ViewModel, guided, and route tests

## Required content

- lesson catalog assembly and canonical metadata ownership
- lesson-ID/day-number/activity-ID roles and fallback behavior
- progress read/write and derived consumer flows
- guided completion write-before-navigation source ordering
- transient Activity Completion versus persisted Lesson Completed
- notebook draft/persistence and independent clearing
- route argument transport and selection
- Hilt/provider/lifetime boundaries
- fake purchase/settings flows and absent real integrations
- data ownership/lifetime/error matrix
- small end-to-end diagrams
- static, local-test, runtime, backup/migration, and concurrency evidence limits

Treat absent backend/network/API flows as `Not observed` only after checking the
manifest, build files, repository contracts, and current source.
