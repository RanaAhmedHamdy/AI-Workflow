# Skill: Android Implementation Plan Authoring v1

## Purpose

Create an Android architecture-aware, design-traceable, evidence-ready implementation plan from an owner-approved feature contract. Do not create production code, tests, Gradle configuration, manifests, resources, schemas, migrations, or implementation tasks.

## Preconditions

Verify:

- feature contract is owner-approved;
- product clarifications are closed;
- applicable Android ADRs are accepted or explicitly provisional;
- required feasibility spikes passed independent verification;
- exact design authority exists;
- Android toolchain, SDK, application/module, UI framework, state, concurrency, dependency-composition, navigation, persistence, lifecycle, localization, accessibility, permissions, testing, and release boundaries needed by this feature are decided;
- applicable readiness gates permit planning.

If a required precondition is absent, contradictory, or merely assumed, return a blocked or verification verdict.

## Required Inputs

Read:

- repository policy;
- context router;
- playbook;
- owner decision register;
- approved feature contract;
- feature input and feature map;
- Android architecture spine;
- applicable ADRs;
- readiness gate;
- accepted feasibility evidence;
- design authority;
- screen contracts;
- exact artifact index and artifacts;
- design system;
- information architecture;
- localization and accessibility authority;
- evidence policy;
- implementation-plan template.

## Required Output

Create or update:

`docs/features/<feature-id>/IMPLEMENTATION_PLAN.md`

Use:

`.templates/mobile/IMPLEMENTATION_PLAN_TEMPLATE.md`

Return one:

