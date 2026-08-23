# Architecture Bootstrap — Operational Guide

[← Greenfield start here](../../README.md) · [Optional Design Authority](../design/README.md) · [Feature Delivery](../mobile/README.md)

Use this workflow after the repository has an approved PRD/product authority and governance is installed. If approved external designs exist and affect architecture, establish their repository authority first.

**Goal:** reach `READY FOR BOUNDED FEATURE INTAKE`. This is **not** implementation authorization and is **not** `IMPLEMENTATION_READINESS_GATE = PASS`.

## Quick start

| Step | Goal                           | What you do / run                                                                                  | Main result                                                                  |
| ---- | ------------------------------ | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| 0    | Confirm inputs                 | Approved PRD, governance, native project/repository, and approved Design Authority when applicable | Bootstrap inputs ready                                                       |
| 1    | Establish initial architecture | Run `architecture-bootstrap` in `INITIAL` mode                                                     | Draft Spine + verified facts + proposed ADRs + owner questions/blockers      |
| 2    | Make material owner decisions  | Answer the surfaced questions; use `adr-lifecycle-governance` for ADR status transitions           | Accepted/amended/provisional/deferred/rejected decisions                     |
| 3    | Reconcile and continue         | Run `architecture-bootstrap` in `RESUME` mode                                                      | Synchronized Spine/ADRs/coverage/Decision Register + next verdict            |
| 4    | Resolve only reported blockers | Owner decision or bounded feasibility spike, then run `RESUME` again                               | Blocker closed or next explicit blocker                                      |
| 5    | Hand off to feature delivery   | Stop when verdict is `READY FOR BOUNDED FEATURE INTAKE`                                            | Select one bounded feature and start [Feature Delivery](../mobile/README.md) |

For the normal happy path, you do **not** need to invoke architecture coverage, documentation consistency, project-structure readiness, or specialist architecture skills manually. `architecture-bootstrap` orchestrates the applicable checks and should call only what the current bootstrap needs.

## Step 0 — Confirm prerequisites

Before running the skill, confirm:

- approved PRD/product authority exists;
- `AGENTS.md` and applicable governance/policy modules are installed;
- `AI_CONTEXT.md` and the Decision Register exist;
- the native project/repository exists when project facts are needed;
- approved Design Authority exists when external designs are intended to constrain architecture.

If completed designs exist but are not yet registered as repository authority, use the [Design Authority workflow](../design/README.md) first.

## Step 1 — Run architecture bootstrap INITIAL

Use the platform skill:

- [iOS `architecture-bootstrap`](../../skills/ios/architecture-bootstrap/SKILL.md)
- [Android `architecture-bootstrap`](../../skills/android/architecture-bootstrap/SKILL.md)

Recommended prompt:

```text
Run architecture-bootstrap in INITIAL mode for this repository.

Use current approved product authority, approved design authority when applicable,
repository governance, and verified repository facts.

Establish the Draft Architecture Spine, identify unresolved material architecture
decisions, and propose only ADRs that genuinely need durable independent rationale.

Do not convert repository/project evidence into owner approval.
Do not accept ADRs for me.
Do not implement feature code.

Continue until you either:
1. need a material owner decision,
2. need bounded feasibility evidence,
3. find an authority contradiction / missing required fact, or
4. reach READY FOR BOUNDED FEATURE INTAKE.
```

Expected output is concise: verified facts, proposed/material decisions, proposed ADRs when justified, blockers/questions for the owner, and the current bootstrap verdict.

## Step 2 — Answer owner decisions

Answer only the material questions the skill surfaced. You do not need to manually edit every architecture document first.

Example:

```text
I approve ADR-IOS-001 as proposed.
Accept ADR-IOS-005 provisionally; implementation depending on it remains blocked
until the named persistence spike passes.
For navigation, follow the approved Design Authority and do not invent a different
screen hierarchy.
Defer the widget decision until a feature actually requires it.
```

Then apply the decisions through `adr-lifecycle-governance` when an ADR lifecycle state changes. The bootstrap skill may invoke that procedure, but the owner decision itself must remain explicit.

Supported lifecycle outcomes include:

- `Accepted`
- `Accepted with amendments`
- `Accepted provisionally`
- `Deferred`
- `Rejected`
- `Superseded`

A repository fact, generated project default, or agent recommendation is never owner approval by itself.

## Step 3 — Run architecture bootstrap RESUME

Recommended prompt:

```text
Apply my explicit architecture decisions using adr-lifecycle-governance where needed,
then run architecture-bootstrap in RESUME mode.

Synchronize only affected canonical artifacts, run the applicable bootstrap coverage
and documentation-consistency checks, and continue until another material owner
choice/evidence blocker is required or the repository reaches
READY FOR BOUNDED FEATURE INTAKE.

Do not implement feature code and do not claim Implementation Readiness Gate PASS.
```

`RESUME` should normally handle:

```text
new owner decisions
        ↓
ADR lifecycle transitions where applicable
        ↓
Architecture Spine synchronization
        ↓
affected architecture coverage / Decision Register / routing updates
        ↓
bootstrap coverage + documentation consistency
        ↓
next bootstrap verdict
```

Do not mechanically modify every authority document for every ADR. Update only artifacts whose current decision, routing, gate requirement, or coverage actually changed.

## Step 4 — Resolve only reported blockers

Most projects should not perform every specialist procedure during bootstrap. Follow only the blocker returned by the skill.

### If an owner decision is required

