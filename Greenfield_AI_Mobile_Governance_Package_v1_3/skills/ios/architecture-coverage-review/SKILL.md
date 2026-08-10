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