- `READY FOR PLAN REVIEW`
- `BLOCKED BY TECHNICAL DECISION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

Do not generate tasks or grant implementation authorization.

## Core Rules

### 1. Contract Bounds the Plan

Every planned module, state holder, repository, data source, use case, route, destination, screen, permission boundary, background component, test, and evidence item must trace to an approved contract requirement or a strictly necessary implementation responsibility.

Do not add later-feature behavior, speculative infrastructure, generalized frameworks, or “future-proofing” modules.

### 2. Accepted Android Decisions Control Mechanisms

Apply accepted ADRs for:

- Android Studio, JDK, Gradle, Android Gradle Plugin, Kotlin, compile SDK, target SDK, and min SDK;
- application ID, namespace, modules, source sets, build types, flavors, and convention plugins;
- Jetpack Compose, Android Views, or hybrid UI;
- presentation state and ViewModel policy;
- Kotlin coroutines, Flow, dispatchers, scope ownership, and cancellation;
- dependency injection/composition;
- navigation, deep links, saved state, and predictive back where applicable;
- persistence, transactions, migrations, backup, and encryption;
- lifecycle, configuration change, process death, and relaunch;
- WorkManager/background execution, services, receivers, notifications, and alarms;
- permissions, manifest boundaries, exported components, providers, app links, Health Connect, billing, authentication, and attestation;
- localization, RTL, adaptive windows, foldables, and accessibility;
- testing, CI, emulator/device evidence, APK/AAB inspection, signing, and release.

Do not silently choose a mechanism because it is common Android practice.

### 3. Preserve Dependency Direction

Define exact allowed dependency direction. A typical feature boundary may be:

`UI/Presentation -> Domain <- Data/Platform adapters`

but use repository authority rather than assuming this exact layering.

Prohibit:

- UI depending directly on database entities, DAOs, clients, billing services, or permission managers;
- domain depending on Android framework types unless explicitly accepted;
- feature-to-feature cycles;
- shared/common/utils dumping grounds;
- service locators or global singletons;
- ad hoc dependency creation inside Activities, Fragments, composables, adapters, or views.

### 4. Plan Presentation State Deliberately

For each route-level workflow, identify:

- lifecycle owner;
- approved state holder, normally a ViewModel when state spans recomposition, navigation, asynchronous work, validation, or recreation;
- immutable UI-state exposure;
- user events and one-way mutation path;
- transient local UI state versus workflow state;
- saved-state/restoration responsibility;
- durable reconstruction source;
- coroutine scope and dispatcher boundaries;
- cancellation behavior;
- terminal states;
- test and preview composition.

Do not require ceremonial ViewModels for static leaf components. Do not place repositories, persistence, network, billing, or permission side effects in leaf UI.

### 5. Plan Dependency Composition Explicitly

Name:

- production composition root;
- feature-level bindings/factories/components;
- scopes and lifetimes;
- constructor injection path;
- test replacement path;
- preview/design-time replacement path;
- missing-configuration fail-closed behavior.

No generic service locator, mutable global registry, or debug conditional may supply fake success in release composition.

### 6. Plan Kotlin Coroutines and Flow

Define:

- structured concurrency ownership;
- lifecycle-aware collection;
- dispatcher injection/selection;
- main-safe state mutation;
- cancellation propagation;
- durable work that must outlive a screen;
- retry, ordering, idempotency, and duplicate side-effect rules;
- hot-flow lifetime and sharing policy;
- exception mapping and bounded terminal states;
- prohibition of `GlobalScope`, unowned jobs, swallowed exceptions, and hardcoded dispatchers where testability requires injection.

### 7. Plan Persistence Completely

When persistence applies, name:

- accepted engine and rationale from ADR authority;
- system of record;
- schema/entity ownership;
- domain/data mapping boundary;
- repository and DAO/data-source boundaries;
- transactions and rollback;
- logical idempotency and duplicate prevention;
- migration/version ownership;
- failed-migration recovery;
- date/time attribution and historical stability;
- concurrency and multi-writer rules;
- test database/store isolation;
- backup/restore and device-transfer policy;
- encryption/file-protection boundary;
- sensitive-data separation;
- deletion/logout/account-removal behavior;
- representative production migration fixtures;
- activity recreation, process death, app relaunch, and device reboot claims kept distinct.

Do not rely on database uniqueness alone as product idempotency. Do not overclaim forensic deletion.

### 8. Plan Lifecycle, Recreation, and Restoration

Explicitly separate:

- recomposition;
- view/fragment recreation;
- configuration change;
- activity recreation;
- navigation restoration;
- process death;
- app relaunch;
- device reboot;
- backup restore or device transfer.

Define what is transient, saveable, reconstructable, durable, or intentionally discarded.

Do not store sensitive payloads in route arguments or saved state. Validate restored identifiers against repositories and recover safely when stale.

### 9. Plan Navigation and Back Behavior

Apply accepted navigation authority.

Define:

- top-level destinations;
- route ownership;
- typed/minimal arguments;
- deep links/app links when approved;
- modal/dialog/sheet behavior;
- system back and predictive-back outcomes where applicable;
- unsaved-draft protection;
- adaptive bottom bar, rail, drawer, or multi-pane mapping only where design authority approves it;
- restoration intent and stale-route recovery.

Back navigation must never silently commit, discard, delete, purchase, transfer, or reassign data.

### 10. Map Exact Screens and Artifacts

For every screen:

- cite exact screen-contract ID;
- cite exact compact, medium, and expanded artifacts as applicable;
- map contract requirements;
- identify route/container and render/content boundaries;
- map loading, empty, populated, disabled, failure, recovery, offline, success, and destructive states;
- map user events;
- list unsupported artifact content to exclude;
- define preview fixtures;
- define runtime evidence and stop conditions.

Previews support development and review but are never runtime evidence.

### 11. Plan Adaptive Android UI

Cover, where applicable:

- compact, medium, and expanded windows;
- portrait and landscape;
- split-screen, freeform, and resized windows;
- foldable postures, hinges, and tabletop/book modes;
- edge-to-edge system bars;
- display cutouts;
- IME insets and keyboard reachability;
- scrolling and overflow;
- mouse, trackpad, keyboard, D-pad, and ChromeOS behavior when in scope;
- state preservation during reflow.

Do not invent fixed dp breakpoints, panes, rails, drawers, or content regions absent from architecture/design authority.

### 12. Plan Localization and RTL from the Start

Define:

- resource ownership;
- stable keys;
- fallback locale;
- plurals, substitutions, and grammatical variants;
- locale-aware formatting;
- no hardcoded user-facing/accessibility strings;
- no sentence-fragment concatenation;
- semantic start/end layout;
- Arabic/Hebrew/approved RTL runtime;
- mixed-direction content;
- long translations and pseudo-locales;
- notifications, widgets, shortcuts, errors, and background-visible strings when applicable;
- deterministic scans and stale/missing-key validation.

Localization and RTL are implementation requirements, not final polish.

### 13. Plan Accessibility with Runtime Evidence

Cover applicable outcomes and implementation ownership for:

- TalkBack semantics, labels, roles, states, values, actions, headings, collections, and traversal;
- focus order/restoration;
- font scaling and display scaling;
- clipping, overlap, truncation, and text shrinking prevention;
- non-color differentiation;
- reduced/removed animations;
- contrast and system visual adaptations;
- minimum touch targets;
- keyboard and D-pad navigation;
- Switch Access and Voice Access;
- magnification;
- live-region and error announcements;
- custom controls;
- Accessibility Scanner/manual audits.

Static source, lint, previews, and screenshots do not prove accessibility runtime behavior.

### 14. Plan Permissions, Manifest, Privacy, and Capabilities

For every applicable protected boundary, define:

- manifest ownership;
- runtime permission flow;
- denial, revocation, and settings recovery;
- exported components and intent filters;
- app links/deep links;
- services, receivers, providers, foreground-service types, notifications, alarms, and WorkManager;
- Health Connect, camera, microphone, media, location, Bluetooth, contacts, calendar, or other sensitive APIs;
- billing/authentication/attestation boundaries;
- data minimization, consent, retention, deletion, backup, and logging redaction;
- dependency manifest and SDK review;
- release fail-closed behavior.

A dependency import or manifest merge does not authorize a capability.

### 15. Define Sufficient Testing and Evidence

For every requirement, select all necessary layers:

- Kotlin/JVM unit;
- presentation-state/ViewModel test;
- repository/integration;
- disk-backed persistence/migration;
- Robolectric only for accepted claims;
- instrumented Android test;
- Compose UI or View UI automation;
- emulator runtime;
- physical-device runtime;
- TalkBack/manual accessibility;
- RTL/pseudo-locale;
- adaptive/foldable/multi-window;
- configuration-change/process-death/relaunch;
- WorkManager/service/notification/background;
- app-link/permission/billing/attestation/service;
- lint/resource/manifest/prohibited-pattern scans;
- APK/AAB, R8, signing, and release inspection.

Every evidence item must name the procedure, destination, expected result, artifact path, and limitation.

### 15A. Define a Compact Verification Matrix

Inside `IMPLEMENTATION_PLAN.md`, define stable unique IDs such as `VM-001` for applicable behavioral/runtime verification scenarios. Each row must name the approved requirement/claim, executable scenario, environment/destination, reproducible preconditions, expected observable result, evidence path, and verification method or known limitation. Runtime-only claims require runtime-capable evidence. Keep the matrix inside the plan; do not create a separate verification artifact solely for it.

`VM-*` rows are planned verification definitions, not a second lifecycle state machine. Do not add per-row `READY`/`PASS` workflow statuses during plan authoring.

### 15B. Keep Current Lifecycle State Internally Consistent

Keep current lifecycle/status/authorization truth in one canonical status block. Historical authoring/review verdicts may remain only when clearly labeled as stage-specific history. Never emit incompatible current-state assertions in different parts of the same artifact.

### 16. Define Implementation Order Only

The plan may define dependency order but must not generate:

- task IDs;
- assignments;
- estimates;
- file-by-file checklists;
- production code;
- tests;
- Gradle edits;
- manifest entries;
- resources;
- schemas or migrations.

### 17. Prohibited Patterns Must Be Explicit

Include feature-relevant prohibitions such as:

- hardcoded user-facing/accessibility strings;
- repositories/DAOs/clients in leaf UI;
- side effects during Compose composition;
- ViewModel creation in recomposition;
- state duplicated across ViewModel, composable, Fragment, Activity, and saved state;
- `GlobalScope` or unowned coroutines;
- hardcoded dispatchers where injection is required;
- global service locators/singletons;
- fake/debug dependencies in release graph;
- phone-only or left/right assumptions;
- fixed-height text;
- previews claimed as runtime evidence;
- in-memory substitutes for required release durability;
- unapproved permissions/exported components/background services;
- silent fallback to simulated success;
- weakened lint, compiler, R8, or test settings without authority.

## Stop Conditions

Stop when:

- the contract is not owner-approved;
- material product behavior remains unresolved;
- ADRs conflict;
- required feasibility evidence is not independently verified;
- exact design authority is missing;
- a required Android architecture decision is absent;
- planning would require invented behavior;
- a protected boundary lacks authorization;
- external configuration lacks fail-closed behavior;
- evidence cannot prove the intended claim;
- readiness routing is contradictory.

## Completion Report

Report:

- files read;
- plan path;
- requirements mapped;
- modules/components proposed;
- Android architecture decisions applied;
- exact artifacts mapped;
- lifecycle/state strategy;
- DI, coroutine, persistence, navigation, localization, accessibility, permission, and evidence coverage;
- risks;
- unresolved decisions;
- readiness implications;
- verdict;
- confirmation that no code, tasks, Gradle files, manifests, resources, schemas, migrations, or tests were created.

## Complexity Tier and Cross-Feature Coherence Rules (v1.6)
- Read `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md` and the feature classification record before applying depth/sizing rules.
- If `feature-complexity-classification` was not executed, or its result is missing/invalid/stale, treat the feature as `COMPLEX` and record `DEFAULTED_TO_COMPLEX`. Never infer a lower tier.
- Use one canonical lifecycle/template family; tier changes mandatory depth and specialist gates, not authority order.
- For every durable mutation, identify all affected consumers/read models and the explicit propagation/invalidation/observation mechanism. A locally successful write with a stale dependent screen is incomplete.
- For actions reachable from multiple entry contexts, define and verify origin-sensitive success/cancel/failure destinations. Normal management must not accidentally execute onboarding/setup completion semantics.
- Any user-committable vertical slice must prove `commit → authoritative state → affected consumer refresh → correct destination` before bounded closure when that journey is in the task's scope. Do not defer all such proof to final convergence.

