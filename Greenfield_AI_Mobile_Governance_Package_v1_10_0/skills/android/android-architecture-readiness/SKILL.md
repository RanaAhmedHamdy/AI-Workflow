---
name: android-architecture-readiness
description: Validates Android architecture during repository bootstrap or for a bounded feature. Bootstrap mode does not require feature plan/tasks and never converts repository evidence into owner approval.
---

# Android Architecture Readiness

## Modes

### BOOTSTRAP
Read current governance, approved product/design authority, Architecture Spine, coverage, proposed/accepted ADRs, Decision Register, and directly relevant repository facts. Verify cross-feature decisions for project/module structure, thin Activity, composition/DI, ViewModel/state ownership, coroutines/Flow, navigation/restoration, persistence/migrations, lifecycle/process death, background work, external services, localization/RTL/adaptation/accessibility, permissions/privacy, testing/CI/evidence, and release boundaries.

Do not require Feature Contract, Plan, Tasks, or task evidence. Existing Gradle/project defaults are evidence, not automatic owner approval.

### FEATURE
Read the bounded feature artifacts and confirm the accepted architecture can be applied without silent new decisions.

## Block when

- a required selection is missing/contradictory for reviewed scope;
- current superseded authority is still active;
- meaningful workflows lack accepted state/lifecycle ownership;
- a protected prerequisite is unauthorized or lacks fail-closed behavior;
- in FEATURE mode, task-level evidence scenarios are missing.

## Verdict

- `Ready for bounded feature intake` (bootstrap only)
- `Ready for planning`
- `Ready with explicit limitations`
- `Blocked`
- `Needs verification`
