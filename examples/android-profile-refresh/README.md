# Android profile refresh demo

## Scenario

Request: **“Add a persisted display name to the profile and show it after refresh or relaunch.”** The fixture is a real Android app with local SQLite persistence, a v1-to-v2 schema change, a `StateFlow`, and lifecycle-aware collection.

## What a generic change can miss

- Existing version-one rows need an explicit migration/default value.
- A refresh coroutine must be owned by the `ViewModel`, not a view callback.
- UI collection must stop when the `Activity` is not started.

The deliberately incomplete example is in [scenario/unsafe-example.md](scenario/unsafe-example.md); it is not a broken app and must not be applied.

## AI-Workflow route

Facts: `persistence`, `schema_migration`, `concurrency`, `lifecycle`.

```bash
ai-workflow route --workflow brownfield --platform android --profile safety \
  --fact persistence --fact schema_migration --fact concurrency --fact lifecycle
```

Expected checks:

| Detected risk | Selected procedure | Guardrail |
| --- | --- | --- |
| Persisted schema change | `android-persistence-migration-readiness` | Preserve existing data and define migration evidence. |
| Refresh coroutine | `kotlin-coroutines-readiness` | Give work an explicit owner and dispatcher boundary. |
| Activity stop/restart | `protected-lifecycle-transaction-review` | Avoid state/UI work leaking over lifecycle changes. |
| Result claim | `android-runtime-evidence-readiness` | Separate unit/build evidence from device-runtime proof. |

The route recommends `COMPLEX` because `schema_migration` is a hard complex escalation. This fixture is intentionally compact; that recommendation does not turn it into a model architecture.

## Safer implementation

`ProfileDatabase` adds and backfills `display_name`; `ProfileRepository` exposes a `StateFlow`; `ProfileViewModel` owns refresh work; `MainActivity` uses `repeatOnLifecycle` while rendering. See [scenario/route.json](scenario/route.json) for the exact facts.

## Run it

Requirements: Android SDK platform 35, JDK 17+, and Gradle 8.8+ (or the generated wrapper once present).

```bash
cd examples/android-profile-refresh
gradle :app:testDebugUnitTest
gradle :app:assembleDebug
```

The test verifies the deterministic legacy-row fallback. An emulator/manual session should additionally launch the app, press **Refresh profile**, relaunch it, and confirm “Ada Lovelace” remains visible. Do not call that runtime evidence until it has actually been performed and recorded.

## Evidence collected

See [VERIFICATION.md](VERIFICATION.md) for the executed-command log. It records build/test evidence separately from pending emulator evidence.

## What this does not prove

It does not prove network behavior, multi-row migration coverage, process-death behavior on every OEM, a production data strategy, or universal agent compatibility.
