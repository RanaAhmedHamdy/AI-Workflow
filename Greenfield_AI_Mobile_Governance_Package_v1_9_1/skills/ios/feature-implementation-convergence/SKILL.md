---
name: feature-implementation-convergence
description: "Audits a completed iOS feature against the approved contract, implementation plan, tasks, architecture, design, cross-cutting requirements, and evidence. Use after implementation to detect drift before owner acceptance; it does not authorize release."
---

# Skill: Feature Implementation Convergence v1

## Purpose

Verify that an implemented mobile feature converges with the owner-approved feature contract, owner-approved implementation plan, owner-approved implementation tasks, architecture authority, design authority, cross-cutting requirements, and required evidence before owner acceptance.

This skill reviews implementation and evidence. It does not approve the feature, authorize release, authorize distribution, or silently repair product or architecture drift. It is not the production-code execution loop: authorized mutation and task-local verification belong to `bounded-feature-implementation`; this skill independently audits the complete feature afterward.

## Preconditions

Verify:

- feature contract is owner-approved;
- implementation plan is owner-approved;
- implementation task set is owner-approved;
- implementation authorization was granted before production implementation;
- implementation tasks are claimed complete or explicitly incomplete;
- applicable source diff, tests, runtime evidence, and documentation are available.

If a prerequisite is missing, stop with the appropriate verdict.

## Required Inputs

Read:

- `AGENTS.md`;
- `AI_CONTEXT.md`;
- `AI_PLAYBOOK.md`;
- owner decision register;
- approved feature contract;
- approved implementation plan;
- approved implementation tasks;
- architecture spine;
- applicable ADRs;
- implementation-readiness gate;
- design authority;
- screen contracts;
- exact artifact index and exact artifacts;
- completed implementation diff;
- automated test outputs;
- runtime evidence;
- production composition evidence;
- documentation changes;
- repository evidence policy.

## Required Output

Create or update:

`docs/features/<feature-id>/READINESS_REPORT.md`

Use:

`.templates/mobile/mobile/READINESS_REPORT_TEMPLATE.md`

Return exactly one:

- `READY FOR FINAL READINESS`
- `READY FOR FEATURE READINESS REVIEW`
- `BLOCKED BY IMPLEMENTATION DEFECT`
- `BLOCKED BY ARCHITECTURE DRIFT`
- `BLOCKED BY SCOPE DRIFT`
- `BLOCKED BY CI`
- `BLOCKED BY MISSING EVIDENCE`
- `BLOCKED BY DOCUMENTATION SYNC`
- `BLOCKED BY REPOSITORY STATE`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

This skill does not grant owner acceptance or release authorization.

## Mandatory Convergence Checks

### 1. Task Completion Integrity

For every implementation task marked complete, verify:

- objective was delivered;
- acceptance criteria are satisfied;
- contract and plan traceability remains valid;
- exact command or procedure was executed;
- environment or destination is named;
- actual outcome is recorded;
- evidence artifact exists at the declared path;
- known limitations are recorded;
- task completion review was performed.

A task marked complete without matching evidence must be reopened.

### 2. Contract-to-Implementation Traceability

Verify:

- every implemented behavior traces to an approved contract requirement;
- every in-scope contract requirement is implemented, blocked, or explicitly `Needs verification`;
- validation, state transitions, destructive behavior, offline behavior, and durability remain contract-faithful;
- no later-feature, deferred, candidate, or unsupported behavior entered production scope;
- no design example or broader PRD behavior silently expanded the feature.

### 3. Plan Conformance

Verify the implementation matches the approved plan for:

- feature and module ownership;
- dependency direction;
- domain boundaries;
- repository contracts;
- persistence ownership;
- presentation-state ownership;
- navigation and restoration;
- dependency composition;
- concurrency and cancellation;
- protected boundaries;
- localization and accessibility;
- testing and evidence.

Any material implementation choice absent from or contradictory to the approved plan is architecture drift unless an owner-approved amendment exists.

### 4. Architecture Conformance

Verify accepted ADRs and the architecture spine remain satisfied.

Flag:

- service locators or hidden global singletons;
- ad hoc dependency construction in UI code;
- infrastructure access from leaf views or composables;
- persistence entities exposed directly to presentation leaves;
- side effects during declarative rendering;
- unowned asynchronous work;
- lifecycle-escaping tasks or collectors;
- weakened concurrency or compiler settings;
- unapproved packages, targets, modules, capabilities, permissions, or services;
- host/application roots owning feature workflows;
- undocumented architecture substitutions.

