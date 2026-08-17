---
name: feature-contract-review
description: "Independently reviews an Android feature contract for exact scope, source authority, behavioral completeness, design fidelity, governance, and implementation leakage. Use after contract authoring and before owner approval or implementation planning."
---

# Skill: Android Feature Contract Review v1

## Purpose

Independently review a completed Android feature contract against the target feature input, feature map, PRD, design authority, Android architecture, and governance.

The primary review question is:

> Did the contract preserve the exact bounded feature scope and source every observable rule without inventing, pulling forward, overclaiming, or leaking Android implementation mechanisms?

A review must not pass merely because every requirement appears somewhere in the broader PRD, design package, existing implementation, Android guidance, or sample code.

## Verdicts

Return exactly one:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

`PASS` means ready for owner approval only. It does not approve planning or implementation.

## Required Inputs

Read:

- completed feature contract;
- target feature input;
- feature map;
- approved PRD;
- owner decision register;
- Android architecture spine;
- applicable ADRs;
- design authority;
- screen contracts;
- design system;
- artifact index;
- exact artifacts;
- readiness gate;
- repository policy;
- context router;
- evidence policy.

## Mandatory Review Method

### 1. Build a Requirement-to-Feature-Input Diff

For every functional requirement, business rule, state event, state guard, validation rule, acceptance scenario, destructive behavior, durability claim, accessibility outcome, and permission-dependent behavior, classify it as:

- `Explicitly supported by target feature input`
- `Explicitly supported by another approved source`
- `Strictly necessary supporting behavior`
- `Owned by later feature`
- `Unsupported invention`
- `Needs owner decision`
- `Needs verification`

The review cannot return `PASS` while any item is classified as `Owned by later feature`, `Unsupported invention`, or hidden `Needs owner decision`.

### 2. Mandatory Validation-Rule Audit

For every validation rule and validation-related state guard, verify an explicit source for:

- required versus optional;
- empty/blank handling;
- uniqueness;
- minimum/maximum;
- zero and negative values;
- decimal handling and rounding;
- date/time selection;
- draft-dirty threshold;
- exact error meaning or copy;
- save/commit eligibility;
- retry eligibility;
- destructive confirmation threshold.

Unsupported validation rules block `PASS` and must move to owner clarification or be removed.

### 3. Check Feature Sequence Ownership

Compare the contract against the feature map.

Flag pulled-forward behavior including full management workflows, historical correction, favorites/repeat, remote lookup, AI, authentication, billing, export/deletion, Health Connect, notifications, widgets, deep links, background work, or candidate/deferred features when assigned elsewhere.

A broad PRD or design reference does not override feature sequencing.

### 4. Check Unsupported Product Rules

Flag unsupported rules such as required fields, uniqueness, numeric constraints, date selection, retry counts, timeouts, exact copy, fixed window breakpoints, pane counts, background timing, permission prompting, process-death guarantees, and notification behavior.

These must trace to authority or move to owner clarification.

### 5. Check Design Authority Paths and Exact Artifacts

Use current active design paths from repository routing.

For each screen verify:

- screen-contract ID;
- exact compact artifact;
- exact medium/expanded artifact where applicable;
- unsupported artifact content excluded;
- static artifact titles not treated as runtime proof;
- responsive alternatives treated as one surface where authority says so.

Do not fail merely because the repository uses a different current directory than a historical convention.

### 6. Check Adaptive UI Drift

Flag:

- arbitrary dp breakpoints;
- invented grids, columns, panes, rails, drawers, or FABs;
- unapproved foldable behavior;
- phone-only assumptions;
- orientation-only assumptions;
- generic “responsive” language;
- missing compact, medium, expanded, split/resized, IME, inset, cutout, hinge, overflow, reflow, or state-preservation outcomes where applicable.

Adaptive descriptions may rearrange approved content but must not introduce new product regions or workflows.

### 7. Check Android Implementation Leakage

Flag unapproved or unnecessary references to:

- Compose, Views, Activities, Fragments, Navigation components;
- ViewModel, StateFlow, LiveData, SavedStateHandle;
- Hilt, Dagger, Koin, service locators;
- Room, DataStore, SQLite, Realm, DAOs, entities, schemas, migrations;
- WorkManager, services, receivers, alarms, foreground services;
- Gradle modules, source sets, package names, build variants;
- permission APIs, manifest classes, providers, SDKs, app links;
- coroutine scopes, dispatchers, Flow operators;
- exact emulator names or test framework classes as product requirements;
- fixed filenames, resource names, production IDs, or provider classes.

