# AGENTS.md — Greenfield Native iOS Overlay

> Version 2.0. Use with `AGENTS.common.md`.
>
> These are reusable defaults, not inferred project facts. Record an explicit decision for every material exception. Verify current Apple toolchain, SDK, simulator, device, signing, and distribution facts during repository initialization rather than pinning this template to future-stale versions.

## 1. Project initialization and verified toolchain

Before planning the first implementation slice, record and verify:

- supported Apple platforms, form factors, orientations, and deployment targets;
- exact Xcode, Swift language mode, SDK, simulator runtime, and macOS build-host requirements;
- project format or approved project generator;
- application, unit-test, UI-test, extension, widget, watch, vision, Catalyst, and other target scope;
- dependency management and `Package.resolved` policy;
- signing-development-team expectations without accessing production credentials;
- build configurations, schemes, test plans, CI commands, archive expectations, and evidence locations;
- release channels and protected distribution workflow.

Do not infer the newest toolchain from this template. A toolchain, SDK, Swift-mode, deployment-target, project-format, or package upgrade is an architecture and delivery change, not an incidental feature task.

## 2. Greenfield defaults

- Swift-first and SwiftUI-first unless an approved platform or product constraint requires UIKit, AppKit, or a hybrid boundary.
- Swift Concurrency for new asynchronous work.
- One repository-approved observation model.
- Observation (`@Observable`) only when compatible with approved deployment targets and architecture.
- Swift Package Manager for external dependencies unless an accepted decision chooses another mechanism.
- Swift Testing for new pure Swift unit and integration tests when supported by the approved baseline.
- XCTest/XCUITest for UI automation, performance, system integration, legacy compatibility, or APIs not covered by Swift Testing.
- String Catalogs or another explicitly approved localization source.
- Keep the first walking skeleton simple. Do not create targets, packages, frameworks, coordinators, layers, or abstractions solely to satisfy a template.

## 3. Thin application and scene host contract

The `App` type, `SceneDelegate`, `AppDelegate`, root UIKit controller, and scene entry points are thin platform hosts.

They may:

- configure application scenes;
- establish the approved composition root;
- install root navigation or application-shell UI;
- register approved platform services and lifecycle hooks;
- configure approved environment and release bindings.

They must not:

- own meaningful feature workflow state;
- contain feature-specific screens or business rules;
- construct feature dependencies ad hoc;
- execute domain operations directly;
- become a global service locator;
- hide dependency, concurrency, navigation, persistence, or lifecycle ownership.

Feature state and behavior live in approved feature presentation, domain, data, and platform boundaries.

## 4. Project structure and dependency direction

Before implementation, record:

- bundle identifier namespace and Swift module naming;
- target and local-package structure;
- application composition-root ownership;
- feature ownership boundaries;
- presentation, domain, data, and platform-integration boundaries;
- allowed dependency directions;
- locations for observable state, routes/coordinators, views, repositories, clients, persistence adapters, background handlers, intents, widgets, and design-system code;
- test-target and fixture ownership;
- criteria for remaining in one application target versus extracting local Swift packages or framework targets.

Recommended logical shape when one application target is sufficient:

```text
App/
  Application/
  Features/
    <Feature>/
      Presentation/
      Domain/
      Data/
  Shared/
    DesignSystem/
    Localization/
    Platform/
    Diagnostics/
    TestingSupport/
AppTests/
AppUITests/
```

This is a logical ownership model, not a requirement to create empty folders or one type per file.

Do not:

- create generic `Utils`, `Base`, `Helpers`, or global `Models` dumping grounds;
- place feature behavior in application entry points;
- create packages or targets merely for template compliance;
- introduce circular dependencies;
- expose persistence or provider implementations directly to leaf UI;
- leave default Xcode template models, dead routes, unreachable screens, or sample production code without contract and task traceability.

## 5. Presentation state and observation

Every meaningful screen or workflow must declare:

- state owner and lifetime;
- durable source of truth;
- event/input boundaries;
- asynchronous ownership and cancellation;
- restoration behavior;
- navigation ownership;
- dependency construction path.

Default contract:

