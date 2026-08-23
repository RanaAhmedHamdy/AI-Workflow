# Android Greenfield Skills Package v1.10.0

Use this self-contained Android pack with root governance policies and `.agents/policies/android/ANDROID_ENGINEERING_POLICY.md`.

## Principles

- Skills are procedures, not authorization.
- Repository/Gradle defaults are evidence, not automatic owner decisions.
- Missing/failing required readiness blocks the affected scope.
- Static source/previews do not prove runtime, accessibility, background, signing, permission, or release behavior.
- Design-bound UI must inspect the exact approved visual before UI code; Markdown-only interpretation is insufficient.

## Recommended routing

### Repository architecture bootstrap
- `architecture-bootstrap`
- `adr-lifecycle-governance`
- `android-project-structure-readiness` in evidence-only mode
- `android-architecture-readiness` in bootstrap mode
- `architecture-coverage-review` in bootstrap mode
- `documentation-consistency-review`

### Before planning / UI tasks
- `android-architecture-readiness` / `android-project-structure-readiness` in feature mode
- `compose-screen-readiness` or `android-views-screen-readiness`
- `android-localization-rtl-readiness`
- `android-adaptive-accessibility-readiness`
- `android-runtime-evidence-readiness`

### Protected/data work
- `android-persistence-migration-readiness`
- `android-permission-capability-readiness`
- `protected-boundary-preflight`
- `kotlin-coroutines-readiness` where applicable

### Authorized implementation
- `bounded-feature-implementation` for the exact authorized coherent task group

### Convergence / completion
- applicable readiness reruns
- `production-fake-detection`
- documentation impact/review
- `pr-review`

Keep Android and iOS skill packs in separate path namespaces when both are installed.
