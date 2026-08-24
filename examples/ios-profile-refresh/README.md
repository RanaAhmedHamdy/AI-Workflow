# iOS profile refresh demo

## Scenario

Request: **“Add a persisted display name and refresh it when the scene returns.”** This is a native SwiftUI application with local JSON persistence, an actor-isolated refresh service, and a `@MainActor` observable UI model.

## What a generic change can miss

- A persisted model needs a recovery/default policy for missing or old data.
- UI state has a main-actor owner; detached work must not update it casually.
- Refresh work needs cancellation/lifetime rules across view disappearance and scene re-entry.

The deliberately incomplete representation is [scenario/unsafe-example.md](scenario/unsafe-example.md); it is documentation only, not a broken target.

## AI-Workflow route

Facts: `persistence`, `concurrency`, `lifecycle`.

```bash
ai-workflow route --workflow brownfield --platform ios --profile safety \
  --fact persistence --fact concurrency --fact lifecycle
```

| Detected risk | Selected procedure | Guardrail |
| --- | --- | --- |
| Local profile evolution | `ios-persistence-migration-readiness` | State recovery and durable-data evidence. |
| Async refresh | `swift-concurrency-readiness` | Actor/UI isolation, cancellation, and ownership. |
| Re-entry/result claim | `ios-runtime-evidence-readiness` | Scene/runtime proof stays distinct from unit/source evidence. |

The route recommends `STANDARD` because persistence, concurrency, and lifecycle are hard standard escalations. It does not impose Android architecture on an iOS app.

## Safer implementation

`ProfileStore` uses atomic local writes and an explicit fallback. `ProfileRefreshService` is an actor. `ProfileViewModel` is `@MainActor`, retains/cancels its current refresh, and updates only after cancellation is checked. SwiftUI's `.task` starts a view-scoped refresh and scene activation deliberately requests a fresh one.

## Run it

Requirements: Xcode 16+ and an installed iOS Simulator runtime.

```bash
cd examples/ios-profile-refresh
xcodebuild -project ProfileRefreshDemo.xcodeproj -scheme ProfileRefreshDemo \
  -destination 'platform=iOS Simulator,name=iPhone 16' test
```

For manual runtime evidence, launch in a simulator, refresh the profile, background/foreground the app, relaunch it, and confirm “Ada Lovelace” remains visible. Do not report this as executed unless the session has actually run.

## Evidence collected

See [VERIFICATION.md](VERIFICATION.md). The fixture is retained even when a host lacks a usable simulator service; that condition is an environment limitation, not a test pass.

## What this does not prove

It does not prove iCloud/Core Data migrations, server/network behavior, every scene configuration, production privacy/capability setup, or universal coding-agent compatibility.
