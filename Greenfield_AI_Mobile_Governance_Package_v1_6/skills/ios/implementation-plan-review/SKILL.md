# Skill: Implementation Plan Review v1

## Purpose
Independently review an implementation plan for contract fidelity, architecture conformance, exact design traceability, persistence correctness, adaptive UI, localization, accessibility, testing, evidence, and readiness honesty.

## Verdicts
- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

PASS means ready for owner plan approval only.

## Required Inputs
Read the plan, owner-approved contract, feature input, feature map, decision register, architecture spine, applicable ADRs, feasibility evidence, readiness gate, design authority, screen contracts, artifact index, design system, information architecture, policy, and context router.

## Mandatory Review
1. Trace every module, state holder, repository, route, screen, test, and evidence item to contract requirements.
2. Fail untraced components, later-feature behavior, invented rules, or omitted requirements.
3. Verify dependency direction, thin host, domain/presentation/persistence separation, no persistence entities in views, no side effects in view bodies, accepted concurrency/navigation/storage decisions, and no unapproved packages.
4. Verify persistence store ownership, disk-backed behavior, transaction boundaries, rollback, idempotency, migration, date attribution, historical stability, test isolation, protection, and sensitive-data separation.
5. Fail uniqueness-only deduplication without logical idempotency identity.
6. Verify exact compact/wide artifacts and unsupported-content exclusions.
7. Verify compact, wide, reduced-width, keyboard, safe-area, overflow, and reflow plans.
8. Verify String Catalog/resource ownership, semantic error wording, locale-aware formatting, Arabic RTL, accessibility-string localization, and hardcoded-string scans.
9. Verify runtime plans for VoiceOver, focus, Dynamic Type, Bold Text, Differentiate Without Color, Button Shapes, Reduce Transparency, Increased Contrast, Reduce Motion, touch targets, and errors.
10. Verify evidence layers can prove claims; reject UI-only arithmetic, screenshot-only durability, static-only accessibility, missing `.xcresult`, destinations, paths, or limitations.
11. Fail task IDs, estimates, assignments, file-by-file checklists, production code, or generated migrations/schemas.
12. Verify blocked gates are reported honestly and implementation is not authorized.

### Verification-Matrix Traceability and State Consistency

- Verify unique stable `VM-*` IDs cover every applicable runtime-only claim with an executable scenario.
- Verify every row traces to approved authority and does not invent behavior.
- Verify environment/destination, preconditions, expected observable result, evidence path, and method/limitation are concrete enough to execute.
- Search the complete artifact for lifecycle/status/approval/readiness/authorization assertions. If two assertions both claim to describe the current state and conflict, return a blocking finding. Historical stage verdicts are allowed only when clearly labeled as historical/stage-specific.

## Finding Format
Finding ID; severity; plan section; contract requirement; authority; problem; correction; verdict impact.

## Pass Criteria
All contract requirements mapped; no drift; ADRs applied; persistence matches audited evidence; design artifacts mapped; adaptive/localization/accessibility explicit; test/evidence sufficient; no tasks/code; unresolved decisions visible; readiness honest.

## Final Report
Verdict, traceability coverage, blocking findings, architecture drift, persistence findings, design/adaptive/localization/accessibility/test gaps, unresolved decisions, readiness implications, exact sections to revise, and statement that PASS means ready for owner plan approval only.

## Complexity Tier and Cross-Feature Coherence Rules (v1.6)
- Read `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md` and the feature classification record before applying depth/sizing rules.
- If `feature-complexity-classification` was not executed, or its result is missing/invalid/stale, treat the feature as `COMPLEX` and record `DEFAULTED_TO_COMPLEX`. Never infer a lower tier.
- Use one canonical lifecycle/template family; tier changes mandatory depth and specialist gates, not authority order.
- For every durable mutation, identify all affected consumers/read models and the explicit propagation/invalidation/observation mechanism. A locally successful write with a stale dependent screen is incomplete.
- For actions reachable from multiple entry contexts, define and verify origin-sensitive success/cancel/failure destinations. Normal management must not accidentally execute onboarding/setup completion semantics.
- Any user-committable vertical slice must prove `commit → authoritative state → affected consumer refresh → correct destination` before bounded closure when that journey is in the task's scope. Do not defer all such proof to final convergence.

