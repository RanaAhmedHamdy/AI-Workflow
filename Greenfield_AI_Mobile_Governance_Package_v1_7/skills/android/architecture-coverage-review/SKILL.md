---
name: architecture-coverage-review
description: Separates decision, implementation, and evidence status for every cross-cutting architecture concern.
---
# Architecture Coverage Review

Evaluate every checklist row. Record decision status, implementation status, and evidence status separately. Identify current home, scope, gap, owner, blocker, next action, and next evidence. Explicitly cover namespace/module structure, thin Activity, composition, ViewModels, route/content, adaptation, localization/RTL, accessibility, lifecycle, background work, protected boundaries, testability, and release.

Do not infer not-applicable from absence or claim runtime support from static evidence. Return `PASS`, `PASS WITH LIMITATIONS`, or `BLOCKED`.

## Complexity Tier and Cross-Feature Coherence Rules (v1.7)
- Read `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md` and the feature classification record before applying depth/sizing rules.
- If `feature-complexity-classification` was not executed, or its result is missing/invalid/stale, treat the feature as `COMPLEX` and record `DEFAULTED_TO_COMPLEX`. Never infer a lower tier.
- Use one canonical lifecycle/template family; tier changes mandatory depth and specialist gates, not authority order.
- For every durable mutation, identify all affected consumers/read models, the active-consumer propagation/invalidation/observation mechanism, and the authoritative catch-up path for inactive/recreated consumers. A locally successful write or event-only update path that can leave a later-recreated screen stale is incomplete.
- For actions reachable from multiple entry contexts, define and verify origin-sensitive success/cancel/failure destinations. Normal management must not accidentally execute onboarding/setup completion semantics.
- Any user-committable vertical slice must prove `commit → authoritative state → affected consumer refresh → correct destination` before bounded closure when that journey is in the task's scope. Do not defer all such proof to final convergence.

