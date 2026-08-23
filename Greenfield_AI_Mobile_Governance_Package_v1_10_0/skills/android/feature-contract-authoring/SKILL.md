---
name: feature-contract-authoring
description: "Authors a bounded, owner-reviewable Android feature contract from approved feature input and repository authority. Use when turning product requirements into a tool-neutral behavioral contract without leaking implementation details or expanding scope."
---

# Skill: Android Feature Contract Authoring v1

## Purpose

Create a complete, tool-neutral, owner-reviewable Android feature contract from one approved feature input without absorbing behavior from later features, broader PRD scope, design examples, Android implementation mechanisms, or framework defaults.

This skill does not authorize planning or implementation.

## Core Rule

The target feature input defines the bounded feature scope.

The PRD, design package, architecture spine, ADRs, feature map, owner decisions, Android platform policy, and verified evidence may clarify, constrain, or provide traceability, but they must not silently expand the feature beyond the target feature input.

A requirement appearing somewhere in the PRD, design package, existing app, Android documentation, or sample code is not automatically in scope for the current feature.

## Required Output

Create or update:

`docs/features/<feature-id>/FEATURE_CONTRACT.md`

Use:

`.templates/mobile/mobile/FEATURE_CONTRACT_TEMPLATE.md`

Return one authoring verdict:

