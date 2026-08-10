# iOS Greenfield Skills Package v1.0

Use with the reusable `AGENTS.md plus `.agents/policies/` shared modules` and `.agents/policies/ios/IOS_ENGINEERING_POLICY.md` overlays.

## Principles

- Skills are procedures, not authorization.
- A missing required skill is a readiness blocker.
- `Blocked`, `Fail`, or `Not ready` stops the affected work unless the accountable owner authorizes a narrower non-blocked slice.
- Exact Xcode, Swift, SDK, deployment-target, dependency, and test-stack versions must be verified in the target repository. This package intentionally avoids hardcoding versions that will become stale.
- Static source, previews, snapshots, and host-side tests do not prove device, accessibility, background, signing, StoreKit, or release behavior.

## Recommended routing

### Before `implementation-plan authoring`
- `ios-architecture-readiness`
- `ios-project-structure-readiness`
- `swift-concurrency-readiness` when async or shared mutable state is involved
- `documentation-consistency-review`
- `architecture-coverage-review`

### Before generating or accepting UI tasks
- `swiftui-screen-readiness` or `uikit-screen-readiness`
- `ios-localization-rtl-readiness`
- `ios-adaptive-accessibility-readiness`
- `ios-runtime-evidence-readiness`

### Before persistence or protected platform work
- `ios-persistence-migration-readiness`
- `ios-privacy-capability-readiness`
- `protected-boundary-preflight`

### Before completion
- rerun all applicable readiness skills
- `production-fake-detection`
- `documentation-impact-assessment`
- `documentation-review`
- `pr-review`

## Package layout

- `shared/`: platform-neutral governance and evidence procedures.
- `ios/`: Apple-platform architecture, SwiftUI/UIKit, concurrency, persistence, privacy, adaptation, and runtime evidence procedures.
