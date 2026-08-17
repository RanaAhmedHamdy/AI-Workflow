# Architecture Templates — Operational Guide

Use these templates during repository bootstrap and whenever accepted architecture changes.

## Recommended order

1. Start from approved PRD/product authority, approved design authority where available, repository policy, and verified repository facts.
2. Create the platform `ARCHITECTURE_SPINE.md` from the iOS or Android template. Record unresolved decisions explicitly.
3. Create proposed `ADR-*.md` files for hard-to-reverse, protected-boundary, or cross-feature choices. Agents propose; the accountable owner decides.
4. After owner ADR review, synchronize accepted decisions: `ADRs → Architecture Spine → cross-feature architecture coverage → implementation readiness gate → AI_CONTEXT.md → decision register`.
5. Use `architecture-coverage-review` when the coverage matrix must be reconciled against decisions, implementation, or evidence.
6. Run the readiness gate for a bounded feature only after its contract, plan, and tasks have passed their required reviews/approvals. A gate PASS means eligible for explicit owner implementation authorization only.

## Artifact roles

- `ARCHITECTURE_SPINE.<platform>.template.md` — integrated current system architecture and cross-feature boundaries.
- `ADR.template.md` — durable record for one significant technical decision, alternatives, consequences, migration/adoption, and required evidence.
- `cross-feature-architecture-coverage.template.md` — independent tracking of Decision, Implementation, and Evidence coverage. It does not replace the spine or ADRs.
- `IMPLEMENTATION_READINESS_GATE.template.md` — reusable project-level gate definition used before bounded implementation authorization.

## When coverage is needed

For a non-trivial greenfield app, create the coverage matrix during architecture bootstrap. For a very small project it may begin mostly empty, `Not applicable`, or `Deferred with conditions`, but those statuses must be justified rather than inferred from silence. Keep it current when cross-feature architecture, implementation, or evidence changes.

## Stop rules

- An unresolved architecture choice is not permission for an agent to choose.
- An accepted ADR does not authorize implementation.
- A contradiction among ADRs, the spine, coverage, readiness, routing, or the decision register blocks affected work.
- Decision coverage, implementation coverage, and evidence coverage are separate claims.
