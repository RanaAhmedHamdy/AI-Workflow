---
name: architecture-coverage-review
description: Separates decision, implementation, and evidence status for every cross-cutting architecture concern.
---
# Architecture Coverage Review

Evaluate every checklist row. Record decision status, implementation status, and evidence status separately. Identify current home, scope, gap, owner, blocker, next action, and next evidence. Explicitly cover namespace/module structure, thin Activity, composition, ViewModels, route/content, adaptation, localization/RTL, accessibility, lifecycle, background work, protected boundaries, testability, and release.

Do not infer not-applicable from absence or claim runtime support from static evidence. Return `PASS`, `PASS WITH LIMITATIONS`, or `BLOCKED`.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
