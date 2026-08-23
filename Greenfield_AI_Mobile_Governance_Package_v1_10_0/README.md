# Greenfield AI Mobile Governance Package

**Version:** 1.10.0  
**Platforms:** Native Android and native iOS  
**Model:** Repository-owned, contract-first, architecture-synchronized, evidence-gated

This package provides reusable governance policies, architecture templates, feature templates, platform-specific skills, readiness gates, convergence procedures, and owner-acceptance controls for greenfield mobile delivery.

The root README is the operational **start-here guide**. You should be able to bootstrap a repository and run the normal delivery lifecycle from this README plus the routed templates and skills. The playbook remains the deeper reference for rationale, edge cases, reusable prompts, and detailed procedures.

## Start here: authority and bootstrap

A greenfield repository should begin from **approved product authority**, normally an approved PRD. The PRD defines product behavior and scope; it does not choose implementation mechanisms unless it explicitly makes them product constraints.

Before feature implementation scales, establish repository governance and the project architecture package.

```text
Approved PRD / product authority
        ↓
Install repository governance and routing
        ↓
Optional: establish approved design authority from completed external designs
        ↓
Architecture bootstrap: evidence → constraints → Draft Spine
        ↓
Propose significant ADR candidates
        ↓
Repository owner reviews ADR lifecycle decisions
        ↓
Synchronize accepted/provisional architecture
        ↓
Architecture coverage + consistency review
        ↓
READY FOR BOUNDED FEATURE INTAKE
```

Do not start from a whole-app implementation request against the PRD. Establish cross-feature architecture first, then deliver one bounded feature or walking-skeleton slice at a time.

## Optional design authority workflow

If complete external designs already exist, use `templates/design/README.md` to register them as repository design authority before downstream feature implementation. The design tool is not prescribed and MCP is optional.

The package does **not** require a design-ingest skill. Preserve imported/exported visual artifacts as source evidence; explicit owner approval makes the identified revision authoritative. Prefer exact local approved artifacts when practical.

For design-bound UI, the core prevention rule is upstream rather than an expensive post-hoc review loop:

```text
Plan maps exact approved visual
        ↓
Task carries concise Design Lock
        ↓
Readiness verifies the visual is inspectable
        ↓
Implementation inspects the actual visual before UI code
        ↓
Implement approved composition; adapt only within documented authority
```

A screen contract/design-system Markdown file supplements the approved visual; it does not replace visual inspection. If the exact approved visual cannot be inspected, the design-bound task blocks rather than improvises.

See `templates/design/README.md` for the standalone optional design workflow and optional MCP/connector guidance.

## Architecture Spine, ADRs, coverage, and readiness

### Architecture Spine

Create the platform-appropriate spine from:

- `templates/architecture/ARCHITECTURE_SPINE.ios.template.md`, or
- `templates/architecture/ARCHITECTURE_SPINE.android.template.md`.

The Architecture Spine is the current integrated architecture authority for cross-feature concerns: project/module structure, composition, state ownership, concurrency, navigation/restoration, persistence/migrations, lifecycle/recovery, localization/RTL, adaptive UI/accessibility, privacy/capabilities, background work, configuration, testing/evidence, CI, and release boundaries.

Populate it from verified repository facts plus approved product/design/governance constraints. Unknown or undecided architecture remains explicit; an agent must not silently choose a hard-to-reverse decision.

### ADRs

Use `templates/architecture/ADR.template.md` for significant hard-to-reverse, protected-boundary, cross-feature, reusable-invariant, or high-migration-cost decisions that deserve independent rationale/history. Agents may propose ADRs; only explicit owner authority can promote them. Supported lifecycle states include `Accepted`, `Accepted with amendments`, `Accepted provisionally`, `Deferred`, `Rejected`, and `Superseded`. Existing project settings are evidence, not automatic approval.

ADR acceptance does **not** authorize feature implementation. After owner review, reconcile every affected canonical artifact. At minimum consider `ADR → Architecture Spine → cross-feature architecture coverage → Decision Register`; update the readiness-gate definition, `AI_CONTEXT.md`, policies, design/feature docs, or other artifacts only when the decision actually changes them. Do not create meaningless document churn.

Any contradiction between current authority artifacts blocks affected work until resolved.

### Cross-feature architecture coverage