- UI-observable workflow state is owned outside leaf render views;
- UI-driving state mutations occur on the approved main-actor boundary;
- leaf views receive plain values and action closures where practical;
- persistence models, contexts, repositories, clients, StoreKit services, authorization services, and application routers are not passed to leaf views;
- durable workflow state reconstructs from persistence rather than relying only on in-memory observation;
- side effects do not run from `body`;
- state holders are not recreated during view recomputation;
- multiple bounded state holders are preferred over one giant feature object when responsibilities differ.

When using Observation:

- choose ownership deliberately with `@State`, typed environment injection, or an approved composition boundary;
- declare actor isolation explicitly;
- do not use `@Observable` merely to imitate a ViewModel naming convention;
- do not expose mutable implementation details broadly.

## 6. Swift concurrency safety

Before enabling or changing strict-concurrency settings, record the approved Swift language mode and migration scope.

Requirements:

- define actor isolation for UI state, persistence contexts, caches, clients, and shared mutable services;
- require `Sendable` correctness across isolation boundaries;
- avoid `@unchecked Sendable` except with documented invariants and focused concurrent tests;
- use structured concurrency;
- justify detached tasks, unstructured `Task` creation, actor escapes, and continuation bridges;
- use lifecycle-owned `.task` or `.task(id:)` for presentation-scoped SwiftUI work where appropriate;
- do not cancel durable persistence, billing, security, export, or background operations merely because a view disappears;
- propagate cancellation;
- resume continuations exactly once;
- map errors to typed product outcomes;
- provide bounded terminal states;
- prevent duplicate side effects and reentrancy errors;
- do not weaken compiler settings or apply broad actor annotations merely to silence diagnostics.

Every asynchronous operation must have an owner, lifetime, cancellation rule, isolation boundary, terminal state, and duplicate-invocation analysis.

## 7. Dependency composition

- Construct clients, repositories, persistence containers, clocks, configuration, diagnostics, analytics, and feature state through an explicit application composition root.
- Prefer initializer injection and protocol boundaries where substitution is required.
- Delegate bounded feature construction to feature factories or equivalent composition boundaries where the root would otherwise become monolithic.
- Typed environment injection is allowed only at explicit root or feature boundaries.
- Environment values must not become a generic service locator.
- Do not add a DI framework unless an accepted decision shows concrete value beyond Swift-native composition.
- Preview and test dependencies must not be selected by release composition.
- Missing production dependencies fail closed.

## 8. SwiftUI screen implementation contract

Every meaningful SwiftUI screen must define:

1. A route/container boundary responsible for obtaining approved state and translating navigation or external events.
2. A render/content view that depends on plain state and action closures where practical.
3. Loading, empty, failure, recovery, disabled, and success states when material.
4. Push, sheet, full-screen cover, tab, split-view, deep-link, restoration, dismissal, save, discard, and cancel behavior where applicable.
5. Device, size-class, orientation, multitasking, locale, RTL, Dynamic Type, input, and accessibility behavior.
6. A preview and verification matrix.

Leaf views must not receive repositories, persistence contexts, API clients, StoreKit services, authorization services, or application routers unless accepted architecture explicitly assigns that responsibility.

Avoid:

- side effects in `body`;
- observable-model recreation during recomputation;
- unowned tasks from `.onAppear` or `.onChange`;
- hardcoded strings;
- fixed-height text;
- hardcoded left/right layout;
- compact-only, portrait-only, or single-window assumptions;
- inaccessible custom controls;
- previews presented as runtime proof.

All previews use deterministic, non-sensitive data and are excluded from release behavior.

## 9. Navigation and restoration

Select and document the navigation approach before multiple feature flows are built.

Requirements:

- use `NavigationStack`, `NavigationSplitView`, coordinators, or UIKit navigation only where approved architecture and information architecture require them;
- use stable, typed, nonsensitive route identifiers;
- do not persist arbitrary `NavigationPath` as the durable system of record;
- persist only minimal restoration intent;
- validate restored identifiers against repositories;
- recover safely when referenced records are missing or stale;
- leaf views emit navigation intents;
- sheets and covers define ownership, dismissal, save/discard, and restoration;
- back, swipe dismissal, or pull-down dismissal must never silently commit, discard, purchase, delete, transfer, or reassign data;
- deep links, universal links, Spotlight, notifications, widgets, App Intents, and external URLs are protected entry points.

