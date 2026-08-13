# AGENTS.md - Brownfield Native Android Overlay

Use with `AGENTS.common.md`. Current repository evidence overrides greenfield preferences.

## Preservation-first rule

- Identify established Gradle, module, UI, state, concurrency, navigation, DI, persistence, networking, localization, adaptive-layout, and testing patterns before editing.
- Do not normalize inconsistent patterns incidentally. A modern recommendation is not authorization to migrate an inherited feature.
- Use characterization evidence before behavior-preserving refactors.

## Android project facts

- App/module structure: [fill in].
- minSdk/targetSdk/compileSdk: [fill in].
- UI stack: [Compose / Views / hybrid].
- Current test framework and commands: [fill in].
- Supported devices/form factors and orientation policy: [fill in or Needs verification].

## Adaptive UI and supported Android surfaces

Preserve the verified support contract and audit current UI against approved device, orientation, and window requirements.

For new or materially changed Compose UI:

- do not introduce phone-only, portrait-only, or fixed-window assumptions;
- inspect the current navigation shell, window handling, state restoration, nearby adaptive patterns, and approved support matrix before editing;
- use the established adaptive mechanism when one exists;
- when no adequate mechanism exists, document the gap and obtain authorization before introducing an application-wide adaptive architecture;
- assess compact, expanded, landscape, resize, RTL, large-text, and relevant input-mode behavior;
- preserve state across orientation and window changes;
- distinguish static evidence and previews from device/runtime verification.

A bounded feature task does not authorize broad navigation-shell, dependency, or architecture migration merely to adopt a preferred adaptive API.

- Skill: `.agents/skills/adaptive-compose/SKILL.md`.

## State and concurrency

- Follow the feature's established ViewModel/state/coroutine pattern.
- Do not introduce a second application-wide state pattern or migrate LiveData/callbacks/flows merely for consistency without explicit scope.
- Preserve lifecycle, cancellation, dispatcher, process-death, and one-off-event behavior unless the task changes it.

## Android protected boundaries

In addition to common boundaries: manifests/exported components, intents/deep links/PendingIntent, network security config, KeyStore/DataStore/Room migrations, WorkManager/services/background restrictions, notifications/FCM, CameraX/media, signing/keystores, Google services files, Play distribution, and production build configuration.

## Verification

Use existing Gradle tasks and nearby test patterns. Runtime claims involving device configuration, resize/orientation, permissions, services, notifications, camera, accessibility, performance, TLS, or release artifacts require matching emulator/device/artifact evidence.
