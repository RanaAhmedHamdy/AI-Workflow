# <Feature Name> — Feature Input

- Feature ID:
- Accountable product owner:
- Status: Draft / Approved for contract authoring
- Product authority:
- Design authority:

## Input provenance and clarification record

Record how this bounded input was assembled so downstream authoring can distinguish authority from facilitation.

- PRD / product-authority references:
- Owner decision references:
- Design/product references used:
- Clarification method or skill used, if any:
- Clarification output/session reference, if retained:
- Last owner review date:

A GrillMe-style or other clarification skill may be used to expose missing behavior and structure owner questions. Its output is not product authority by itself. Material answers must be grounded in approved authority or explicit owner decisions, then normalized into this Feature Input before contract authoring.

## Purpose and user outcome

Describe the user-visible outcome and why the feature exists. Keep this product-facing and implementation-neutral.

## Actors and permissions

List user/persona roles and any product-authorized permission or entitlement differences.

## In-scope behavior

Describe the behavior that belongs to this feature now.

## Explicit exclusions and later features

List behavior that must not be pulled into this feature.

## Product rules and data semantics

Define product rules, terminology, durability expectations, historical semantics, validation meaning, destructive behavior, and other observable invariants. Do not prescribe repositories, databases, framework types, or other implementation mechanisms unless product authority explicitly requires them.

## Invocation contexts and navigation outcomes

For every action that opens another screen, sheet, flow, or reusable surface, define the originating context and what must happen on success, cancel/back, and failure.

| Origin / Entry Context | Trigger | Destination / Mode | Success Return / Destination | Cancel / Back Return | Failure Behavior |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

Rules:
- Do not use ambiguous destinations such as `Home / Settings` or `previous screen` when the exact product context is known.
- If the same visual screen is reused from multiple origins, record each origin/mode separately. Shared visuals do not imply shared save/cancel semantics.
- Normal management, onboarding/setup, deep-link, restored, and modal entry contexts must be distinguished whenever their post-action behavior differs.
- If an outcome is genuinely unknown, mark `Needs owner decision`; do not invent it during contract authoring.

## Durable mutations and cross-screen effects

For every user action that changes durable product state, identify the product-visible consumers that must become consistent.

| Durable Mutation | User-Visible Source | Affected Screens / Consumers | Expected Observable Change | Required Timing |
|---|---|---|---|---|
|  |  |  |  |  |

Describe product expectations, not propagation mechanisms. Example: `Saving a meal updates Home consumed totals immediately without manual refresh or app relaunch.`

## Critical end-to-end user journeys

Define the vertical journeys whose correctness matters as a complete flow rather than as isolated screens.

### Journey A — <Name>

**Given** ...  
**When** ...  
**Then** the durable result is ...  
**And** affected consumers show ...  
**And** the user ends at ...

Add further journeys as needed. Include starting context, action, durable result, affected-screen result, final destination, and material cancel/failure behavior.

## Lifecycle and re-entry expectations

State the product expectation when an affected consumer is:

- currently visible when the mutation occurs;
- entered after the mutation occurred;
- recreated after view/state-holder destruction;
- restored after app process relaunch when durability applies;
- restored after device reboot when explicitly required.

A consumer must not depend solely on having been visible when the mutation happened. If a later entry/recreation must show the latest committed state, state that explicitly.

## Required screens and design artifacts

For each required screen or reusable surface, cite the governing screen contract/design artifact when available. Note material modes/states that share the same visual surface but have different product behavior.

## Supported platforms, form factors, locales, and accessibility expectations

## Privacy, regulated, and protected-boundary implications

## Complexity and risk signals

Mark every applicable signal. These are inputs to the platform `feature-complexity-classification` skill; they do **not** assign the tier themselves.

- [ ] Durable persistence mutation
- [ ] Schema or data migration
- [ ] Multiple screens/features consume changed data
- [ ] Multiple navigation / invocation contexts
- [ ] Destructive operation
- [ ] Historical-data invariant or correction semantics
- [ ] Concurrency, idempotency, or duplicate-prevention requirement
- [ ] Date/timezone/DST/manual-clock/reconciliation behavior
- [ ] Offline, relaunch, or reboot durability requirement
- [ ] Privacy/security/protected platform boundary
- [ ] External platform capability / permission
- [ ] Materially complex adaptive/accessibility behavior
- [ ] Other high-risk signal: <describe>

If the classification skill is not executed, cannot complete, or its result is missing/invalid/stale, downstream work MUST default to `COMPLEX` and record `DEFAULTED_TO_COMPLEX`.

## Known assumptions and open questions

Separate confirmed authority from assumptions. Mark unresolved observable product behavior as `Needs owner decision` rather than allowing downstream artifacts to invent it.

This input does not approve a feature contract, assign implementation mechanisms, or authorize implementation.
