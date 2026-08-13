---
name: android-architecture-readiness
description: Blocks Android planning or implementation when architecture, presentation ownership, lifecycle, protected prerequisites, or current artifacts are unresolved or contradictory.
---
# Android Architecture Readiness

## Procedure
1. Read current spec, plan, tasks, architecture spine, coverage matrix, accepted ADRs, and `AI_CONTEXT.md`.
2. Verify status/authorization consistency across them.
3. Identify concerns touched: project structure, thin Activity, composition, ViewModels, navigation, persistence, background work, services, process death, backup, localization/adaptation/accessibility.
4. Confirm accepted canonical decisions and no active superseded contradiction.
5. Confirm every meaningful screen/workflow has a named lifecycle-retained state owner, scope, creation mechanism, and durable/ephemeral boundary.
6. Confirm external prerequisites or approved fail-closed behavior.
7. Confirm task-level evidence scenarios.

## Verdict
- Ready for planning
- Ready with explicit limitations
- Blocked

If blocked, list exact stale/contradictory artifacts, missing decisions, owner action, and smallest safe slice.