## 10. Persistence and local data integrity

Persistence technology is an architecture decision. Evaluate SwiftData, Core Data, SQLite-based solutions, files, Keychain, protected stores, and server-backed sources against deployment target, migration, concurrency, testing, protection, backup, deletion, and data-volume needs.

Requirements:

- define the system of record;
- define schema/model ownership and versioning before durable data ships;
- define migration strategy and representative production fixtures;
- define failed-migration recovery;
- isolate persistence through approved actors, model actors, contexts, or single-owner boundaries;
- use explicit atomic operations for multi-record updates;
- define rollback;
- define logical idempotency in addition to uniqueness where required;
- define stale-write behavior;
- preserve historical data and date attribution;
- define backup, device transfer, file protection, Keychain, caches, temporary data, deletion, logout, and account removal;
- isolate test stores;
- verify process termination and relaunch;
- do not use in-memory storage as a release substitute;
- do not expose persistence entities to leaf views;
- do not overclaim forensic deletion.

SwiftData is not an automatic default. Core Data is not automatically rejected as legacy. Select from approved product and deployment constraints.

## 11. Networking and external services

Before adding a networking client, backend SDK, Firebase configuration, analytics SDK, crash SDK, AI provider, or other external service, define:

- transport and endpoint ownership;
- authentication and credential boundaries;
- request/response contracts and versioning;
- timeout, retry, cancellation, idempotency, and offline behavior;
- ATS, certificate, and trust expectations;
- privacy, minimization, logging, and redaction;
- configuration and environment separation;
- test, staging, and production composition;
- attestation and fail-closed behavior where required.

Prefer platform `URLSession` unless an accepted decision justifies another stack.

Do not embed production secrets in source, assets, generated settings, or client-visible configuration.

A retained configuration file such as `GoogleService-Info.plist` does not authorize SDK initialization or capability use. Its repository location, target membership, Copy Bundle Resources status, build-product inclusion, automatic-initialization behavior, privacy impact, and future-feature authority must be explicit. A pure-local slice must prove that no out-of-scope SDK initializes, no network call occurs, and no external user-data transfer occurs.

## 12. Localization, RTL, and formatting

- Zero hardcoded user-facing or accessibility-facing strings in SwiftUI, UIKit, observable state, domain error mapping, notifications, widgets, intents, or background handlers.
- Use String Catalogs or another approved localization source with stable keys and reviewed fallback behavior.
- Use locale-aware formatting for dates, times, measurements, currencies, numbers, lists, percentages, units, and plurals.
- Do not concatenate translated sentence fragments.
- Use leading/trailing and semantic alignment rather than hardcoded left/right behavior.
- Exercise at least one approved RTL locale and representative long translations.
- Verify Arabic/Hebrew shaping where applicable, mixed-direction text, numerals, units, punctuation, truncation, and fallback.
- Treat localization-key parity, stale keys, missing keys, malformed substitutions, and untranslated fallback as deterministic validation targets.

## 13. Adaptive UI and supported Apple surfaces

Define the supported matrix before a representative screen is considered complete:

- iPhone device classes and orientations;
- iPad compact and regular widths;
- Split View, Slide Over where supported, Stage Manager, and reduced-width multitasking;
- multiple scenes/windows and external display where in scope;
- physical keyboard, pointer, trackpad, Full Keyboard Access, Switch Control, and Voice Control;
- Mac Catalyst or Designed for iPad scope;
- visionOS, watchOS, tvOS, widgets, Live Activities, and extensions only when explicitly in scope;
- light/dark appearance, accessibility content sizes, Bold Text, Button Shapes, Differentiate Without Color, Increased Contrast, Reduce Motion, and Reduce Transparency;
- safe areas, keyboard, sheets, popovers, menus, toolbars, and pointer interaction.

Implementation requirements:

- avoid fixed-size, portrait-only, compact-only, and single-window assumptions;
- preserve one business state across layout variants;
- use size classes and container-relative layout intentionally rather than device-name checks;
- use split-view navigation only when information architecture requires it;
- preserve state across rotation, resizing, multitasking, scene changes, and restoration;
- keep focused fields and required actions reachable with the keyboard shown;
- avoid clipping or hidden actions at accessibility text sizes;
- distinguish previews and snapshots from simulator/device evidence.

