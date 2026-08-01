# AGENTS.md - Brownfield Native iOS Overlay

Use with `AGENTS.common.md`. Current repository evidence overrides greenfield preferences.

## Preservation-first rule

- Identify the established Xcode/project-generation, UI, state, concurrency, navigation, dependency, persistence, localization, and testing patterns before editing.
- Do not migrate UIKit to SwiftUI, Combine to Observation, callbacks to async/await, CocoaPods to SPM, or navigation architecture merely because a newer default exists.
- Use characterization evidence before behavior-preserving refactors.

## iOS project facts

- Deployment target/platforms: [fill in].
- Project generation/dependency management: [fill in].
- UI stack: [SwiftUI / UIKit / hybrid].
- Current test framework/schemes/commands: [fill in].
- Supported devices, iPad/multitasking/Catalyst/orientation policy: [fill in or Needs verification].

## UI and adaptation

- Preserve verified supported devices and navigation behavior.
- For new or materially changed UI, avoid unnecessary fixed-size, compact-only, orientation, or Dynamic-Type assumptions within approved scope.
- Do not introduce NavigationSplitView, Observation, new grid/layout architecture, Catalyst support, or multitasking behavior without reviewing deployment target and owner expectations.
- Check localization/catalogs, RTL, Dynamic Type, VoiceOver semantics/focus, contrast, and permission/degraded states when relevant.

## State and concurrency

- Follow established actor/queue/Combine/async-await patterns at the affected boundary.
- UI state mutations must respect the repository's verified main-thread/MainActor contract.
- Do not introduce a second application-wide observation/concurrency model without explicit scope.

## iOS protected boundaries

In addition to common boundaries: entitlements, provisioning, certificates, keychain groups, ATS, URL schemes/universal links, push capabilities, background modes/BGTaskScheduler, privacy manifests/usage descriptions, StoreKit, signing/export options, and App Store distribution.

## Verification

Use established schemes and test plans. Simulator/device claims involving permissions, notifications, background execution, accessibility, performance, universal links, signing, or archives require matching runtime/artifact evidence.
