# Native demo fixtures

These are deliberately small, local native projects—not sample application architectures. Each fixture demonstrates one ordinary request that can hide mobile-specific risk:

| Fixture | Ordinary request | Risks made visible |
| --- | --- | --- |
| [Android profile refresh](android-profile-refresh/README.md) | Add a persisted display name and show it after refresh/relaunch. | SQLite migration integrity, coroutine ownership, lifecycle-aware Flow collection. |
| [iOS profile refresh](ios-profile-refresh/README.md) | Add a persisted display name and refresh it when the scene returns. | persistence evolution, `MainActor` UI ownership, structured task lifetime and scene re-entry. |

The fixtures do not prove a production architecture, universal migration safety, device coverage, or compatibility with every coding agent. They prove the bounded failure modes described in their READMEs and distinguish source/unit/native-build evidence from runtime evidence.
