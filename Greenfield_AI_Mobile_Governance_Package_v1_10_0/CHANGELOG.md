# Changelog

## Unreleased product UX/routing

- Added progressive `skills`, `safety`, `feature`, and `full` adoption profiles; Safety is the installer default.
- Added the canonical routing registry, generated profile-aware context/first-safe-change documents, profile transition support, and the compact SMALL feature record.
- Retired three active Android aliases, preserving useful runtime guidance in the canonical procedure and documenting compatibility aliases.
- Expanded iOS implementation-plan authoring/review around concurrency isolation, scene/re-entry, target/configuration ownership, privacy/capabilities, accessibility, and archive evidence.

## 1.10.0

- Simplified the Design and Architecture operational READMEs into quick-start tables with exact prompts, explicit next-step links, and a 5-step architecture happy path; detailed architecture mechanics remain as reference material.
- Added direct root navigation links between Design Authority, Architecture Bootstrap, and Feature Delivery workflows.
- Added a compact optional Design Authority workflow with tool-neutral local-artifact guidance; design-tool MCP/connectors remain optional.
- Added `architecture-bootstrap` and `adr-lifecycle-governance` to both iOS and Android platform packs.
- Added explicit ADR lifecycle states for accepted amendments, provisional acceptance, deferral/rejection, and supersession; repository/project evidence can no longer be treated as automatic owner approval.
- Added architecture-bootstrap readiness (`READY FOR BOUNDED FEATURE INTAKE`) and clarified that the feature Implementation Readiness Gate cannot PASS before Feature Contract, Plan, and Tasks exist.
- Added bootstrap/feature modes to platform architecture/project-structure/coverage reviews and strengthened documentation consistency around provisional/superseded authority.
- Added low-cost Design Lock enforcement across Feature Input/Contract, iOS+Android Plans/Tasks, screen readiness, task review, and bounded implementation: design-bound UI must inspect the exact approved visual before coding and may not redesign under vague “more native” rationale.
- Kept post-hoc visual comparison optional by default to reduce tokens/time; one pre-code inspection per unchanged governing visual/task execution is the normal path.
- Added Android skill-package routing documentation parallel to iOS and cleaned package metadata from distribution output.

## Unreleased repository hardening

- Corrected iOS skill installation and routing documentation to use the self-contained `.agents/skills/ios/` package instead of a non-existent `shared/` directory.
- Updated the iOS skill-package heading and layout guidance to v1.9.1 and documented intentional platform-scoped duplicate skill names for Android/iOS standalone installation.
- Removed an accidental iOS `plist`/entitlement reference from the Android bounded implementation procedure.
- Added repository-level validation so macOS metadata and cross-platform routing leaks can be checked before public distribution. A repository CI workflow is not currently included.

## 1.9.1

- Expanded the root README into an operational start-here guide covering PRD-first repository bootstrap, Architecture Spine/ADR usage, architecture synchronization, canonical repository layout, and project-level versus feature-level artifacts.
- Clarified that GrillMe-style clarification may seed/refine Feature Input, but its output must be normalized into reviewed `FEATURE_INPUT.md` and cannot become product authority by itself.
- Updated the v2.2 playbook and governance pipeline to preserve Feature Input as the canonical intake before contract authoring.
- Added an architecture-template operational README and Feature Input provenance/clarification fields.
- Corrected the recommended repository layout to include `IMPLEMENTATION_READINESS_AUDIT.md` and all architecture/governance template families.

## 1.9

- Synchronized skills with v1.8+ evidence timing so bounded tasks no longer execute convergence/final-readiness checks by default.
- Centralized duplicated feature-delivery invariants into a shared policy module.
- Added conditional policy loading to reduce context/token overhead without weakening authority.
- Added coherent vertical task rules and removed the need for one task per UI concern.
- Added evidence reuse, compact long-running verification summaries, representative runtime matrices, and manual validation guidance.
- Made feature readiness review an independent spot-check of exhaustive convergence, with escalation on inconsistency/high risk.
- Added accurate convergence blocker taxonomy.
- Added automatic complexity-classification routing with safe default to COMPLEX.
- Updated pipeline/playbook to reflect the optimized governance path.


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
