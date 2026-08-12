# AGENTS.md - Brownfield Native iOS Overlay

> Version 1.4. Use with `AGENTS.common.md`. Current repository evidence overrides greenfield preferences. New Apple APIs and current recommendations are evidence inputs, not authorization to migrate working code.

## Preservation-first rule

- Identify the established Xcode/project-generation, target, package, UI, state, concurrency, navigation, dependency, persistence, localization, capability, and testing patterns before editing.
- Do not migrate UIKit to SwiftUI, ObservableObject/Combine to Observation, callbacks to async/await, Core Data to SwiftData, CocoaPods/Carthage to Swift Package Manager, XCTest to Swift Testing, coordinators to NavigationStack, or project files to a generator merely because a newer default exists.
- Use characterization evidence before behavior-preserving refactors.
- Make the smallest coherent change that fits the verified local architecture.
- Record inconsistencies and modernization candidates separately unless the task explicitly authorizes migration.

## Required project facts

Before implementation, verify:

- supported platforms and deployment targets;
- exact Xcode, Swift language mode, SDK, macOS host, and project format/generator;
- application, extension, widget, test, watch, vision, and other targets;
- dependency managers, lock/resolution files, and package ownership;
- UI stack and navigation architecture;
- state/observation and concurrency models;
- persistence technology, schema/migration ownership, and isolation model;
- schemes, configurations, test plans, CI commands, signing expectations, and runtime matrix;
- supported iPhone/iPad/multitasking/Catalyst/orientation/accessibility scope.

Unknown facts remain `Needs verification`.

## Project and target preservation

- Preserve verified target boundaries, bundle identifiers, groups/folders, local packages, frameworks, build settings, schemes, and project-generation workflow.
- Do not move files between targets or packages without checking target membership, resources, generated files, tests, and CI.
- Do not introduce a second project-generation system.
- Avoid broad folder/group normalization and unrelated package updates.
- When adding a new feature, follow the nearest coherent ownership and dependency pattern unless it violates an approved requirement or protected boundary.
- A bad existing pattern may be contained locally, but replacing it across the repository requires explicit migration scope.

## Application host and composition

- Preserve the established `App`, AppDelegate, SceneDelegate, root-controller, coordinator, and composition-root responsibilities.
- Do not move feature state or domain logic into application entry points.
- Do not introduce a global service locator or duplicate dependency container.
- New dependencies must enter through the established composition boundary or an approved extension of it.
- Preview/test composition must not leak into release composition.

## UI, navigation, and adaptation

For new or materially changed UI:

- follow the established SwiftUI/UIKit/hybrid boundary;
- preserve the current navigation owner and deep-link routing;
- avoid compact-only, portrait-only, fixed-size, or single-scene assumptions within approved scope;
- inspect current size-class, split-view, multitasking, keyboard, pointer, safe-area, sheet/popover, and restoration patterns;
- use the established adaptive mechanism when adequate;
- when no adequate mechanism exists, document the gap before introducing application-wide navigation or adaptive architecture;
- preserve state across rotation, resizing, scene transitions, and restoration as required;
- verify localization, RTL, Dynamic Type, VoiceOver, focus, contrast, Reduce Motion, and permission/degraded states when relevant.

Do not introduce `NavigationSplitView`, a new coordinator/router, Observation, new layout architecture, Catalyst, Stage Manager, visionOS, or another target family without checking deployment targets and owner-approved scope.

## State, observation, and concurrency

- Follow the affected feature's established `ObservableObject`, Observation, Combine, delegate/callback, actor, queue, or async/await pattern.
- UI state mutation must respect the verified main-thread or `MainActor` contract.
- Do not add a second application-wide observation or concurrency model for consistency alone.
- Preserve cancellation, ordering, idempotency, reentrancy, lifecycle, and restoration behavior unless the task changes them.
- New async bridges must resume continuations exactly once and propagate cancellation.
- Do not use `@unchecked Sendable`, broad `@MainActor`, detached tasks, or compiler-setting relaxations to suppress diagnostics without documented invariants and tests.
- Enabling Swift 6 language mode or stricter concurrency checking is a migration task, not a feature-side cleanup.

## Persistence and migrations

