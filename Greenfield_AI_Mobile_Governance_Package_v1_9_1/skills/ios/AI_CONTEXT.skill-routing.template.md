# iOS Skill Routing Template

| Need | Read first | Status |
|---|---|---|
| Feature complexity classification | `.agents/skills/ios/feature-complexity-classification/SKILL.md` | Run before contract authoring; if omitted, downstream work defaults to COMPLEX |
| Skill index | `.agents/skills/ios/README.md` | Active routing |
| Architecture readiness | `.agents/skills/ios/ios-architecture-readiness/SKILL.md` | Mandatory before planning and implementation |
| Project structure | `.agents/skills/ios/ios-project-structure-readiness/SKILL.md` | Mandatory before target/package/source-tree approval |
| Swift concurrency | `.agents/skills/ios/swift-concurrency-readiness/SKILL.md` | Mandatory for async/shared mutable state |
| SwiftUI screens | `.agents/skills/ios/swiftui-screen-readiness/SKILL.md` | Mandatory for SwiftUI work |
| UIKit screens | `.agents/skills/ios/uikit-screen-readiness/SKILL.md` | Mandatory for UIKit work |
| Localization and RTL | `.agents/skills/ios/ios-localization-rtl-readiness/SKILL.md` | Mandatory for user-facing UI |
| Adaptation and accessibility | `.agents/skills/ios/ios-adaptive-accessibility-readiness/SKILL.md` | Mandatory for UI completion |
| Persistence and migrations | `.agents/skills/ios/ios-persistence-migration-readiness/SKILL.md` | Mandatory for durable-data work |
| Privacy and capabilities | `.agents/skills/ios/ios-privacy-capability-readiness/SKILL.md` | Mandatory for protected Apple platform boundaries |
| Runtime evidence | `.agents/skills/ios/ios-runtime-evidence-readiness/SKILL.md` | Mandatory during task definition and completion |
| Bounded implementation | `.agents/skills/ios/bounded-feature-implementation/SKILL.md` | Mandatory for authorized production-code task execution |
| Production integrity | `.agents/skills/ios/production-fake-detection/SKILL.md` | Mandatory before implementation and merge readiness |
| Documentation consistency | `.agents/skills/ios/documentation-consistency-review/SKILL.md` | Mandatory when current artifacts may conflict |
| Architecture coverage | `.agents/skills/ios/architecture-coverage-review/SKILL.md` | Mandatory after material planning |
| Protected boundary | `.agents/skills/ios/protected-boundary-preflight/SKILL.md` | Mandatory before protected changes |
| Documentation impact | `.agents/skills/ios/documentation-impact-assessment/SKILL.md` | Mandatory before finalizing plans and after implementation |
| PR review | `.agents/skills/ios/pr-review/SKILL.md` | Mandatory before readiness |


## Shared feature-delivery policy routing

For contract, plan, task, implementation, convergence, or readiness work, route `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md`. Load other policy modules conditionally according to `AGENTS.md`.
