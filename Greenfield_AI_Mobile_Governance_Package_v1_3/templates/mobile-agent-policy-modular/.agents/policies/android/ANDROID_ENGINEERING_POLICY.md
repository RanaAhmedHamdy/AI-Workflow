# Android Engineering Policy

> Greenfield native Android overlay. Use with root `AGENTS.md` and the shared policy modules.

## 1. Initialization

Verify and record:

- Android Studio;
- AGP, Gradle, Kotlin, and JDK;
- compile, target, and minimum SDK;
- application namespace and ID;
- application, library, benchmark, baseline-profile, test-fixture, and dynamic-feature scope;
- build variants, flavors, signing placeholders, and environments;
- Version Catalog and dependency policy;
- Compose/Views, Navigation, lifecycle, persistence, DI, background-work, and test-stack decisions;
- CI commands, emulator/managed-device matrix, APK/AAB outputs, and evidence paths.

Do not infer current versions from this policy.

## 2. Defaults

- Kotlin and Gradle Kotlin DSL.
- Version Catalog unless another reproducible approach is approved.
- Compose-first unless Views or hybrid UI is approved.
- Structured coroutines.
- Immutable/read-only UI state, normally through `StateFlow`.
- Lifecycle-aware state collection.
- Android `ViewModel` for meaningful route-level workflows unless an ADR chooses another owner.
- One approved composition mechanism.
- Resource-based localization.
- No premature modules, convention plugins, code generators, or layers.

## 3. Thin hosts

`Application`, Activities, host Fragments, and top-level navigation hosts may configure platform concerns, composition, theme, edge-to-edge behavior, and approved entry points.

They must not:

- own feature workflow state;
- manually create ViewModels;
- construct databases, DAOs, repositories, workers, schedulers, or providers ad hoc;
- execute domain work;
- contain feature screen implementations;
- become service locators.

## 4. Structure and dependencies

Before implementation, record:

- package and module boundaries;
- composition-root ownership;
- presentation/domain/data/platform boundaries;
- dependency direction;
- locations for routes, content, ViewModels, repositories, data sources, workers, services, receivers, providers, and design system;
- criteria for remaining single-module versus extraction.

Avoid root-package feature code, generic `utils`, circular dependencies, and UI-to-infrastructure coupling.

## 5. ViewModel and state

Every meaningful workflow declares:

- owner and lifetime;
- durable source of truth;
- events;
- async ownership;
- restoration;
- navigation;
- composition path.

Default:

- ViewModel owns route-level state;
- UI consumes immutable state;
- events enter explicitly;
- domain work runs outside leaf Composables;
- state required after process death reconstructs from durable state plus minimal saved identifiers;
- `SavedStateHandle` is not durable storage;
- dependencies come from approved DI/composition.

## 6. Compose contract

Each meaningful screen defines:

1. stateful route boundary;
2. stateless content boundary;
3. material states;
4. navigation/back/modal/restoration behavior;
5. compact/medium/expanded and input/accessibility behavior;
6. preview and verification matrix.

Leaf content must not receive ViewModels, repositories, DAOs, services, workers, or `NavController`.

Prohibit side effects during composition, unowned coroutine launches, non-lifecycle collection, hardcoded strings, fixed-height text, absolute left/right assumptions, phone-only layouts, and preview data driving production.

## 7. Coroutines and Flow

- Use structured concurrency.
- Use `viewModelScope` for presentation-owned work.
- Use approved lower-layer scopes only for durable work.
- Never use `GlobalScope`.
- Propagate cancellation.
- Define terminal states.
- Guard duplicate side effects.
- Handle errors explicitly.
- Define `stateIn`/`shareIn` policies.
- Inject dispatchers when architecture or deterministic testing requires it.

## 8. Navigation and restoration

Define:

- approved navigation framework;
- typed or validated route arguments;
- stable nonsensitive identifiers;
- route ownership;
- modal save/discard/cancel behavior;
- system back and predictive back;
- deep/app-link contracts;
- Activity recreation;
- process-death restoration;
- resize and multi-window restoration.

Do not place secrets or large payloads in routes.

## 9. Persistence

Select Room, DataStore, files, SQL alternatives, encrypted storage, Keystore-backed secrets, or server-backed sources through architecture decision.

Define:

- system of record;
- schema/version ownership;
- migrations and recovery;
- transactions and rollback;
- idempotency and duplicates;
- stale writes;
- date attribution;
- process-death/relaunch behavior;
- backup, restore, transfer, deletion, cache, and logout;
- test stores and fixtures.

Do not expose persistence entities to leaf UI or use in-memory release substitutes.

## 10. Lifecycle and process death

Cover applicable:

