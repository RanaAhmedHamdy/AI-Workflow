# Skill: Android Implementation Task Review v1

## Purpose

Independently review an Android implementation task set for scope fidelity, dependency correctness, task sizing, architecture conformance, ViewModel/state ownership, dependency composition, coroutine safety, lifecycle/restoration, persistence correctness, exact design traceability, localization/RTL, accessibility/adaptation, permission boundaries, evidence sufficiency, and authorization honesty.

`PASS` means ready for owner task approval only.

## Verdicts

Return exactly one:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

## Required Inputs

Read:

- implementation tasks;
- approved feature contract;
- approved implementation plan;
- feature map;
- Android architecture spine;
- applicable ADRs;
- readiness gate;
- design authority;
- screen contracts;
- exact artifacts;
- repository policy;
- evidence policy.

## Mandatory Review

### 1. Coverage and Traceability

Verify every:

- contract requirement;
- plan component;
- module/source/resource responsibility;
- domain invariant;
- repository/persistence responsibility;
- ViewModel/presentation-state responsibility;
- DI/composition responsibility;
- coroutine/lifecycle responsibility;
- navigation/restoration responsibility;
- screen;
- localization/RTL responsibility;
- accessibility/adaptive responsibility;
- permission/privacy/background responsibility;
- evidence obligation;

is covered by at least one task.

Flag orphan tasks and uncovered authority items.

### 2. Scope Fidelity

Fail tasks that:

- pull forward later features;
- invent product rules;
- include unsupported artifact content;
- introduce remote lookup, auth, billing, AI, history, Health Connect, notifications, widgets, background work, or permissions outside scope;
- broaden repository restructuring beyond the feature;
- add speculative modules or abstractions;
- silently enable protected capabilities.

### 3. Dependency Graph

Verify:

- dependencies are explicit;
- graph is acyclic;
- prerequisites precede consumers;
- module/resource structure precedes use;
- domain/contracts precede data and presentation consumers;
- DI bindings follow interfaces and precede composition consumers;
- schemas/migrations precede repository use;
- repositories/use cases precede ViewModel integration;
- ViewModel/navigation precede route/screen integration;
- localization/accessibility/adaptive work is integrated at the right point;
- evidence/convergence follows relevant implementation.

Fail hidden dependencies and circular sequencing.

### 4. Task Sizing

Flag tasks that are:

- too broad;
- multi-layer without one coherent outcome;
- impossible to review independently;
- trivial and evidence-free;
- duplicate;
- ambiguous;
- split so finely that implementation and its meaningful verification are disconnected.

### 5. Android Architecture Conformance

Verify tasks preserve:

- approved module/source-set boundaries;
- dependency direction;
- exact Compose/Views choice;
- lifecycle-aware presentation state;
- ViewModel use where required and not ceremonial;
- immutable UI-state/event boundaries;
- isolated persistence;
- one approved DI/composition path;
- no service locator/global singleton;
- no repositories/DAOs/clients in leaf UI;
- no side effects in Compose composition or view binding;
- accepted navigation and saved-state rules;
- accepted localization/security/permission policies;
- no fake release composition.

### 6. ViewModel, Coroutine, and Flow Tasks

Verify explicit tasks or acceptance criteria for:

- stable state-holder lifetime;
- no recreation during recomposition;
- transient versus workflow/durable state;
- structured concurrency;
- dispatcher ownership/injection;
- lifecycle-aware collection;
- cancellation propagation;
- durable work ownership;
- hot-flow lifetime/sharing;
- exception/error mapping;
- reentrancy, ordering, retry, idempotency, duplicate effects;
- bounded terminal states;
- focused state-transition tests.

Fail `GlobalScope`, unowned jobs, swallowed errors, broad main-thread execution used to hide isolation issues, or state duplicated across layers.

### 7. Dependency Composition Tasks

Verify:

- production composition root/bindings;
- feature scopes and lifetimes;
- constructor injection/approved equivalent;
- test replacements;
- preview replacements;
- fail-closed missing configuration;
- no debug/test fake binding in release;
- no ad hoc dependency construction in Activities, Fragments, composables, views, or adapters.

### 8. Persistence Tasks

Verify explicit tasks or acceptance criteria for:

- schema/entity/version ownership;
- repository and DAO/data-source boundaries;
- domain mapping;
- disk-backed release behavior;
- transactions and rollback;
- logical idempotency;
- duplicate prevention;
- migration initialization and fixtures;
- failed-migration recovery;
- date attribution/historical stability;
- concurrency/single-writer behavior;
- test database isolation;
- backup/sensitive-storage policy;
- deletion/logout/account removal;
- activity recreation versus process-death/relaunch evidence;
- no uniqueness-only idempotency;
- no forensic deletion overclaim.

### 9. Design and UI Tasks

For every screen verify:

- exact compact artifact;
- exact medium/expanded artifact where applicable;
- supported states;
- error/recovery/offline/disabled/success;
- exclusions;
- route/container and render/content boundaries;
- preview fixtures;
- compact/medium/expanded/resized/foldable behavior;
- IME/system insets/cutouts/overflow;
- RTL/accessibility obligations;
- no hardcoded strings;
- no fixed-height text;
- no left/right assumptions;
- no repositories or side effects in leaf UI;
- previews not used as runtime proof.

### 10. Lifecycle, Navigation, and Restoration Tasks

Verify coverage for:

