# iOS Engineering Policy

> Greenfield native iOS overlay. Use with root `AGENTS.md` and the shared policy modules.

## 1. Initialization

Verify and record:

- supported Apple platforms, devices, orientations, and deployment targets;
- Xcode, Swift mode, SDK, simulator runtime, and macOS host;
- project format or generator;
- app, unit-test, UI-test, extension, widget, watch, vision, Catalyst, and other targets;
- package management and `Package.resolved`;
- development-team expectations without accessing production credentials;
- configurations, schemes, test plans, CI, archive, and evidence paths;
- release channels.

Do not infer current versions from this policy.

## 2. Defaults

- Swift-first and SwiftUI-first unless UIKit/AppKit/hybrid is approved.
- Swift Concurrency.
- One approved observation model.
- Observation only when compatible with deployment target and architecture.
- Swift Package Manager unless otherwise decided.
- Swift Testing for supported pure Swift tests.
- XCTest/XCUITest for UI, system, performance, legacy, or unsupported cases.
- String Catalogs or another approved source.
- No premature targets, packages, frameworks, coordinators, or layers.

## 3. Thin hosts

`App`, `SceneDelegate`, `AppDelegate`, root controllers, and scene entry points may configure scenes, composition, root navigation, platform services, lifecycle hooks, and approved environment bindings.

They must not own feature workflow state, contain feature screens/business rules, construct dependencies ad hoc, execute domain work, or become service locators.

## 4. Structure and dependencies

Before implementation, record:

- bundle/module naming;
- target/package structure;
- composition root;
- feature boundaries;
- presentation/domain/data/platform boundaries;
- dependency direction;
- locations for state, routes, views, repositories, clients, persistence, background handlers, intents, widgets, and design system;
- test ownership;
- extraction criteria.

Avoid generic dumping grounds, circular dependencies, feature behavior in hosts, leaf-UI infrastructure access, and unused Xcode template code.

## 5. Presentation state

Every workflow declares:

- owner and lifetime;
- durable source of truth;
- inputs/events;
- async ownership and cancellation;
- restoration;
- navigation;
- composition path.

Default:

- observable workflow state lives outside leaf render views;
- UI state mutations occur on the approved main-actor boundary;
- leaf views receive values and actions;
- persistence models, contexts, repositories, clients, StoreKit services, authorization services, and app routers stay out of leaf views;
- durable state reconstructs from persistence;
- no side effects in `body`;
- no state-holder recreation during recomputation.

## 6. Swift concurrency

- Define actor isolation.
- Require `Sendable` correctness.
- Avoid `@unchecked Sendable` without invariants and tests.
- Use structured concurrency.
- Justify detached/unstructured tasks and continuation bridges.
- Prefer `.task`/`.task(id:)` for presentation-scoped SwiftUI work where appropriate.
- Do not cancel durable operations because a view disappears.
- Propagate cancellation.
- Resume continuations exactly once.
- Map typed outcomes.
- Bound terminal states.
- Prevent duplicate side effects.
- Do not weaken compiler settings to silence diagnostics.

Every async operation names owner, lifetime, cancellation, isolation, terminal states, and duplicate behavior.

## 7. Composition

Construct clients, repositories, persistence containers, clocks, configuration, diagnostics, analytics, and state through an explicit composition root.

Prefer initializer injection and bounded feature factories. Typed environment injection is allowed only at explicit boundaries. No generic environment service locator. No preview/test dependency in release composition.

## 8. SwiftUI contract

Each meaningful screen defines:

1. route/container boundary;
2. render/content view using plain state and actions;
3. material states;
4. navigation, modal, restoration, save/discard/cancel behavior;
5. device, size-class, multitasking, locale, RTL, Dynamic Type, input, and accessibility behavior;
6. preview and verification matrix.

Avoid side effects in `body`, state recreation, unowned tasks, hardcoded strings, fixed-height text, left/right assumptions, compact-only layouts, inaccessible controls, and previews treated as proof.

## 9. Navigation and restoration

Define approved navigation ownership and use stable typed nonsensitive identifiers.

Persist minimal restoration intent, validate restored identifiers, and recover safely from stale records.

Leaf views emit navigation intents. Sheets/covers define save, discard, cancel, dismissal, and restoration. Dismissal must not silently commit, delete, purchase, transfer, or reassign data.

Deep links, universal links, Spotlight, notifications, widgets, App Intents, and external URLs are protected.

## 10. Persistence

Select SwiftData, Core Data, SQLite, files, Keychain, protected stores, or server sources through architecture decision.

Define:

- system of record;
- schema/model ownership;
- versioning and migration fixtures;
- failed-migration recovery;
- actor/context ownership;
- transactions and rollback;
- idempotency;
- stale writes;
- date attribution and historical integrity;
- backup, transfer, protection, Keychain, cache, deletion, and logout;
- test stores;
- process termination and relaunch.

No in-memory release substitute. No persistence entities in leaf views. Do not overclaim forensic deletion.

## 11. External services and retained configuration

Before adding networking, backend SDKs, Firebase, analytics, crash reporting, AI, or other providers, define endpoints, credentials, contracts, timeout/retry/cancellation/idempotency, ATS/trust, privacy/redaction, environment separation, attestation, outage behavior, and fail-closed outcomes.

Prefer `URLSession` unless an ADR justifies another stack.

A retained `GoogleService-Info.plist` or similar file does not authorize SDK initialization. Document repository path, target membership, Copy Bundle Resources status, build-product inclusion, automatic initialization, linked SDKs, network behavior, privacy impact, active/dormant status, and authority.

