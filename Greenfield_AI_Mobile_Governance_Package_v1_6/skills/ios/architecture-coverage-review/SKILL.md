---
name: architecture-coverage-review
description: Reviews cross-cutting architecture coverage before implementation readiness or convergence.
---

# Architecture Coverage Review

## Read first

- Current task and root `AGENTS.md`.
- `AI_CONTEXT.md`.
- Current feature specification, plan, tasks, accepted ADRs, architecture maps, and directly relevant code/configuration.
- Repository architecture coverage checklist.

## Procedure

1. Establish reviewed scope, branch, revision, and worktree state.
2. Evaluate every material concern:
   - application/target/package structure;
   - ownership and dependency direction;
   - state, concurrency, lifecycle, restoration;
   - navigation and external entry points;
   - persistence, migrations, backup, deletion;
   - networking and external services;
   - localization, RTL, adaptation, accessibility;
   - permissions, privacy manifests, capabilities, entitlements;
   - background execution, notifications, widgets, extensions;
   - configuration, environments, feature flags;
   - analytics, logging, crash reporting, performance;
   - security, signing, release, rollback;
   - testing and runtime evidence.
3. Record three separate statuses:
   - **Decision**: Decided / Deferred with conditions / Not applicable / Unresolved blocker.
   - **Implementation**: Not started / Partial / Implemented / Contradictory.
   - **Evidence**: None / Static / Host test / Instrumented / Runtime-device / External service / Release artifact.
4. Record evidence, gap, owner, blocker, and smallest safe next action.
5. Route source/decision contradictions to `documentation-consistency-review`.
6. Do not infer support or `Not applicable` from absence.
7. Return pass/block result.

## Output

- scope;
- concern matrix;
- contradictions;
- unresolved owner questions;
- runtime/release handoffs;
- pass/block verdict.

## Complexity Tier and Cross-Feature Coherence Rules (v1.6)
- Read `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md` and the feature classification record before applying depth/sizing rules.
- If `feature-complexity-classification` was not executed, or its result is missing/invalid/stale, treat the feature as `COMPLEX` and record `DEFAULTED_TO_COMPLEX`. Never infer a lower tier.
- Use one canonical lifecycle/template family; tier changes mandatory depth and specialist gates, not authority order.
- For every durable mutation, identify all affected consumers/read models and the explicit propagation/invalidation/observation mechanism. A locally successful write with a stale dependent screen is incomplete.
- For actions reachable from multiple entry contexts, define and verify origin-sensitive success/cancel/failure destinations. Normal management must not accidentally execute onboarding/setup completion semantics.
- Any user-committable vertical slice must prove `commit → authoritative state → affected consumer refresh → correct destination` before bounded closure when that journey is in the task's scope. Do not defer all such proof to final convergence.

