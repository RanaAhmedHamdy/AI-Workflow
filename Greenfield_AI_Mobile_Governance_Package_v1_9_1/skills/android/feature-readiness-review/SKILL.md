---
name: feature-readiness-review
description: "Independently reviews the final Android feature state, readiness report, and evidence package for owner acceptance. Use after implementation convergence to decide PASS, FAIL, BLOCKED, owner-decision, or verification status without authorizing release or publication."
---

# Skill: Feature Readiness Review v1

## Purpose

Independently review a completed feature readiness report, final implementation state, and evidence package to determine whether the feature is ready for repository-owner acceptance.

`PASS` means ready for owner feature acceptance only. It does not authorize release, signing, distribution, store submission, or production publication.

## Verdicts

Return exactly one:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

## Required Inputs

Make the following sources available for escalation. Do not read every source exhaustively up front when the convergence report and spot-check set are internally consistent:


- `AGENTS.md`;
- `AI_CONTEXT.md`;
- `AI_PLAYBOOK.md`;
- owner decision register;
- approved feature contract;
- approved implementation plan;
- approved implementation tasks;
- completed `READINESS_REPORT.md`;
- architecture spine;
- applicable ADRs;
- architecture coverage matrix;
- pre-implementation readiness gate;
- design authority;
- screen contracts;
- exact artifact index and exact artifacts;
- complete implementation diff;
- automated test results;
- runtime evidence;
- production-fake report;
- documentation-review report;
- PR-review report.

## Review Depth: Independent Spot-Check by Default

The convergence report is the exhaustive whole-feature proof. This readiness review independently challenges that proof; it does not automatically repeat convergence.

Start with:

- `READINESS_REPORT.md`;
- approved contract/plan/tasks and current status/authorization records;
- CI summary;
- blocking findings and limitations;
- critical vertical journey evidence;
- architecture/protected-boundary exceptions or changes;
- documentation/repository-state summary.

Then spot-check at minimum one critical user journey, one architecture boundary, one persistence/protected invariant when applicable, and one referenced evidence artifact. Escalate to the complete diff/evidence/design package only when the report is inconsistent, a spot-check fails, a high-risk boundary changed, evidence provenance is unclear, or policy explicitly requires full review.

`PASS` still requires no unresolved blocking finding; this optimization reduces duplicate reading, not acceptance criteria.

## Final-Readiness Precondition

Before `PASS`, verify every applicable `FINAL-READINESS` obligation recorded by convergence is closed with actual evidence or is explicitly owner-authorized not applicable. A report still marked `READY FOR FINAL READINESS` is not eligible for `PASS`.

## Mandatory Review

### 1. Authority and Status Integrity

Verify:

- contract, plan, and tasks were owner-approved;
- implementation authorization existed before production implementation;
- convergence was performed after implementation;
- readiness review is independent from convergence authoring where repository policy requires independence;
- owner feature acceptance remains pending unless already explicitly recorded;
- release authorization is not implied by feature readiness.

Fail contradictory or self-authorizing status claims.

### 2. Task Completion Integrity

Verify every completed task has:

- satisfied acceptance criteria;
- actual command or procedure;
- named environment or destination;
- actual result;
- evidence path;
- limitations;
- completion-review status.

Fail tasks closed without matching evidence.

### 3. Contract Coverage and Scope Fidelity

Verify:

- every in-scope contract requirement is implemented and evidenced;
- every validation rule and state transition remains source-authorized;
- no later-feature, candidate, deferred, or unsupported behavior is present;
- excluded behavior remains absent;
- no design artifact or broad PRD clause silently expanded scope.

Report uncovered requirements and orphan implementation behavior.

### 4. Plan and Architecture Conformance

Verify implementation preserves:

- approved module/target boundaries;
- dependency direction;
- domain/presentation/data separation;
- state-holder ownership;
- dependency composition;
- concurrency and cancellation model;
- navigation and restoration policy;
- persistence and migration design;
- protected-boundary rules;
- no unapproved packages, modules, targets, services, or capabilities.

Fail hidden architecture substitutions or undocumented plan drift.

### 5. Design and Screen Conformance

For every implemented screen, verify:

- exact approved artifacts are cited;
- compact and wide references are respected where applicable;
- screen-contract states are covered;
- unsupported artifact content is excluded;
- adaptive derivation stays within design authority;
- static artifact titles are not presented as runtime or accessibility proof.

### 6. Automated Test Sufficiency

Verify the selected test layers can prove the claims.

Fail:

- UI-only proof of domain calculations;
- generic “run tests” wording;
- missing commands, destinations, or result artifacts;
- tests executed against the wrong persistence or dependency composition;
- stale or unrelated CI artifacts;
- skipped failures hidden as success.

### 7. Runtime Evidence Sufficiency

Verify named scenarios and results for applicable:

- compact and expanded windows;
- reduced/split/resized/multitasking behavior;
- keyboard/IME and insets;
- orientation/posture/reflow;
- state preservation and reconstruction;
- process termination and relaunch;
- approved locales and RTL;
- screen reader and focus;
- text scaling;
- reduced motion and non-color differentiation;
- alternate input;
- physical-device-only behavior where required.

Reject source-only, preview-only, snapshot-only, or host-only claims for runtime behavior.

### 8. Persistence and Data Integrity

Where applicable, verify evidence for:

- schema/version ownership;
- real disk-backed behavior;
- migration initialization;
- representative migration fixtures;
- atomicity and rollback;
- logical idempotency;
- duplicate prevention;
- stale-write behavior;
- relaunch durability;
- date attribution and historical stability;
- isolated test stores;
- backup/protection/deletion behavior.

Fail uniqueness-only idempotency claims or screenshot-only durability claims.

### 9. Localization and RTL

Verify:

- hardcoded-string scans are current;
- approved resource system is authoritative;
- pluralization and formatting are locale-aware;
- no sentence-fragment concatenation exists;
- approved RTL locales were tested at runtime;
- mixed-direction text, long translations, and truncation are covered;
- accessibility-facing strings are localized.

### 10. Accessibility

Verify runtime evidence for applicable:

- screen-reader semantics;
- focus order and restoration;
- text scaling/reflow;
- non-color differentiation;
- reduced motion;
- contrast/transparency adaptation;
- touch targets;
- custom controls;
- keyboard/switch/voice/pointer input;
- errors and live announcements.

Fail broad accessibility claims based only on source or static design.

### 11. Privacy and Protected Boundaries

Verify applicable:

- permissions/capabilities/entitlements/exported components are authorized;
- privacy declarations and usage descriptions are complete;
- sensitive data and logs are redacted;
- external transfers are explicit and authorized;
- backup, retention, and deletion rules are honored;
- protected external configuration fails closed;
- third-party dependencies satisfy privacy and supply-chain requirements.

Any unauthorized external transfer is blocking.

### 12. Production Composition

Require a current production-fake detection result.

Fail release composition containing:

- mocks, demos, previews, samples, or test bindings;
- fake provider success;
- fixed success identifiers;
- no-op infrastructure;
- debug bypasses;
- in-memory substitutes for required durability;
- silent simulated fallback.

### 13. Documentation and Governance Synchronization

Verify:

- readiness report reflects actual evidence;
- task completion status is current;
- architecture coverage is updated;
- decisions and ADRs are synchronized;
- known limitations remain visible;
- no document claims release readiness or authorization without owner authority;
- canonical paths and filenames are consistent.

### 14. PR Review Quality

Verify the PR review covered the complete coherent diff and reported:

- blockers;
- non-blockers;
- test gaps;
- commands run;
- runtime layers not proven;
- documentation impact.

A clean PR review is necessary but not sufficient for `PASS`.

## Finding Format

For every finding include:

- Finding ID;
- Severity: Blocking / Major / Minor;
- Area;
- Contract requirement or task ID;
- Plan/ADR/design authority;
- Problem;
- Evidence checked;
- Required correction;
- Verdict impact.

## Pass Criteria

Return `PASS` only when:

1. all approved contract requirements are implemented and evidenced;
2. no scope drift exists;
3. all completed tasks have matching evidence;
4. the approved plan and architecture are preserved;
5. exact design traceability is complete;
6. automated and runtime evidence are sufficient;
7. persistence and migration claims are proven where applicable;
8. localization and approved RTL locales are verified;
9. accessibility and adaptive claims are runtime-backed;
10. privacy and protected boundaries pass;
11. production composition is free of fakes and bypasses;
12. documentation is synchronized;
13. known limitations are honest;
14. owner acceptance and release authorization remain external.

## Final Report

Include:

- verdict;
- feature and revision;
- task completion summary;
- contract coverage;
- scope drift;
- plan/architecture findings;
- design findings;
- automated test gaps;
- runtime evidence gaps;
- persistence findings;
- localization/RTL findings;
- accessibility findings;
- adaptive/lifecycle findings;
- privacy/protected-boundary findings;
- production-fake findings;
- documentation/governance findings;
- PR-review findings;
- owner decisions required;
- exact sections or tasks requiring revision;
- statement that `PASS` means ready for owner feature acceptance only.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
