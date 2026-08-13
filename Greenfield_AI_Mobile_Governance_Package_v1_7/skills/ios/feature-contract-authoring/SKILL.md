# Skill: Feature Contract Authoring

## Purpose

Create a complete, tool-neutral, owner-reviewable feature contract from a repository feature input while preventing product, architecture, design, localization, accessibility, persistence, and evidence drift.

This skill does not authorize implementation.

## Inputs

- Feature ID or feature-input path.
- Repository authority and routing documents.
- Product authority.
- Approved owner decisions.
- Architecture spine and applicable ADRs.
- Design authority, screen contracts, design system, artifact index, and exact design artifacts.
- Feature-contract template.

## Required Output

Create or update the repository’s canonical feature-contract path, normally:

`docs/features/<feature-id>/FEATURE_CONTRACT.md`

Use:

`.templates/mobile/FEATURE_CONTRACT_TEMPLATE.md`

Return one authoring verdict:

- `READY FOR OWNER APPROVAL`
- `BLOCKED BY PRODUCT CLARIFICATION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

Never mark the contract approved.

## Authority Order

Apply authority in this order unless the repository defines a stricter order:

1. Current explicit owner direction.
2. Root repository policy.
3. Approved owner decisions.
4. Approved product authority and reviewed feature input.
5. Accepted architecture spine and ADRs.
6. Approved design authority and exact artifacts.
7. Verified implementation and evidence.
8. Context routing, playbooks, skills, and imported guidance.

A skill explains how to work. It does not authorize behavior or implementation.

## Workflow

### 1. Route and Load Context

Read the smallest complete authority set needed for the feature.

At minimum inspect:

- root repository policy;
- context router;
- active lifecycle/playbook;
- owner decision register;
- approved product authority;
- feature map;
- target feature input;
- architecture spine;
- applicable ADRs;
- readiness gate;
- design authority;
- artifact index;
- applicable screen contracts;
- design system;
- information architecture;
- traceability records.

Record all files read.

### 2. Establish Feature Boundary

Extract without reinterpretation:

- feature purpose;
- user outcome;
- actors;
- entry points;
- in-scope behavior;
- exclusions;
- PRD references;
- screen contracts;
- exact design artifact IDs;
- responsive and RTL expectations;
- dependencies;
- protected boundaries;
- unresolved questions;
- strict directives.

Candidate and deferred capabilities must remain excluded unless explicitly promoted by owner authority.

### 3. Separate Behavior from Implementation

Allowed in a feature contract:

- observable user behavior;
- business rules;
- state transitions;
- validation;
- success, failure, recovery, offline, cancellation, and destructive behavior;
- durability and integrity invariants;
- screen behavior;
- adaptive outcomes;
- localization and RTL behavior;
- accessibility outcomes;
- privacy and protected-boundary outcomes;
- acceptance scenarios;
- evidence requirements.

Prohibited unless an accepted authority makes the mechanism itself mandatory:

- schemas;
- ORM entities;
- persistence-engine selection;
- migration APIs;
- repository implementation details;
- SDK classes;
- framework-specific UI hierarchies;
- dependency-injection mechanics;
- providers;
- model names;
- prompts;
- quotas;
- prices;
- retry constants;
- secrets;
- production identifiers;
- analytics mechanisms.

Write:

> A committed record survives process termination and relaunch without duplication or loss.

Do not write:

> Store the record as a SwiftData `@Model`.

### 4. Resolve Clarifications from Authority First

Before creating an owner question:

1. search the approved product source;
2. inspect the feature input;
3. inspect owner decisions;
4. inspect screen contracts;
5. inspect exact design authority;
6. inspect accepted architecture constraints.

Classify each material ambiguity as:

- `Resolved from authority`
- `Needs owner decision`
- `Needs verification`
- `Authority conflict`

Do not ask technical implementation questions in the feature-contract clarification register.

### 5. Author Observable Requirements

Every requirement must be:

- observable;
- testable;
- unambiguous;
- attributed to source authority;
- bounded to the feature;
- explicit about applicable failure and recovery;
- free of unauthorized implementation detail.

Reject vague requirements such as:

- use best practices;
- make responsive;
- handle errors gracefully;
- match design;
- support accessibility;
- use clean architecture.

Replace them with measurable outcomes.

### 6. Preserve Exact Design Authority

For every applicable screen:

- cite the screen-contract ID;
- cite exact artifact IDs;
- distinguish product behavior from visible design intent;
- list routine states derivable from the approved design system;
- list unsupported copy or candidate behavior that must be excluded;
- state unresolved owner decisions.

Do not replace approved screen composition with generic platform defaults.

Static design artifacts do not prove runtime accessibility, adaptation, localization, contrast, or device behavior.

### 7. Define Adaptive Outcomes

For each applicable surface define:

- compact phone composition;
- regular-width tablet composition;
- reduced tablet width or split-view behavior;
- keyboard-visible behavior;
- safe-area behavior;
- overflow and scrolling behavior;
- information hierarchy;
- control reachability;
- state preservation during reflow.

Do not merely say “responsive” or “adaptive.”

### 8. Define Localization and RTL Outcomes

Require:

- localization resources for every user-facing and accessibility-facing string;
- no hardcoded strings;
- no sentence-fragment concatenation;
- locale-aware date, time, number, measurement, currency, percentage, and plural formatting;
- English fallback when defined by repository policy;
- semantic leading/trailing alignment;
- correct Arabic or other RTL shaping;
- mixed-direction number and unit readability;
- no uppercase transformation that damages localized content.

Do not invent final copy where product authority has not approved it. Define the message purpose and required meaning.

### 9. Define Accessibility Outcomes

For applicable surfaces define:

- screen-reader labels, values, hints, grouping, and focus order;
- focus movement after errors, save, cancel, and navigation;
- maximum text-size reflow;
- Bold Text;
- Differentiate Without Color;
- Button Shapes;
- Reduce Transparency;
- Increased Contrast;
- Reduce Motion;
- touch-target behavior;
- error announcement;
- no clipping or unreachable content.

Do not claim verification from artifact titles or static design files.

### 10. Define Evidence Scenarios

For each critical behavior name:

- observable scenario;
- expected result;
- evidence layer;
- environment or destination;
- artifact path;
- known limitations.

The contract specifies evidence obligations. It must not claim tests or runtime checks were executed.

### 11. Populate the Template

Complete every applicable section.

Do not leave silent gaps. Use:

- `N/A — owner-authorized because ...`
- `Needs owner decision`
- `Needs verification`

when appropriate.

### 12. Self-Check Before Completion

Confirm:

- no invented behavior;
- no unauthorized implementation mechanism;
- no missing source traceability;
- no missing exact design artifact;
- no generic adaptive language;
- no missing localization/RTL outcome;
- no missing accessibility outcome;
- no hidden owner assumption;
- no candidate/deferred scope promotion;
- no false evidence claim;
- no approval claim;
- no implementation authorization claim.

## Stop Conditions

Stop and return a blocked verdict when:

- product authorities materially conflict;
- feature input contradicts approved product behavior;
- exact design artifacts materially conflict with approved screen contracts;
- a required owner decision changes scope or core behavior;
- required authority is missing;
- the requested contract would require inventing behavior.

Do not stop merely because implementation readiness is blocked. A contract can be ready for owner approval while production implementation remains blocked.

## Completion Report

Report:

- files read;
- file created or updated;
- requirements added;
- clarifications resolved from authority;
- remaining owner decisions;
- unsupported artifact content excluded;
- contradictions found;
- authoring verdict;
- confirmation that no production code, technical plan, tasks, schema, provider, or persistence mechanism was created.

## Feature-Input Journey Integrity Rules (v1.7)

Before authoring observable states or transitions, treat the reviewed Feature Input as the primary bounded statement of journey intent:

- Build an invocation-context matrix from `Origin / Entry Context → Trigger → Destination / Mode → Success Return → Cancel/Back Return → Failure Behavior`.
- Preserve distinct modes when one reusable visual screen is entered from multiple origins. Never collapse a search-review form, historical edit form, onboarding setup form, or normal-management form into one behavioral state merely because they share UI.
- For every durable mutation, copy the product-declared affected screens/consumers and required timing into the contract as observable cross-screen consistency requirements. Do not invent the implementation propagation mechanism in the contract.
- Author critical end-to-end acceptance journeys that include starting context, durable result, affected-consumer result, and final destination.
- Preserve lifecycle/re-entry expectations: an inactive or recreated consumer that is required to show current committed state must do so even if it did not observe the original mutation event.
- If the Feature Input omits a material success/cancel/failure destination, affected consumer, or re-entry expectation and no higher authority answers it, mark `Needs owner decision`; do not guess.
- State-transition matrices must be checked against the invocation-context matrix. A transition may not route a reusable screen into another mode's return semantics.

The Feature Input states **what** the journey must do. The contract formalizes that behavior. Implementation mechanisms belong in the implementation plan.

## Complexity Tier and Cross-Feature Coherence Rules (v1.7)
- Read `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md` and the feature classification record before applying depth/sizing rules.
- If `feature-complexity-classification` was not executed, or its result is missing/invalid/stale, treat the feature as `COMPLEX` and record `DEFAULTED_TO_COMPLEX`. Never infer a lower tier.
- Use one canonical lifecycle/template family; tier changes mandatory depth and specialist gates, not authority order.
- For every durable mutation, identify all affected consumers/read models and the explicit propagation/invalidation/observation mechanism. A locally successful write with a stale dependent screen is incomplete.
- For actions reachable from multiple entry contexts, define and verify origin-sensitive success/cancel/failure destinations. Normal management must not accidentally execute onboarding/setup completion semantics.
- Any user-committable vertical slice must prove `commit → authoritative state → affected consumer refresh → correct destination` before bounded closure when that journey is in the task's scope. Do not defer all such proof to final convergence.

