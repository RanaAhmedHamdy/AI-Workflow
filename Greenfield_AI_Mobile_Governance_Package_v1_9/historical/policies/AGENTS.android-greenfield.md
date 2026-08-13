# AGENTS.md — Greenfield Native Android Overlay

> Version 2.0. Use with `AGENTS.common.md`.
>
> These are reusable defaults, not inferred project facts. Record an explicit decision for every material exception. Verify current Android Studio, AGP, Gradle, Kotlin, JDK, SDK, Compose, device, and Play requirements during repository initialization rather than pinning this template to future-stale versions.

## 1. Project initialization and verified toolchain

Before planning the first implementation slice, record and verify:

- supported Android form factors and device classes;
- exact Android Studio, Android Gradle Plugin, Gradle, Kotlin, JDK, compile SDK, target SDK, and minimum SDK;
- application namespace, application ID, manifest ownership, and resource roots;
- application, library, dynamic-feature, benchmark, baseline-profile, test-fixture, and test-module scope;
- build variants, product flavors, signing placeholders, and environment separation;
- dependency management, Version Catalog, lockfile, repository, and checksum policy;
- Compose, Views, Material, Navigation, lifecycle, persistence, background-work, and test-stack decisions;
- shared CI commands, managed-device or emulator matrix, APK/AAB expectations, and evidence locations.

Do not infer newest versions from this template. A toolchain, SDK, target-SDK, dependency, or build-system upgrade is an architecture and delivery change, not an incidental feature task.

## 2. Greenfield defaults

- Kotlin and Gradle Kotlin DSL.
- Version Catalog for dependency versions unless an accepted decision chooses another reproducible approach.
- Compose-first UI unless approved product or platform constraints require Views or a hybrid boundary.
- Coroutines with structured concurrency.
- Immutable/read-only UI state, normally exposed through `StateFlow`.
- Lifecycle-aware state collection.
- Android `ViewModel` as the default state owner for meaningful route-level workflows; alternatives require an accepted ADR.
- One approved dependency-composition mechanism.
- Resource-based localization with deterministic locale-key validation.
- Keep the first walking skeleton simple. Do not create modules, layers, convention plugins, code generators, or abstractions solely to satisfy a template.

## 3. Thin Android host contract

`Application`, `MainActivity`, other activities, fragments used only as hosts, and top-level navigation hosts are thin platform boundaries.

They may:

- configure edge-to-edge behavior and system UI;
- install the application theme;
- establish the approved application composition root;
- host the root application or navigation UI;
- register approved lifecycle, app-link, permission, background, and platform hooks.

They must not:

- own meaningful feature workflow state;
- manually instantiate feature ViewModels;
- construct databases, DAOs, repositories, gateways, use cases, workers, schedulers, or provider clients ad hoc;
- execute domain operations directly;
- contain feature-specific screen implementations;
- become a generic service locator;
- hide required dependency, lifecycle, or protected-boundary ownership.

## 4. Project structure and dependency direction

Before implementation, record:

- namespace and source roots;
- app and composition-root ownership;
- feature ownership boundaries;
- presentation, domain, data, and platform boundaries;
- allowed dependency directions;
- ViewModel, route, content, navigation, repository, data source, worker, receiver, service, provider, and design-system locations;
- build-variant and source-set ownership;
- criteria for remaining single-module versus extracting modules.

Recommended logical shape when a single application module is sufficient:

```text
app/
  src/main/
    <namespace>/
      application/
      features/
        <feature>/
          presentation/
          domain/
          data/
      shared/
        designsystem/
        localization/
        platform/
        testing/
```

This is an ownership model, not a requirement to create empty directories.

Do not:

- place feature code in root packages, activities, generic `utils`, `common`, `base`, or unrelated source sets;
- create modules merely to satisfy the template;
- introduce circular module dependencies;
- let UI depend directly on persistence or provider implementations;
- add a dependency-injection framework without an accepted decision.

