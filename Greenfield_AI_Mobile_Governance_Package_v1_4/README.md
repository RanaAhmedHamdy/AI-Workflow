# Greenfield AI Mobile Governance Package

**Version:** 1.5  
**Platforms:** Native Android and native iOS  
**Model:** Repository-owned, contract-first, architecture-synchronized, evidence-gated

This package provides reusable governance policies, playbooks, architecture templates, feature templates, platform-specific skills, readiness gates, convergence procedures, and owner-acceptance controls for greenfield mobile delivery.

## Canonical lifecycle

Feature input → feature contract → independent contract review → owner approval → implementation plan → independent plan review → owner approval → implementation tasks → independent task review → owner approval → implementation readiness audit → explicit owner implementation authorization → bounded feature implementation → task evidence closure → feature convergence → `READINESS_REPORT.md` → independent readiness review → owner feature acceptance → separate release authorization.


## How to use the skills

Use the skills in lifecycle order. Run platform-specific variants from `skills/ios/` or `skills/android/` where both exist. Supporting readiness skills are invoked when the plan, task set, or current implementation slice makes them applicable.

| Step | Goal | Primary skill / procedure | Main input | Main output / verdict | Can implementation start? |
|---|---|---|---|---|---|
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
| 14 | Audit whole-feature convergence | `feature-implementation-convergence` | Completed implementation, approved authorities, tests, runtime evidence, docs | `READINESS_REPORT.md` and convergence verdict | No new scope; this is post-implementation verification |
| 15 | Run independent feature readiness review | `feature-readiness-review` | `READINESS_REPORT.md`, implementation, evidence, governing authorities | Feature readiness verdict | No |
| 16 | Accept the feature | Repository owner | Passing independent readiness review | Owner feature acceptance | No release authority |
| 17 | Merge / sign / distribute / release | Repository-specific release procedure | Accepted feature + separate release authorization | Release evidence / distribution result | Only after separate explicit release authorization |

### Supporting skills

The primary lifecycle above is intentionally small. Invoke specialized skills when their concern applies rather than treating every skill as a separate lifecycle phase.

| Concern | Typical supporting skills |
|---|---|
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

- `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v2_1_Agent_Native.docx` is the latest agent-native playbook and does not use Spec Kit. It is updated to use `IMPLEMENTATION_TASKS.md`, a pre-implementation `IMPLEMENTATION_READINESS_AUDIT.md`, and a post-implementation `READINESS_REPORT.md`.
- `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v2_0_Agent_Native.docx` and `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v1_5_iOS_Android.docx` are retained unchanged as earlier editions. They are not the canonical agent-native workflow.
- `Mobile_Feature_Delivery_Governance_Pipeline.docx` is the human-readable end-to-end lifecycle reference.

## Package structure

```text
templates/
  mobile-agent-policy-modular/
  governance/
  architecture/
  mobile/
skills/
  android/
  ios/
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
