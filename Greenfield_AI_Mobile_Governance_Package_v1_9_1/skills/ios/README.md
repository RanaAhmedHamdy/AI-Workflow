# iOS Greenfield Skills Package v1.9.1

Use this platform package with the reusable root `AGENTS.md`, the modular `.agents/policies/` governance files, and `.agents/policies/ios/IOS_ENGINEERING_POLICY.md` overlay from the Greenfield package.

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

### During authorized implementation
- `bounded-feature-implementation` for each explicitly authorized coherent task group

### Before completion
- rerun all applicable readiness skills
- `production-fake-detection`
- `documentation-impact-assessment`
- `documentation-review`
- `pr-review`

## Package layout

This iOS directory is intentionally **self-contained** so an iOS-only repository can install it without also copying Android skills.

- `ios/`: Apple-platform procedures plus local copies of the cross-cutting governance/review skills required by the iOS lifecycle.
- There is **no `shared/` skill directory** in v1.9.1. Cross-cutting skills such as `production-fake-detection`, `documentation-consistency-review`, and `pr-review` are installed from this `ios/` package and routed through `.agents/skills/ios/...`.
- For a repository that contains both native Android and native iOS, keep the platform packs in separate path namespaces (`.agents/skills/android/` and `.agents/skills/ios/`) rather than flattening both into one directory.

See `INSTALL.md` and `AI_CONTEXT.skill-routing.template.md` for the concrete paths.

## Feature complexity classification

Run `feature-complexity-classification/SKILL.md` before feature-contract authoring when possible. If it is not run, or its result is missing/invalid/stale, all downstream iOS governance MUST default the feature to `COMPLEX`; never infer SMALL or STANDARD.