## 5. Presentation state and ViewModel contract

Every meaningful screen or workflow must declare:

- state owner and lifetime;
- durable source of truth;
- event/input boundary;
- asynchronous ownership and cancellation;
- navigation ownership;
- restoration and process-death behavior;
- dependency construction path.

Default contract:

- route-level workflow state is owned by an Android `ViewModel`;
- UI-facing streams are immutable/read-only;
- state is normally exposed as a single coherent UI state or clearly bounded state streams;
- events enter through explicit methods or event types;
- asynchronous domain work is owned by the ViewModel or lower domain/data boundary, never by leaf Composables;
- state required after process death reconstructs from durable state plus minimal saved identifiers or inputs where appropriate;
- `SavedStateHandle` stores only bounded, nonsensitive restoration input and is not a substitute for durable storage;
- ViewModels, repositories, and dependencies come from the approved composition mechanism;
- Activities and Composables do not manually instantiate ViewModels or infrastructure.

Do not create a ViewModel merely to wrap static display values. Stateless leaf UI remains stateless.

## 6. Dependency composition

Before implementation, select and record the approved composition approach, such as Hilt, Dagger, Koin, or manual composition.

Requirements:

- one authoritative production composition path;
- explicit scopes and lifetime ownership;
- deterministic test replacement;
- deterministic preview/design-time composition;
- no service locator;
- no ad hoc construction in Activities, Fragments, Composables, workers, or receivers;
- no debug, fake, preview, or test bindings in release composition;
- missing production bindings fail closed.

If Hilt or another framework is selected, record:

- application/component ownership;
- Activity, navigation-graph, ViewModel, repository, worker, and singleton scopes;
- replacement strategy for tests;
- generated-code and build implications;
- release-graph inspection requirements.

## 7. Compose screen implementation contract

Every meaningful Compose screen must define:

1. A stateful route boundary that obtains the approved ViewModel/state holder, collects state lifecycle-aware, and translates navigation and external events.
2. A stateless content boundary that accepts plain immutable state and callbacks and does not accept a ViewModel, repository, use case, DAO, service, worker, or `NavController`.
3. Loading, empty, failure, recovery, disabled, and success states when material.
4. Navigation, back, modal, deep-link, restoration, and dismissal behavior where applicable.
5. Compact, medium, expanded, resize, fold, locale, RTL, font-scale, display-scale, input, and accessibility behavior where applicable.
6. A preview and verification matrix.

All previews use deterministic, non-sensitive data and belong to stateless content or isolated components.

Previews are not runtime, TalkBack, lifecycle, persistence, process-death, navigation, performance, or device evidence.

Prohibited patterns include:

- domain, repository, database, provider, or navigation side effects during composition;
- state-holder creation during recomposition;
- unowned coroutine launches;
- collecting flows without lifecycle awareness;
- passing `NavController` or infrastructure to leaf content;
- hardcoded strings;
- fixed-height text that clips under scaling;
- absolute left/right assumptions;
- phone-only or portrait-only composition;
- preview or sample data entering production behavior.

## 8. Coroutines and Flow safety

Before implementation, record coroutine, dispatcher, and Flow rules.

Requirements:

- use structured concurrency;
- define scope ownership;
- use `viewModelScope` for presentation-owned work;
- use approved lower-layer scopes only for durable work whose lifetime exceeds a ViewModel;
- inject dispatchers where deterministic testing or architecture requires it;
- never use `GlobalScope`;
- do not launch fire-and-forget work that silently drops failure;
- propagate cancellation;
- distinguish presentation cancellation from durable transaction or background-work ownership;
- define terminal states for user-visible asynchronous workflows;
- avoid unbounded hot-flow lifetimes;
- define sharing policy for `stateIn` and `shareIn`;
- handle exceptions at explicit boundaries;
- serialize or guard duplicate side effects;
- do not use broad dispatcher switching merely to silence thread-safety problems.

