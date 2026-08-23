---
name: implementation-task-authoring
description: "Authors a dependency-ordered iOS implementation task set from an approved feature contract and approved implementation plan. Use after plan approval to create reviewable task definitions only, without modifying production code, tests, schemas, migrations, or project files."
---

# Skill: Implementation Task Authoring v1

## Purpose

Generate a dependency-ordered, reviewable implementation task set from an owner-approved feature contract and owner-approved implementation plan.

This skill creates task definitions only. It must not create production code, tests, schemas, migrations, or project files.

## Preconditions

Verify:

- feature contract is owner-approved;
- implementation plan is owner-approved;
- implementation-plan review is `PASS`;
- unresolved product decisions are closed;
- unresolved technical decisions that block task decomposition are closed;
- applicable pre-task governance documents are synchronized.

If any prerequisite is missing, stop with the appropriate verdict.

## Required Inputs

Read:

- `AGENTS.md`;
- `AI_CONTEXT.md`;
- `AI_PLAYBOOK.md`;
- owner decision register;
- approved feature contract;
- approved implementation plan;
- feature map;
- architecture spine;
- applicable ADRs;
- readiness gate;
- design authority;
- screen contracts;
- exact artifact index/artifacts;
- evidence policy;
- task template.

## Required Output

Create or update:

`docs/features/<feature-id>/IMPLEMENTATION_TASKS.md`

Use:

`.templates/mobile/ios/IMPLEMENTATION_TASKS_TEMPLATE.md`

Return one:

- `READY FOR TASK REVIEW`
- `BLOCKED BY PLAN ISSUE`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

Do not grant implementation authorization.

## Core Rules

### 1. Contract and Plan Bound the Tasks

Every task must trace to:

- one or more approved contract requirement IDs; and
- one or more approved implementation-plan sections.

Do not add behavior, modules, screens, or technical choices absent from the approved authorities.

### 2. One Bounded Outcome per Task

A task should deliver one coherent outcome that can be independently reviewed and verified.

Split tasks when they combine unrelated:

- domain behavior;
- persistence;
- presentation;
- localization;
- accessibility;
- runtime evidence;
- documentation.

Do not create giant “implement feature” tasks.

### 3. Dependency Order Must Be Explicit

Define a directed acyclic dependency graph.

Typical order:

1. bounded source/resource structure;
2. domain values and invariants;
3. repository contracts;
4. persistence adapters and migrations;
5. use cases;
6. presentation state;
7. navigation/composition;
8. screen implementation;
9. localization/RTL;
10. accessibility/adaptive behavior;
11. tests/evidence;
12. convergence review.

Adapt this only when the approved plan requires another order.

### 4. Tasks May Name Concrete Artifacts Carefully

Unlike the implementation plan, tasks may name:

- target modules;
- source directories;
- expected files/types;
- test targets;
- evidence outputs.

Only do so when names are established by the approved plan, accepted repository conventions, or architecture authority.

Do not invent concrete names merely to appear precise.

### 5. No Architecture Reopening

Tasks must apply accepted ADRs.

Do not create tasks to reconsider:

- persistence engine;
- navigation strategy;
- dependency injection approach;
- concurrency model;
- localization approach;
- security boundary;

unless the approved plan explicitly contains an unresolved decision task.

### 6. Verification Is Part of Each Task

Each task must define:

- acceptance criteria;
- test layer;
- command/procedure;
- environment;
- evidence path;
- known limitation.

A task is not complete merely because source files exist.

### 6A. Verification-Matrix Mapping and Current-State Integrity

- Every task that implements or proves matrix-covered behavior must list `Verification Matrix Coverage` with the applicable approved `VM-*` IDs from the implementation plan, or an explicit `N/A` rationale when no matrix scenario applies.
- Do not copy the full matrix scenario into each task; reference stable IDs and keep the detailed definition authoritative in the approved plan.
- Do not invent new `VM-*` IDs in the task set.
- Keep current task-set lifecycle/status/authorization truth in one canonical status block. Historical authoring/review verdicts may remain only when clearly labeled as stage-specific history; they must not contradict the current state.

### 7. Cross-Cutting Requirements Are First-Class

Do not defer these to final polish:

- localization;
- Arabic RTL;
- accessibility;
- adaptive UI;
- keyboard/safe-area behavior;
- privacy;
- persistence integrity;
- production-fake detection.

Integrate them into relevant tasks and keep final convergence tasks.

### 8. Implementation Authorization Is External

Every implementation task remains non-executable until the repository owner or defined authorization gate grants implementation authorization.

The agent must not self-authorize because tasks are approved.

### 9. No Production Code During Task Generation

Do not:

- create Swift files;
- edit Xcode projects;
- create schemas;
- create migrations;
- generate tests;
- run implementation commands;
- change readiness gates.

## Mandatory Task Fields

Every task must include:

- task ID;
- objective;
- contract references;
- plan references;
- authority references;
- dependencies;
- allowed scope;
- prohibited scope;
- acceptance criteria;
- verification layer;
- procedure/command;
- environment;
- evidence path;
- limitation;
- authorization statement.

## Task Sizing Guidance

A task is too large when:

- it spans multiple architectural layers;
- it covers more than one user-facing screen plus unrelated infrastructure;
- it cannot be reviewed from one primary outcome;
- its evidence requires unrelated test suites;
- failure would obscure which boundary was violated.

A task is too small when:

- it creates only a trivial symbol without independent value;
- it has no meaningful acceptance evidence;
- it exists only to inflate task count.

## Design-Bound UI Task Rule

For every UI task classify `DESIGN-BOUND UI`, `NON-DESIGN UI`, or `NON-UI`. A design-bound task must carry a concise Design Lock containing the exact approved visual artifact/path or deterministic locator, required variant/state, binding composition/hierarchy/grouping/action placement, and only documented permitted adaptations. It must explicitly require the implementation agent to inspect the actual visual before UI code. Artifact IDs or Markdown descriptions alone are insufficient. If the approved visual cannot be named/inspected, task authoring is blocked rather than free to improvise.

Do not duplicate the whole visual description in the task; keep the lock concise and let the artifact remain the visual source of truth.

## Stop Conditions

Stop when:

- plan is not approved;
- plan review is not `PASS`;
- a task would require inventing behavior;
- an unresolved technical decision affects dependency order;
- design authority is missing for a planned screen;
- persistence authority is provisional where production tasks depend on it;
- readiness routing is contradictory.

## Completion Report

Report:

- files read;
- task-set path;
- task count;
- dependency summary;
- contract and plan coverage;
- cross-cutting coverage;
- unresolved blockers;
- authoring verdict;
- confirmation that no production code or tests were created.

## Task Coherence and Verification Economy

- Every applicable concern needs explicit ownership and verification; it does **not** require a separate task. Prefer one coherent vertical task when state, route, rendering, resources, accessibility/adaptation, and focused verification naturally share one implementation boundary.
- Split tasks only for real dependency, risk, authorization, ownership, or review boundaries. Reject tasks that exist only to inflate task count or separate inseparable code/test work.
- Label each verification obligation `TASK-CLOSURE`, `FEATURE-CONVERGENCE`, or `FINAL-READINESS`.
- Make only `TASK-CLOSURE` evidence block an ordinary bounded task. Expensive cross-cutting checks such as full manual accessibility, file protection, network isolation, broad performance baselines, signing/archive inspection, or physical reboot belong later unless the current task directly changes that boundary.
- Reuse one result artifact across multiple verification rows when it actually proves them.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