Answer it explicitly, then run `RESUME` again.

### If feasibility evidence is required

Run the named bounded spike only. A spike proves a technical question; it is not feature implementation.

Record:

- the question being proved;
- pass/fail criteria;
- exact evidence produced;
- resulting recommendation or remaining uncertainty.

Then return to `architecture-bootstrap RESUME` so the owner can accept, amend, keep provisional, defer, or reject the affected decision.

### If authority contradicts

Resolve the contradiction in current authority before continuing. Historical text may remain only when clearly marked superseded/historical.

### If facts need verification

Inspect only the missing repository/tool/platform facts. Existing settings remain evidence, not automatic approval.

## Step 5 — Stop at architecture bootstrap readiness

Valid bootstrap verdicts are:

- `READY FOR BOUNDED FEATURE INTAKE`
- `READY WITH EXPLICIT LIMITATIONS`
- `BLOCKED — OWNER DECISION`
- `BLOCKED — FEASIBILITY EVIDENCE`
- `BLOCKED — AUTHORITY CONTRADICTION`
- `NEEDS VERIFICATION`

`READY FOR BOUNDED FEATURE INTAKE` means the repository has enough accepted cross-feature architecture for the intended first bounded slice and no current contradiction blocks that slice. Explicitly deferred decisions may remain when they do not affect it.

It does **not** approve a feature, authorize planning, authorize implementation, accept a feature, or authorize release.

**Next:** select one bounded feature and continue with [Feature Delivery](../mobile/README.md).

---

# How architecture-bootstrap works internally

The sections below are reference material. A new user does not normally execute them one-by-one.

## Authority categories

Keep these distinct:

- **Verified repository fact** — observed project/tool/configuration evidence.
- **Architecture-driving constraint** — approved product/design/governance requirement the architecture must satisfy.
- **Proposal** — agent-recommended technical choice.
- **Owner decision** — explicit accept/amend/defer/reject direction.
- **Canonical architecture** — accepted decision synchronized into the ADR/Spine.
- **Implementation evidence** — proof that an accepted/provisional decision actually works.

## Internal bootstrap sequence

`architecture-bootstrap` should perform the following only as needed:

1. Gather relevant repository evidence without treating generated defaults as approval.
2. Extract architecture-driving constraints from approved authority.
3. Seed/update the Draft Architecture Spine.
4. Classify unresolved choices as routine, Spine-level, ADR candidate, feasibility-required, or owner clarification.
5. Draft only significant ADR proposals.
6. Stop for explicit owner architecture decisions where required.
7. Route provisional decisions to bounded feasibility evidence when proof is genuinely needed.
8. Integrate accepted decisions into the canonical Spine.
9. Synchronize only affected architecture/coverage/Decision Register/routing/gate artifacts.
10. Run `architecture-coverage-review` in `BOOTSTRAP` mode.
11. Run `documentation-consistency-review`.
12. Return the architecture-bootstrap verdict.

## When an ADR is warranted

A choice is normally an ADR candidate when one or more apply:

- protected boundary;
- cross-feature or system-wide impact;
- reusable architecture invariant or technical policy;
- material constraint on future implementation choices;
- meaningful alternatives/tradeoffs worth preserving;
- substantial reversal, migration, security, privacy, release, or operational cost.

Do not create one ADR per Spine heading.

## Accepted provisionally

Use `Accepted provisionally` when the owner approves a direction but dependent implementation must remain blocked until named feasibility/evidence criteria pass. The ADR must state the blocker and exit criteria.

## Coverage during bootstrap

`cross-feature-architecture-coverage.md` keeps three independent states:

- **Decision** — has the architecture been decided?
- **Implementation** — has the accepted decision been implemented?
- **Evidence** — has the behavior been proved?

During bootstrap, `Implementation: Not started` and `Evidence: None` can be completely correct while decision coverage is sufficient. Never infer `Not applicable` merely because a concern is blank.

## Implementation readiness is later

Architecture bootstrap may update the reusable `IMPLEMENTATION_READINESS_GATE.md` definition when an accepted architecture decision changes future requirements, but it must **not execute or PASS that feature gate**.

The Implementation Readiness Gate is evaluated later, after the bounded feature has an owner-approved Feature Contract, Implementation Plan, and Implementation Tasks.

## Artifact roles

- `ARCHITECTURE_SPINE.<platform>.template.md` — integrated current cross-feature architecture.
- `ADR.template.md` — durable record for one significant decision and its lifecycle/history.
- `cross-feature-architecture-coverage.template.md` — Decision / Implementation / Evidence coverage.
- `IMPLEMENTATION_READINESS_GATE.template.md` — later feature/slice eligibility gate; PASS still requires explicit owner implementation authorization.

## Supporting skills

Normal bootstrap is orchestrated by `architecture-bootstrap`. Supporting skills are called only when applicable:

- `adr-lifecycle-governance`
- platform architecture readiness
- project-structure readiness in evidence-only/bootstrap mode
- `architecture-coverage-review` in bootstrap mode
- `documentation-consistency-review`
- specialist platform readiness skills for decisions/spikes that genuinely need them

## Efficiency rules

- Read only active authority and architecture concerns relevant to the current decision batch.
- Batch material owner questions instead of stopping for every small unknown.
- Reuse verified repository evidence until relevant files/settings change.
- Synchronize once per coherent decision batch where safe.
- Do not run feature-only readiness/evidence procedures before Feature Input/Contract/Plan/Tasks exist.
