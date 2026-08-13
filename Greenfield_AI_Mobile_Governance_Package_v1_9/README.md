# Greenfield AI Mobile Governance Package

**Version:** 1.9  
**Platforms:** Native Android and native iOS  
**Model:** Repository-owned, contract-first, architecture-synchronized, evidence-gated

This package provides reusable governance policies, playbooks, architecture templates, feature templates, platform-specific skills, readiness gates, convergence procedures, and owner-acceptance controls for greenfield mobile delivery.

## Feature Input is journey authority

`templates/mobile/mobile/FEATURE_INPUT_TEMPLATE.md` now captures the product journey before contract authoring: invocation origin and mode, exact success/cancel/failure destinations, durable mutations and affected consumers, critical end-to-end journeys, lifecycle/re-entry expectations, and complexity/risk signals. The same visual screen may be reused from multiple origins, but each origin keeps its own behavioral return semantics.

The contract, plan, and task templates carry these fields forward, including active-consumer refresh and inactive/recreated-consumer catch-up. Downstream safeguards are not a substitute for missing product intent. If a material navigation outcome, affected consumer, or re-entry expectation is absent and no higher authority resolves it, authoring must surface an owner decision rather than invent behavior.


## Efficiency model (v1.9)

The package preserves contract, architecture, protected-boundary, and vertical-journey rigor while reducing duplicate proof:

- Policy modules are routed conditionally through `AI_CONTEXT.md`; unrelated policy files are not ceremonial mandatory reads.
- Shared journey/complexity/evidence invariants live once in `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` and are referenced by platform skills.
- Bounded implementation executes `TASK-CLOSURE` evidence only by default.
- `FEATURE-CONVERGENCE` proves cross-task integration once; `FINAL-READINESS` owns expensive device/manual/platform checks.
- One valid artifact may satisfy multiple `VM-*` rows.
- Readiness review independently spot-checks convergence and escalates to full review only on inconsistency/high risk.
- Coherent vertical tasks are preferred over one task per UI concern.
- Manual validation is encouraged for subjective/device-only properties but never replaces deterministic behavior/data correctness tests.

## Canonical lifecycle

Feature input → feature complexity classification (or COMPLEX by default) → feature contract → independent contract review → owner approval → implementation plan → independent plan review → owner approval → implementation tasks → independent task review → owner approval → implementation readiness audit → explicit owner implementation authorization → bounded feature implementation → task evidence closure → feature convergence → `READINESS_REPORT.md` → applicable final-readiness evidence closure → independent readiness review → owner feature acceptance → separate release authorization.


## How to use the skills

Use the skills in lifecycle order. Run platform-specific variants from `skills/ios/` or `skills/android/` where both exist. Supporting readiness skills are invoked when the plan, task set, or current implementation slice makes them applicable.