Create `docs/architecture/cross-feature-architecture-coverage.md` from `templates/architecture/cross-feature-architecture-coverage.template.md` for a non-trivial greenfield app, or whenever cross-feature concerns need explicit tracking.

The coverage matrix is not a second architecture design. It records three different states for each concern:

- **Decision** — has the architecture been decided?
- **Implementation** — has the accepted decision been implemented?
- **Evidence** — has the required behavior been proved?

Use `architecture-coverage-review` in `BOOTSTRAP`, `FEATURE-READINESS`, or `CONVERGENCE` mode as applicable. In bootstrap mode, `Implementation: Not started` / `Evidence: None` may be correct while decision coverage is sufficient. Do not infer `Not applicable` merely because a concern is absent.

### Implementation readiness gate

Create `docs/architecture/IMPLEMENTATION_READINESS_GATE.md` from `templates/architecture/IMPLEMENTATION_READINESS_GATE.template.md`. It is the reusable project-level gate definition used to determine whether a bounded feature/slice can become **eligible** for explicit owner implementation authorization. A `PASS` never authorizes implementation by itself.

The feature Implementation Readiness Gate is not the architecture-bootstrap exit check: it cannot PASS before an approved Feature Contract, Plan, and Tasks exist. Architecture bootstrap ends at `READY FOR BOUNDED FEATURE INTAKE`.

See `templates/architecture/README.md` for the detailed approved-PRD → repository evidence → Draft Spine → ADR/owner decision → synchronization → architecture-bootstrap-readiness procedure. Use `architecture-bootstrap` as the resumable orchestrator and `adr-lifecycle-governance` for ADR status transitions.

## Feature Input is journey authority

`FEATURE_INPUT.md` is the normalized, bounded product intake consumed by feature complexity classification and feature-contract authoring. It captures the feature purpose, boundaries, product rules, invocation origins/modes, exact success/cancel/failure destinations, durable mutations and affected consumers, critical end-to-end journeys, lifecycle/re-entry expectations, design references, protected-boundary implications, and complexity/risk signals.

### You do not need to fill Feature Input directly from the PRD in one pass

The PRD is the chain-top product authority, but Feature Input may be assembled and refined from multiple approved sources:

```text
PRD / product authority
        ↓
select one bounded feature
        ↓
seed FEATURE_INPUT.md
        ↓
optional GrillMe-style / clarification skill
        ↓
owner answers material product questions
        ↓
update and review FEATURE_INPUT.md
        ↓
Status: Approved for contract authoring
```

A clarification skill may start from a short intake rather than a complete template. Its output may be used to populate or refine `FEATURE_INPUT.md`. The skill is **not** product authority: material answers must come from the PRD, approved design/product authority, or explicit owner decisions. Agent-generated assumptions must remain assumptions or `Needs owner decision`.

For consistency and traceability, normalize clarification results into the canonical Feature Input **before** feature-contract authoring. Do not let GrillMe output bypass Feature Input and silently become contract authority.

The same visual screen may be reused from multiple origins, but each origin keeps its own behavioral return semantics. Downstream safeguards are not a substitute for missing product intent. If a material navigation outcome, affected consumer, or re-entry expectation is absent and no higher authority resolves it, authoring must surface an owner decision rather than invent behavior.

## Canonical project bootstrap lifecycle

```text
1. Approve PRD / product authority.
2. Install AGENTS.md, policies, AI_CONTEXT.md, Decision Register, templates, and platform skills.
3. Optional: import already-completed designs and explicitly record approved design authority.
4. Run architecture bootstrap: gather repository facts as evidence and extract architecture-driving constraints.
5. Seed Draft ARCHITECTURE_SPINE.md and classify unresolved choices.
6. Create only significant proposed ADRs; run bounded feasibility spikes when a provisional decision requires proof.
7. Owner accepts/amends/provisionally accepts/defers/rejects decisions; agents never self-promote evidence to approval.
8. Synchronize affected ADR/Spine/coverage/Decision Register/routing or gate definitions.
9. Run architecture coverage + documentation consistency and reach READY FOR BOUNDED FEATURE INTAKE.
10. Select one bounded feature and create/refine FEATURE_INPUT.md.
```

## Canonical feature delivery lifecycle

