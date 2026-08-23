---
name: implementation-plan-review
description: "Independently reviews an Android implementation plan for contract fidelity, architecture, lifecycle, dependency composition, coroutines, persistence, adaptive UI, localization, accessibility, permissions, testing, and evidence. Use before owner plan approval."
---

# Skill: Android Implementation Plan Review v1

## Purpose

Independently review an Android implementation plan for contract fidelity, architecture conformance, exact design traceability, lifecycle correctness, dependency composition, coroutine safety, persistence integrity, adaptive UI, localization, accessibility, permissions, testing, evidence, and readiness honesty.

## Verdicts

Return exactly one:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

`PASS` means ready for owner plan approval only. It does not authorize task generation or implementation.

## Required Inputs

Read:

- implementation plan;
- owner-approved feature contract;
- feature input and feature map;
- owner decision register;
- Android architecture spine;
- applicable ADRs;
- feasibility evidence;
- readiness gate;
- design authority;
- screen contracts;
- artifact index and exact artifacts;
- design system and information architecture;
- repository policy;
- context router;
- evidence policy.

## Mandatory Review

### 1. Traceability and Scope Fidelity

Trace every planned module, source set, state holder, ViewModel, repository, DAO/data source, use case, route, screen, permission, background component, test, and evidence item to contract requirements and accepted authority.

Fail:

- untraced components;
- later-feature behavior;
- invented product rules;
- speculative “future-proofing” infrastructure;
- repository-wide restructuring beyond the feature;
- omitted contract requirements;
- Android mechanisms chosen without accepted decisions.

### 2. Toolchain, SDK, Module, and Build Conformance

Verify the plan applies exact accepted decisions for:

- Android Studio/JDK/Gradle/AGP/Kotlin;
- compile SDK, target SDK, min SDK;
- namespace/application ID;
- modules/source sets;
- build types/flavors;
- dependency catalog/convention-plugin ownership;
- shared CI commands and test destinations.

Fail silent defaults, unapproved modules, empty template modules, or unrelated restructuring.

### 3. Architecture and Dependency Direction

Verify:

- feature boundaries are clear;
- dependency direction is explicit and acyclic;
- domain is not polluted by Android framework types unless authorized;
- UI does not own repositories, DAOs, clients, billing, permissions, or persistence;
- shared code has precise ownership;
- no service locator/global singleton;
- production composition is distinct from test/preview composition;
- no fake release bindings.

### 4. Presentation State and ViewModel Correctness

Verify each workflow screen has an appropriate lifecycle-aware state owner when needed.

Check:

- route/content split;
- immutable UI state;
- explicit user events;
- one-way mutation;
- transient versus workflow state;
- saved-state and durable reconstruction boundaries;
- no ViewModel ceremony for static leaves;
- no ViewModel creation during recomposition;
- no raw persistence entities exposed to UI;
- no duplicate mutable state across Activity/Fragment/ViewModel/composable;
- no repositories or routers passed into leaf UI;
- previews use deterministic fixtures.

### 5. Coroutine and Flow Safety

Verify:

- structured concurrency;
- scope ownership;
- lifecycle-aware collection;
- dispatcher ownership/injection;
- main-safe UI state mutation;
- cancellation propagation;
- durable work not cancelled merely because a composable disappears;
- hot-flow lifetime/sharing policy;
- exception mapping;
- reentrancy, ordering, retry, idempotency, and duplicate-effect handling;
- bounded terminal states.

Fail `GlobalScope`, unowned jobs, fire-and-forget calls, swallowed exceptions, broad main-thread execution used to silence problems, or hardcoded dispatchers contrary to authority.

### 6. Dependency Composition

Verify:

- one approved production composition path;
- feature scopes/lifetimes;
- constructor injection or accepted equivalent;
- deterministic test replacement;
- deterministic preview replacement;
- missing configuration fails closed;
- debug/test modules cannot enter release graph;
- no ad hoc dependency construction in Activities, Fragments, composables, views, or adapters.

### 7. Persistence and Migration

Verify explicit design for:

- system of record;
- schema/entity ownership;
- domain mapping;
- repository and DAO/data-source boundaries;
- transactions and rollback;
- logical idempotency;
- duplicate prevention beyond uniqueness alone;
- migration/version ownership;
- failed-migration recovery;
- date attribution/historical stability;
- concurrency/single-writer rules;
- disk-backed release behavior;
- test-store isolation;
- backup/device transfer;
- sensitive storage;
- deletion/logout/account removal;
- representative migration fixtures;
- process-death and relaunch evidence.

Fail forensic deletion overclaims or conflation of activity recreation, process death, relaunch, reboot, and backup restore.

### 8. Navigation, Lifecycle, and Restoration

Verify:

- accepted navigation approach;
- top-level destinations and route ownership;
- minimal non-sensitive route arguments;
- system back/predictive-back behavior;
- explicit discard/commit/destructive actions;
- configuration-change handling;
- activity/fragment recreation;
- process-death restoration;
- stale restored-ID recovery;
- deep/app-link boundaries;
- no sensitive payloads in route or saved state;
- adaptive navigation matches design authority.

### 9. Compose/Views Screen Conformance

For each screen verify:

