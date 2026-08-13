# Changelog

## 1.7

- Expanded `FEATURE_INPUT_TEMPLATE.md` so journey intent is captured before contract authoring: invocation context/mode, exact success/cancel/failure outcomes, durable mutation → affected-consumer expectations, critical vertical journeys, and lifecycle/re-entry behavior.
- Added Feature Input complexity/risk signals without allowing the input author to self-assign SMALL/STANDARD/COMPLEX.
- Updated iOS and Android `feature-complexity-classification` skills to verify Feature Input signals and never treat blank/legacy signal lists as evidence for a lower tier.
- Updated iOS and Android `feature-contract-authoring` skills to preserve origin-sensitive behavior for reused screens, consumer effects, vertical journeys, and inactive/recreated-consumer expectations.
- Updated iOS and Android `feature-contract-review` skills to block state-transition aliasing, ambiguous post-action destinations, missing consumer/re-entry coverage, and disagreement between reachability/state/acceptance journeys.
- Retained the fail-safe rule: if complexity classification is not run, cannot complete, or is missing/invalid/stale, downstream work defaults to **COMPLEX**.
- Updated README and complexity-tier policy to make Feature Input the product-level journey authority while keeping implementation mechanisms in downstream plans.
- Carried lifecycle catch-up through contract/plan/task templates and platform implementation/readiness skills so consumers recreated after a mutation cannot rely solely on having observed the original event.

## 1.6

- Added platform-specific `feature-complexity-classification` skills under both `skills/ios/` and `skills/android/`.
- Added shared `FEATURE_COMPLEXITY_TIER_POLICY.md` with SMALL, STANDARD, and COMPLEX scoring, hard COMPLEX triggers, and task-depth guidance.
- Defined a fail-safe default: if classification was not run, is missing, invalid, or stale, downstream work defaults to **COMPLEX**.
- Made feature contract, implementation plan, implementation tasks, authoring/review skills, bounded implementation, and convergence tier-aware without duplicating template families.
- Added mandatory mutation-to-consumer propagation analysis and verification so successful durable writes refresh affected cross-feature consumers.
- Added entry-context-aware post-save/cancel/failure navigation semantics to prevent management flows from incorrectly entering onboarding or another origin.
- Added vertical journey closure at bounded-task completion for committable slices: commit → consumer refresh → correct destination.
- Updated README lifecycle, supporting-skill routing, package structure, and complexity-tier guidance.

## 1.5

- Added stable `VM-*` verification IDs inside implementation plans without introducing separate verification artifacts or per-scenario lifecycle bureaucracy.
- Implementation tasks now map bounded work to approved `VM-*` IDs instead of repeating full verification-matrix prose.
- Plan/task reviews now block contradictory current lifecycle, approval, readiness, or implementation-authorization assertions within the same artifact.
- Runtime-evidence readiness now checks `VM-*` scenario executability before evidence collection.
- Feature implementation convergence now verifies whole-feature `VM-*` evidence closure once, without duplicating bounded implementation.
- Updated implementation plan/task templates with canonical current-state fields and verification-ID mapping.
- README now includes an ordered how-to-use-the-skills lifecycle table.


## 1.4

- Added platform-specific `bounded-feature-implementation` skills for iOS and Android.
- Defined implementation as an explicitly authorized production-mutation procedure with task-local verification and evidence closure.
- Kept `feature-implementation-convergence` independent and whole-feature in scope; implementation does not duplicate its broad post-implementation audit or create `READINESS_REPORT.md`.
- Updated the canonical lifecycle, modular policies, platform procedure routing, task template, package README, governance pipeline, and agent-native playbook.
- Retained earlier playbook editions unchanged.

## 1.3

- Removed broken hook configuration.
- Removed macOS metadata.
- Updated package README.
- Retained both playbooks; updated v2.0 agent-native lifecycle and canonical filenames.
- Added pre-implementation readiness audit distinction.
- Normalized Android and iOS skill directories while keeping platform-specific same-named skills separate.
- Added missing Android coroutine, persistence/migration, permission/capability, and Views readiness procedures.
- Moved reusable feature templates outside skill folders.
- Moved architecture and readiness templates under `templates/architecture/`.
- Moved superseded policies to `historical/policies/`.
- Added AI context, decision register, feature input, and implementation readiness audit templates.
- Updated iOS installation/routing documentation away from old AGENTS and Spec Kit references.