## 9. Navigation, back, and restoration

Select and document Navigation Compose, Fragment Navigation, or another approved mechanism before multiple feature flows are built.

Requirements:

- typed or otherwise validated route arguments;
- stable, nonsensitive identifiers;
- no raw meal text, images, tokens, secrets, or large payloads in routes;
- route/container ownership of navigation;
- leaf content emits navigation intents only;
- explicit modal save/discard/cancel behavior;
- predictable system back and predictive-back behavior where supported and in scope;
- deep links and app links treated as protected external entry points;
- process-death restoration reconstructs from durable state and minimal identifiers;
- state is preserved across Activity recreation, configuration changes, window resize, and navigation restoration.

## 10. Persistence and local data integrity

Persistence technology is an architecture decision. Evaluate Room, DataStore, files, SQL-based alternatives, encrypted storage, Keystore-backed secrets, and server-backed sources against product, SDK, migration, concurrency, testability, backup, and data-volume requirements.

Requirements:

- define the system of record;
- define schema/version ownership and migrations before durable data ships;
- use explicit transactions for multi-record operations;
- define rollback and failed-migration recovery;
- define logical idempotency in addition to uniqueness where product behavior requires it;
- define stale-write behavior and concurrency ownership;
- define date attribution and historical integrity;
- isolate test stores and migration fixtures;
- verify process termination and relaunch;
- define backup, restore, device transfer, deletion, cache, and logout behavior;
- do not use in-memory storage as a release substitute for required durability;
- do not expose persistence entities directly to leaf UI.

## 11. Android lifecycle and process death

Plans and tasks must explicitly cover applicable:

- Activity recreation;
- configuration changes;
- process death;
- background and foreground transitions;
- multi-window and freeform resize;
- fold posture and hinge changes;
- navigation restoration;
- IME visibility and focus;
- app upgrade and migration.

Do not claim process-death resilience from ViewModel recreation alone. Required workflow state must reconstruct from durable state or approved saved identifiers.

Runtime evidence for process death must name the emulator/device, OS version, termination procedure, expected recovered state, actual result, and artifact.

## 12. Adaptive UI and supported surfaces

Define the supported Android surface matrix before a representative screen is considered complete.

Default review considers:

- compact, medium, and expanded window size classes;
- portrait and landscape;
- phones, tablets, foldables, and ChromeOS-capable/resizable devices where in scope;
- split-screen, freeform, and multi-window;
- fold posture and hinge;
- edge-to-edge, status/navigation bars, display cutouts, and IME;
- touch, keyboard, mouse, trackpad, D-pad, and switch input;
- RTL;
- font scale and display scale;
- color correction/inversion, animation settings, and accessibility services.

Implementation requirements:

- consume adaptive/window information at the correct app, shell, feature, or screen boundary;
- preserve one business state across layout variants;
- preserve state across resize, orientation, recreation, and process restoration;
- avoid phone-only, portrait-only, fixed-root, or stretch-only tablet layouts;
- use navigation rail, drawer, list-detail, supporting pane, or other adaptive patterns only when information architecture requires them;
- keep actions reachable with IME and system insets;
- avoid clipping or hidden actions at large font/display scales;
- provide representative compact and expanded previews where feasible;
- produce named emulator/device runtime evidence for required configurations.

Static inspection and previews do not prove compatibility.

## 13. Localization and RTL

- Zero hardcoded user-facing or accessibility-facing strings in Activities, Fragments, Composables, ViewModels, use cases, workers, receivers, services, error mappers, or notifications.
- Use Android resources, plurals, format arguments, and approved localized domain content.
- Do not concatenate translated sentence fragments.
- Use locale-aware formatting for dates, times, numbers, currencies, percentages, lists, measurements, and units.
- Use start/end semantics, logical alignment, and bidirectional-safe formatting.
- Define required locales and fallback behavior before UI implementation.
- Maintain locale-key parity through a deterministic check.
- Exercise pseudo-locales where useful, at least one approved RTL locale, representative long translations, mixed-direction content, and large-font configurations.
- Treat untranslated fallback, stale keys, malformed plurals, and hardcoded strings as deterministic failures.