- exact screen contract and inspectable approved visual artifacts;
- design-bound screens carry a concise Design Lock/permitted adaptations rather than relying on vague “native adaptation”;
- route/container and stateless/render boundary;
- all required states;
- validation, failure, recovery, offline, disabled, and success behavior;
- no side effects during composition/rendering;
- no state-holder recreation;
- no hardcoded strings;
- no fixed-height text;
- no absolute left/right assumptions;
- no phone-only assumptions;
- previews for representative states where supported;
- previews not treated as runtime evidence.

### 10. Adaptive and Resizable UI

Verify plans for:

- compact/medium/expanded windows;
- portrait/landscape;
- split screen/freeform/resizing;
- foldable postures/hinges where supported;
- IME/system bars/cutouts/insets;
- overflow and scrolling;
- state preservation during reflow;
- keyboard/mouse/trackpad/D-pad where in scope.

Fail arbitrary breakpoints, invented panes/rails/drawers, and generic “responsive” wording.

### 11. Localization and RTL

Verify:

- authoritative string-resource ownership;
- zero hardcoded user-facing/accessibility strings;
- stable keys and fallback locale;
- plurals/substitutions/grammatical variants;
- locale-aware formatting;
- no sentence-fragment concatenation;
- semantic start/end;
- approved RTL runtime and mixed-direction content;
- long translation and pseudo-locale coverage;
- background-visible strings;
- deterministic hardcoded-string and stale-key scans.

### 12. Accessibility

Verify implementation and runtime plans for:

- TalkBack semantics and traversal;
- focus order/restoration;
- font/display scaling;
- non-color differentiation;
- reduced animations;
- contrast/visual adaptations;
- touch targets;
- keyboard/D-pad;
- Switch Access and Voice Access;
- magnification;
- error/live-region announcements;
- custom controls;
- manual/Accessibility Scanner evidence.

Reject static-only accessibility proof.

### 13. Permissions, Manifest, Privacy, and Background Boundaries

Verify exact authorization and fail-closed behavior for:

- manifest permissions and runtime permission flows;
- denial/revocation/settings recovery;
- exported components and intent filters;
- app links;
- services/receivers/providers;
- foreground service types;
- notifications and exact alarms;
- WorkManager/background execution;
- Health Connect and sensitive frameworks;
- billing/authentication/attestation;
- analytics/crash/logging redaction;
- data minimization, retention, backup, and deletion;
- dependency manifest/supply-chain review;
- release configuration.

Fail any capability inferred merely from a dependency or framework import.

### 14. Verification Quality

Every evidence row must state:

- observable claim;
- test/evidence layer;
- exact command/procedure;
- destination/environment;
- expected result;
- artifact path;
- limitation.

Reject:

- generic “run tests”;
- previews/screenshots as sole proof of behavior;
- JVM-only proof of device behavior;
- Robolectric overreach;
- UI-only arithmetic proof;
- static-only accessibility proof;
- source-only manifest/signing proof;
- missing reports/results;
- evidence planned before implementation prerequisites;
- no physical-device evidence for claims that require it.

### 15. Planning Boundary and Authorization Honesty

Fail if the plan contains:

- task IDs;
- estimates or assignments;
- production code;
- generated Gradle/manifests/resources/schemas/migrations/tests;
- file-by-file implementation checklist masquerading as a plan;
- self-approval;
- implementation authorization;
- claims readiness gates passed without matching evidence.

### Verification-Matrix Traceability and State Consistency

- Verify unique stable `VM-*` IDs cover every applicable runtime-only claim with an executable scenario.
- Verify every row traces to approved authority and does not invent behavior.
- Verify environment/destination, preconditions, expected observable result, evidence path, and method/limitation are concrete enough to execute.
- Search the complete artifact for lifecycle/status/approval/readiness/authorization assertions. If two assertions both claim to describe the current state and conflict, return a blocking finding. Historical stage verdicts are allowed only when clearly labeled as historical/stage-specific.

## Finding Format

Finding ID; severity; plan section; contract requirement; authority; problem; required correction; verdict impact.

## Pass Criteria

A plan receives `PASS` only when:

1. all contract requirements are mapped;
2. no scope drift exists;
3. accepted Android decisions are applied;
4. modules and dependency direction are sound;
5. lifecycle-aware state, ViewModel, DI, coroutine, navigation, and persistence boundaries are explicit;
6. exact design artifacts and adaptive behavior are mapped;
7. localization/RTL and accessibility are initial requirements;
8. permissions/protected boundaries are authorized and fail closed;
9. tests and evidence can prove the claims;
10. no tasks/code/configuration were generated;
11. unresolved decisions are visible;
12. readiness and authorization remain honest.

## Final Report

Include:

- verdict;
- traceability coverage;
- blocking findings;
- scope drift;
- toolchain/module issues;
- architecture/DI issues;
- ViewModel/presentation-state issues;
- coroutine/Flow issues;
- persistence issues;
- lifecycle/navigation/restoration issues;
- design/adaptive issues;
- localization/RTL issues;
- accessibility issues;
- permission/privacy/background issues;
- evidence gaps;
- unresolved decisions;
- readiness implications;
- exact sections to revise;
- statement that `PASS` means ready for owner plan approval only.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
