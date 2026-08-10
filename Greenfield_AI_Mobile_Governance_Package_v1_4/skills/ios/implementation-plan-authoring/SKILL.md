# Skill: Implementation Plan Authoring v1

## Purpose
Create an architecture-aware, design-traceable, evidence-ready implementation plan from an owner-approved feature contract. Do not create production code or tasks.

## Preconditions
Verify:
- feature contract is owner-approved;
- product clarifications are closed;
- applicable ADRs are accepted or explicitly provisional;
- required feasibility spikes passed independent verification;
- exact design authority exists.

If not, return a blocked verdict.

## Required Inputs
Read repository policy, context router, playbook, decision register, target contract, feature input, feature map, architecture spine, applicable ADRs, readiness gate, accepted feasibility evidence, design authority, screen contracts, artifact index, design system, information architecture, and localization/accessibility authority.

## Required Output
Create `docs/features/<feature-id>/IMPLEMENTATION_PLAN.md` using `.templates/mobile/IMPLEMENTATION_PLAN_TEMPLATE.md`.

Return one:
- `READY FOR PLAN REVIEW`
- `BLOCKED BY TECHNICAL DECISION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

## Core Rules
1. Every planned component must trace to an approved contract requirement.
2. Do not add later-feature behavior.
3. Accepted ADRs control technical choices.
4. Cite exact screen contracts and compact/wide artifact IDs.
5. Separate domain, persistence, presentation, navigation, and host ownership.
6. Leaf views must not own persistence/network side effects.
7. Persistence design must name store ownership, transactions, rollback, idempotency, migration, date attribution, test isolation, protection, and sensitive-store boundaries.
8. Do not rely on uniqueness alone as product idempotency.
9. Do not overclaim forensic deletion.
10. Adaptive design must cover compact, wide, reduced width, keyboard, safe areas, overflow, and state preservation without inventing content.
11. Localization and RTL are part of initial implementation; prohibit hardcoded user-facing and accessibility strings.
12. Accessibility requires runtime verification, not static-artifact claims.
13. Match each requirement to sufficient test/evidence layers.
14. Define implementation order only; do not generate tasks, estimates, assignments, or code.
15. Do not claim implementation authorization.

### Verification Matrix and Current-State Integrity

- Define a compact verification matrix inside `IMPLEMENTATION_PLAN.md` using stable unique IDs such as `VM-001`.
- Each applicable row must identify the approved requirement/claim, executable scenario, environment/destination, required preconditions, expected observable result, evidence path, and verification method or known limitation.
- Runtime-only claims must map to runtime-capable evidence. Do not create a separate verification artifact solely for this matrix.
- Treat `VM-*` rows as planned verification definitions, not a second lifecycle state machine; do not add per-row `READY`/`PASS` workflow statuses during plan authoring.
- Keep current lifecycle/status/authorization truth in one canonical status block. Historical authoring/review verdicts may remain only when clearly labeled as stage-specific history. Never emit incompatible current-state assertions in the same artifact.

## Mandatory Sections
Authority/status; scope/exclusions; assumptions; traceability; architecture; modules; domain; persistence; presentation state; navigation; screen mapping; adaptive UI; localization/RTL; accessibility; error/recovery/offline/cancellation; tests; evidence; dependency order; risks; unresolved decisions; readiness; prohibited patterns; documentation impact.

## Stop Conditions
Stop when the contract is not owner-approved, product behavior remains unresolved, ADRs conflict, required spike evidence is not independently verified, exact design authority is missing, or planning would require invented behavior.

## Completion Report
Report files read, plan path, requirements mapped, modules proposed, exact artifacts mapped, ADRs applied, risks, unresolved decisions, readiness implications, verdict, and confirmation that no code or tasks were created.