### 5. Design Conformance

For every implemented screen or surface, verify:

- exact approved compact and wide artifacts are referenced where applicable;
- screen-contract behavior and state coverage are implemented;
- unsupported artifact content remains excluded;
- loading, empty, failure, recovery, disabled, success, offline, and destructive states are covered when applicable;
- intermediate adaptive behavior is derived only within approved design-system authority;
- static design titles are not treated as runtime evidence.

### 6. Localization and Bidirectional Layout

Verify:

- zero hardcoded user-facing and accessibility-facing strings;
- approved localization resources are complete;
- pluralization and substitutions are correct;
- locale-aware dates, times, numbers, measurements, units, currencies, percentages, and lists are used;
- sentence-fragment concatenation is absent;
- approved RTL locales render correctly at runtime;
- leading/trailing semantics are preserved;
- mixed-direction content is readable;
- long translations and truncation are tested;
- notifications, widgets, extensions, background messages, and errors are included when applicable.

### 7. Accessibility Runtime

Verify runtime evidence appropriate to the platform for:

- screen-reader labels, values, roles/traits, actions, headings, and announcements;
- focus order and focus restoration;
- text scaling and reflow;
- non-color differentiation;
- contrast and transparency adaptation where applicable;
- reduced motion;
- touch target sizing;
- keyboard, switch, voice, pointer, or alternate input where in scope;
- accessible custom controls;
- error announcement and recovery.

Source inspection, previews, snapshots, or artifact titles are not sufficient proof.

### 8. Adaptive and Lifecycle Runtime

Verify named runtime scenarios for applicable platform environments, including:

- compact window;
- expanded window/tablet;
- reduced, split, resized, or multitasking window;
- orientation or posture change where supported;
- keyboard/IME and system insets;
- safe regions and cutouts;
- state preservation during reflow;
- background/foreground transitions;
- configuration, scene, or process reconstruction;
- termination and relaunch.

Do not claim support for untested platform surfaces.

### 9. Persistence and Data Integrity

When applicable, verify:

- store initialization;
- schema/version ownership;
- migration from representative prior versions;
- failed-migration recovery;
- real disk-backed behavior;
- atomic multi-record operations;
- rollback;
- logical idempotency;
- stale-write and duplicate prevention;
- relaunch durability;
- date attribution and historical stability;
- test-store isolation;
- backup and protection rules;
- deletion/logout/account-removal behavior;
- representative production migration fixtures.

Screenshots alone cannot prove persistence, rollback, idempotency, or migration.

### 10. Privacy and Protected Boundaries

Verify applicable:

- privacy manifests or platform equivalents;
- permission and capability declarations;
- usage descriptions;
- entitlements;
- exported components and external entry points;
- URL/app links;
- background modes or services;
- sensitive-framework use;
- data minimization, consent, retention, and deletion;
- backup and transfer rules;
- log, analytics, trace, and crash redaction;
- third-party dependency privacy and supply-chain requirements;
- fail-closed behavior for missing protected configuration.

Any app-originated unauthorized external transfer is a blocking privacy failure.

### 11. Production Composition Integrity

Run production-fake detection against release composition.

Fail for:

- manufactured provider responses;
- fixed success identifiers;
- accept-all validation;
- placeholder authorization, receipts, signatures, tokens, or attestation;
- no-op repositories, workers, schedulers, migrations, or background handlers;
- in-memory substitutes for required durability;
- preview, sample, demo, mock, or test bindings in release composition;
- debug bypasses entering release behavior;
- silent fallback from unavailable infrastructure to simulated success.

### 12. Automated Verification and CI

Verify:

- narrow task-level tests passed;
- domain/state tests passed;
- repository/integration tests passed;
- persistence/migration tests passed where applicable;
- UI automation passed where applicable;
- localization/resource validation passed;
- prohibited-pattern scans passed;
- full CI passed on the approved toolchain;
- current machine-readable result artifacts are published;
- failed or skipped tests are explained.

### 13. Evidence Validity

Every evidence record must name:

- observable contract;
- environment/destination and OS/runtime;
- command/session;
- expected result;
- actual result;
- artifact path;
- limitations.

Reject:

- previews as runtime evidence;
- snapshots as sole behavioral proof;
- host tests as proof of device-only behavior;
- screenshots as proof of calculations, durability, rollback, duplicate prevention, screen-reader behavior, or security;
- stale result artifacts;
- generic “tests passed” claims without commands and paths.

