# {{FEATURE_NAME}} — Android Implementation Tasks

**Feature ID:** `{{FEATURE_ID}}`  
**Feature Contract:** `{{FEATURE_CONTRACT_PATH}}`  
**Implementation Plan:** `{{IMPLEMENTATION_PLAN_PATH}}`  
**Feature Tier:** `{{SMALL_STANDARD_COMPLEX}}`  
**Classification Status:** `{{EXECUTED_OR_DEFAULTED_TO_COMPLEX}}`  
**Status:** Draft — task review required  
**Implementation Authorization:** NOT GRANTED  
**Execution Procedure:** `bounded-feature-implementation` after explicit authorization

---

Header status fields above are summary mirrors only. The canonical current-state fields live in this status section; if a mirror and canonical field disagree, the artifact is inconsistent and must fail review.

## 1. Task-Set Authority and Status

### 1.1 Authority

1. Current explicit owner direction.
2. Root repository policy and protected boundaries.
3. Approved owner decisions.
4. Owner-approved feature contract.
5. Owner-approved implementation plan.
6. Accepted Android architecture spine and applicable ADRs.
7. Approved design authority and exact artifacts.
8. Readiness gates and verified evidence.
9. Context router, playbook, and skills.

### 1.2 Status

- Task authoring verdict: `{{AUTHORING_VERDICT}}`
- Task review verdict: `{{REVIEW_VERDICT}}`
- Owner approval: `PENDING`
- Implementation authorization: `NOT GRANTED`
- Current lifecycle state: `TASK DRAFT`

---

## 2. Scope Boundary

### 2.1 In Scope

{{IN_SCOPE}}

### 2.2 Explicitly Excluded

{{EXCLUSIONS}}

---

## 3. Dependency Graph

| Task ID | Depends On | Unlocks | Blocking Gate |
|---|---|---|---|
| {{TASK_ID}} | {{DEPENDENCIES}} | {{UNLOCKS}} | {{GATE}} |

No circular or hidden dependencies are allowed.

---

## 4. Implementation Tasks

### {{TASK_ID}} — {{TASK_TITLE}}

**Objective**  
{{OBJECTIVE}}

**Contract traceability**
- {{CONTRACT_REQUIREMENT}}

**Plan traceability**
- {{PLAN_SECTION}}

**Android architecture/design authority**
- {{ADR_OR_DESIGN_REFERENCE}}

**Depends on**
- {{DEPENDENCY}}

**Allowed scope**
- {{ALLOWED_SCOPE}}

**Prohibited scope**
- {{PROHIBITED_SCOPE}}

**Implementation notes**
- {{IMPLEMENTATION_NOTES}}

Implementation notes may apply approved architecture but must not reopen decisions or add behavior.

**Acceptance criteria**
1. {{CRITERION}}
2. {{CRITERION}}

**Verification Matrix Coverage**
- {{VM_ID_OR_NA}}

Use only `VM-*` IDs defined by the approved implementation plan. Do not duplicate the full matrix scenario here. Use `N/A — {{RATIONALE}}` only when no plan scenario applies.

**Verification**
- Observable contract: {{OBSERVABLE_CONTRACT}}
- Test/evidence layer: {{TEST_LAYER}}
- Verification timing: {{TASK_CLOSURE_FEATURE_CONVERGENCE_FINAL_READINESS}}
- Blocking scope: {{TASK_ID_OR_GATE}}
- Evidence cost class: {{LOW_MEDIUM_HIGH}}
- Exact procedure/command: {{PROCEDURE}}
- Destination/environment: {{DESTINATION}}
- Expected result: {{EXPECTED_RESULT}}
- Evidence path: {{EVIDENCE_PATH}}
- Limitation: {{LIMITATION}}

**Completion gate**
- [ ] Contract requirements satisfied.
- [ ] Plan boundaries preserved.
- [ ] Applicable Android architecture rules preserved.
- [ ] Applicable tests pass.
- [ ] All applicable `TASK-CLOSURE` machine-readable/runtime evidence exists. Deferred `FEATURE-CONVERGENCE` / `FINAL-READINESS` evidence is explicitly referenced but does not block this bounded task unless this task owns that gate.
- [ ] No prohibited scope or protected capability added.
- [ ] No release fake, bypass, or preview/test binding entered production composition.
- [ ] Task completion review passed.
- [ ] Every durable mutation in this task identifies and refreshes all affected consumers, or records why no consumer update is expected.
- [ ] Every user-committable vertical slice proves commit → consumer refresh → correct entry-context destination before task closure.
- [ ] Save/cancel/failure navigation is verified for each applicable entry/presentation context; normal management cannot accidentally execute onboarding/setup completion.

**Authorization**
- May execute only after explicit implementation authorization is granted.
- Execute through `bounded-feature-implementation` (or repository-equivalent) for the exact authorized task group; whole-feature convergence remains separate.

---

## 5. Required Android Task Families