- configuration change;
- Activity/Fragment recreation;
- saved state;
- process death;
- app relaunch;
- stale restored IDs;
- system back/predictive back;
- explicit discard/commit/destructive actions;
- deep/app links if approved;
- adaptive navigation;
- sensitive payload exclusion from routes/saved state.

### 11. Localization and RTL Tasks

Verify:

- resource key ownership;
- all user-facing/accessibility strings localized;
- plurals/substitutions/formatting;
- no fragment concatenation;
- semantic start/end;
- approved RTL runtime;
- mixed-direction text;
- long translation and pseudo-locale evidence;
- notification/widget/shortcut/background strings when applicable;
- hardcoded-string and stale-key scans.

### 12. Accessibility Tasks

Verify task-level implementation and runtime evidence for:

- TalkBack semantics/traversal;
- focus order/restoration;
- font/display scaling;
- non-color differentiation;
- reduced animations;
- contrast/visual adaptations;
- touch targets;
- keyboard/D-pad;
- Switch Access/Voice Access where supported;
- magnification;
- error/live announcements;
- custom controls.

Fail source-only, lint-only, preview-only, or screenshot-only proof.

### 13. Permission, Manifest, Privacy, and Background Tasks

Verify explicit approved tasks for applicable:

- manifest/runtime permissions;
- denial/revocation/settings recovery;
- exported components/intent filters;
- app links;
- services/receivers/providers;
- foreground-service types;
- notifications/exact alarms;
- WorkManager/background execution;
- Health Connect and other sensitive APIs;
- billing/authentication/attestation;
- data minimization/redaction/retention/backup/deletion;
- SDK manifest/supply-chain review;
- release fail-closed behavior.

Fail any unapproved capability or implicit authorization.

### 14. Verification Quality

Every task must state:

- test/evidence layer;
- exact command/procedure;
- destination/environment;
- expected observable result;
- evidence path;
- limitation.

Fail:

- generic “run tests” wording;
- previews/screenshots as sole proof;
- JVM tests used to prove emulator/device-only behavior;
- Robolectric overreach;
- UI-only arithmetic proof;
- source-only accessibility or manifest proof;
- missing machine-readable reports;
- evidence planned before prerequisites;
- no physical-device layer for claims that require one;
- stale or non-reproducible artifact paths.

### 15. Authorization Honesty

Fail if tasks:

- mark themselves executable before authorization;
- ask the agent to begin implementation automatically;
- grant authorization after review;
- change owner approval;
- claim readiness gates passed without evidence;
- create or modify code/configuration during task generation.

### 16. Final Convergence

Verify final tasks cover:

- contract-to-implementation traceability;
- Android architecture/module conformance;
- DI/composition;
- ViewModel/state/coroutine/lifecycle correctness;
- design conformance;
- localization/RTL;
- accessibility;
- adaptive/resizable/foldable UI;
- persistence/migration/process-death/relaunch;
- permissions/privacy/background/network;
- production fakes and release graph;
- documentation synchronization;
- clean CI and current Android-native machine-readable reports/artifacts;
- APK/AAB/manifest/R8/signing inspection where applicable.

### Verification-Matrix Traceability and Current-State Consistency

- Verify every task that implements or proves matrix-covered behavior lists the applicable approved `VM-*` IDs.
- Verify every referenced `VM-*` ID exists in the approved implementation plan and is relevant to the task.
- Reject invented IDs, required matrix scenarios with no implementation/evidence owner, and unnecessary duplication of full matrix scenario prose inside tasks.
- Search the complete task artifact for lifecycle, approval, readiness, and implementation-authorization assertions. If two assertions both claim to describe the current state and conflict, return a blocking finding. Historical stage verdicts are allowed only when clearly labeled as historical/stage-specific.

## Finding Format

- Finding ID;
- Severity;
- Task ID/section;
- Contract requirement;
- Plan section;
- Problem;
- Required correction;
- Verdict impact.

## Pass Criteria

A task set receives `PASS` only when:

1. all approved requirements and plan responsibilities are covered;
2. no scope drift exists;
3. dependency graph is acyclic and correct;
4. task sizes are bounded;
5. accepted Android architecture is preserved;
6. ViewModel, DI, coroutine, lifecycle, navigation, and persistence responsibilities are explicit;
7. exact design and cross-cutting behavior are represented;
8. permissions/protected boundaries are authorized;
9. evidence is sufficient and Android-appropriate;
10. final convergence is complete;
11. authorization remains external;
12. no production code/configuration/tests were generated.

## Final Report

Include:

- verdict;
- task count;
- coverage summary;
- blocking findings;
- scope drift;
- dependency issues;
- oversized/undersized tasks;
- architecture/module issues;
- DI issues;
- ViewModel/coroutine/lifecycle issues;
- persistence issues;
- design/adaptive issues;
- localization/RTL issues;
- accessibility issues;
- permission/privacy/background issues;
- evidence gaps;
- readiness/authorization issues;
- exact tasks requiring revision;
- statement that `PASS` means ready for owner task approval only.

## Verification-Cost Review

Fail or request revision when a task:

- makes unrelated `FEATURE-CONVERGENCE` or `FINAL-READINESS` evidence block ordinary task closure;
- demands duplicate reruns solely for unique artifact names;
- splits one coherent UI/vertical implementation into ceremonial tasks without dependency/risk value;
- lacks task-local vertical proof for a user-committable journey in its scope;
- replaces deterministic behavioral/data correctness tests with manual-only validation.

Manual/device validation is acceptable for subjective visual/accessibility/adaptive quality and physical-device-only claims when assigned to the appropriate later gate.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