## 14. Accessibility

Plans, tasks, and convergence evidence must cover applicable:

- VoiceOver labels, values, traits, actions, headings, state descriptions, and traversal;
- logical focus order;
- validation and error announcements;
- modal focus restoration;
- Dynamic Type, including approved accessibility sizes;
- Bold Text;
- Button Shapes;
- Differentiate Without Color;
- Increased Contrast;
- Reduce Transparency;
- Reduce Motion;
- touch targets;
- Switch Control;
- Full Keyboard Access;
- pointer/trackpad interaction;
- Voice Control;
- adaptive reflow and state preservation;
- long translations and RTL.

Manual evidence must identify:

- exact simulator/device;
- OS version;
- locale;
- content size;
- accessibility settings;
- procedure;
- expected result;
- actual result;
- artifact;
- limitation.

A generic three-item accessibility log cannot satisfy a task whose acceptance criteria name additional settings or scenarios.

## 15. Privacy, security, capabilities, and platform declarations

Treat as protected:

- `PrivacyInfo.xcprivacy` and third-party privacy manifests;
- required-reason APIs;
- `Info.plist` usage descriptions;
- entitlements, App Groups, Keychain groups, associated domains, URL schemes, and capabilities;
- ATS exceptions and certificate behavior;
- push notifications, background modes, BGTaskScheduler, location, camera, microphone, photos, contacts, Bluetooth, HealthKit, HomeKit, and sensitive frameworks;
- StoreKit, subscriptions, receipts, and entitlement state;
- analytics, crash reporting, logging, and tracking domains;
- signing, provisioning, export compliance, notarization, TestFlight, and App Store distribution.

Every collected or transferred data category requires an approved purpose, minimization, disclosure/consent rule, retention, deletion, backup, logging, and recovery contract.

A framework import, configuration file, plist key, package, or entitlement does not authorize capability use.

## 16. Background execution and extensions

Select BGTaskScheduler, background URLSession, push-triggered work, processing tasks, refresh tasks, widgets, Live Activities, App Intents, or extensions only from approved product needs.

Define:

- scheduling ownership;
- identifiers and registration;
- expiration handling;
- cancellation;
- retries and terminal states;
- deduplication and idempotency;
- data protection;
- foreground/startup reconciliation;
- user-visible recovery;
- exact evidence.

Background execution is opportunistic unless Apple guarantees otherwise. Do not promise exact execution timing.

App and extension targets share data only through approved App Group or other documented boundaries.

## 17. Dependency and supply-chain policy

- Prefer source-based Swift packages from trustworthy maintainers when equivalent to binary dependencies.
- Record dependency purpose, owner, version rule, license, privacy impact, binary content, transitive dependencies, platform support, and removal plan.
- Commit `Package.resolved` when repository policy requires reproducible application dependency resolution.
- Avoid branch-based or unbounded dependency rules for release code without explicit justification.
- Verify binary package checksums, signatures, privacy manifests, and provenance.
- Inspect generated build products and embedded frameworks.
- Do not update unrelated packages during a feature task.

## 18. Testing and evidence defaults

Select exact strategy, commands, simulator/device matrix, and evidence paths during initialization.

Typical layers:

- Swift Testing for pure Swift unit, state, domain, repository, migration, and integration tests where supported;
- XCTest where required for existing APIs, performance, Objective-C interoperability, or unsupported cases;
- XCUITest for user journeys and system interaction;
- previews and snapshots for bounded development and visual-regression evidence;
- simulator runtime;
- physical-device runtime;
- VoiceOver/manual accessibility;
- Dynamic Type and RTL runtime;
- process termination and relaunch;
- background execution;
- universal-link/deep-link verification;
- StoreKit test/staging evidence;
- privacy-manifest and entitlement inspection;
- archive/export/signing evidence;
- external-service attestation.

Every task must name:

- observable contract;
- test/evidence layer;
- configuration/environment;
- command or procedure;
- expected result;
- actual result;
- artifact path;
- unsupported or unverified layers.

