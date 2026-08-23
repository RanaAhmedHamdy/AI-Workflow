---
name: architecture-coverage-review
description: Separates decision, implementation, and evidence status for cross-cutting Android architecture in bootstrap, feature-readiness, or convergence mode.
---

# Architecture Coverage Review

## Modes

- `BOOTSTRAP`: approved product/design/governance authority + Spine + ADRs + Decision Register + coverage + relevant repository facts. No Feature Contract/Plan/Tasks required.
- `FEATURE-READINESS`: add approved feature artifacts and gate obligations.
- `CONVERGENCE`: add implementation and evidence.

Evaluate every applicable concern, including namespace/module structure, thin Activity, composition/DI, feature ownership/dependency direction, ViewModels/state, coroutines/Flow, navigation/restoration, persistence/migrations, lifecycle/process death, background work, external services, localization/RTL/adaptation/accessibility, permissions/privacy, configuration, observability/performance, testability/CI/release, production composition.

Record **Decision**, **Implementation**, and **Evidence** status separately plus current home, gap, owner, blocker, and next action. Do not infer `Not applicable` from absence or runtime support from static evidence.

In `BOOTSTRAP`, `Implementation: Not started` and `Evidence: None` are valid when the required decisions exist and first-slice blockers are explicit.

Return `PASS`, `PASS WITH LIMITATIONS`, or `BLOCKED`. Bootstrap PASS means sufficient architecture for bounded feature intake, not implementation readiness.
