# Native mobile coverage matrix

The Greenfield package currently contains **32 canonical Android skill directories** and **31 iOS skill directories**. The one-directory difference is a platform-specific procedure, not a claim of symmetric operational depth.

## Core capability parity

| Concern | Android | iOS |
|---|---|---|
| Architecture bootstrap orchestration | `architecture-bootstrap` | `architecture-bootstrap` |
| ADR lifecycle governance | `adr-lifecycle-governance` | `adr-lifecycle-governance` |
| Architecture readiness | `android-architecture-readiness` | `ios-architecture-readiness` |
| Project structure | `android-project-structure-readiness` | `ios-project-structure-readiness` |
| Concurrency | `kotlin-coroutines-readiness` | `swift-concurrency-readiness` |
| Declarative UI | `compose-screen-readiness` | `swiftui-screen-readiness` |
| Legacy/imperative UI | `android-views-screen-readiness` | `uikit-screen-readiness` |
| Localization + RTL | `android-localization-rtl-readiness` | `ios-localization-rtl-readiness` |
| Adaptive UI + accessibility | `android-adaptive-accessibility-readiness` | `ios-adaptive-accessibility-readiness` |
| Durable data + migrations | `android-persistence-migration-readiness` | `ios-persistence-migration-readiness` |
| Platform permissions/privacy/capabilities | `android-permission-capability-readiness` | `ios-privacy-capability-readiness` |
| Runtime evidence | `android-runtime-evidence-readiness` | `ios-runtime-evidence-readiness` |
| Feature contract/plan/tasks | Yes | Yes |
| Independent reviews | Yes | Yes |
| Bounded implementation | Yes | Yes |
| Convergence + readiness | Yes | Yes |
| Production fake detection | Yes | Yes |
| Protected-boundary preflight | Yes | Yes |
| Documentation review/impact/consistency | Yes | Yes |
| Characterization tests | Yes | Yes |

## Why Android has more directories

The former Android count was inflated by three retired aliases. The remaining difference is purposeful rather than a functional-coverage score:

1. `adaptive-compose`, `localization-rtl-readiness`, and `runtime-evidence-readiness` were retired as active Android aliases. Their compatibility mapping is recorded in [`SKILL_ALIASES.md`](SKILL_ALIASES.md); the useful runtime guidance was merged into `android-runtime-evidence-readiness`.
2. Android retains `protected-lifecycle-transaction-review` and `publish-ai-mr`, while iOS retains `agent-drift-detection` as a distinct specialist procedure.

## Is anything actually missing from iOS?

No critical Greenfield mobile category is missing based on the current lifecycle. The major iOS-specific risks—Swift concurrency, SwiftUI/UIKit, persistence/migrations, privacy manifests/required-reason APIs, capabilities/entitlements, adaptive UI/accessibility, localization/RTL, and runtime evidence—already have dedicated coverage. The iOS implementation-plan author/review procedures now explicitly review actor isolation, task lifetime, scene/re-entry, target/build ownership, extensions/background work, privacy/entitlements, and archive-sensitive evidence. This is operational parity for iOS-relevant failures, not line-count parity with Android.

There are **optional parity candidates**, not current blockers:

- A platform-neutral `publish-ai-mr` could eventually be shared by both packs.
- Android could gain an explicit `agent-drift-detection` skill if the existing consistency/convergence reviews are not sufficient in practice.
- iOS could gain a dedicated guarded lifecycle/transaction skill if real projects demonstrate repeated StoreKit/auth/background transaction failure modes that are not adequately covered by persistence, privacy/capability, concurrency, bounded implementation, and runtime-evidence procedures.

Do not add skills only to make the counts equal. Add one when a repeated failure mode has a distinct trigger, procedure, and evidence contract.

## Intentional duplicate-name policy

Cross-cutting skills are duplicated inside Android and iOS so a team can copy **only one platform pack** and still receive a complete workflow. Keep them.

For a dual-platform repository, install under separate path namespaces:

```text
.agents/skills/android/...
.agents/skills/ios/...
```

and route the concrete platform path in `AI_CONTEXT.md`. Do not flatten both packs into the same directory.