```text
Feature Input
→ feature complexity classification (or COMPLEX by default)
→ feature contract
→ independent contract review
→ owner approval
→ implementation plan
→ independent plan review
→ owner approval
→ implementation tasks
→ independent task review
→ owner approval
→ implementation readiness audit
→ explicit owner implementation authorization
→ bounded feature implementation
→ task evidence closure
→ feature convergence
→ READINESS_REPORT.md
→ applicable final-readiness evidence closure
→ independent readiness review
→ owner feature acceptance
→ separate release authorization
```

## How to use the skills

Use skills in lifecycle order. Run platform-specific variants from `skills/ios/` or `skills/android/`. Supporting readiness skills are invoked only when the architecture, plan, task set, current implementation slice, or evidence obligations make them applicable.

Project bootstrap uses `architecture-bootstrap` plus `adr-lifecycle-governance`; these run before the feature table below. Design setup is an optional README/template workflow, not a mandatory skill.

| Step | Goal | Primary skill / procedure | Main input | Main output / verdict | Implementation allowed? |
|---|---|---|---|---|---|
| 0 | Normalize feature intake | Optional GrillMe-style clarification + `FEATURE_INPUT_TEMPLATE.md` | PRD/product authority + bounded feature context + owner answers | Reviewed `FEATURE_INPUT.md` | No |
| 1 | Classify feature complexity | `feature-complexity-classification` | Feature input + architecture/risk context | `SMALL`, `STANDARD`, or `COMPLEX`; missing/invalid/stale classification defaults to `COMPLEX` | No |
| 2 | Define bounded observable behavior | `feature-contract-authoring` | Reviewed Feature Input + product/design/architecture authority | `FEATURE_CONTRACT.md` | No |
| 3 | Independently review contract | `feature-contract-review` | Contract + governing authorities | Review verdict | No |
| 4 | Approve contract | Repository owner | Reviewed contract | Owner approval | No |
| 5 | Design implementation approach | `implementation-plan-authoring` | Approved contract + accepted ADRs + architecture/design + repository facts | `IMPLEMENTATION_PLAN.md` | No |
| 6 | Independently review plan | `implementation-plan-review` | Contract + plan + architecture/design | Review verdict | No |
| 7 | Approve plan | Repository owner | Reviewed plan | Owner approval | No |
| 8 | Generate dependency-ordered work | `implementation-task-authoring` | Approved contract + approved plan | `IMPLEMENTATION_TASKS.md` | No |
| 9 | Independently review task set | `implementation-task-review` | Contract + plan + tasks | Review verdict | No |
| 10 | Approve task set | Repository owner | Reviewed tasks | Owner approval | No |
| 11 | Prove implementation readiness | Applicable readiness skills + `protected-boundary-preflight` + readiness gate | Approved artifacts + architecture/design + repository facts | `IMPLEMENTATION_READINESS_AUDIT.md` | No; PASS means eligible only |
| 12 | Authorize exact work | Repository owner | Passing readiness audit + exact task IDs | Explicit implementation authorization | Yes, only named scope |
| 13 | Implement bounded task group | `bounded-feature-implementation` | Approved artifacts + exact authorization + exact approved visual for design-bound UI | Code/config/docs + TASK-CLOSURE evidence | Only authorized scope |
| 14 | Verify whole-feature convergence | `feature-implementation-convergence` | Complete coherent feature diff + linked evidence | Convergence verdict + `READINESS_REPORT.md` | No new scope |
| 15 | Close final readiness | Applicable specialist readiness skills | Remaining FINAL-READINESS obligations | Evidence closure | No release authority |
| 16 | Independently review readiness | `feature-readiness-review` | Contract/plan/tasks/readiness report/evidence | Acceptance recommendation | No release authority |
| 17 | Accept feature | Repository owner | Independent readiness result | Feature acceptance | No release authority |
| 18 | Release | Separate repository-defined process | Accepted feature + release evidence | Explicit release authorization | Only after separate authorization |

`bounded-feature-implementation` mutates the repository only for explicitly authorized task IDs. `feature-implementation-convergence` does **not** implement the feature; it independently verifies the complete coherent feature against the approved contract, plan, tasks, architecture, design, cross-cutting requirements, and required evidence.

## Recommended canonical repository layout

