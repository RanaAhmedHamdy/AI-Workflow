# Feature Delivery Invariants

These rules are shared by iOS and Android feature delivery. Skills reference this policy instead of duplicating the same instructions. They are mandatory whenever the routed lifecycle stage touches the concern.

## 1. Complexity

- Run the platform `feature-complexity-classification` before contract authoring when no fresh classification exists.
- Classification uses Feature Input risk signals plus verified repository/architecture context; the input does not self-assign a tier.
- If classification cannot run, fails, or is missing/invalid/stale, record `DEFAULTED_TO_COMPLEX` and apply `COMPLEX`. Never infer a lower tier.
- Use one lifecycle/template family. Tier changes mandatory depth and specialist gates, not authority order.

## 2. Journey and state coherence

- Preserve distinct invocation modes when one visual screen is reused from different origins.
- Every multi-entry action must have explicit origin-sensitive success, cancel/back, and failure destinations. Normal management must never accidentally execute onboarding/setup completion semantics.
- State-transition matrices must agree with the invocation-context matrix.

## 3. Mutation-to-consumer coherence

For every durable mutation identify:

- authoritative write/source of truth;
- all affected consumers/read models;
- active-consumer update/invalidation/observation mechanism;
- inactive/recreated-consumer catch-up behavior on later entry;
- timing expectation and stale-state risk;
- executable verification.

A locally successful write, event-only refresh path, or correct local screen that can leave another dependent surface stale is incomplete.

## 4. Vertical closure

When a user-committable journey is inside a bounded task, task closure must prove the applicable chain:

`commit → authoritative state → affected consumer refresh/catch-up → correct origin-sensitive destination`

Do not defer all vertical proof to final convergence.

## 5. Evidence economy without weaker proof

Evidence is executed at the earliest stage where it is necessary, but not earlier:

- `TASK-CLOSURE`: proves the bounded task's immediate behavior/architecture.
- `FEATURE-CONVERGENCE`: proves cross-task integration/regression after assembly.
- `FINAL-READINESS`: expensive platform/device/security/privacy/performance/manual-runtime evidence required before acceptance/release, normally not before ordinary task closure.

Prefer the cheapest deterministic evidence that proves the claim. One valid artifact may satisfy multiple verification rows when it actually covers them. Never rerun solely to manufacture unique artifact filenames.

Manual validation is appropriate for subjective or service/device-only properties such as final visual fidelity, screen-reader flow, alternate-input ergonomics, representative RTL/adaptive quality, and physical-device reboot. It must not replace deterministic tests for domain rules, navigation destinations, mutation propagation, atomicity, idempotency, or migration correctness.

Use representative risk-based runtime matrices rather than every-screen × every-device × every-locale × every-setting combinations. Add configurations when the feature risk requires them.
