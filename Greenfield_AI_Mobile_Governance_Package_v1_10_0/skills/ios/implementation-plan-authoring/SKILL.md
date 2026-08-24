---
name: implementation-plan-authoring
description: "Authors an architecture-aware, design-traceable, evidence-ready iOS implementation plan from an owner-approved feature contract. Use after contract approval and technical readiness; it creates the plan only, not production code or implementation tasks."
---

# Skill: Implementation Plan Authoring v1

## Purpose
Create an architecture-aware, design-traceable, evidence-ready implementation plan from an owner-approved feature contract. Do not create production code or tasks.

## Preconditions
Verify:
- feature contract is owner-approved;
- product clarifications are closed;
- applicable ADRs are accepted or explicitly provisional;
- required feasibility spikes passed independent verification;
- exact design authority exists.

If not, return a blocked verdict.

## Required Inputs
Read repository policy, context router, playbook, decision register, target contract, feature input, feature map, architecture spine, applicable ADRs, readiness gate, accepted feasibility evidence, design authority, screen contracts, artifact index, design system, information architecture, and localization/accessibility authority.

## Required Output
Create `docs/features/<feature-id>/IMPLEMENTATION_PLAN.md` using `.templates/mobile/ios/IMPLEMENTATION_PLAN_TEMPLATE.md`.

Return one:
- `READY FOR PLAN REVIEW`
- `BLOCKED BY TECHNICAL DECISION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

## Core Rules
1. Every planned target, module, type, state owner, store, route, scene, extension, test, and evidence item must trace to an approved contract requirement or a strictly necessary implementation responsibility. Do not add later-feature behavior or speculative infrastructure.
2. Accepted ADRs control Xcode/project generation, Swift language mode, deployment targets, package/dependency choices, architecture, persistence, navigation, test stack, privacy/capabilities, and build/archive decisions. Repository defaults are evidence, not approval.
3. State the allowed dependency direction and composition root. Separate presentation, domain, persistence, platform adapters, navigation, and app/scene host ownership. Views and view controllers must not construct clients, own persistence, or hide long-lived side effects.
4. For each SwiftUI route or UIKit workflow, name the owner of UI-observable state, navigation, transient state, durable reconstruction, user events, terminal states, preview/test replacements, and restoration. Do not add a ceremonial state holder to a static leaf, and do not duplicate mutable state between views, coordinators, and stores.
5. Plan Swift concurrency explicitly: actor isolation for mutable services; `@MainActor` ownership of UI-observable state; `Sendable` crossings; task parent/lifetime/cancellation; structured versus unstructured work; async-sequence lifetime; error mapping; reentrancy and duplicate-effect handling. A `Task` can inherit surrounding actor isolation, so state the intended isolation rather than assuming background execution. Detached work needs an explicit lifetime, cancellation, and captured-value rationale.
6. Plan scene/re-entry behavior distinctly: view recreation, navigation restoration, scene activation/backgrounding, termination/relaunch, multiple windows, external display, extension handoff, and device/backup restore. Never place sensitive payloads in route/restoration state; validate restored identifiers and recover from stale data safely.
7. Persistence plans must name system of record, entity/model ownership, mapping boundary, transactions/rollback, logical idempotency, migration/version ownership, failed-migration recovery, multi-writer/actor rules, test-store isolation, backup/transfer policy, file protection, sensitive-store separation, and logout/deletion behavior. Do not rely on uniqueness alone or overclaim forensic deletion.
8. Name exact application, extension, widget, intent, and test target membership; resource/build-phase ownership; scheme/configuration/xcconfig effects; local/external package products; entitlement/capability ownership; privacy manifest/usage-description implications; and archive/export/signing evidence where relevant. A source file compiling in one target does not prove the release target includes the intended resources or configuration.
9. For design-bound UI, cite and inspect exact approved visual artifacts and record a concise Design Lock: binding composition, hierarchy, grouping, action placement, and permitted adaptations. Map SwiftUI state/navigation ownership or UIKit controller/coordinator lifecycle to the approved behavior.
10. Adaptive plans cover applicable iPhone/iPad size classes, Split View/Stage Manager, orientation, sheets/popovers, safe areas, keyboard, toolbars/menus, pointer/keyboard input, overflow, and state preservation. Do not invent panes, breakpoints, or content not authorized by the design.
11. Localization and RTL start with the plan: String Catalog or other approved resource ownership, stable keys, plural/format rules, language/region launch, accessibility strings, semantic leading/trailing layout, mixed-direction values, and long-text behavior. Never concatenate translated sentence fragments.
12. Accessibility plans name Dynamic Type including accessibility sizes, VoiceOver labels/values/actions/headings and focus order (including sheets/split contexts), contrast/reduced-motion alternatives, custom-control semantics, and a runtime verification journey. Static previews, source review, and snapshots do not prove these claims.
13. Match each requirement to an appropriate test/evidence layer: Swift Testing/XCTest for deterministic behavior, UI/runtime evidence for navigation/lifecycle, simulator/device/manual evidence for accessibility/adaptive/localization, and archive/configuration inspection for release-sensitive claims. Define implementation order only; do not generate tasks, estimates, assignments, code, or implementation authorization.

### Verification Matrix and Current-State Integrity

- Define a compact verification matrix inside `IMPLEMENTATION_PLAN.md` using stable unique IDs such as `VM-001`.
- Each applicable row must identify the approved requirement/claim, executable scenario, environment/destination, required preconditions, expected observable result, evidence path, and verification method or known limitation.
- Runtime-only claims must map to runtime-capable evidence. Do not create a separate verification artifact solely for this matrix.
- Treat `VM-*` rows as planned verification definitions, not a second lifecycle state machine; do not add per-row `READY`/`PASS` workflow statuses during plan authoring.
- Keep current lifecycle/status/authorization truth in one canonical status block. Historical authoring/review verdicts may remain only when clearly labeled as stage-specific history. Never emit incompatible current-state assertions in the same artifact.

## Mandatory Sections
Authority/status; scope/exclusions; assumptions; traceability; project/target/configuration ownership; architecture/dependency direction; composition; domain; persistence/migration; actor isolation/concurrency; presentation state; SwiftUI/UIKit ownership; navigation; scenes/re-entry/restoration; background/extensions; privacy/capabilities/entitlements; screen mapping; adaptive UI; localization/RTL; accessibility; error/recovery/offline/cancellation; tests; runtime/archive evidence; dependency order; risks; unresolved decisions; readiness; prohibited patterns; documentation impact.

## Stop Conditions
Stop when the contract is not owner-approved, product behavior remains unresolved, ADRs conflict, required spike evidence is not independently verified, exact design authority is missing, target/capability ownership is unknown, or planning would require invented behavior.

## Completion Report
Report files read, plan path, requirements mapped, modules proposed, exact artifacts mapped, ADRs applied, risks, unresolved decisions, readiness implications, verdict, and confirmation that no code or tasks were created.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