- Activity recreation;
- configuration changes;
- process death;
- background/foreground;
- multi-window/freeform;
- fold posture;
- navigation restoration;
- IME/focus;
- upgrade/migration.

ViewModel recreation alone does not prove process-death resilience.

## 11. Adaptive surfaces

Define the supported matrix:

- compact, medium, expanded;
- portrait/landscape;
- phones, tablets, foldables, ChromeOS-capable/resizable devices;
- split-screen, freeform, multi-window;
- fold posture and hinge;
- edge-to-edge, bars, cutouts, and IME;
- touch, keyboard, mouse, trackpad, D-pad, and switch input;
- RTL;
- font and display scaling.

Preserve one business state across layouts and lifecycle changes. Provide named emulator/device runtime evidence.

## 12. Localization and RTL

- No hardcoded user-facing or accessibility strings.
- Use resources, plurals, format arguments, and locale-aware formatting.
- Do not concatenate translated fragments.
- Use start/end semantics and bidi-safe formatting.
- Define locales and fallback.
- Validate locale-key parity.
- Exercise pseudo-locales, one approved RTL locale, long translations, mixed-direction content, and large scaling.

## 13. Accessibility

Cover applicable:

- TalkBack semantics and traversal;
- focus and restoration;
- validation announcements;
- live regions;
- touch targets;
- keyboard/D-pad;
- Switch Access and Voice Access;
- font/display scaling;
- non-color differentiation;
- animation reduction;
- error recovery;
- adaptive reflow.

Manual evidence names device/emulator, OS, locale, settings, procedure, expected result, actual result, artifact, and limitation.

## 14. Permissions and platform declarations

Treat as protected:

- manifest and runtime permissions;
- notification permission;
- foreground-service types;
- exact alarms;
- location, camera, microphone, media, contacts, Bluetooth, nearby devices, and Health Connect;
- exported Activities, Services, Receivers, and Providers;
- intent filters, app links, deep links, and schemes;
- WorkManager, JobScheduler, foreground services, alarms, and boot receivers;
- Play Integrity;
- billing;
- signing and Play distribution.

A dependency, manifest entry, or config resource does not authorize use.

## 15. External services

Before networking or SDK integration, define endpoints, credentials, contracts, retry/cancellation/idempotency, offline behavior, transport security, privacy/redaction, environment composition, attestation, and fail-closed behavior.

Do not embed production secrets in source or resources.

## 16. Background work

Use WorkManager, foreground services, alarms, or push-triggered work only from approved need.

Define constraints, retries, terminal states, unique-work identity, cancellation, process-death/reboot behavior, user-visible recovery, and evidence.

No no-op workers, debug success, or unsupported timing guarantees.

## 17. Supply chain

Record dependency purpose, owner, version rule, license, privacy impact, transitive/native content, SDK support, and removal plan.

Review manifest merger, generated code, consumer rules, and R8/ProGuard effects. Avoid dynamic versions and unrelated upgrades.

## 18. Testing and evidence

Applicable layers include:

- JVM tests;
- coroutine/Flow tests;
- repository/integration tests;
- Room/DataStore migration tests;
- instrumented tests;
- Compose UI tests;
- emulator and physical-device runtime;
- TalkBack/manual evidence;
- process death;
- background work;
- app links and permissions;
- lint/resource checks;
- APK/AAB, manifest, dependency, signing, and R8 inspection;
- Play service, billing, attestation, or backend evidence.

Compilation and previews do not prove runtime-only behavior.

## 19. Production integrity

Inspect source sets, variants, manifest merger, DI bindings, generated configuration, `BuildConfig`, package products, APK/AAB contents, R8 output, and runtime initialization.

Prohibit release fakes, manufactured success, placeholder authorization, no-op workers/migrations, in-memory durability substitutes, debug bypasses, sample data, fake endpoints, dead routes, and unused template code.

## 20. Required Android procedures

Provide equivalents for:

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
- `feature-implementation-convergence`;
- `feature-readiness-review`;
- `documentation-consistency-review`;
- `pr-review`.

## 21. Android acceptance evidence

Before owner acceptance, include applicable:

- Gradle build/test results;
- machine-readable reports;
- process termination and relaunch;
- Activity recreation;
- rollback and migration;
- compact/medium/expanded, resize, fold, and IME;
- locales, RTL, pseudo-locales, and long text;
- TalkBack, focus, announcements, input, and scaling;
- permission and manifest inspection;
- app-link and external-entry verification;
- background work and deduplication;
- production DI/source-set integrity;
- APK/AAB, manifest, dependency, R8, and signing inspection where authorized;
- privacy/network inspection;
- current documentation and architecture coverage.
