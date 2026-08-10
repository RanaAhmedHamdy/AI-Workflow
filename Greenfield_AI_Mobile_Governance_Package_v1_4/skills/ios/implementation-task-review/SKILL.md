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
