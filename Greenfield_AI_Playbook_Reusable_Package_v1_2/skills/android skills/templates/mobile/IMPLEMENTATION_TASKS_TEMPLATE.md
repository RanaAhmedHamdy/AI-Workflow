# {{FEATURE_NAME}} — Android Implementation Tasks

**Feature ID:** `{{FEATURE_ID}}`  
**Feature Contract:** `{{FEATURE_CONTRACT_PATH}}`  
**Implementation Plan:** `{{IMPLEMENTATION_PLAN_PATH}}`  
**Status:** Draft — task review required  
**Implementation Authorization:** NOT GRANTED

---

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

**Verification**
- Observable contract: {{OBSERVABLE_CONTRACT}}
- Test/evidence layer: {{TEST_LAYER}}
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
- [ ] Required machine-readable and runtime evidence exists.
- [ ] No prohibited scope or protected capability added.
- [ ] No release fake, bypass, or preview/test binding entered production composition.
- [ ] Task completion review passed.

**Authorization**
- May execute only after explicit implementation authorization is granted.

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
- [ ] Evidence commands, destinations, expected results, paths, and limitations are explicit.
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
