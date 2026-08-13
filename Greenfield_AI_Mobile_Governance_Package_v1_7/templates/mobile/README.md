# Mobile Governance Templates v1.8

This package separates **product/user-journey truth** from **platform implementation mechanics**.

## Structure

```text
mobile/
  FEATURE_INPUT_TEMPLATE.md
  FEATURE_CONTRACT_TEMPLATE.md
  IMPLEMENTATION_READINESS_AUDIT_TEMPLATE.md
  READINESS_REPORT_TEMPLATE.md
ios/
  IMPLEMENTATION_PLAN_TEMPLATE.md
  IMPLEMENTATION_TASKS_TEMPLATE.md
android/
  IMPLEMENTATION_PLAN_TEMPLATE.md
  IMPLEMENTATION_TASKS_TEMPLATE.md
```

## Routing rule

- Feature Input is shared. It defines product outcomes, invocation contexts, mutation-to-consumer effects, end-to-end journeys, re-entry/recreation expectations, and risk signals.
- Feature Contract is shared. Observable behavior should remain platform-neutral unless product authority intentionally differs by platform. Platform-specific evidence/accessibility details may be filled using the selected platform context.
- Implementation Plan and Implementation Tasks are platform-specific because execution mechanics differ materially between iOS/iPadOS and Android.
- Readiness Audit and Readiness Report are shared; platform-specific runtime evidence is filled from the selected plan/tasks and platform skills.

## Complexity default

Feature Input risk signals inform the platform complexity-classification skill but do not assign the tier. If classification was not executed, or is missing/invalid/stale, downstream work defaults to **COMPLEX**.

## Verification timing

Evidence must run at the earliest stage where it is necessary, but not earlier:

- `TASK-CLOSURE`: proves the bounded task's direct outcome. Critical vertical journeys and directly changed persistence/migration semantics belong here.
- `FEATURE-CONVERGENCE`: proves cross-task integration and regression once the feature is assembled.
- `FINAL-READINESS`: expensive platform/device/security/privacy/performance/manual-runtime checks required before acceptance/release but normally not before each bounded task closes.

One valid artifact may satisfy multiple VM rows when it actually contains the required scenarios. Do not rerun tests solely to manufacture unique artifact filenames.

## Convergence blocker taxonomy

Readiness reports distinguish `IMPLEMENTATION`, `CI`, `EVIDENCE`, `DOCUMENTATION`, `REPOSITORY_STATE`, and `OWNER_DECISION` blockers. Missing evidence or an uncommitted tree must not be mislabeled as a production implementation defect.