## 14. Accessibility

Plans, tasks, and convergence evidence must cover applicable:

- TalkBack labels, roles, state descriptions, headings, actions, and traversal;
- focus order, restoration, and announcements;
- live regions for validation and asynchronous status;
- touch-target sizing;
- keyboard and D-pad navigation;
- Switch Access and Voice Access;
- large font scale and display scale;
- non-color differentiation;
- reduced or removed animations;
- color correction and inversion;
- error identification and recovery;
- modal focus behavior;
- adaptive reflow without lost state.

TalkBack/manual evidence must identify:

- exact device/emulator;
- OS version;
- locale;
- font/display settings;
- accessibility services;
- procedure;
- expected result;
- actual result;
- artifact;
- limitation.

## 15. Permissions, manifests, capabilities, and external entry points

Treat as protected:

- manifest permissions;
- runtime permissions;
- notification permission;
- foreground-service types;
- exact alarms;
- background location;
- camera, microphone, photos/media, contacts, Bluetooth, nearby devices, and Health Connect;
- exported Activities, Services, Receivers, and Providers;
- intent filters, app links, deep links, and custom schemes;
- WorkManager, JobScheduler, foreground services, alarms, and boot receivers;
- Play Integrity or another attestation mechanism;
- billing and entitlement;
- signing, APK/AAB, Play Console, internal testing, staged rollout, and production publication.

A dependency, manifest entry, JSON/XML configuration file, service declaration, or provider metadata does not authorize capability use.

Configuration retained for future features must have explicit repository location, source-set and target inclusion, initialization behavior, privacy impact, and inactive-status evidence.

## 16. Networking and external services

Before adding a networking client or provider SDK, define:

- endpoint and environment ownership;
- authentication and credential boundaries;
- request/response contracts and versioning;
- timeout, retry, cancellation, idempotency, and offline behavior;
- transport security and certificate expectations;
- privacy, logging, and redaction;
- test, staging, and production composition;
- attestation and fail-closed behavior where required.

Do not embed production secrets in source, resources, generated configuration, or client-visible assets. Missing configuration fails closed.

## 17. Background work and scheduled execution

Select WorkManager, foreground services, alarms, push-triggered work, or another mechanism only from approved product needs.

Define:

- scheduling ownership;
- constraints;
- retries and terminal states;
- unique-work or other deduplication identity;
- cancellation;
- expedited/foreground behavior;
- process-death behavior;
- reboot behavior where required;
- user-visible recovery;
- data protection;
- exact evidence.

Do not use no-op workers, debug-only success, network-reachability callbacks as execution guarantees, or exact timing promises unsupported by Android.

## 18. Dependency and supply-chain policy

- Record dependency purpose, owner, version rule, license, privacy impact, transitive dependencies, native/binary content, SDK support, and removal plan.
- Use reproducible version constraints.
- Do not add unbounded dynamic versions.
- Verify repositories, checksums, signatures, and provenance where supported.
- Review manifest-merger effects, consumer rules, R8/ProGuard implications, and generated code.
- Do not update unrelated dependencies during a feature task.

## 19. Testing and evidence defaults

Select exact commands and device matrix during initialization.

Typical layers:

- local JVM unit tests;
- coroutine and Flow tests;
- repository/integration tests;
- Room/DataStore migration tests;
- Robolectric only where explicitly accepted for its bounded purpose;
- instrumented tests;
- Compose UI tests;
- emulator runtime;
- physical-device runtime;
- TalkBack/manual accessibility;
- process-death/relaunch evidence;
- background-work evidence;
- app-link and permission evidence;
- lint and resource validation;
- release APK/AAB, manifest, dependency, signing, and R8 inspection;
- Play service, billing, attestation, or backend evidence where applicable.