Include only applicable families, but do not omit an applicable responsibility.

### 5.1 Module, Source-Set, Resource, and Manifest Structure

{{STRUCTURE_TASKS}}

### 5.2 Domain Models and Invariants

{{DOMAIN_TASKS}}

### 5.3 Dependency Composition / DI

{{DI_TASKS}}

### 5.4 Persistence, Migration, and Data Integrity

{{PERSISTENCE_TASKS}}

### 5.5 Use Cases and Repository Integration

{{USE_CASE_TASKS}}

### 5.6 ViewModel, Presentation State, Coroutines, and Flow

{{PRESENTATION_TASKS}}

### 5.7 Navigation, Back Behavior, Lifecycle, and Restoration

{{NAVIGATION_LIFECYCLE_TASKS}}

### 5.8 Compose / View Screen Implementation and Previews

{{UI_TASKS}}

### 5.9 Localization and Approved RTL Locales

{{LOCALIZATION_TASKS}}

### 5.10 Accessibility

{{ACCESSIBILITY_TASKS}}

### 5.11 Adaptive, Resizable, Foldable, IME, and Insets

{{ADAPTIVE_TASKS}}

### 5.12 Permissions, Manifest Components, Privacy, and Background Work

{{PRIVACY_CAPABILITY_TASKS}}

### 5.13 CI, Emulator/Device Runtime, and Release Evidence

{{CI_EVIDENCE_TASKS}}

---

## 6. UI Task Mandatory Checks

Every applicable route/screen task must state:

- [ ] Exact screen contract and artifact IDs.
- [ ] Route/container versus stateless/render boundary.
- [ ] ViewModel/state-holder owner and lifetime where workflow state requires one.
- [ ] Immutable UI state and explicit event interface.
- [ ] No repositories, DAOs, clients, permission managers, billing services, or routers in leaf UI.
- [ ] No side effects during Compose composition or view rendering/binding.
- [ ] No state-holder recreation during recomposition.
- [ ] Loading, empty, populated, disabled, failure, recovery, offline, and success states as applicable.
- [ ] Deterministic previews for representative states where the selected UI toolkit supports them.
- [ ] Previews are not treated as runtime evidence.
- [ ] Compact, medium, expanded, split/resized, orientation, and fold/posture behavior as applicable.
- [ ] IME, edge-to-edge, system bars, cutouts, hinges, insets, scrolling, and overflow.
- [ ] Localized strings, plurals, formatting, RTL, mixed-direction text, and long translations.
- [ ] TalkBack semantics, focus, text/display scaling, touch targets, alternative input, and announcements.

---

## 7. ViewModel, Coroutine, and DI Mandatory Checks

Applicable tasks must ensure:

- [ ] Lifecycle-aware state ownership.
- [ ] No ceremonial ViewModel for static leaf UI.
- [ ] No duplicate mutable state across Activity, Fragment, ViewModel, composable, and saved state.
- [ ] Structured concurrency and explicit scope ownership.
- [ ] Dispatcher ownership/injection follows architecture.
- [ ] Lifecycle-aware Flow collection.
- [ ] Cancellation propagates correctly.
- [ ] Durable work is not cancelled solely because UI disappears.
- [ ] No `GlobalScope`, unowned jobs, fire-and-forget calls, or swallowed errors.
- [ ] One approved production dependency-composition path.
- [ ] Deterministic test and preview replacements.
- [ ] No service locator/global singleton/ad hoc UI construction.
- [ ] No fake/debug/test binding in release composition.

---

## 8. Persistence Mandatory Checks

Applicable tasks must ensure:

- [ ] Schema/entity/version ownership.
- [ ] Repository, DAO, data-source, and domain-mapping boundaries.
- [ ] Disk-backed release behavior.
- [ ] Transactions and rollback.
- [ ] Logical idempotency and duplicate prevention.
- [ ] Migration initialization, fixtures, and failed-migration recovery.
- [ ] Date attribution and historical stability.
- [ ] Concurrency/single-writer rules.
- [ ] Test database/store isolation.
- [ ] Backup, restore, transfer, and sensitive-storage policy.
- [ ] Deletion/logout/account-removal behavior.
- [ ] Activity recreation, process death, app relaunch, reboot, and backup restore are not conflated.
- [ ] No uniqueness-only idempotency claim.
- [ ] No forensic deletion overclaim.

---

## 9. Permission and Protected-Boundary Mandatory Checks

Applicable tasks must ensure:

- [ ] Explicit owner-approved permission/capability scope.
- [ ] Manifest and runtime ownership.
- [ ] Denial, revocation, and settings recovery.
- [ ] Exported components and intent filters audited.
- [ ] App links/deep links verified when approved.
- [ ] Services, receivers, providers, foreground-service types, notifications, alarms, and WorkManager explicitly authorized.
- [ ] Health Connect, camera, microphone, media, location, Bluetooth, contacts, calendar, billing, authentication, and attestation are not inferred from imports.
- [ ] Data minimization, redaction, retention, backup, deletion, and dependency-manifest review.
- [ ] Missing configuration fails closed.
- [ ] Release artifacts are inspected before compliance or release claims.

