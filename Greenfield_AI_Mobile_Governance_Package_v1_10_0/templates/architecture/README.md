# Architecture Templates — Operational Guide

Use this guide to move from approved product/design authority and verified repository facts to a synchronized architecture baseline that is **ready for bounded feature intake**. Feature implementation readiness is a later gate.

## Authority categories

Keep these distinct throughout the workflow:

- **Verified repository fact** — observed project/tool/configuration evidence.
- **Architecture-driving constraint** — approved product/design/governance requirement the architecture must satisfy.
- **Proposal** — agent-recommended technical choice.
- **Owner decision** — explicit accept/amend/defer/reject direction.
- **Canonical architecture** — accepted decision synchronized into the ADR/Spine.
- **Implementation evidence** — proof that the accepted/provisional decision works.

A generated project setting, existing package, or current source layout is evidence of the repository state; it is not automatic owner approval.

## Architecture bootstrap — canonical procedure

### Step 0 — Prerequisites

Confirm:

- approved PRD/product authority;
- repository governance (`AGENTS.md` + applicable policy modules);
- `AI_CONTEXT.md` and Decision Register;
- approved design authority when designs exist and affect architecture;
- platform project/repository exists when repository facts are needed.

### Step 1 — Gather repository evidence

Inspect only relevant current project facts: project/module/target structure, toolchain, language mode, deployment/minimum SDK settings, packages/dependencies, schemes/build variants, test structure, existing dependency direction, and other facts needed by architecture.

Use project-structure readiness in **evidence-only/bootstrap mode** where available. Record unknowns as `Needs verification`. Do not convert generated defaults into owner decisions.

### Step 2 — Extract architecture-driving constraints

Read approved product/design/governance authority and extract only constraints with architectural consequences.

Example: `data survives relaunch` implies durable persistence is required; it does not select SwiftData, Room, Core Data, SQLite, or another mechanism.

### Step 3 — Seed the Draft Architecture Spine

Create the platform `ARCHITECTURE_SPINE.md` from the iOS or Android template and set `Status: Draft`.

For each section record one of:

- verified constraint/fact;
- already accepted decision;
- proposed direction;
- unresolved decision;
- justified `Not applicable`.

The first Spine is a decision map, not permission for the agent to fill every gap.

### Step 4 — Classify unresolved choices

Classify each material unresolved choice as:

- **Derivable/routine** — no owner architecture choice needed;
- **Spine-level decision** — material but a standalone ADR adds little value;
- **ADR candidate** — durable independent rationale/change history is useful;
- **Feasibility required** — evidence is needed before responsible acceptance;
- **Owner clarification required** — authority is missing.

Treat a choice as an ADR candidate when any of these apply:

- protected boundary;
- cross-feature/system-wide impact;
- reusable architecture invariant or technical policy;
- material constraint on future implementation choices;
- meaningful competing alternatives/tradeoffs;
- substantial reversal, migration, security, privacy, release, or operational cost.

Do not create one ADR per Spine heading.

### Step 5 — Draft proposed ADRs

Use `ADR.template.md`. Separate verified facts, proposed owner decisions, unresolved questions, alternatives, consequences, required evidence, and downstream synchronization.

Status remains `Proposed` until explicit owner authority changes it.

### Step 6 — Owner decision loop

The accountable owner may choose:

- `Accepted`;
- `Accepted with amendments`;
- `Accepted provisionally`;
- `Deferred`;
- `Rejected`;
- `Superseded` for historical decisions replaced by a successor.

Use `adr-lifecycle-governance` for status transitions. Agents do not self-promote ADRs.

`Accepted provisionally` requires a named blocking spike/evidence set and explicit exit criteria. It may establish direction while still blocking dependent production implementation.

### Step 7 — Feasibility spikes where required

A feasibility spike answers a bounded technical question and produces evidence; it is not product-feature implementation.

Record the question, alternatives if relevant, pass/fail criteria, evidence, and the owner decision needed afterward. Do not turn a spike into speculative production architecture.

### Step 8 — Build the canonical Spine

After owner decisions, integrate accepted decisions into the Spine so it describes the current architecture. ADRs retain rationale/history; the Spine is the integrated current view.

### Step 9 — Synchronize affected authority

For each accepted/amended decision, reconcile all **affected** canonical artifacts. At minimum consider:

`ADR → Architecture Spine → architecture coverage → Decision Register`

Also update `IMPLEMENTATION_READINESS_GATE.md`, `AI_CONTEXT.md`, policies, design authority, feature artifacts, or other documentation only when the decision changes their canonical requirements/routing/content.

Do not mechanically edit every file for every ADR.

### Step 10 — Run architecture coverage in BOOTSTRAP mode

Create/update `cross-feature-architecture-coverage.md` and keep Decision / Implementation / Evidence statuses separate.

During bootstrap it is valid for implementation/evidence to remain `Not started` / `None` while decision coverage is sufficient. Do not infer `Not applicable` from a blank.

### Step 11 — Run documentation consistency

Block current contradictions such as:

- repository evidence presented as accepted owner decision;
- two current ADR decisions that conflict;
- accepted ADR not reflected in the current Spine;
- provisional decision presented as fully proven;
- superseded wording still presented as current authority;
- routing/status documents disagreeing about the current phase.

### Step 12 — Architecture bootstrap exit check

Return one:

- `READY FOR BOUNDED FEATURE INTAKE`
- `READY WITH EXPLICIT LIMITATIONS`
- `BLOCKED — OWNER DECISION`
- `BLOCKED — FEASIBILITY EVIDENCE`
- `BLOCKED — AUTHORITY CONTRADICTION`
- `NEEDS VERIFICATION`

Ready means the repository has enough accepted cross-feature architecture for the intended first bounded feature and no current contradiction blocks it. Other decisions may remain explicitly deferred when they do not affect that slice.

This state does **not** approve a feature, authorize planning, authorize implementation, establish feature acceptance, or authorize release.

## Implementation readiness is later

Do not claim `IMPLEMENTATION_READINESS_GATE = PASS` during architecture bootstrap. That gate requires an owner-approved Feature Contract, Implementation Plan, and Implementation Tasks.

Architecture bootstrap may update the reusable gate definition when an accepted architecture decision changes future requirements. The gate is executed only after the bounded feature lifecycle reaches the required artifacts.

## Artifact roles

- `ARCHITECTURE_SPINE.<platform>.template.md` — integrated current system architecture and cross-feature boundaries.
- `ADR.template.md` — durable record for one significant technical decision, lifecycle state, alternatives, consequences, adoption/migration, and required evidence.
- `cross-feature-architecture-coverage.template.md` — independent Decision / Implementation / Evidence coverage; it does not replace the Spine or ADRs.
- `IMPLEMENTATION_READINESS_GATE.template.md` — reusable feature/slice gate definition executed before bounded implementation authorization, not during architecture bootstrap.

## Skills

Primary orchestration:

- `architecture-bootstrap`
- `adr-lifecycle-governance`

Supporting skills, invoked only when applicable:

- platform architecture readiness in bootstrap/feature mode;
- project-structure readiness in evidence-only/feature mode;
- `architecture-coverage-review` in bootstrap/feature/convergence mode;
- `documentation-consistency-review`;
- specialist platform readiness skills for decisions/spikes that actually need them.

## Efficiency rules

- Read only active authority and active architecture concerns.
- Batch owner questions by decision area instead of stopping after every small unknown.
- Reuse verified repository evidence until the relevant files/settings change.
- Synchronize once per coherent owner-decision batch where safe.
- Do not run feature-only readiness/evidence procedures before Feature Input/Contract/Plan/Tasks exist.
