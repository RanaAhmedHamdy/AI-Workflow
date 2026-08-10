# Skill: Android Implementation Task Authoring v1

## Purpose

Generate a dependency-ordered, reviewable Android implementation task set from an owner-approved feature contract and owner-approved implementation plan.

This skill creates task definitions only. It must not create production code, tests, Gradle configuration, manifests, resources, schemas, migrations, project files, or evidence artifacts.

## Preconditions

Verify:

- feature contract is owner-approved;
- implementation plan is owner-approved;
- implementation-plan review is `PASS`;
- unresolved product decisions are closed;
- unresolved technical decisions that block decomposition are closed;
- applicable readiness and governance documents are synchronized;
- Android architecture decisions required by the feature are accepted;
- exact design authority exists;
- evidence policy and task template are current.

If any prerequisite is missing, stop with the appropriate verdict.

## Required Inputs

Read:

- `AGENTS.md` or root repository policy;
- context router;
- playbook;
- owner decision register;
- approved feature contract;
- approved implementation plan;
- feature map;
- Android architecture spine;
- applicable ADRs;
- readiness gate;
- design authority;
- screen contracts;
- exact artifact index/artifacts;
- evidence policy;
- task template.

## Required Output

Create or update:

`docs/features/<feature-id>/IMPLEMENTATION_TASKS.md`

Use:

`.templates/mobile/IMPLEMENTATION_TASKS_TEMPLATE.md`

Return one:

- `READY FOR TASK REVIEW`
- `BLOCKED BY PLAN ISSUE`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

Do not grant implementation authorization.

## Core Rules

### 1. Contract and Plan Bound Every Task

Every task must trace to:

- one or more approved contract requirement IDs; and
- one or more approved implementation-plan sections.

Do not add behavior, modules, screens, dependencies, permissions, services, resources, technical choices, or release work absent from approved authority.

### 2. One Bounded Outcome per Task

A task should deliver one coherent outcome that can be independently reviewed and verified.

Split tasks when they combine unrelated:

- Gradle/module/resource structure;
- domain behavior;
- dependency composition;
- persistence/migration;
- use cases;
- ViewModel/presentation state;
- navigation/lifecycle/restoration;
- Compose/View screen implementation;
- localization/RTL;
- accessibility/adaptation;
- permissions/manifest/background components;
- runtime evidence;
- documentation.

Do not create giant “implement feature” tasks or trivial evidence-free symbol tasks.

### 3. Dependency Order Must Be Explicit and Acyclic

Define a directed acyclic graph.

Typical order, adapted to accepted architecture:

1. bounded module/source/resource structure;
2. domain values and invariants;
3. repository contracts;
4. dependency-composition interfaces/bindings;
5. persistence entities/DAOs/adapters and migrations;
6. use cases;
7. ViewModel/presentation state;
8. navigation, lifecycle, and restoration composition;
9. screen implementation and previews;
10. localization and RTL;
11. accessibility and adaptive behavior;
12. permissions/background/protected boundaries where applicable;
13. automated tests and runtime evidence;
14. convergence review.

Prerequisites must precede consumers. Adapt order only when the approved plan requires it.

### 4. Tasks May Name Concrete Android Artifacts Carefully

Tasks may name:

- Gradle modules and source sets;
- package directories;
- expected Kotlin types;
- resource files and keys;
- manifest ownership;
- ViewModels, repositories, DAOs, use cases, composables, Fragments, Activities, adapters, workers, services, receivers, or providers;
- test source sets;
- commands and evidence outputs.

Only do so when names are established by the approved plan, accepted repository conventions, or architecture authority.

Do not invent names merely to appear precise.

### 5. No Architecture Reopening

Tasks must apply accepted ADRs.

Do not create tasks to reconsider:

- Compose versus Views;
- ViewModel/state model;
- DI framework/composition approach;
- coroutine/Flow model;
- navigation strategy;
- persistence engine;
- module structure;
- localization approach;
- permission/capability boundary;
- background execution strategy;
- security/release boundary;

unless the approved plan explicitly contains an unresolved decision task.

### 6. Verification Is Part of Every Task

Each task must define:

- acceptance criteria;
- test/evidence layer;
- exact command/procedure;
- environment/destination;
- expected observable result;
- evidence path;
- known limitation.

A task is not complete merely because Kotlin files, resources, manifest entries, modules, previews, or tests exist.

### 6A. Verification-Matrix Mapping and Current-State Integrity

- Every task that implements or proves matrix-covered behavior must list `Verification Matrix Coverage` with the applicable approved `VM-*` IDs from the implementation plan, or an explicit `N/A` rationale when no matrix scenario applies.
- Do not copy the full matrix scenario into each task; reference stable IDs and keep the detailed definition authoritative in the approved plan.
- Do not invent new `VM-*` IDs in the task set.
- Keep current task-set lifecycle/status/authorization truth in one canonical status block. Historical authoring/review verdicts may remain only when clearly labeled as stage-specific history; they must not contradict the current state.

### 7. Android Cross-Cutting Requirements Are First-Class

Do not defer these to final polish:

- localization and approved RTL locales;
- TalkBack and accessibility semantics;
- adaptive/resizable/foldable UI;
- IME/system insets/cutouts;
- ViewModel and lifecycle ownership;
- coroutine cancellation and Flow lifetime;
- dependency injection/composition;
- persistence integrity/migrations/process-death recovery;
- privacy/permissions/manifest boundaries;
- production-fake detection;
- previews for representative states;
- runtime evidence.

Integrate them into relevant tasks and retain final convergence tasks.

### 8. UI Task Requirements

Every route/screen task must state, as applicable:

