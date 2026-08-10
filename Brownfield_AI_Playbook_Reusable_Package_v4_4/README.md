# Brownfield AI Playbook Reusable Package v4.4

Contents:

- `playbook/` — DOCX and Markdown editions of the v4.4 playbook.
- `checklists/` — reusable architecture-coverage checklist.
- `templates/` — AGENTS policy templates.
- `skills/` — reusable governance, testing, review, adaptive UI, and publishing skills.
- `repository-starter/` — prompt templates, guarded runners, focused architecture-spec examples, Graphify policy, and clearly labeled project-specific examples.

Read `repository-starter/README.md` before copying workflow files into another repository. Shell mechanics and policy text may be reusable, but manifests, checkpoints, Graphify override rows, evidence paths, revisions, decisions, test counts, and project status must be regenerated or adapted.

## Canonical brownfield lifecycle

Safe setup → repository discovery → documentation/provenance review → first characterization tests → feature understanding → architecture/design validation → architecture coverage gate → verification questions and accountable decisions → no-edit implementation audit → testing safety net → controlled refactor or bounded feature/defect work → independent review → documentation impact → explicit publish → CI/runtime/release verification.

Brownfield work uses two tracks:

- **Standard bounded track:** use when the requirement is clear, low risk, and does not cross protected or owner-sensitive boundaries.
- **Decision-sensitive track:** use when work affects authentication, data integrity, persistence, signing, certificates, permissions, notifications, camera, release, backend contracts, or unresolved product behavior.

## How to use the skills

Use the smallest skill set that matches the current brownfield task. Not every skill is required for every change. The lifecycle below shows where each reusable skill normally fits.

| Step | Goal | Primary skill / procedure | Main input | Main output / verdict | Code edits allowed? |
|---|---|---|---|---|---|
| 1 | Establish safe repository context | Brownfield onboarding / repository discovery from the playbook | Repository, root policy, build/test commands, sensitive boundaries | Reviewed project/context foundation | No |
| 2 | Preserve current behavior before risky changes | `characterization-tests` | Existing behavior, seams, current tests | Focused characterization coverage and evidence | Tests only unless a seam is explicitly authorized |
| 3 | Understand the active feature or defect path | Feature documentation / no-edit investigation from the playbook | Context index, feature docs, directly relevant source/tests | Current behavior, active/deferred paths, risks, Needs verification | No |
| 4 | Check cross-feature architecture coverage | `architecture-coverage-review` | Architecture maps, feature docs, current evidence | Verified / Needs verification / Not observed / Not applicable classifications and routed gaps | No |
| 5 | Resolve protected or owner-sensitive uncertainty | Verification questions + accountable decision workflow | Coverage gaps, decisions, protected boundaries, owner input | Reviewed decision record / safe next action | No |
| 6 | Preflight protected changes | `protected-boundary-preflight` | Proposed bounded change, protected areas, current repository state | PASS / BLOCKED / owner decision required | Only after PASS and explicit authorization |
| 7 | Plan one bounded implementation item | Brownfield plan/checkpoint workflow | Reviewed decisions, no-edit audit, context, relevant skills | One authorized task with allowed files, verification, and stop conditions | No |
| 8 | Implement one approved fix, refactor, test, or feature slice | Approved repository plan + applicable platform/project skills | Exact authorized task and current source | Small coherent diff + focused verification | **Yes, only inside the authorized boundary** |
| 9 | Validate adaptive Compose behavior when applicable | `adaptive-compose` | Compose UI change, window classes, adaptive requirements | Adaptive UI findings / verification evidence | Yes, only within the authorized UI task |
| 10 | Assess documentation impact | `documentation-impact-assessment` | Coherent implementation diff + existing docs | Which docs must change, must not change, or need verification | Docs only as required |
| 11 | Review updated documentation | `documentation-review` | Changed docs + governing evidence | Documentation review findings / PASS when supported | No production edits |
| 12 | Independently review the implementation diff | `pr-review` | Complete coherent diff, tests, evidence, protected boundaries | Blocking findings, non-blocking findings, test gaps, risk level | No new feature scope |
| 13 | Publish explicitly after human review | `publish-ai-mr` | Reviewed/staged diff, verification summary, branch state | Safe push and create/reuse MR; no auto-merge | Publication only |
| 14 | Verify CI/runtime/release evidence | Repository-specific CI/release procedures | MR/branch, deterministic scripts, simulator/device/runtime evidence | Merge/release evidence appropriate to the change | Release actions only when separately authorized |