Every task must name:

- observable contract;
- test/evidence layer;
- command or procedure;
- configuration/environment;
- expected result;
- actual result;
- artifact path;
- unsupported or unverified layers.

Compilation, previews, screenshots, and host tests do not prove TalkBack, process death, multi-window, permission flows, background execution, app links, billing, attestation, signing, APK/AAB behavior, or physical-device behavior.

## 20. Production integrity

Release source sets and the release dependency graph must not contain or silently select:

- fake repositories, DAOs, gateways, provider clients, or workers;
- manufactured provider responses;
- fixed successful identifiers;
- accept-all validation;
- placeholder authorization, billing, attestation, or receipts;
- no-op WorkManager jobs, schedulers, migrations, or background components;
- in-memory substitutes for required durable state;
- debug menus or bypasses;
- preview/sample data driving production behavior;
- mock servers or fake endpoints;
- permissive fallback from unavailable infrastructure to simulated success.

Inspect:

- source sets;
- build variants;
- manifest merger;
- DI bindings;
- generated configuration;
- `BuildConfig` flags;
- package products;
- APK/AAB contents;
- R8 output;
- runtime initialization.

## 21. Required Android procedures and routing

The repository must install or provide equivalent procedures for:

- `android-architecture-readiness`;
- `android-project-structure-readiness`;
- `compose-screen-readiness`;
- `android-views-screen-readiness` when Views are used;
- `kotlin-coroutines-readiness`;
- `android-localization-rtl-readiness`;
- `android-adaptive-accessibility-readiness`;
- `android-persistence-migration-readiness`;
- `android-permission-capability-readiness`;
- `android-runtime-evidence-readiness`;
- `production-fake-detection`;
- `documentation-consistency-review`;
- `feature-implementation-convergence`;
- `feature-readiness-review`;
- `pr-review`.

Run architecture, structure, coroutine, permission/capability, persistence, and evidence readiness before planning or implementation where applicable. Run Compose/Views, localization, adaptive, and accessibility readiness before implementing and before completing user-facing UI. Rerun all applicable procedures before convergence and PR review.

A missing procedure or a `Blocked`, `Fail`, or `Not ready` verdict stops the affected work unless the accountable owner explicitly authorizes a narrower non-blocked slice.

## 22. Android convergence requirements

Before owner acceptance, the readiness report must include applicable evidence for:

- Gradle build and test results;
- local and instrumented tests;
- final machine-readable test reports;
- process termination and relaunch;
- Activity recreation and state restoration;
- failed-write rollback and persistence migration;
- compact, medium, expanded, resize, fold, and IME scenarios;
- approved locales, RTL, pseudo-locales, and long text;
- TalkBack, focus, announcements, keyboard/D-pad, and large font/display scaling;
- permission and manifest inspection;
- app-link and external-entry verification;
- background work and deduplication;
- production DI/source-set integrity;
- APK/AAB, manifest, dependency, R8, signing, and release inspection where authorized;
- privacy/network inspection;
- current documentation and architecture coverage.

## 23. Task completion rules

- File, class, module, preview, build, or route existence is not completion.
- A stub, simulated implementation, no-op mechanism, unreachable flow, dead route, unused template model, compile-only result, or preview-only path remains incomplete.
- Every task identifies requirement, architecture decision, package/module boundary, protected boundary, behavioral acceptance criteria, prohibited patterns, evidence scenarios, evidence artifact path, and stop condition.
- Device, background execution, provider, attestation, TalkBack, process-death, reboot, performance, APK/AAB, signing, and release tasks cannot be completed from compilation, previews, screenshots, or host unit tests.
- Task completion gates are checked only after evidence is produced and completion review passes.