| Step | Goal | Primary skill / procedure | Main input | Main output / verdict | Can implementation start? |
|---|---|---|---|---|---|
| 0 | Classify feature complexity | `feature-complexity-classification` from `skills/ios/` or `skills/android/` | Feature input + architecture/risk context | `SMALL`, `STANDARD`, or `COMPLEX`; if not run, downstream work MUST default to `COMPLEX` | No |
| 1 | Define the bounded feature | `feature-contract-authoring` | Feature input, product authority, design authority, architecture context | `FEATURE_CONTRACT.md` → `READY FOR CONTRACT REVIEW` | No |
| 2 | Independently review the feature contract | `feature-contract-review` | `FEATURE_CONTRACT.md` and governing authorities | Contract review verdict | No |
| 3 | Approve the feature contract | Repository owner | Reviewed contract | Owner approval recorded | No |
| 4 | Design the implementation approach | `implementation-plan-authoring` | Approved contract, ADRs, design authority, repository architecture | `IMPLEMENTATION_PLAN.md` → `READY FOR PLAN REVIEW` | No |
| 5 | Independently review the implementation plan | `implementation-plan-review` | Approved contract + implementation plan + architecture/design authority | Plan review verdict | No |
| 6 | Approve the implementation plan | Repository owner | Reviewed plan | Owner approval recorded | No |
| 7 | Generate dependency-ordered implementation work | `implementation-task-authoring` | Approved contract + approved plan | `IMPLEMENTATION_TASKS.md` | No |
| 8 | Independently review the task set | `implementation-task-review` | Contract + plan + tasks | Task review verdict | No |
| 9 | Approve the task set | Repository owner | Reviewed tasks | Owner approval recorded | No |
| 10 | Prove implementation readiness | Platform readiness skills + `protected-boundary-preflight` + implementation readiness audit | Approved contract, plan, tasks, repository state | `IMPLEMENTATION_READINESS_AUDIT.md` → `PASS`, `BLOCKED`, or `NEEDS VERIFICATION` | No — `PASS` only makes the feature eligible for owner authorization |
| 11 | Authorize implementation | Repository owner | Passing readiness audit and synchronized authority | Explicit implementation authorization for the bounded scope | **Yes, but only for the authorized scope** |
| 12 | Implement one authorized task group | `bounded-feature-implementation` | Exact authorized task IDs + approved contract/plan/tasks + applicable readiness results | Production changes, focused tests, task-level evidence, bounded completion report | Yes — only inside the authorized task group |
| 13 | Repeat bounded implementation | `bounded-feature-implementation` | Next dependency-valid authorized task group | Additional implemented task groups and evidence | Yes — until the approved task set is complete |
| 14 | Audit whole-feature convergence | `feature-implementation-convergence` | Completed implementation, approved authorities, current task/convergence evidence, docs | `READINESS_REPORT.md`; `READY FOR FINAL READINESS`, `READY FOR FEATURE READINESS REVIEW`, or categorized blocker | No new scope; this is post-implementation verification |
| 15 | Close applicable final-readiness evidence | Existing platform runtime/accessibility/privacy/persistence/performance readiness procedures, only as applicable | `READINESS_REPORT.md` + deferred `FINAL-READINESS` obligations | Manual/device/platform evidence recorded; report updated | No |
| 16 | Run independent feature readiness review | `feature-readiness-review` | Updated `READINESS_REPORT.md`, critical evidence, governing authorities | Independent spot-check verdict; escalates on inconsistency/high risk | No |
| 17 | Accept the feature | Repository owner | Passing independent readiness review | Owner feature acceptance | No release authority |
| 18 | Merge / sign / distribute / release | Repository-specific release procedure | Accepted feature + separate release authorization | Release evidence / distribution result | Only after separate explicit release authorization |

### Supporting skills

The primary lifecycle above is intentionally small. Feature complexity uses one tier-aware lifecycle rather than three duplicated template/skill families. If complexity classification was not run or is unavailable/stale, all downstream skills MUST treat the feature as COMPLEX. See `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`.

The primary lifecycle above is intentionally small. Invoke specialized skills when their concern applies rather than treating every skill as a separate lifecycle phase.

| Concern | Typical supporting skills |
|---|---|
| Complexity and governance depth | `feature-complexity-classification` (platform-specific); SMALL/ STANDARD/ COMPLEX obligations from `FEATURE_COMPLEXITY_TIER_POLICY.md` |
| Architecture and project structure | `architecture-coverage-review`, `ios-architecture-readiness`, `android-architecture-readiness`, platform project-structure readiness |
| UI implementation readiness | `swiftui-screen-readiness`, `uikit-screen-readiness`, `compose-screen-readiness`, `android-views-screen-readiness`, adaptive readiness skills |
| Concurrency and lifecycle | `swift-concurrency-readiness`, `kotlin-coroutines-readiness`, lifecycle/transaction review skills |
| Persistence and migration | Platform persistence/migration readiness skills, `characterization-tests` where legacy behavior must be preserved |
| Localization, RTL, accessibility, adaptive UI | Platform localization/RTL readiness, adaptive/accessibility readiness, runtime evidence readiness |
| Privacy and protected boundaries | Platform privacy/permission/capability readiness, `protected-boundary-preflight` |
| Evidence and production integrity | `runtime-evidence-readiness`, `production-fake-detection`, `documentation-impact-assessment`, `documentation-review`, `pr-review` |