The exact paths are repository-defined and must be recorded in `AI_CONTEXT.md`, but this package uses the following recommended convention. Keep package distribution structure separate from installed repository structure.

```text
repo/
├── AGENTS.md
├── AI_CONTEXT.md
├── AI_PLAYBOOK.md                       # if the repository keeps a local workflow policy
│
├── .agents/
│   ├── policies/
│   │   ├── FEATURE_DELIVERY_INVARIANTS.md
│   │   ├── GOVERNANCE_LIFECYCLE.md
│   │   ├── IMPLEMENTATION_POLICY.md
│   │   ├── EVIDENCE_AND_COMPLETION.md
│   │   ├── PROTECTED_BOUNDARIES.md
│   │   └── ios/ or android/
│   └── skills/
│       ├── ios/                          # copy selected iOS skills
│       └── android/                      # copy selected Android skills
│
├── .templates/
│   ├── governance/
│   │   ├── AI_CONTEXT.template.md
│   │   ├── DECISION_REGISTER.template.md
│   │   └── FEATURE_COMPLEXITY_TIER_POLICY.md
│   ├── design/
│   │   ├── README.md
│   │   ├── DESIGN_AUTHORITY.template.md
│   │   └── DESIGN_ARTIFACT_INDEX.template.md
│   ├── architecture/
│   │   ├── ADR.template.md
│   │   ├── ARCHITECTURE_SPINE.<platform>.template.md
│   │   ├── cross-feature-architecture-coverage.template.md
│   │   └── IMPLEMENTATION_READINESS_GATE.template.md
│   └── mobile/
│       ├── mobile/
│       │   ├── FEATURE_INPUT_TEMPLATE.md
│       │   ├── FEATURE_CONTRACT_TEMPLATE.md
│       │   ├── IMPLEMENTATION_READINESS_AUDIT_TEMPLATE.md
│       │   └── READINESS_REPORT_TEMPLATE.md
│       └── ios/ or android/
│           ├── IMPLEMENTATION_PLAN_TEMPLATE.md
│           └── IMPLEMENTATION_TASKS_TEMPLATE.md
│
├── docs/
│   ├── product/
│   │   └── approved/PRD.md
│   ├── decisions/
│   │   └── DECISION_REGISTER.md
│   ├── design/
│   │   └── approved/
│   │       ├── DESIGN_AUTHORITY.md
│   │       ├── DESIGN_ARTIFACT_INDEX.md
│   │       └── artifacts/...              # optional local approved visual exports
│   ├── architecture/
│   │   ├── ARCHITECTURE_SPINE.md
│   │   ├── adrs/ADR-*.md
│   │   ├── cross-feature-architecture-coverage.md
│   │   └── IMPLEMENTATION_READINESS_GATE.md
│   ├── feature-inputs/
│   │   └── <feature-id>/feature-input.md
│   ├── features/
│   │   └── <feature-id>/
│   │       ├── FEATURE_CONTRACT.md
│   │       ├── IMPLEMENTATION_PLAN.md
│   │       ├── IMPLEMENTATION_TASKS.md
│   │       ├── IMPLEMENTATION_READINESS_AUDIT.md
│   │       └── READINESS_REPORT.md
│   ├── verification/<feature-id>/...
│   └── release/...
│
└── <application source / project files>
```

Do not install `historical/` files as active authority. If your repository uses different paths, record the canonical paths in `AI_CONTEXT.md` and keep skills/templates synchronized with them.

## Canonical repository artifacts and their roles

### Project-level authority and architecture

- `docs/product/approved/PRD.md` — chain-top approved product behavior and scope.
- `AGENTS.md` + `.agents/policies/` — operational governance and protected-boundary rules.
- `AI_CONTEXT.md` — current routing; it does not create authority.
- `docs/design/approved/DESIGN_AUTHORITY.md` — optional owner-approved visual/interaction authority and permitted-adaptation policy.
- `docs/design/approved/DESIGN_ARTIFACT_INDEX.md` — optional exact artifact/variant/revision mapping; local approved visual exports are preferred when practical.
- `docs/decisions/DECISION_REGISTER.md` — owner decisions and synchronization obligations.
- `docs/architecture/ARCHITECTURE_SPINE.md` — integrated cross-feature architecture authority.
- `docs/architecture/adrs/ADR-*.md` — accepted significant technical decisions and rationale/history.
- `docs/architecture/cross-feature-architecture-coverage.md` — decision/implementation/evidence coverage across architecture concerns.
- `docs/architecture/IMPLEMENTATION_READINESS_GATE.md` — reusable gate definition for implementation eligibility.