- screen contract and exact artifacts;
- route/container versus stateless/render boundary;
- approved state holder/ViewModel lifetime;
- immutable UI-state and event contract;
- no repositories/DAOs/clients/routers in leaf UI;
- no side effects during composition/rendering;
- loading, empty, populated, disabled, failure, recovery, offline, and success states;
- preview fixtures for representative states;
- compact/medium/expanded and resized behavior;
- IME/insets/overflow;
- RTL and long-text behavior;
- TalkBack/focus/touch/input behavior;
- runtime evidence beyond previews.

### 9. ViewModel and Coroutine Task Requirements

Applicable tasks must enforce:

- lifecycle-aware ViewModel ownership;
- no state-holder recreation during recomposition;
- immutable exposed state;
- explicit events;
- structured concurrency;
- dispatcher ownership/injection;
- lifecycle-aware Flow collection;
- cancellation propagation;
- durable work not cancelled solely by screen disappearance;
- no `GlobalScope` or unowned jobs;
- bounded terminal states;
- focused state-transition tests.

### 10. Dependency Composition Task Requirements

Applicable tasks must enforce:

- one production composition path;
- approved scopes/lifetimes;
- constructor injection/accepted binding path;
- deterministic test replacements;
- deterministic preview replacements;
- no service locator/global singleton;
- no ad hoc creation in UI;
- no fake/debug/test bindings in release graph;
- missing required configuration fails closed.

### 11. Persistence Task Requirements

Applicable tasks or acceptance criteria must cover:

- schema/entity/version ownership;
- repository and DAO/data-source boundaries;
- domain mapping;
- disk-backed release behavior;
- transactions and rollback;
- logical idempotency;
- duplicate prevention;
- migration initialization and representative fixtures;
- failed migration recovery;
- date attribution/historical stability;
- concurrency/single-writer rules;
- test database isolation;
- backup/sensitive-storage policy;
- deletion/logout/account removal;
- activity recreation, process death, app relaunch, and reboot kept distinct;
- no uniqueness-only idempotency;
- no forensic deletion overclaim.

### 12. Permission, Manifest, and Background Task Requirements

When applicable, tasks must name exact approved boundaries for:

- manifest permissions;
- runtime permission denial/revocation/settings recovery;
- exported components/intent filters;
- app links;
- services/receivers/providers;
- foreground service types;
- notifications/exact alarms;
- WorkManager/background execution;
- Health Connect/camera/microphone/media/location/Bluetooth/etc.;
- billing/authentication/attestation;
- data minimization, redaction, retention, backup, and release inspection.

No task may silently enable a protected capability.

### 13. Evidence Tasks Must Match Android Claims

Use appropriate evidence:

- unit/ViewModel/domain tests;
- repository/integration tests;
- disk-backed migration/relaunch tests;
- instrumented tests;
- Compose UI/View UI tests;
- emulator runtime;
- physical-device runtime;
- TalkBack/manual accessibility;
- RTL/pseudo-locale;
- multi-window/foldable/configuration-change/process-death;
- WorkManager/service/notification;
- permissions/app links/billing/attestation;
- lint/resource/manifest/prohibited-pattern scans;
- APK/AAB/R8/signing/release inspection.

Previews and screenshots are never sole proof of runtime behavior.

### 14. Implementation Authorization Is External

Every implementation task remains non-executable until the repository owner or defined authorization gate grants implementation authorization.

The agent must not self-authorize because tasks are approved or reviewed.

### 15. No Production Work During Task Generation

Do not:

- create/edit Kotlin or Java files;
- edit Gradle files/version catalogs/convention plugins;
- edit AndroidManifest.xml;
- create resources or localization files;
- create schemas/entities/DAOs/migrations;
- generate tests or previews;
- run implementation commands;
- add permissions, services, receivers, providers, workers, or dependencies;
- change readiness gates;
- produce evidence claiming implementation exists.

## Mandatory Task Fields

Every task must include:

- task ID;
- objective;
- contract references;
- plan references;
- authority references;
- dependencies;
- allowed scope;
- prohibited scope;
- implementation notes bounded by the plan;
- acceptance criteria;
- verification layer;
- exact procedure/command;
- environment/destination;
- expected result;
- evidence path;
- limitation;
- authorization statement.

## Task Sizing Guidance

A task is too large when:

- it spans multiple architectural layers without a single coherent outcome;
- it covers more than one user-facing screen plus unrelated infrastructure;
- it combines module restructuring, persistence, ViewModel, UI, permissions, and evidence;
- it cannot be reviewed independently;
- its evidence requires unrelated suites;
- failure would obscure which boundary was violated.

A task is too small when:

- it creates only a trivial symbol/resource with no independent value;
- it has no meaningful acceptance evidence;
- it exists only to inflate task count;
- it separates inseparable code and test responsibilities without review value.

## Stop Conditions

Stop when:

- plan is not owner-approved;
- plan review is not `PASS`;
- a task would require inventing behavior or architecture;
- unresolved technical decisions affect dependency order;
- design authority is missing for a planned screen;
- persistence authority/evidence is provisional where production tasks depend on it;
- permission/capability authorization is absent;
- test/evidence destination or artifact path cannot be named;
- readiness routing or implementation authorization is contradictory.

## Completion Report

Report:

- files read;
- task-set path;
- task count;
- dependency summary;
- contract and plan coverage;
- Android architecture coverage;
- ViewModel/DI/coroutine/lifecycle coverage;
- localization/RTL/accessibility/adaptive coverage;
- persistence/permission/privacy/background coverage;
- evidence coverage;
- unresolved blockers;
- authoring verdict;
- confirmation that no production code, tests, Gradle files, manifests, resources, schemas, migrations, permissions, or implementation commands were created.