A pure-local slice must prove no out-of-scope SDK initializes and no external transfer occurs.

## 12. Localization and RTL

- No hardcoded user-facing or accessibility strings.
- Use String Catalogs or approved localization source.
- Use locale-aware formatting.
- Do not concatenate translated fragments.
- Use leading/trailing semantics.
- Exercise an approved RTL locale and long translations.
- Verify shaping, mixed-direction text, numerals, units, punctuation, truncation, and fallback.
- Validate missing/stale keys and substitutions.

## 13. Adaptive Apple surfaces

Define:

- iPhone devices and orientations;
- iPad compact/regular widths;
- Split View, Stage Manager, and reduced width;
- scenes/windows and external display where in scope;
- physical keyboard, pointer, trackpad, Full Keyboard Access, Switch Control, and Voice Control;
- Catalyst/Designed for iPad scope;
- extensions only when in scope;
- light/dark, accessibility sizes, Bold Text, Button Shapes, Differentiate Without Color, Increased Contrast, Reduce Motion, and Reduce Transparency;
- safe areas, keyboard, sheets, popovers, menus, and toolbars.

Preserve one business state across layouts, rotation, resizing, multitasking, scenes, and restoration. Keep focused fields and actions reachable.

## 14. Accessibility

Cover applicable:

- VoiceOver labels, values, traits, actions, headings, states, and traversal;
- focus order;
- validation announcements;
- modal focus restoration;
- Dynamic Type;
- Bold Text;
- Button Shapes;
- Differentiate Without Color;
- Increased Contrast;
- Reduce Transparency;
- Reduce Motion;
- touch targets;
- Switch Control;
- Full Keyboard Access;
- pointer/trackpad;
- Voice Control;
- adaptive reflow and state preservation;
- long translations and RTL.

Manual evidence names device/simulator, OS, locale, content size, settings, procedure, expected result, actual result, artifact, and limitation.

## 15. Privacy and capabilities

Treat as protected:

- privacy manifests and required-reason APIs;
- `Info.plist` usage descriptions;
- entitlements, App Groups, Keychain groups, associated domains, URL schemes, and capabilities;
- ATS exceptions;
- notifications, background modes, BGTaskScheduler, location, camera, microphone, photos, contacts, Bluetooth, HealthKit, HomeKit, and sensitive frameworks;
- StoreKit, receipts, and entitlement state;
- analytics, crash reporting, logging, and tracking;
- signing, provisioning, export compliance, TestFlight, and App Store distribution.

A framework import, plist, package, or entitlement does not authorize use.

## 16. Background execution and extensions

Use BGTaskScheduler, background URLSession, push-triggered work, widgets, Live Activities, App Intents, or extensions only from approved needs.

Define registration, scheduling, expiration, cancellation, retries, terminal states, deduplication, protection, foreground/startup reconciliation, recovery, and evidence.

Background execution is opportunistic unless Apple guarantees otherwise.

## 17. Supply chain

Record package purpose, owner, version rule, license, privacy impact, binary content, transitive dependencies, platform support, and removal plan.

Use reproducible rules. Verify binary checksums, signatures, privacy manifests, provenance, generated products, and embedded frameworks. Avoid unrelated upgrades.

## 18. Testing and evidence

Applicable layers include:

- Swift Testing;
- XCTest;
- XCUITest;
- previews and snapshots;
- simulator and physical-device runtime;
- VoiceOver/manual evidence;
- Dynamic Type and RTL;
- process termination and relaunch;
- background execution;
- universal/deep links;
- StoreKit test/staging;
- privacy-manifest and entitlement inspection;
- archive/export/signing evidence;
- external-service attestation.

Compilation, previews, snapshots, and host tests do not prove runtime-only behavior.

Machine-readable `.xcresult` artifacts must exist at the canonical path and match the final source revision.

## 19. Production integrity

Inspect target membership, configurations, conditional compilation, dependency containers, environment values, generated configuration, package products, Copy Bundle Resources, and archive contents.

Prohibit simulated success, fixed identifiers, accept-all validation, placeholder authorization/attestation/receipts, no-op repositories/workers/migrations, in-memory durability substitutes, preview/test dependencies, debug bypasses, dead routes, unused template models, and fake fallback.

Future configuration may remain in the repository only with explicit active/dormant status and target/build behavior.

## 20. Required iOS procedures

Provide equivalents for:

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
- `feature-implementation-convergence`;
- `feature-readiness-review`;
- `documentation-consistency-review`;
- `pr-review`.

## 21. iOS acceptance evidence

Before owner acceptance, include applicable:

- focused and full builds;
- unit, integration, persistence, migration, UI, and CI results;
- current `.xcresult`;
- OS-level process termination/relaunch;
- failed-write rollback;
- background/foreground transitions;
- compact iPhone, regular iPad, reduced-width multitasking, orientation, keyboard, safe area, and reflow;
- locales, RTL, mixed direction, and long translations;
- VoiceOver, focus, announcements, modal restoration, Dynamic Type, Bold Text, Button Shapes, Differentiate Without Color, Increased Contrast, Reduce Transparency, Reduce Motion, touch targets, and alternative input;
- privacy manifest, required-reason API, capability, entitlement, package, target-membership, and network inspection;
- production-composition integrity;
- archive/signing/release evidence only after release authorization;
- current documentation and architecture coverage.