- `READY FOR OWNER APPROVAL`
- `BLOCKED BY PRODUCT CLARIFICATION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

Never mark the contract approved, plan-ready, task-ready, implementation-authorized, release-ready, or verified.

## Authority Order

1. Current explicit owner direction.
2. Root repository policy and protected-boundary rules.
3. Approved owner decisions.
4. Approved product authority.
5. Target feature input.
6. Feature map and dependency sequence.
7. Accepted Android architecture spine and ADRs.
8. Approved design authority, screen contracts, and exact artifacts.
9. Verified implementation and produced evidence.
10. Context router, playbook, skills, imported guidance, Android samples, and model suggestions.

When the target feature input intentionally narrows broader PRD behavior for sequencing, preserve the narrower feature boundary.

## Workflow

### 1. Load Required Context

Read:

- root repository policy;
- context router;
- active playbook;
- owner decision register;
- approved PRD;
- feature map;
- target feature input;
- Android architecture spine;
- applicable ADRs;
- implementation-readiness gate;
- design authority;
- screen contracts;
- design system;
- information architecture;
- artifact index;
- exact artifact references;
- evidence policy.

Record files read.

### 2. Build a Scope Ledger Before Writing

Create an internal scope ledger with four categories:

#### A. Explicitly In Scope

Only behavior directly stated in the target feature input.

#### B. Required Supporting Behavior

Behavior strictly necessary to make an explicitly in-scope outcome coherent, safe, testable, accessible, localizable, recoverable, or durable.

Supporting behavior must not introduce a later-feature workflow or a technical mechanism.

#### C. Explicitly Excluded or Sequenced Later

All exclusions in the target feature input plus behavior owned by dependent or later features.

#### D. Clarification Candidates

Material observable behavior not resolved by authority.

Do not author settled requirements until every proposed behavior is classified.

### 3. Enforce Feature Ownership

Before adding a requirement, ask:

1. Is the behavior explicitly present in the target feature input?
2. Is it strictly necessary to complete, protect, or recover an in-scope action?
3. Does the feature map assign it to another feature?
4. Would adding it pull forward a later workflow?
5. Is it merely present in the broader PRD, an Android sample, an artifact, or an existing implementation?

If a later feature owns the behavior, exclude it and record the dependency.

### 4. Source-Back Every Validation Rule

Every validation rule, required-field rule, uniqueness rule, zero-value policy, draft-dirty threshold, exact error wording, date-selection rule, decimal policy, destructive threshold, retry eligibility rule, or save-enabled condition must map to an explicit approved source:

- target feature input;
- approved PRD;
- owner decision;
- approved screen contract;
- approved design authority.

If no explicit source exists:

- do not place the rule in functional requirements;
- do not place it in business rules;
- do not place it in state guards;
- do not place it in acceptance scenarios as settled behavior;
- add it to the clarification register as `Needs owner decision`.

A generic phrase such as “validate input” or “show an error” does not authorize invented field-level rules or copy.

### 5. Prevent Unsupported Product Rules

Do not convert ambiguity or platform convention into a requirement.

The following normally require explicit product/design authority or owner clarification:

- required versus optional fields;
- zero-value policy;
- uniqueness constraints;
- date selection;
- decimal precision and rounding;
- maximum lengths;
- destructive thresholds;
- exact error wording;
- fixed breakpoints or pane counts;
- fixed retry counts or timeouts;
- process-death guarantees stronger than approved durability wording;
- background execution timing;
- exact notification behavior;
- permission prompting strategy;
- sign-in or entitlement gates.

### 6. Separate Behavior from Android Implementation

Allowed:

- observable behavior;
- business rules;
- state transitions;
- validation outcomes;
- success, failure, recovery, offline, cancellation, and destructive outcomes;
- durability and idempotency invariants;
- adaptive and resizable-window outcomes;
- localization and RTL behavior;
- accessibility outcomes;
- permission/capability outcomes;
- evidence obligations.

Prohibited unless explicitly mandated by accepted authority:

- Jetpack Compose, Android Views, Fragments, Activities, or Navigation components;
- ViewModel, `StateFlow`, LiveData, `SavedStateHandle`, or lifecycle APIs;
- Hilt, Dagger, Koin, service locators, or manual DI classes;
- Room, DataStore, SQLite, Realm, files, schema, DAO, entity, or migration APIs;
- WorkManager, services, receivers, exact alarms, foreground services, or notification APIs;
- coroutine scopes, dispatchers, Flow operators, mutexes, or implementation-specific state machines;
- Gradle modules, source-set names, build variants, package names, or concrete file paths;
- permission API classes, manifest declarations, providers, SDKs, or production identifiers;
- fixed dp breakpoints or framework-specific adaptive components;
- test frameworks as product behavior.

### 7. Resolve Clarifications from Authority First

For every potential owner question, inspect all approved sources first.

Classify each ambiguity as:

- `Resolved from authority`
- `Needs owner decision`
- `Needs verification`
- `Authority conflict`

Do not ask the owner to decide something already resolved by approved product or design authority.

Do not ask for exact final copy unless wording itself is a product decision. Define required meaning when exact wording is not authoritative.

### 8. Preserve Exact Design Authority

For each applicable screen:

- cite the screen-contract ID;
- cite exact compact artifact(s);
- cite exact medium/expanded artifact(s) when applicable;
- distinguish product behavior from visual intent;
- list unsupported artifact content to exclude;
- derive only routine states permitted by design authority;
- do not invent layouts, destinations, panes, rails, drawers, FABs, or workflows absent from approved authority.

Artifact titles, design notes, and static mockups are not runtime, accessibility, RTL, foldable, or device evidence.

### 9. Define Adaptive Outcomes Without Inventing Layouts

Define, where applicable:

- compact-window composition;
- medium-window composition;
- expanded-window composition;
- reduced, split-screen, freeform, or resized behavior;
- orientation and fold/posture changes;
- IME/keyboard reachability;
- system-bar, cutout, hinge, and inset behavior;
- overflow and scrolling;
- information hierarchy;
- state preservation during reflow.

Do not specify arbitrary dp breakpoints, unapproved grids, unapproved panes, unapproved rails/drawers, or extra content regions.

### 10. Localization and RTL

Require observable outcomes, not resource APIs.

Require:

- localizable user-facing and accessibility-facing text;
- locale-aware dates, times, numbers, measurements, currencies, and lists;
- correct plurals and grammatical variants;
- no translated sentence-fragment concatenation;
- semantic start/end behavior rather than left/right assumptions;
- correct RTL mirroring and shaping;
- mixed-direction readability;
- long-translation and text-expansion handling;
- localization of errors, notifications, shortcuts, widgets, and background-visible text when applicable.

Do not prescribe Android resource classes or formatter APIs in the contract unless accepted architecture explicitly mandates them.

### 11. Accessibility

Define outcomes for applicable categories:

- TalkBack/screen-reader names, roles, states, values, actions, headings, and traversal;
- focus order and focus restoration;
- font scaling and display scaling;
- reflow without clipping, overlap, or forced text shrinking;
- non-color differentiation;
- reduced/removed animation;
- contrast and visual-effect adaptation;
- touch target reachability;
- keyboard, D-pad, Switch Access, and Voice Access where supported;
- error and live-state announcements;
- custom-control semantics;
- magnification compatibility.

Do not claim accessibility verification from static artifacts, previews, source inspection, lint alone, or artifact names.

### 12. Privacy, Permissions, and Protected Boundaries

Define observable rules for any app-originated external transfer, sensitive data use, permission request, notification, background behavior, exported entry point, health data, billing, authentication, attestation, or release-protected boundary.

Missing authorization or configuration must fail closed into an explicit unavailable, local-only, queued, recoverable, or denied state approved by the contract.

Do not infer a permission, manifest declaration, service, receiver, provider, foreground service, app link, Health Connect integration, billing dependency, or analytics behavior merely because a library or artifact references it.

### 13. Evidence Requirements

Separate evidence layers:

- local JVM/unit test;
- repository/integration test;
- disk-backed persistence or migration test;
- Robolectric only where repository authority accepts it for the claim;
- instrumented Android test;
- Compose UI or View UI automation;
- emulator runtime;
- physical-device runtime;
- TalkBack/manual accessibility runtime;
- RTL/pseudo-locale runtime;
- configuration-change/process-death/relaunch runtime;
- background/service evidence;
- external-service or attestation evidence;
- APK/AAB/manifest/signing/release evidence.

A preview or screenshot may support visual-state evidence only. It must not alone prove calculations, durability, migration, rollback, duplicate prevention, process-death recovery, TalkBack, permissions, background work, security, signing, or release composition.

For each acceptance scenario, assign every evidence layer needed to prove the claim.

### 14. Durability Wording

Use the narrowest approved durability statement.

Do not silently strengthen “screen recreation,” “activity recreation,” “app relaunch,” or “process termination” into stronger guarantees such as device reboot, backup restore, cross-device transfer, or multi-process consistency without authority.

### 15. Owner Review Wording

The agent must not write:

- “Approve as written”;
- “Zero risk”;
- “No ambiguity”;
- “Implementation can begin”;
- “Android best practice requires this” as product authority.

When unresolved material product decisions exist, state that approval is blocked pending those decisions.

### 16. Contract Self-Audit

Before completion, create an internal trace table for every requirement and validation rule:

| Requirement/Rule | Target feature-input clause | PRD source | Owner decision | Screen contract | Owning feature | In scope? |
|---|---|---|---|---|---|---|

Any item without explicit support or a documented strictly necessary supporting reason must be removed or moved to clarification.

### 17. Stop Conditions

Return `BLOCKED BY PRODUCT CLARIFICATION` when unresolved observable behavior affects, for example:

- required fields;
- valid value ranges;
- date ownership;
- destructive confirmation thresholds;
- naming uniqueness;
- durability scope;
- exact save/commit eligibility;
- permission-dependent fallback;
- offline availability;
- entitlement behavior.

Return `BLOCKED BY AUTHORITY CONFLICT` when approved sources conflict.

Return `NEEDS VERIFICATION` only for evidence-dependent technical or runtime claims, not unresolved product behavior.

Implementation readiness being blocked does not itself block contract authoring unless the missing technical decision changes observable product behavior.

## Completion Report

Report:

- files read;
- contract path;
- requirements added;
- requirements deliberately excluded as later-feature scope;
- unsupported rules moved to clarification;
- clarifications resolved from authority;
- unresolved owner decisions;
- exact artifacts mapped;
- unsupported artifact content excluded;
- Android implementation mechanisms avoided;
- authoring verdict;
- confirmation that no code, plan, tasks, Gradle files, manifest entries, resources, schemas, permissions, or Android mechanisms were created.

## Feature-Input Journey Integrity Rules (v1.9)

Before authoring observable states or transitions, treat the reviewed Feature Input as the primary bounded statement of journey intent:

- Build an invocation-context matrix from `Origin / Entry Context → Trigger → Destination / Mode → Success Return → Cancel/Back Return → Failure Behavior`.
- Preserve distinct modes when one reusable visual screen is entered from multiple origins. Never collapse a search-review form, historical edit form, onboarding setup form, or normal-management form into one behavioral state merely because they share UI.
- For every durable mutation, copy the product-declared affected screens/consumers and required timing into the contract as observable cross-screen consistency requirements. Do not invent the implementation propagation mechanism in the contract.
- Author critical end-to-end acceptance journeys that include starting context, durable result, affected-consumer result, and final destination.
- Preserve lifecycle/re-entry expectations: an inactive or recreated consumer that is required to show current committed state must do so even if it did not observe the original mutation event.
- If the Feature Input omits a material success/cancel/failure destination, affected consumer, or re-entry expectation and no higher authority answers it, mark `Needs owner decision`; do not guess.
- State-transition matrices must be checked against the invocation-context matrix. A transition may not route a reusable screen into another mode's return semantics.

The Feature Input states **what** the journey must do. The contract formalizes that behavior. Implementation mechanisms belong in the implementation plan.

## Complexity Classification Routing

Before applying tier depth, inspect the current classification record. If no fresh valid record exists, run the platform `feature-complexity-classification` procedure first. If it cannot produce a valid result, record `DEFAULTED_TO_COMPLEX` and continue as COMPLEX. Do not interrupt contract authoring merely to ask for a tier that can be derived or safely defaulted.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
