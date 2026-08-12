# Skill: Feature Complexity Classification v1

## Purpose
Classify one bounded Android feature as SMALL, STANDARD, or COMPLEX before contract authoring so governance depth scales to actual risk without creating duplicate template families. Classification does not authorize planning or implementation.

## Default Safety Rule
If this skill is not run, cannot complete, or its result is missing/invalid/stale, downstream authoring/review/implementation skills MUST use `COMPLEX` and record `DEFAULTED_TO_COMPLEX`. Never silently assume SMALL or STANDARD.

## Required Inputs
Read the feature input, repository policy, product authority, feature map/dependencies, architecture spine/ADRs, design authority, known persistence/lifecycle/capability boundaries, and `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`.

## Classification Procedure
1. Bound the requested feature and list directly affected screens, modules/features, durable stores, navigation entry contexts, and external/platform boundaries.
2. Score all +1 and +2 signals from the tier policy.
3. Evaluate every hard COMPLEX trigger.
4. Assign `COMPLEX` immediately when any hard trigger applies. Otherwise use the score bands: `0–2 SMALL`, `3–6 STANDARD`, `7+ COMPLEX`.
5. Promote upward whenever evidence is insufficient to justify a lower tier. Never downgrade by assumption.
6. Record the exact signals, score, hard triggers, and specialist readiness skills that become applicable.
7. Do not generate implementation tasks, estimates, code, or authorization.

## Required Output
Return a classification record containing:
- `Classification status: EXECUTED`
- `Feature tier: SMALL | STANDARD | COMPLEX`
- `Score`
- `Triggered signals`
- `Hard COMPLEX triggers`
- `Required specialist skills/gates`
- `Rationale`

## Stop Conditions
If the feature boundary is materially unresolved or authority conflicts prevent reliable scoring, return `NEEDS OWNER DECISION` and instruct downstream skills to use `COMPLEX` until resolved.
