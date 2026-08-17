# Feature Complexity Tier Policy

**Version:** 1.1  
**Applies to:** Native iOS and native Android feature delivery

## Purpose

Scale governance depth to feature risk without creating separate Small/Standard/Complex template families. One lifecycle and one template set remain canonical. Tier controls which sections, gates, specialist skills, task depth, and evidence obligations are mandatory.

## Default rule

If the platform `feature-complexity-classification` skill was not executed for the current feature, or its output is missing/invalid/stale, the feature MUST be treated as **COMPLEX**. Never infer SMALL or STANDARD from intuition, task count, or apparent UI size.

## Tiers

| Tier | Typical shape | Baseline governance | Typical task guidance |
|---|---|---|---|
| SMALL | Bounded low-risk change, usually 1–2 screens, no migration/protected lifecycle/cross-feature durable propagation | Core contract, compact plan, focused tasks and verification | 2–5 coherent tasks |
| STANDARD | Multiple states/screens or ordinary durable persistence/navigation, bounded cross-feature integration | Core + state/navigation/persistence/cross-feature propagation + runtime UI checks | 5–10 coherent tasks |
| COMPLEX | Migration, historical integrity, protected boundaries, concurrency/idempotency, date/time lifecycle, multiple entry contexts/consumers, or similarly high-risk behavior | Full applicable governance, specialist readiness, vertical integration and runtime convergence | 10–20+ tasks when justified |

Task counts are guidance, never acceptance criteria. Do not split work merely to hit a range.

## Feature-input signal handling

The Feature Input may declare complexity/risk signals to make product risk visible before classification. Those declarations are evidence inputs only. The platform classifier must verify them against repository/product/architecture context and may discover additional signals. Unchecked, blank, legacy, or incomplete Feature Input signal lists MUST NOT be interpreted as absence of risk or as justification for SMALL/STANDARD. If the classifier is not executed, the default-to-COMPLEX rule applies.

## Scoring signals

Add one point for each applicable signal: additional feature consumer, multiple navigation entry contexts, durable persistence mutation, destructive operation, offline/relaunch requirement, materially complex adaptive/accessibility UI.

Add two points for each applicable signal: schema migration, historical-data invariant, concurrency/idempotency correctness, date/timezone/DST lifecycle behavior, cross-feature atomic/coherent mutation, privacy/security/protected boundary.

Default score interpretation: `0–2 SMALL`, `3–6 STANDARD`, `7+ COMPLEX`.

## Hard COMPLEX triggers

Any of the following makes the feature COMPLEX regardless of score unless an explicit owner-approved exception exists:

- persistence/schema migration;
- historical data immutability or destructive historical mutation;
- timezone/DST/manual-clock/date reconciliation;
- concurrency/idempotency correctness across durable mutations;
- payment/financial transaction integrity;
- sensitive privacy/security/protected platform boundary;
- cross-feature atomic mutation where stale consumers can produce incorrect user-visible state.

## Risk-triggered specialist skills

Tier sets baseline rigor. Specialist skills remain concern-triggered. A SMALL or STANDARD candidate with a hard trigger is promoted to COMPLEX. UI, persistence/migration, localization/RTL, accessibility/adaptive, concurrency, permissions/privacy, lifecycle/runtime-evidence, and protected-boundary skills run whenever their concern applies.

## Required classification record

Each feature contract must record:

- classification status: `EXECUTED` or `DEFAULTED_TO_COMPLEX`;
- resulting tier;
- score and triggered signals when executed;
- hard triggers;
- classifier skill path/version;
- owner-approved exception, if any.

Classification never grants implementation authorization.


## Automatic classification routing

Contract authoring must attempt the platform `feature-complexity-classification` when no fresh valid classification is present. If the classifier cannot run or cannot safely classify, record `DEFAULTED_TO_COMPLEX` and continue under COMPLEX obligations rather than asking the agent to infer a lower tier.

The classifier uses Feature Input risk signals as inputs, not as a self-assigned result. Specialist gates remain risk-triggered; a tier does not require running every specialist skill.