---

## 10. Final Convergence Tasks

{{CONVERGENCE_TASKS}}

At minimum include applicable tasks for:

Deferred evidence rule: convergence/final-readiness tasks own expensive cross-cutting checks that were intentionally not task-closing evidence. One existing artifact may satisfy multiple VM rows when it contains the required scenarios; do not create redundant reruns solely for unique artifact names.

Task-coherence rule: every applicable concern must have explicit ownership, but it does not require its own task. Prefer coherent vertical tasks when state, route, rendering, resources, accessibility/adaptation, and focused verification share one implementation boundary. Split only for real dependency, risk, authorization, ownership, or review value.

Manual-validation rule: assign subjective/device-only validation to convergence/final-readiness where appropriate; keep deterministic task-closing tests for navigation, mutation propagation, domain/data correctness, atomicity, idempotency, and migrations.

- contract-to-implementation traceability review;
- Android toolchain/module/source-set conformance;
- architecture and dependency-direction review;
- DI/composition review;
- ViewModel/state/coroutine/Flow/lifecycle review;
- navigation/back/restoration review;
- exact design conformance;
- localization and approved RTL runtime;
- TalkBack/accessibility runtime;
- adaptive/resizable/foldable/IME/insets runtime;
- persistence/migration/process-death/relaunch review;
- permission/manifest/privacy/background/network review;
- production-fake and release-graph review;
- documentation synchronization;
- clean CI and current Android-native machine-readable test, lint, manifest, and runtime artifacts;
- APK/AAB/R8/signing inspection where applicable.

---

## 11. Deferred and Later-Feature Items

{{DEFERRED_ITEMS}}

---

## 12. Task Review Checklist

- [ ] Every task traces to the approved contract and plan.
- [ ] Each task has one bounded outcome.
- [ ] Dependencies are explicit and acyclic.
- [ ] No later-feature behavior is included.
- [ ] No task reopens accepted Android architecture.
- [ ] No task grants implementation authorization.
- [ ] Module/source/resource/manifest changes are bounded and authorized.
- [ ] ViewModel/state ownership is explicit where required and not ceremonial.
- [ ] DI/composition is explicit; no service locator or ad hoc UI construction.
- [ ] Coroutine/Flow ownership, cancellation, and terminal states are explicit.
- [ ] Persistence includes rollback, logical idempotency, migration, relaunch, and process-death evidence where applicable.
- [ ] UI maps to exact screen contracts and artifacts.
- [ ] Previews exist for representative states where supported but are not runtime evidence.
- [ ] Localization, approved RTL locales, accessibility, and adaptation are not deferred to cleanup.
- [ ] Permission/manifest/background/protected boundaries are explicit and owner-authorized.
- [ ] Evidence commands, destinations, expected results, paths, limitations, timing, blocking scope, and cost class are explicit.
- [ ] Expensive unrelated runtime checks are not made task-blocking merely because they are required before final readiness.
- [ ] Existing valid evidence is reused across VM rows where coverage is real and traceable.
- [ ] Final convergence tasks are present.
- [ ] No production code, tests, Gradle files, manifests, resources, schemas, migrations, or permissions were generated by task authoring.

---

## 13. Final Verdict

**Task authoring verdict:** `{{AUTHORING_VERDICT}}`

Allowed values:

- `READY FOR TASK REVIEW`
- `BLOCKED BY PLAN ISSUE`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

This task set does not authorize implementation.


## Tier-Aware Task Sizing and Closure

- SMALL: prefer 2–5 coherent tasks. Do not create placeholder task families for non-applicable concerns.
- STANDARD: prefer 5–10 coherent tasks and ensure cross-feature propagation/navigation integration has an explicit owner.
- COMPLEX: use as many dependency-bounded tasks as needed (often 10–20+) for migration, protected boundaries, concurrency/idempotency, lifecycle/recovery, runtime evidence, and convergence.
- Counts are guidance only. Never split or merge work solely to match a number.
- If complexity classification was not executed or is missing/invalid/stale, generate tasks under COMPLEX obligations.

### Mandatory Mutation Propagation Task Check

For each persistent mutation implemented by a task, name: authoritative write, affected consumer(s), active-consumer refresh/invalidation mechanism, inactive/recreated-consumer catch-up mechanism when applicable, expected timing, stale-state failure mode, and executable verification. A repository test alone cannot close a user-visible cross-feature mutation.

### Mandatory Origin-Sensitive Navigation Task Check

For each save/commit/cancel path reachable from multiple origins (for example Home, Settings, onboarding/setup, restored route), verify the destination/result separately for every origin. Shared feature UI may be reused; completion semantics may not be conflated. If a reusable screen has distinct modes, the task must not map one mode into another mode's return state simply because they share rendering.