### Feature-level intake and delivery

- `docs/feature-inputs/<feature-id>/feature-input.md` — bounded, reviewed product/journey intake.
- `docs/features/<feature-id>/FEATURE_CONTRACT.md` — precise observable behavioral contract.
- `docs/features/<feature-id>/IMPLEMENTATION_PLAN.md` — application of accepted architecture to the approved feature.
- `docs/features/<feature-id>/IMPLEMENTATION_TASKS.md` — dependency-ordered authorized-ready work decomposition.
- `docs/features/<feature-id>/IMPLEMENTATION_READINESS_AUDIT.md` — feature/slice gate execution before implementation authorization.
- `docs/features/<feature-id>/READINESS_REPORT.md` — post-implementation convergence/readiness evidence and blockers.

## Authority boundaries to remember

- **PRD / product authority** defines product behavior and scope.
- **Approved design authority** defines binding visual/interaction properties for the explicitly approved artifact revision; imported files or newer external revisions do not become authority by themselves.
- **Repository/tool evidence** describes observed current state and must not be silently promoted into owner architecture decisions.
- **Feature Input** normalizes the bounded feature journey and product intent; it may be refined through clarification but cannot invent authority.
- **Feature Contract** makes approved feature behavior precise and testable without choosing implementation mechanisms.
- **Architecture Spine** defines the current integrated system architecture.
- **ADRs** capture significant accepted technical decisions and their rationale/history.
- **Cross-feature coverage** tracks whether architecture concerns are decided, implemented, and evidenced.
- **Implementation Plan** applies accepted architecture to the approved feature; it must not silently reopen ADRs or invent product behavior.
- **Implementation Tasks** decompose the approved plan; tasks cannot create new product decisions.

## Efficiency model

The package preserves contract, architecture, protected-boundary, and vertical-journey rigor while reducing duplicate proof:

- Policy modules are routed conditionally through `AI_CONTEXT.md`; unrelated policy files are not ceremonial mandatory reads.
- Shared journey/complexity/evidence invariants live once in `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` and are referenced by platform skills.
- Bounded implementation executes `TASK-CLOSURE` evidence only by default.
- `FEATURE-CONVERGENCE` proves cross-task integration once; `FINAL-READINESS` owns expensive device/manual/platform checks.
- One valid artifact may satisfy multiple `VM-*` rows.
- Readiness review independently spot-checks convergence and escalates to full review only on inconsistency/high risk.
- Coherent vertical tasks are preferred over one task per UI concern.
- Design-bound UI prevents drift cheaply: exact artifact mapping → concise Design Lock → one pre-code visual inspection per unchanged governing artifact/task execution. Do not require a separate screenshot-diff review for every screen by default.
- Manual validation is encouraged for subjective/device-only properties but never replaces deterministic behavior/data correctness tests.

## Complexity tiers

The package keeps one canonical feature lifecycle with shared product/readiness templates and platform-specific implementation plan/task templates. Feature Input risk checkboxes inform classification but never self-assign a tier; blank/legacy inputs do not justify a lower tier. If classification is not run, cannot complete, or is missing/invalid/stale, downstream work defaults to **COMPLEX** and records the default.

Tier changes mandatory depth rather than selecting duplicate templates. SMALL uses the core bounded sections and focused verification; STANDARD additionally requires explicit state/navigation/persistence and cross-feature propagation coverage; COMPLEX requires every applicable protected-boundary, migration, concurrency/idempotency, lifecycle/recovery, historical-integrity, and runtime-evidence obligation. Specialist platform skills still run whenever their concern applies.

A durable mutation is not complete merely because its local repository or screen succeeds. Plans/tasks must identify affected consumers and verify mutation → committed source of truth → dependent consumer refresh/catch-up → correct post-action destination.

## Installation

The recommended bootstrap path is `uvx`, which fetches the AI-Workflow CLI directly from GitHub. A user does **not** need to clone AI-Workflow first.

For the simplest installation, first change into the **root of the receiving mobile repository**:

```bash
cd /path/to/your/mobile-app
```