Compilation, previews, snapshots, and host tests do not prove VoiceOver, Dynamic Type, scene restoration, multitasking, background execution, permissions, universal links, StoreKit, HealthKit, signing, archive, or device behavior.

Machine-readable `.xcresult` or other approved result artifacts must exist at the canonical path and correspond to the final corrected source revision. Stale path references block evidence validity.

## 19. Production integrity

Release composition must not contain or silently select:

- simulated provider success;
- fixed successful identifiers;
- accept-all validation;
- placeholder authorization, attestation, or receipts;
- no-op repositories, schedulers, background handlers, or migrations;
- in-memory substitutes for required durable state;
- preview/test dependencies;
- debug menus or bypasses;
- dead routes or unreachable future-feature placeholders;
- default template models with no contract or plan traceability;
- silent fallback from unavailable infrastructure to fake success.

Inspect:

- target membership;
- build configurations;
- conditional compilation;
- dependency containers;
- environment values;
- generated configuration;
- package products;
- Copy Bundle Resources;
- archived application contents.

Configuration retained for future features may remain in the repository, but its active target/build inclusion and runtime initialization must be explicitly authorized and evidenced.

## 20. Required iOS procedures and routing

The repository must install or provide equivalent procedures for:

- `ios-architecture-readiness`;
- `ios-project-structure-readiness`;
- `swift-concurrency-readiness`;
- `swiftui-screen-readiness`;
- `uikit-screen-readiness` when UIKit is used;
- `ios-localization-rtl-readiness`;
- `ios-adaptive-accessibility-readiness`;
- `ios-persistence-migration-readiness`;
- `ios-privacy-capability-readiness`;
- `ios-runtime-evidence-readiness`;
- `production-fake-detection`;
- `documentation-consistency-review`;
- `feature-implementation-convergence`;
- `feature-readiness-review`;
- `pr-review`.

Run architecture, structure, concurrency, privacy/capability, persistence, and evidence readiness before planning or implementation where applicable. Run SwiftUI/UIKit, localization, adaptive, and accessibility readiness before implementing and before completing user-facing UI. Rerun all applicable procedures before convergence and PR review.

A missing procedure or a `Blocked`, `Fail`, or `Not ready` verdict stops the affected work unless the accountable owner explicitly authorizes a narrower non-blocked slice.

## 21. iOS convergence requirements

Before owner acceptance, the readiness report must include applicable evidence for:

- focused and full builds;
- unit, integration, persistence, migration, UI, and CI results;
- current `.xcresult` or approved machine-readable result artifacts;
- OS-level process termination and relaunch;
- failed-write rollback preserving prior valid state;
- background and foreground transitions;
- compact iPhone, regular-width iPad, reduced-width/multitasking, orientation, keyboard, safe-area, and reflow behavior;
- approved locales, RTL, mixed-direction text, and long translations;
- VoiceOver, focus, announcements, modal restoration, Dynamic Type, Bold Text, Button Shapes, Differentiate Without Color, Increased Contrast, Reduce Transparency, Reduce Motion, touch targets, and applicable alternative input;
- privacy manifest, required-reason API, capability, entitlement, package, target-membership, and network inspection;
- production-composition integrity;
- archive/signing/release inspection only after release authorization;
- current documentation, architecture coverage, and PR review.

Every scenario records environment, procedure, expected result, actual result, artifact path, limitation, and verdict.

## 22. Task completion rules

- File, type, target, scheme, package, preview, route, or build existence is not completion.
- Stubs, preview-only flows, compile-only integration, unreachable paths, dead routes, unused template models, simulated services, no-op lifecycle handling, and stale evidence remain incomplete.
- Every task identifies requirement, architecture decision, target/package boundary, protected boundary, behavioral acceptance criteria, prohibited patterns, evidence scenarios, evidence artifact path, and stop condition.
- Runtime-only tasks remain open until matching simulator, device, service, archive, or release evidence exists.
- Completion boxes are checked only after acceptance criteria, evidence, and task completion review pass.
- Feature implementation completion is followed by convergence, `READINESS_REPORT.md`, independent readiness review, and repository-owner feature acceptance.
- Feature acceptance does not authorize signing, TestFlight, App Store submission, or production publication.