### When to use which reusable skill

| Skill | Use it when | Do not use it as |
|---|---|---|
| `characterization-tests` | Existing behavior must be captured before a fix/refactor or when current behavior is unclear | A reason to freeze known-bad behavior permanently |
| `architecture-coverage-review` | You need to determine whether important cross-feature concerns are actually understood and evidenced | A replacement for direct source inspection or owner decisions |
| `protected-boundary-preflight` | The proposed work touches owner-sensitive, security, privacy, data, signing, permission, release, or other protected boundaries | Authorization by itself |
| `adaptive-compose` | Android Compose UI must behave correctly across compact, medium, expanded, RTL, font-scale, or other adaptive conditions | A generic UI implementation skill for unrelated work |
| `documentation-impact-assessment` | A code/test/config diff may require durable documentation changes | A requirement to update every document after every change |
| `documentation-review` | Documentation was created or changed and its claims need evidence/provenance review | A substitute for implementation review |
| `pr-review` | A coherent implementation diff is ready for independent engineering review | Whole-repository re-analysis or automatic approval |
| `publish-ai-mr` | The diff has already been reviewed and the user explicitly authorizes publishing | Auto-merge, auto-approval, force-push, or hidden publication |

## Standard bounded track

Use this track when the requirement is clear and low risk:

1. Load reviewed context and the relevant feature documentation.
2. Explain current behavior and the intended bounded change.
3. Add or confirm focused tests where needed.
4. Implement the smallest authorized change.
5. Run focused and repository-required verification.
6. Run documentation impact only when the diff can affect durable context.
7. Run independent `pr-review` on the coherent diff.
8. Publish only through explicit `publish-ai-mr` authorization.

## Decision-sensitive track

Use this track when protected boundaries or unresolved behavior are involved:

1. Gather direct evidence from current docs/source/tests.
2. Run `architecture-coverage-review` where the concern is cross-feature or architecture-sensitive.
3. Generate only verification questions that block a concrete next action.
4. Record accountable owner decisions without editing production code.
5. Run the no-edit implementation audit against those decisions.
6. Run `protected-boundary-preflight` before any protected mutation.
7. Authorize exactly one bounded action with explicit allowed/forbidden scope.
8. Implement and verify that action only.
9. Run documentation impact/review when durable context changed.
10. Independently review the complete diff with `pr-review`.
11. Publish only after explicit human authorization.

## Key execution rules

- Skills and playbooks do not grant authorization.
- Current source wins over stale orientation documentation when establishing current behavior.
- Unclear claims remain `Needs verification`; do not manufacture certainty.
- Do not scan the entire repository when focused context is sufficient.
- Do not mix feature work, refactoring, dependency upgrades, and unrelated cleanup in one bounded task.
- Characterization tests preserve evidence of current behavior; they do not automatically declare that behavior correct.
- `pr-review` reviews the coherent diff; it does not silently fix or approve the change.
- `publish-ai-mr` is a publication procedure only. It must not force-push, auto-approve, auto-merge, or create duplicate merge requests.
- Signing, store upload, production credentials, and release actions remain separately protected.

## Package installation

1. Read the canonical playbook in `playbook/BROWNFIELD_PLAYBOOK.md` or the DOCX edition.
2. Read `repository-starter/README.md` before copying starter workflow files.
3. Select and install the AGENTS template appropriate to the target platform/repository.
4. Copy only the reusable skills that fit the repository workflow.
5. Regenerate or adapt project-specific context, checkpoints, manifests, evidence paths, decisions, revisions, and status records.
6. Do not copy example project state as if it were current authority in a new repository.