### 8. Check Evidence Validity

For every acceptance scenario, verify that the named evidence can prove the claim.

Flag:

- previews/screenshots alone for calculations, durability, rollback, duplicate prevention, TalkBack, permissions, process death, background work, or release integrity;
- local JVM tests used to prove device-only behavior;
- Robolectric used beyond repository-approved claim boundaries;
- generic “instrumented test” wording with no destination or observable contract;
- UI-only proof of domain arithmetic;
- static inspection used to prove accessibility;
- source existence used to prove manifest merge, signing, or release composition.

Require distinct evidence layers where needed.

### 9. Check Accessibility Overclaiming

Flag:

- “accessible” derived from artifact title, lint, or preview;
- unsupported numerical contrast claims;
- broad TalkBack support without runtime evidence obligations;
- color-only status;
- missing focus, traversal, error announcement, font/display scaling, keyboard/D-pad, Switch Access, or Voice Access outcomes where applicable;
- fixed-height text or text-shrinking requirements;
- mechanism-specific wording where behavioral wording is sufficient.

### 10. Check Localization and RTL

Verify:

- all user-facing and accessibility-facing copy is localizable;
- plurals and formatting outcomes are stated where applicable;
- no fragment concatenation;
- semantic start/end behavior;
- RTL mirroring and mixed-direction content;
- long-translation/text-expansion behavior;
- error, notification, widget, shortcut, and background-visible text coverage when in scope.

Flag any Android resource mechanism imposed as product behavior without authority.

### 11. Check Durability Scope

Verify that activity recreation, configuration change, process death, app relaunch, device reboot, backup restore, and cross-device transfer are not conflated.

If durability is evidence-dependent, the contract may state the invariant but must not claim it has already been verified.

### 12. Check Permissions and Protected Boundaries

Flag wording that silently authorizes permissions, exported components, services, receivers, providers, app links, foreground services, Health Connect, billing, analytics, attestation, or external transfer.

Prefer explicit observable stop conditions and fail-closed outcomes.

### 13. Check Clarification Quality

Verify that:

- unsupported observable rules appear in clarification;
- existing authority answers are not re-asked;
- technical mechanism questions are excluded;
- owner decisions are not self-approved;
- minor copy choices do not unnecessarily block approval;
- design choices already resolved by design authority are not reopened.

### 14. Check Owner-Review and Approval Claims

Fail or require correction for:

- “Approve as written”;
- “Zero risk”;
- “No ambiguity”;
- claims implementation can begin;
- claims all decisions are resolved while unsupported rules remain;
- self-marked approval;
- claims readiness gates passed without evidence;
- claims runtime evidence exists when only requirements were written.

### 15. Check State and Behavior Consistency

Verify state events and guards do not introduce unsupported rules or out-of-scope workflows.

Pay particular attention to save eligibility, draft retention, retry, cancellation, process recovery, permission denial, offline states, and background-visible behavior.

## Finding Format

For every finding include:

- Finding ID;
- Severity: Blocking / Major / Minor;
- Contract section or requirement;
- Target feature-input clause;
- Explicit source check;
- Owning feature when different;
- Problem;
- Required correction;
- Suggested disposition: remove / defer / clarify / reword / add traceability / add evidence.

## Pass Criteria

A contract may receive `PASS` only when:

1. every requirement maps to the target feature input, another approved source, or documented strictly necessary supporting behavior;
2. every validation rule has an explicit source;
3. no later-feature behavior is pulled forward;
4. no unsupported product rule is hidden as a requirement;
5. design references are complete and current;
6. adaptive outcomes are explicit and introduce no new content;
7. localization and RTL are behavioral and implementation-neutral;
8. accessibility outcomes do not overclaim;
9. permission/protected-boundary behavior is authorized and fail-closed;
10. evidence layers are sufficient for each claim;
11. owner decisions are visible;
12. approval and implementation status are accurate;
13. Android implementation mechanisms have not leaked into product authority without mandate.

## Final Report

Include:

1. verdict;
2. scope-diff summary;
3. validation-rule audit;
4. blocking findings;
5. major findings;
6. minor findings;
7. later-feature behavior found;
8. unsupported product rules found;
9. Android implementation leakage found;
10. adaptive UI drift;
11. design traceability gaps;
12. localization/RTL gaps;
13. accessibility gaps;
14. evidence gaps;
15. durability-scope gaps;
16. permission/protected-boundary gaps;
17. owner decisions required;
18. exact sections that must be rerun;
19. statement that `PASS` means ready for owner approval only.

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
