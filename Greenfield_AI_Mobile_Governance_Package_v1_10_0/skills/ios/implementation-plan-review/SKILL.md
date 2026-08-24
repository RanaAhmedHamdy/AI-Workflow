---
name: implementation-plan-review
description: "Independently reviews an iOS implementation plan for contract fidelity, architecture, design traceability, persistence, adaptive UI, localization, accessibility, testing, evidence, and readiness honesty. Use before owner plan approval."
---

# Skill: Implementation Plan Review v1

## Purpose
Independently review an implementation plan for contract fidelity, architecture conformance, exact design traceability, persistence correctness, adaptive UI, localization, accessibility, testing, evidence, and readiness honesty.

## Verdicts
- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

PASS means ready for owner plan approval only.

## Required Inputs
Read the plan, owner-approved contract, feature input, feature map, decision register, architecture spine, applicable ADRs, feasibility evidence, readiness gate, design authority, screen contracts, artifact index, design system, information architecture, policy, and context router.

## Mandatory Review
1. Trace every module, state holder, repository, route, screen, test, and evidence item to contract requirements.
2. Fail untraced components, later-feature behavior, invented rules, or omitted requirements.
3. Verify Swift language/concurrency settings, deployment target, application/extension/widget/test target membership, resource build phases, scheme/configuration/xcconfig ownership, package products, and build/archive evidence. Fail a plan that assumes a file, privacy string, entitlement, resource, or configuration reaches the production target without evidence.
4. Verify dependency direction, a thin app/scene host, domain/presentation/persistence/platform separation, one production composition path, deterministic test/preview replacements, no persistence entities in views, no side effects in view bodies, accepted navigation/storage decisions, and no unapproved packages.
5. Verify each workflow names a UI-observable state owner, navigation owner, transient/durable reconstruction boundary, SwiftUI or UIKit lifecycle ownership, and restoration behavior. Fail duplicated mutable state, network/store ownership in a leaf view, sensitive route/restoration payloads, or stale restored identifiers without recovery.
6. Verify actor isolation, `@MainActor` UI-state ownership, `Sendable` crossings, task parent/lifetime/cancellation, structured versus unstructured work, async-sequence lifetime, continuation safety, error mapping, reentrancy, ordering, idempotency, and duplicate side-effect protection. Do not accept broad `@MainActor` merely to silence diagnostics; task isolation may inherit from context and must be intentional.
7. Verify persistence store ownership, disk-backed behavior, transaction boundaries, rollback, idempotency, migration, date attribution, historical stability, test isolation, backup/transfer, protection, sensitive-data separation, multi-writer isolation, and deletion/log-out claims.
8. Fail uniqueness-only deduplication without logical idempotency identity.
9. Verify scene activation/backgrounding, termination/relaunch, multiple-window, external-display, extension, background-task, and handoff behavior when applicable. The plan must not conflate view recreation, scene re-entry, relaunch, and backup restore.
10. Verify exact approved compact/wide visual artifacts are inspectable, design-bound mappings include a concise Design Lock/permitted adaptations, and unsupported content is excluded.
11. Verify applicable iPhone/iPad widths, Split View/Stage Manager, orientation, keyboard/safe-area/sheet/popover/toolbar behavior, pointer/keyboard input, overflow, and reflow preservation. Reject invented panes or generic “adaptive” claims.
12. Verify String Catalog/resource ownership, semantic error wording, locale-aware formatting, language/region launch, Arabic RTL, mixed-direction content, accessibility-string localization, and hardcoded-string scans.
13. Verify runtime plans for VoiceOver focus order (including sheets/split contexts), Dynamic Type including accessibility sizes, Bold Text, Differentiate Without Color, Button Shapes, Reduce Transparency, Increased Contrast, Reduce Motion, touch targets, custom controls, and errors.
14. Verify privacy usage descriptions/manifests, required-reason APIs, capability/entitlement ownership, extension restrictions, and archive/export/signing inspection whenever the route facts require them.
15. Verify evidence layers can prove claims; reject UI-only arithmetic, screenshot-only durability, static-only accessibility, missing test result bundles, destinations, paths, archive inspection, or limitations.
16. Fail task IDs, estimates, assignments, file-by-file checklists, production code, or generated migrations/schemas. Verify blocked gates are reported honestly and implementation is not authorized.

### Verification-Matrix Traceability and State Consistency

- Verify unique stable `VM-*` IDs cover every applicable runtime-only claim with an executable scenario.
- Verify every row traces to approved authority and does not invent behavior.
- Verify environment/destination, preconditions, expected observable result, evidence path, and method/limitation are concrete enough to execute.
- Search the complete artifact for lifecycle/status/approval/readiness/authorization assertions. If two assertions both claim to describe the current state and conflict, return a blocking finding. Historical stage verdicts are allowed only when clearly labeled as historical/stage-specific.

## Finding Format
Finding ID; severity; plan section; contract requirement; authority; problem; correction; verdict impact.

## Pass Criteria
All contract requirements mapped; no drift; ADRs applied; persistence matches audited evidence; design artifacts mapped; adaptive/localization/accessibility explicit; test/evidence sufficient; no tasks/code; unresolved decisions visible; readiness honest.

## Final Report
Verdict, traceability coverage, blocking findings, architecture drift, persistence findings, design/adaptive/localization/accessibility/test gaps, unresolved decisions, readiness implications, exact sections to revise, and statement that PASS means ready for owner plan approval only.

## Shared Feature Delivery Invariants

Read and apply `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` plus `templates/governance/FEATURE_COMPLEXITY_TIER_POLICY.md`. These shared rules govern complexity defaulting, origin-aware navigation, mutation-to-consumer coherence, recreated-consumer catch-up, vertical journey closure, evidence timing/reuse, and representative/manual runtime validation.
