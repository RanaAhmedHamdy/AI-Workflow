---
name: feature-contract-review
description: "Independently reviews an iOS feature contract for authority fidelity, behavioral completeness, design conformance, adaptive UI, localization, RTL, accessibility, protected boundaries, evidence quality, and implementation leakage. Use after authoring and before owner approval."
---

# Skill: Feature Contract Review

## Purpose

Independently review a completed feature contract for authority fidelity, behavioral completeness, design conformance, adaptive UI quality, localization, RTL, accessibility, protected boundaries, evidence quality, and implementation leakage.

Do not rewrite silently. Report findings with exact section and requirement references.

## Verdicts

Return exactly one:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

`PASS` means ready for owner approval, not ready for implementation.

## Required Inputs

- Completed feature contract.
- Source feature input.
- Product authority.
- Owner decision register.
- Architecture spine and applicable ADRs.
- Design authority.
- Screen contracts.
- Design system.
- Artifact index and exact artifact references.
- Readiness gate.
- Repository policy and context router.

## Review Procedure

### 1. Authority Fidelity

Check that:

- authority order matches repository policy;
- behavior traces to approved product sources;
- owner decisions are applied;
- conflicts are not silently reconciled;
- skills and imported guidance do not override authority;
- candidate and deferred capabilities remain excluded.

### 2. Scope Fidelity

Check that:

- all feature-input in-scope behavior is present;
- all exclusions remain excluded;
- dependencies are accurate;
- protected boundaries are preserved;
- no unrelated feature was absorbed into the contract.

### 3. Requirement Quality

Every requirement must be:

- observable;
- testable;
- unambiguous;
- source-attributed;
- behavior-focused;
- explicit about failure and recovery when applicable.

Flag vague language including:

- responsive;
- accessible;
- graceful;
- robust;
- best practice;
- properly;
- match design;
- handle errors.

unless followed by measurable outcomes.

### 4. Implementation Leakage

Fail any unauthorized selection of:

- persistence engine;
- schema;
- ORM entity;
- migration API;
- repository implementation;
- SDK class;
- framework-specific UI hierarchy;
- provider;
- model name;
- prompt;
- quota;
- price;
- retry constant;
- secret;
- production identifier.

Accepted architecture invariants may be referenced, but the contract must remain behavioral.

### 5. Design Traceability

For every applicable surface verify:

- screen-contract ID exists;
- exact design artifact IDs exist;
- product behavior and visual intent are separated;
- unsupported artifact content is excluded;
- routine states are identified;
- unresolved visual decisions are visible;
- approved composition is not replaced by a generic platform screen.

### 6. Adaptive UI Review

Check for explicit outcomes for:

- compact phone;
- regular-width tablet;
- reduced tablet width;
- keyboard presentation;
- safe areas;
- overflow;
- scrolling;
- information hierarchy;
- control reachability;
- state preservation during reflow.

Fail generic statements such as “support iPhone and iPad” or “use adaptive layouts.”

### 7. Localization and RTL Review

Check that:

- all user-facing and accessibility-facing strings are localizable;
- no hardcoded-string assumptions are present;
- sentence-fragment concatenation is prohibited;
- formatting is locale-aware;
- RTL uses semantic leading/trailing behavior;
- Arabic or other RTL shaping is considered;
- mixed-direction values remain readable;
- uppercase rules do not damage localized content.

### 8. Accessibility Review

Check explicit outcomes for applicable settings and assistive technologies:

- screen reader;
- focus order;
- maximum text size;
- Bold Text;
- Differentiate Without Color;
- Button Shapes;
- Reduce Transparency;
- Increased Contrast;
- Reduce Motion;
- touch targets;
- error announcements.

Static design titles must not be treated as evidence.

### 9. Failure, Recovery, Offline, and Destructive Review

Check that:

- failed writes preserve prior valid state;
- cancellation consequences are explicit;
- destructive actions require explicit intent;
- partial failure is represented honestly;
- offline behavior is explicit;
- unavailable external work has a bounded fallback where authority requires it;
- silent loss, duplication, commit, deletion, purchase, or transfer is prohibited.

### 10. Persistence and Integrity Review

Check that:

- durability is expressed as an invariant;
- historical snapshots or immutable records remain protected;
- duplicate prevention is specified;
- interruption and relaunch behavior are specified;
- implementation mechanisms are not selected prematurely;
- blocked feasibility work is not falsely claimed as complete.

### 11. Acceptance Scenario Review

Check that scenarios cover:

- happy path;
- validation;
- failure;
- recovery;
- cancellation;
- offline behavior;
- relaunch or restoration where applicable;
- compact layout;
- wide layout;
- RTL;
- maximum text size;
- screen reader;
- keyboard-visible interaction.

Each critical scenario must name an evidence layer without claiming evidence exists.

### 12. Clarification Review

Check that:

- existing answers were resolved from authority;
- only material behavior questions remain;
- technical questions are excluded;
- recommendations and consequences are stated;
- owner decisions are not self-approved.

### 13. Approval and Status Review

Fail if the agent:

- marks the contract approved;
- claims implementation authorization;
- claims readiness gates passed without evidence;
- claims runtime verification from static artifacts;
- claims completed tests not actually run.

## Finding Format

For each finding report:

- Finding ID;
- Severity: Blocking / Major / Minor;
- Contract section or requirement;
- Source authority;
- Problem;
- Required correction;
- Suggested wording when useful.

## Final Report

Include:

1. verdict;
2. blocking findings;
3. major findings;
4. minor findings;
5. missing traceability;
6. unsupported behavior found;
7. implementation leakage found;
8. adaptive UI gaps;
9. localization/RTL gaps;
10. accessibility gaps;
11. evidence gaps;
12. owner decisions required;
13. statement that `PASS` means ready for owner approval only.

## Feature-Input Journey Integrity Review (v1.9)

Before returning `PASS`, compare the contract directly with the Feature Input journey sections:

- Every material invocation context has an exact success, cancel/back, and failure outcome, or an explicit unresolved owner decision.
- Reused visual screens preserve distinct behavioral modes/origins; no state transition aliases one mode into another mode's save/cancel destination.
- Every durable mutation names all product-declared affected screens/consumers and the required observable timing.
- Critical end-to-end journeys prove the complete product path: origin → action → durable result → affected-consumer result → final destination.
- Lifecycle/re-entry expectations cover consumers that were inactive, newly created, or reconstructed after the mutation when the Feature Input requires current committed state.
- The contract does not manufacture a propagation technology, navigation destination, or lifecycle promise that is absent from product/owner authority.
- Ambiguous slash destinations such as `Home / Settings`, generic `previous screen`, or equivalent wording are blocking when the Feature Input supplies or requires a specific origin-sensitive outcome.

Fail the review when the state model, success/failure sections, reachability matrix, and acceptance scenarios disagree about the same journey.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