Then run one of:

```bash
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow greenfield --platform ios
# or
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow greenfield --platform android
```

When `--target` is omitted, the current working directory is the receiving repository. In other words, **yes, run the command from the project root** unless you provide `--target` explicitly.

To run the command from somewhere else:

```bash
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow greenfield --platform ios \
  --target /path/to/your/mobile-app
```

Preview the complete plan before writing with `--dry-run`:

```bash
cd /path/to/your/mobile-app
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow greenfield --platform ios --dry-run
```

The installer performs steps 2–5 below using the applicable platform files and seeds `AI_CONTEXT.md` plus the decision register from templates. It does not create project-specific architecture, feature, readiness, evidence, or release artifacts before the receiving repository has the facts and approvals required to author them. Use `--skills-only` only when the repository already owns the rest of the governance/bootstrap structure. Existing destination paths are not replaced unless `--force` is explicitly supplied.

For frequent use, the CLI may be installed persistently with:

```bash
uv tool install git+https://github.com/RanaAhmedHamdy/AI-Workflow.git
```

After that, run `ai-workflow greenfield --platform ios` or `ai-workflow greenfield --platform android` from the receiving repository root.

Contributors working from an AI-Workflow checkout can still use `python3 tools/install.py ...`; when running that script from inside the AI-Workflow checkout, pass `--target /path/to/receiving/repository` so the framework repository itself is not used as the target by accident.

Manual/bootstrap lifecycle:

1. Confirm the approved PRD/product authority path.
2. Copy `templates/mobile-agent-policy-modular/AGENTS.md` to the repository root and install its `.agents/policies/` modules.
3. Select the relevant platform policy and skills from `skills/android/` or `skills/ios/` and install them under the repository’s skill location.
4. Copy governance, architecture, and mobile templates into the repository template location.
5. Create `AI_CONTEXT.md` from `templates/governance/AI_CONTEXT.template.md` and `docs/decisions/DECISION_REGISTER.md` from its template.
6. Optional: follow `templates/design/README.md` if completed external designs should become approved repository design authority.
7. Run the detailed `templates/architecture/README.md` bootstrap flow (or `architecture-bootstrap`) through owner-gated ADR decisions and `READY FOR BOUNDED FEATURE INTAKE`.
8. Create/update architecture coverage and the reusable implementation-readiness gate definition, then record canonical paths in `AI_CONTEXT.md`; do not claim the feature gate passes yet.
9. Select one bounded feature; create/refine and review Feature Input before contract authoring.
10. Replace every remaining placeholder and record canonical paths/owners; do not install `historical/` files as active authority.

## Playbooks

- `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v2_3_Agent_Native.docx` is the latest agent-native detailed playbook. It follows the same PRD → architecture bootstrap → normalized Feature Input → contract/plan/tasks → readiness → bounded implementation → convergence flow described here.
- Earlier playbooks are retained under `historical/playbooks/` when present and are not canonical.
- `Mobile_Feature_Delivery_Governance_Pipeline.docx` is the human-readable end-to-end lifecycle reference.

## Package distribution structure

```text
templates/
  mobile-agent-policy-modular/
  governance/
  design/
  architecture/
  mobile/
skills/
  android/
  ios/
historical/
playbook/
```

Android and iOS skills remain separate even when they share a skill name. Their required inputs, platform contracts, evidence layers, and verdict semantics may differ. Do not merge them solely by name.

## Important semantics

- Skills and templates do not authorize work.
- Clarification output does not become product authority by itself.
- Imported design files do not become approved design authority by file presence alone.
- A design-bound UI task must inspect the exact approved visual before coding; Markdown-only interpretation is insufficient.
- Repository/tool evidence does not become an owner architecture decision by itself.
- ADR acceptance does not authorize implementation.
- Readiness `PASS` means eligible for owner implementation authorization only.
- Implementation completion does not establish feature acceptance.
- Applicable deferred `FINAL-READINESS` evidence must close before independent readiness can PASS.
- Feature acceptance does not authorize release.
- Runtime-only claims require matching runtime evidence.
- Configuration retained for future features must have explicit target/source-set inclusion, runtime initialization, privacy impact, and active/dormant status.

## Hooks

No hooks are included. Hook execution is repository-specific and must be added only through explicit repository policy.