### Key execution rule

`bounded-feature-implementation` changes the repository for an explicitly authorized task group. `feature-implementation-convergence` does **not** implement the feature; it independently verifies the completed feature against the approved contract, plan, tasks, architecture, design, cross-cutting requirements, and required evidence.

## Playbooks

- `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v2_2_Agent_Native.docx` is the latest agent-native playbook and does not use Spec Kit. It is updated to use `IMPLEMENTATION_TASKS.md`, a pre-implementation `IMPLEMENTATION_READINESS_AUDIT.md`, and a post-implementation `READINESS_REPORT.md`.
- `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v2_1_Agent_Native.docx`, `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v2_0_Agent_Native.docx`, and `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v1_5_iOS_Android.docx` are retained as earlier editions. They are not the canonical agent-native workflow.
- `Mobile_Feature_Delivery_Governance_Pipeline.docx` is the human-readable end-to-end lifecycle reference.

## Package structure

```text
templates/
  mobile-agent-policy-modular/
  governance/  # includes FEATURE_COMPLEXITY_TIER_POLICY.md
  architecture/
  mobile/
skills/
  android/  # includes feature-complexity-classification
  ios/      # includes feature-complexity-classification
historical/
  policies/
playbook/
```

Android and iOS skills remain separate even when they share a skill name. Their required inputs, platform contracts, evidence layers, and verdict semantics may differ. Do not merge them solely by name.

## Canonical repository artifacts

- `FEATURE_CONTRACT.md`
- `IMPLEMENTATION_PLAN.md`
- `IMPLEMENTATION_TASKS.md`
- `IMPLEMENTATION_READINESS_AUDIT.md`
- `READINESS_REPORT.md`

## Important semantics

- Skills and templates do not authorize work.
- ADR acceptance does not authorize implementation.
- Readiness `PASS` means eligible for owner implementation authorization only.
- Implementation completion does not establish feature acceptance.
- Applicable deferred `FINAL-READINESS` evidence must close before independent readiness can PASS.
- Feature acceptance does not authorize release.
- Runtime-only claims require matching runtime evidence.
- Configuration retained for future features must have explicit target/source-set inclusion, runtime initialization, privacy impact, and active/dormant status.

## Installation

1. Copy `templates/mobile-agent-policy-modular/AGENTS.md` to the repository root and install its `.agents/policies/` modules.
2. Select the relevant platform policy and skills from `skills/android/` or `skills/ios/`.
3. Copy governance, architecture, and mobile templates into the repository template location.
4. Create `AI_CONTEXT.md` from `templates/governance/AI_CONTEXT.template.md`.
5. Replace every placeholder and record canonical paths and owners.
6. Do not install files under `historical/` as active authority.

## Hooks

No hooks are included. Hook execution is repository-specific and must be added only through explicit repository policy.


## Complexity tiers

The package keeps one canonical feature lifecycle with shared product/readiness templates and platform-specific implementation plan/task templates. Feature Input risk checkboxes inform classification but never self-assign a tier; blank/legacy inputs do not justify a lower tier. Tier changes mandatory depth rather than selecting duplicate templates. SMALL uses the core bounded sections and focused verification; STANDARD additionally requires explicit state/navigation/persistence and cross-feature propagation coverage; COMPLEX requires every applicable protected-boundary, migration, concurrency/idempotency, lifecycle/recovery, historical-integrity, and runtime-evidence obligation. Specialist platform skills still run whenever their concern applies.

A durable mutation is not complete merely because its local repository or screen succeeds. Plans/tasks must identify affected consumers and verify mutation → committed source of truth → dependent consumer refresh → correct post-action destination.