### 13A. Verification-Matrix Closure

When the approved implementation plan defines `VM-*` scenarios, verify whole-feature closure once at convergence:

- every required `VM-*` ID is accounted for by current evidence or an explicit blocking/needs-verification limitation;
- evidence matches the scenario environment, procedure, expected observable result, and declared evidence path closely enough to prove the claim;
- task-level `Verification Matrix Coverage` references resolve to approved IDs;
- no required scenario silently disappears because tasks were marked complete;
- evidence is not reassigned to a different scenario merely because it is convenient;
- convergence does not rerun bounded implementation or manufacture missing evidence.

A required `VM-*` scenario with no valid evidence and no explicit blocking limitation prevents a ready verdict.

### 14. Documentation Synchronization

Verify current status and evidence are synchronized across:

- feature contract, only when observable behavior changed through approved change control;
- implementation plan, only when an approved implementation amendment occurred;
- implementation tasks and completion status;
- ADRs and architecture spine when owner-approved technical decisions changed;
- architecture coverage matrix;
- readiness and authorization records;
- evidence index;
- known limitations;
- release documentation, only when separately authorized.

Fail unsupported, stale, contradictory, or self-authorizing claims.

### 15. Final PR Review

Review the complete coherent target-branch diff and nearby tests.

Report:

- blocking findings;
- non-blocking findings;
- questions;
- test gaps;
- commands run;
- runtime layers not proven;
- documentation impact.

Do not merge or authorize publication.

## Stop Conditions

Stop and return a blocking verdict when:

- an implemented behavior lacks contract authority;
- a contract requirement is silently omitted;
- implementation contradicts an accepted ADR or approved plan;
- release composition contains a fake, mock, bypass, or no-op substitute;
- required `TASK-CLOSURE` or `FEATURE-CONVERGENCE` runtime evidence is missing; deferred `FINAL-READINESS` evidence alone yields `READY FOR FINAL READINESS` rather than an implementation blocker;
- persistence claims lack disk-backed or migration evidence;
- accessibility or adaptive support is claimed from static evidence only;
- protected-boundary configuration is missing or unauthorized;
- current documentation contradicts implementation or authorization state;
- owner decision is required to determine whether drift is acceptable.

## Readiness Transition

If all implementation/convergence checks pass but applicable `FINAL-READINESS` evidence remains, return `READY FOR FINAL READINESS` and list only those deferred checks. If no final-readiness evidence remains, return `READY FOR FEATURE READINESS REVIEW`. CI, evidence, documentation, and repository-state blockers must use their own categories rather than `BLOCKED BY IMPLEMENTATION DEFECT`.

## Completion Report

Report:

- files read;
- implementation revision;
- tasks reviewed and reopened;
- contract coverage;
- plan and architecture conformance;
- design conformance;
- automated test summary;
- runtime evidence summary;
- persistence and migration result;
- localization/RTL result;
- accessibility result;
- adaptive/lifecycle result;
- privacy/protected-boundary result;
- production-fake verdict;
- documentation synchronization;
- PR-review outcome;
- unresolved limitations;
- convergence verdict;
- confirmation that feature acceptance and release authorization remain external.

## Convergence Evidence and Blocker Classification

At convergence:

- execute/collect `FEATURE-CONVERGENCE` evidence once;
- collect applicable `FINAL-READINESS` evidence only when this gate is designated to own it, otherwise leave it explicitly pending for final readiness;
- map existing valid artifacts to every verification row they satisfy before scheduling reruns; rerun only genuinely missing/stale scenarios;
- prefer coherent result bundles and compact summaries over one execution per `VM-*` ID.

Classify blockers accurately:

- `IMPLEMENTATION` — production behavior/architecture/data defect;
- `CI` — build/lint/static pipeline failure;
- `EVIDENCE` — missing/stale/insufficient proof;
- `DOCUMENTATION` — canonical docs/status/traceability mismatch;
- `REPOSITORY_STATE` — branch/worktree/commit state policy issue;
- `OWNER_DECISION` — unresolved authority.

Do not label evidence, documentation, or repository-state housekeeping as an implementation defect.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
When manual evidence remains, output:

MANUAL ACTION REQUIRED
[ ] <check> — <environment> — PASS when <short criterion>

Ask the user to reply PASS/FAIL + notes.
