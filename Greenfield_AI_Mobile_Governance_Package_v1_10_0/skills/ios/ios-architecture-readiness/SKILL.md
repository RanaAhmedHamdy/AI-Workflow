---
name: ios-architecture-readiness
description: Validates iOS architecture either during repository bootstrap or for a bounded feature. Bootstrap mode does not require feature plan/tasks and never converts repository evidence into owner approval.
---

# iOS Architecture Readiness

## Modes

### BOOTSTRAP
Inspect the cross-feature baseline: verified toolchain/project facts, supported platform/form factors, project/target structure, SwiftUI/UIKit/hybrid direction, Observation/state model, Swift concurrency/isolation, navigation/restoration, composition, persistence/migration direction, external services, background/extension policy, privacy/capabilities, localization/accessibility/adaptation, testing/CI/evidence, and release boundaries.

Return missing decisions/contradictions without requiring Feature Contract, Plan, Tasks, or task evidence. Provisional decisions remain explicit.

### FEATURE
Inspect the bounded feature scope plus accepted architecture and verify every required selection/evidence obligation is current before planning/implementation.

## Block when

- a required selection is missing or contradictory for the reviewed scope;
- repository/generated settings are being treated as owner-approved solely because they exist;
- a plan silently chooses a framework, target, capability, or dependency;
- strict concurrency or language-mode changes lack required migration/verification scope;
- a protected platform boundary lacks authorization;
- external configuration lacks fail-closed behavior;
- in FEATURE mode, tasks lack concrete evidence scenarios.

## Verdict

- `Ready for bounded feature intake` (bootstrap only)
- `Ready for planning`
- `Ready with explicit limitations`
- `Blocked`
- `Needs verification`
