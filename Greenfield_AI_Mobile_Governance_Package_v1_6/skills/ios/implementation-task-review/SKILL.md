# Skill: Implementation Task Review v1

## Purpose

Independently review an implementation task set for scope fidelity, dependency correctness, task sizing, architecture conformance, exact design traceability, evidence sufficiency, and authorization honesty.

`PASS` means ready for owner task approval only.

## Verdicts

Return exactly one:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

## Required Inputs

Read:

- implementation tasks;
- approved feature contract;
- approved implementation plan;
- feature map;
- architecture spine;
- applicable ADRs;
- readiness gate;
- design authority;
- screen contracts;
- exact artifacts;
- repository policy;
- evidence policy.

## Mandatory Review

### 1. Coverage and Traceability

Verify every:

- contract requirement;
- plan component;
- screen;
- persistence responsibility;
- localization/RTL responsibility;
- accessibility responsibility;
- adaptive responsibility;
- evidence obligation;

is covered by at least one task.

Flag orphan tasks and uncovered authority items.

### 2. Scope Fidelity

Fail tasks that:

- pull forward later features;
- invent product rules;
- include excluded artifact content;
- introduce network, auth, AI, billing, history, or remote lookup outside scope;
- broaden repository restructuring beyond the feature.

### 3. Dependency Graph

Verify:

- dependencies are explicit;
- graph is acyclic;
- prerequisites precede consumers;
- migrations/schema precede repository use;
- repositories/use cases precede presentation integration;
- evidence/convergence follows implementation.

Fail hidden dependencies and circular sequencing.

### 4. Task Sizing

Flag tasks that are:

- too broad;
- multi-layer without justification;
- impossible to review independently;
- trivial and evidence-free;
- duplicate;
- ambiguous.

### 5. Architecture Conformance

Verify tasks preserve:

- modular boundaries;
- dependency direction;
- isolated persistence;
- MainActor presentation ownership;
- no persistence entities in leaf views;
- no side effects in view bodies;
- accepted navigation and composition;
- accepted localization and security policies.

### 6. Persistence Tasks

Verify explicit tasks or acceptance criteria for:

- schema/version ownership;
- disk-backed repository behavior;
- atomic schedule and meal commits;
- rollback;
- logical idempotency;
- relaunch durability;
- test-store isolation;
- date attribution;
- migration initialization;
- no uniqueness-only idempotency;
- no forensic deletion overclaim.

### 7. Design Tasks

For every screen, verify:

- exact compact artifact;
- exact wide artifact where applicable;
- supported states;
- error/recovery;
- exclusions;
- compact/wide/reduced-width behavior;
- keyboard/safe area;
- RTL/accessibility obligations.

### 8. Verification Quality

Every task must state:

- test layer;
- command/procedure;
- destination;
- evidence path;
- limitation.

Fail:

- screenshots as sole proof of behavior;
- UI-only arithmetic proof;
- source-only accessibility proof;
- generic “run tests” wording;
- missing `.xcresult` obligations;
- evidence planned before relevant implementation exists.

### 9. Authorization Honesty

Fail if tasks:

- mark themselves executable before authorization;
- ask the agent to start implementation;
- grant authorization automatically after review;
- change owner approval;
- claim readiness gates passed without evidence.

### 10. Final Convergence

Verify final tasks cover:

- traceability;
- architecture;
- design;
- localization/RTL;
- accessibility;
- adaptive UI;
- persistence/relaunch;
- privacy/network;
- production fakes;
- documentation;
- clean CI/current result bundle.

### Verification-Matrix Traceability and Current-State Consistency

- Verify every task that implements or proves matrix-covered behavior lists the applicable approved `VM-*` IDs.
- Verify every referenced `VM-*` ID exists in the approved implementation plan and is relevant to the task.
- Reject invented IDs, required matrix scenarios with no implementation/evidence owner, and unnecessary duplication of full matrix scenario prose inside tasks.
- Search the complete task artifact for lifecycle, approval, readiness, and implementation-authorization assertions. If two assertions both claim to describe the current state and conflict, return a blocking finding. Historical stage verdicts are allowed only when clearly labeled as historical/stage-specific.

## Finding Format

- Finding ID;
- Severity;
- Task ID/section;
- Contract requirement;
- Plan section;
- Problem;
- Required correction;
- Verdict impact.

## Pass Criteria

A task set receives `PASS` only when:

1. all approved requirements and plan responsibilities are covered;
2. no scope drift exists;
3. dependency graph is acyclic and correct;
4. task sizes are bounded;
5. accepted architecture is preserved;
6. exact design and cross-cutting behavior are represented;
7. evidence is sufficient;
8. final convergence is complete;
9. authorization remains external;
10. no production code was generated.

## Final Report

Include:

- verdict;
- task count;
- coverage summary;
- blocking findings;
- scope drift;
- dependency issues;
- oversized/undersized tasks;
- architecture issues;
- persistence issues;
- design/adaptive issues;
- localization/RTL issues;
- accessibility issues;
- evidence gaps;
- readiness/authorization issues;
- exact tasks requiring revision;
- statement that PASS means ready for owner task approval only.

## Complexity Tier and Cross-Feature Coherence Rules (v1.6)
- Read `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md` and the feature classification record before applying depth/sizing rules.
- If `feature-complexity-classification` was not executed, or its result is missing/invalid/stale, treat the feature as `COMPLEX` and record `DEFAULTED_TO_COMPLEX`. Never infer a lower tier.
- Use one canonical lifecycle/template family; tier changes mandatory depth and specialist gates, not authority order.
- For every durable mutation, identify all affected consumers/read models and the explicit propagation/invalidation/observation mechanism. A locally successful write with a stale dependent screen is incomplete.
- For actions reachable from multiple entry contexts, define and verify origin-sensitive success/cancel/failure destinations. Normal management must not accidentally execute onboarding/setup completion semantics.
- Any user-committable vertical slice must prove `commit → authoritative state → affected consumer refresh → correct destination` before bounded closure when that journey is in the task's scope. Do not defer all such proof to final convergence.

