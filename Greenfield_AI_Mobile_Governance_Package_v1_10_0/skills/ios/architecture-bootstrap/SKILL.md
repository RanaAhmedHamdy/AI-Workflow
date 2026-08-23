---
name: architecture-bootstrap
description: "Orchestrates the repository architecture phase from approved product/design authority and verified repository facts through owner-gated ADR decisions, synchronized architecture coverage, and readiness for bounded feature intake. It does not authorize feature implementation."
---

# Architecture Bootstrap

## Purpose

Build or resume the cross-feature architecture baseline without turning repository evidence or agent recommendations into owner approval.

Use this skill before bounded Feature Input begins, or resume it after owner decisions / feasibility evidence arrive.

## Authority model

Keep these categories separate:

- **Verified fact** — repository/tool/design/platform evidence.
- **Constraint** — approved product/design/governance requirement that architecture must satisfy.
- **Proposal** — agent-recommended technical choice.
- **Owner decision** — explicit accept/amend/defer/reject direction.
- **Canonical architecture** — accepted decision synchronized into the current ADR/Spine authority.
- **Implementation evidence** — proof that an accepted/provisional decision works.

A verified project setting is not automatic owner architecture approval.

## Modes

- `INITIAL` — establish the first architecture baseline.
- `RESUME` — continue after owner decisions, amendments, or feasibility evidence.
- `AMENDMENT` — reconcile new owner-approved architecture direction with existing accepted authority.

## Minimal read strategy

Start with `AGENTS.md`, `AI_CONTEXT.md`, approved PRD/product authority, approved design authority when present, decision register, Architecture Spine, architecture coverage, and directly relevant repository facts. Load ADRs/specialist skills only for concerns that are active. Do not exhaustively read feature artifacts that do not yet exist.

## Procedure

1. Verify bootstrap prerequisites and canonical paths.
2. Gather repository facts in evidence-only mode. Record unknowns as `Needs verification`; do not choose from generated defaults.
3. Extract architecture-driving constraints from approved product/design/governance authority. Do not translate product behavior directly into mechanisms.
4. Seed/update `ARCHITECTURE_SPINE.md` as `Draft`, distinguishing accepted decisions, proposals, unresolved choices, and justified non-applicability.
5. Classify unresolved choices as:
   - derivable/routine;
   - Spine-level decision;
   - ADR candidate;
   - feasibility evidence required;
   - owner clarification required.
6. Treat a choice as an ADR candidate when it crosses a protected boundary, affects multiple features/system-wide behavior, establishes a reusable invariant/policy, materially constrains future implementation, has meaningful alternatives/tradeoffs, or is expensive to reverse/migrate.
7. Draft ADR candidates as `Proposed`. Never promote them without explicit owner authority.
8. Stop for owner decisions where required. Use `adr-lifecycle-governance` for status transitions.
9. For provisional decisions, run only the bounded feasibility spike/evidence required by the owner-approved exit criteria; a spike is not feature implementation.
10. Synchronize every accepted/amended decision into all **affected** canonical artifacts. Reconcile at minimum the ADR, Spine, coverage matrix, and Decision Register; update readiness-gate definitions, `AI_CONTEXT.md`, policies, feature docs, or design docs only when their content/routing/requirements actually change.
11. Run `architecture-coverage-review` in `BOOTSTRAP` mode and `documentation-consistency-review`.
12. Return the architecture-bootstrap readiness verdict below.

## Architecture-bootstrap readiness verdicts

- `READY FOR BOUNDED FEATURE INTAKE`
- `READY WITH EXPLICIT LIMITATIONS`
- `BLOCKED — OWNER DECISION`
- `BLOCKED — FEASIBILITY EVIDENCE`
- `BLOCKED — AUTHORITY CONTRADICTION`
- `NEEDS VERIFICATION`

`READY` requires no current authority contradiction and enough accepted architecture for the intended first bounded slice. Cross-feature decisions not needed by that slice may remain explicitly deferred with conditions.

Implementation and runtime-evidence coverage may honestly remain `Not started` / `None` during bootstrap. That is not a failure when decision coverage is sufficient and blockers are explicit.

## Important separation

Do **not** run the feature `IMPLEMENTATION_READINESS_GATE` to claim PASS during architecture bootstrap. That gate requires an approved Feature Contract, Plan, and Tasks. Architecture bootstrap may update the reusable gate definition when architecture changes its requirements, but cannot pass the gate before feature artifacts exist.

Architecture bootstrap readiness does not approve a feature, authorize planning, authorize implementation, establish feature acceptance, or authorize release.

## Efficiency

- Read only active authority and active ADR concerns.
- Reuse current verified facts; do not rerun unchanged discovery solely for ceremony.
- Prefer one synchronization pass after owner decisions rather than editing the same authority after every question.
- Stop at the first material owner/feasibility blocker instead of generating speculative downstream documents.