- Follow the established Core Data, SwiftData, SQLite, file, Keychain, cache, or server-source boundaries.
- Do not migrate persistence technology merely because another framework is newer.
- Inspect model versions, migrations, contexts/actors/queues, backup rules, file protection, deletion, and recovery before changing durable data.
- Destructive or multi-record changes require explicit transaction/atomicity review.
- Test migrations from supported production schemas using representative data.
- In-memory stores are allowed for tests but must not replace required release durability.

## Dependencies and supply chain

- Preserve the established dependency manager unless migration is explicitly authorized.
- For new dependencies, record purpose, owner, version rule, license, privacy impact, binary content, transitive dependencies, platform support, and removal plan.
- Do not update unrelated packages or regenerate lockfiles/resolution files without reviewing the resulting graph.
- Prefer source packages over equivalent binaries where repository policy permits.
- Verify binary provenance and checksums.
- Commit the repository's established lock/resolution artifacts.

## Localization and accessibility

- Follow established String Catalog, `.strings`, `.stringsdict`, generated-resource, or localization-tooling conventions.
- Do not hardcode new user-facing or accessibility-facing strings.
- Use locale-aware formatting and avoid concatenated sentence fragments.
- Preserve leading/trailing semantics and test RTL where applicable.
- Verify Dynamic Type, including accessibility sizes where supported.
- Provide VoiceOver labels, values, traits, actions, state descriptions, headings, and focus behavior.
- Static source and snapshots do not prove assistive-technology behavior.

## Protected iOS boundaries

In addition to common boundaries, treat these as protected:

- entitlements, provisioning profiles, certificates, signing identities, export options, and distribution;
- Keychain groups, App Groups, associated domains, URL schemes, universal links, and deep links;
- ATS, certificate pinning, network extensions, VPN, and transport security;
- push notifications, background modes, BGTaskScheduler, background URLSession, Live Activities, widgets, and extensions;
- privacy manifests, required-reason APIs, usage descriptions, tracking, analytics, advertising, and data collection;
- StoreKit, subscriptions, receipts, offers, entitlement state, and App Store server integration;
- camera, microphone, photos, contacts, location, Bluetooth, HealthKit, HomeKit, Nearby Interaction, and other permissioned frameworks;
- App Store Connect, TestFlight, notarization, archive/export, and production environment mutation.

Run protected-boundary preflight before modification. Existing capabilities or entitlements do not authorize expanding their use.

## Testing and verification

Use established schemes, test plans, destinations, and CI commands.

- Prefer the nearest existing unit/integration framework for bounded changes.
- Swift Testing may be introduced only when compatible with the approved Xcode baseline and test-strategy scope.
- Keep XCTest/XCUITest where required for existing suites, UI automation, performance, Objective-C interoperability, or unsupported APIs.
- Runtime claims involving lifecycle, scene restoration, permissions, notifications, background execution, Dynamic Type, VoiceOver, universal links, StoreKit, performance, signing, archives, or distribution require matching simulator/device/service/artifact evidence.
- Report exact commands, destinations, OS versions, outcomes, and limitations.

## Production integrity

Do not add release-path fakes, preview/test dependencies, no-op persistence or background handlers, fixed success identifiers, placeholder receipts/authorization, permissive validation, debug bypasses, or silent simulated success. Missing services/configuration must use the repository's verified fail-closed or degraded behavior.

## Required brownfield iOS skills and routing

Use repository skills or equivalent procedures for:

- `ios-brownfield-architecture-readiness`;
- `ios-project-structure-readiness`;
- `swift-concurrency-readiness`;
- `swiftui-screen-readiness` or the repository's UIKit equivalent;
- `ios-localization-rtl-readiness`;
- `ios-adaptive-accessibility-readiness`;
- `ios-persistence-migration-readiness`;
- `ios-privacy-capability-readiness`;
- `ios-runtime-evidence-readiness`;
- `characterization-tests`;
- `production-fake-detection`;
- `documentation-consistency-review`.

Before planning or implementation, determine which procedures apply. A missing required procedure or `Blocked`, `Fail`, or `Not ready` verdict stops the affected work unless the accountable owner authorizes a narrower non-blocked slice.

## Completion rules

- Existing code, a successful build, target membership, or test-file creation is not completion.
- Every task names the preserved contract, changed behavior, target/package boundary, protected boundary, regression risks, evidence scenarios, evidence artifact, and stop condition.
- Modernization not required for the approved behavior remains a separate follow-up rather than hidden scope.
