# {{FEATURE_NAME}} — iOS/iPadOS Implementation Plan

**Feature ID:** `{{FEATURE_ID}}`  
**Feature Contract:** `{{FEATURE_CONTRACT_PATH}}`  
**Feature Tier:** `{{SMALL_STANDARD_COMPLEX}}`  
**Classification Status:** `{{EXECUTED_OR_DEFAULTED_TO_COMPLEX}}`  
**Status:** Draft — plan review required  
**Implementation Authorization:** NOT GRANTED

Header status fields above are summary mirrors only. The canonical current-state fields live in this status section; if a mirror and canonical field disagree, the artifact is inconsistent and must fail review.

## 1. Authority and Status

- Authoring verdict: `{{AUTHORING_VERDICT}}`
- Review verdict: `{{REVIEW_VERDICT}}`
- Owner approval: `PENDING`
- Implementation authorization: `NOT GRANTED`
- Current lifecycle state: `PLAN DRAFT`
- iOS/iPadOS architecture baseline: {{IOS_ARCHITECTURE_BASELINE}}

Current lifecycle state and implementation authorization are canonical current-state fields. Historical authoring/review verdicts are stage-specific history and must never contradict these current-state fields.

## 2. Scope and Exclusions

### In Scope

{{IN_SCOPE}}

### Explicitly Excluded

{{EXCLUSIONS}}

## 3. Assumptions and Preconditions

| ID | Assumption / Precondition | Source | Status | Blocking Impact |
|---|---|---|---|---|
| AP-001 | {{ASSUMPTION}} | {{SOURCE}} | Confirmed / Needs verification | {{IMPACT}} |

Unchecked assumptions must not become implementation choices.

## 4. Requirements-to-Plan Traceability

| Contract Requirement | Planned Component / Responsibility | Design Reference | iOS ADR Constraint | Test Layer(s) | Evidence |
|---|---|---|---|---|---|
| {{REQ_ID}} | {{COMPONENT}} | {{DESIGN_REF}} | {{ADR_REF}} | {{TEST_LAYER}} | {{EVIDENCE}} |

## 5. Apple Toolchain and Build Baseline

| Concern | Accepted Decision | Authority | Feature Impact |
|---|---|---|---|
| Xcode / SDK | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
| Swift language mode / strict concurrency | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
| Deployment target / supported platforms | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
| Bundle identifier / module name | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
| Build configurations / schemes / test plans | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
| CI entry command | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |

## 6. Architecture Mapping

### Feature Boundary

{{FEATURE_BOUNDARY}}

### Dependency Direction

{{DEPENDENCY_DIRECTION}}

### Protected Boundaries

{{PROTECTED_BOUNDARIES}}

### Prohibited Cross-Layer Dependencies

{{PROHIBITED_DEPENDENCIES}}

## 7. Target, Module, Source, Resource, and Capability Ownership

| Target / Module / Resource Owner | Responsibility | Allowed Dependencies | Prohibited Responsibilities |
|---|---|---|---|
| {{MODULE}} | {{RESPONSIBILITY}} | {{ALLOWED}} | {{PROHIBITED}} |

Do not create targets, local packages, frameworks, or shared abstractions merely for template compliance.

## 8. Domain Model and Value Semantics

| Domain Type | Responsibility | Invariants | Apple Framework Exposure | Persistence Exposure |
|---|---|---|---|---|
| {{TYPE}} | {{RESPONSIBILITY}} | {{INVARIANTS}} | None / Explicitly approved | None / Adapter-only |

## 9. Dependency Composition

### Accepted Composition / DI Architecture

{{DI_ARCHITECTURE}}

### Production Composition Root

{{PRODUCTION_COMPOSITION}}

### Feature Scopes and Lifetimes

{{FEATURE_SCOPES}}

### Test Replacement

{{TEST_COMPOSITION}}

### Preview / Design-Time Replacement

{{PREVIEW_COMPOSITION}}

### Missing-Configuration Fail-Closed Behavior

{{DI_FAIL_CLOSED}}

## 10. Persistence Design

### Accepted Architecture

{{PERSISTENCE_ARCHITECTURE}}

### System of Record and Schema Ownership

{{SYSTEM_OF_RECORD}}

### Repository, Persistence Adapter, and Data-Source Boundaries

{{REPOSITORY_BOUNDARIES}}

### Domain Mapping

{{DOMAIN_MAPPING}}

### Transactions and Atomicity

{{TRANSACTION_RULES}}

### Duplicate Prevention and Logical Idempotency

{{IDEMPOTENCY_RULES}}

### Migration, Versioning, and Failed-Migration Recovery

{{MIGRATION_RULES}}

### Date Attribution and Historical Integrity

{{DATE_RULES}}

### Concurrency and Single-Writer Rules

{{PERSISTENCE_CONCURRENCY}}

### Backup, Restore, Device Transfer, and Sensitive Data Separation

{{SENSITIVE_DATA_RULES}}

### Test Store and Production Migration Fixtures

{{PERSISTENCE_TEST_PLAN}}

## 11. Presentation State and Swift Observation Design

| Observable State Holder | Lifetime Owner | Owned State | Inputs | Events / Outputs | Execution / Isolation Boundary | Reconstruction Source |
|---|---|---|---|---|---|---|
| {{STATE_HOLDER}} | {{LIFETIME}} | {{STATE}} | {{INPUTS}} | {{OUTPUTS}} | {{BOUNDARY}} | {{RECONSTRUCTION}} |

### State Rules

{{STATE_RULES}}

Route-level workflows use an approved lifecycle-aware observable state holder when state spans view recomputation, asynchronous work, validation, navigation, recreation, or durable recovery. Static leaf UI does not require ceremonial observable owners.

## 12. Swift Concurrency and Async Sequence Design

### Scope Ownership

{{SCOPE_OWNERSHIP}}

### Executor / Actor Ownership

{{EXECUTOR_ACTOR_PLAN}}

### Observation / Async Sequence Exposure and Lifecycle-Aware Consumption

{{OBSERVATION_ASYNC_SEQUENCE_PLAN}}

### Cancellation and Durable Work

{{CANCELLATION_PLAN}}

### Ordering, Retry, Reentrancy, and Duplicate Side Effects

{{ORDERING_IDEMPOTENCY_PLAN}}

### Error Mapping and Terminal States

{{ASYNC_ERROR_PLAN}}

Prohibit unowned `Task` instances, unjustified `Task.detached`, swallowed exceptions, and fire-and-forget production work.

## 13. Lifecycle, Recreation, and Restoration

### View Recalculation and Local UI State

{{VIEW_RECALCULATION_STATE}}

### Scene/View Recreation and Adaptive Reflow

{{SCENE_RECREATION}}

### Navigation Restoration State

{{NAV_RESTORATION_STATE}}

### Process Death and App Relaunch

{{PROCESS_DEATH_RELAUNCH}}

### Device Reboot, Backup Restore, and Transfer Boundaries

{{REBOOT_BACKUP_TRANSFER}}

### Stale Restoration Recovery

{{STALE_RESTORATION}}

Keep each lifecycle class distinct. Do not store sensitive payloads in route arguments or restoration payloads.

## 14. Navigation and Back Behavior

{{NAVIGATION_PLAN}}

### Entry-Context Result Semantics

| Entry Context / Presentation Mode | Save/Commit Success | Cancel/Back | Failure | Forbidden Destination |
|---|---|---|---|---|
| {{ENTRY_CONTEXT}} | {{SUCCESS_RESULT}} | {{CANCEL_RESULT}} | {{FAILURE_RESULT}} | {{FORBIDDEN_DESTINATION}} |

Normal management, Settings, Home, onboarding/setup, restored, modal, and split-view contexts must not share an ambiguous post-save route. Generic `dismiss()` is insufficient unless the route owner proves the correct origin-sensitive result.

Include top-level destinations, route ownership, minimal arguments, adaptive navigation, system back/dismissal gestures, modal/dialog behavior, universal/deep links if approved, discard protection, and restoration.

## 15. Screen-by-Screen Mapping

### {{SCREEN_CONTRACT_ID}} — {{SCREEN_NAME}}

- Design binding: DESIGN-BOUND / NOT DESIGN-BOUND
- Exact approved visual artifacts/paths: {{ARTIFACT_IDS_AND_PATHS}}
- Required variants/states: {{REQUIRED_VARIANTS}}
- Design Lock — preserve: {{COMPOSITION_HIERARCHY_GROUPING_ACTION_PLACEMENT}}
- Permitted adaptations: {{PLATFORM_ACCESSIBILITY_LOCALIZATION_RESPONSIVE_OR_OWNER_APPROVED_ONLY}}
- Contract requirements: {{REQUIREMENTS}}
- Route/container boundary: {{ROUTE_BOUNDARY}}
- Render/content boundary: {{CONTENT_BOUNDARY}}
- observable state holder/state holder: {{STATE_HOLDER}}
- Composition: {{COMPOSITION}}
- State mapping: {{STATE_MAPPING}}
- Actions/events: {{ACTIONS}}
- Failure/recovery/offline: {{FAILURE_RECOVERY}}
- Preview fixtures: {{PREVIEW_FIXTURES}}
- Unsupported content excluded: {{EXCLUDED_CONTENT}}
- Runtime stop conditions: {{STOP_CONDITIONS}}

## 16. Adaptive and Resizable UI Plan

### Compact Window

{{COMPACT_PLAN}}

### Medium Window

{{MEDIUM_PLAN}}

### Expanded Window / Tablet

{{EXPANDED_PLAN}}

### Split View, Multitasking, and Reduced Width

{{REDUCED_WIDTH_PLAN}}

### iPad Multitasking and Window Reconfiguration

{{IPAD_MULTITASKING_PLAN}}

### Orientation

{{ORIENTATION_PLAN}}

### Software Keyboard, Safe Areas, System Bars, Insets, and Overflow

{{KEYBOARD_SAFE_AREA_INSETS_PLAN}}

### Hardware Keyboard, Mouse, Trackpad, and Pointer Where In Scope

{{ALTERNATIVE_INPUT_PLAN}}

### State Preservation During Reflow

{{REFLOW_STATE_PLAN}}

## 17. Localization and RTL Plan

### String Resource Ownership

{{STRING_PLAN}}

### Plurals, Substitutions, and Grammar

{{PLURAL_PLAN}}

### Locale-Aware Formatting

{{FORMATTING_PLAN}}

### RTL and Bidirectional Content

{{RTL_PLAN}}

### Long Translation and Pseudo-Locale Verification

{{TEXT_EXPANSION_PLAN}}

### Notifications, Widgets, Shortcuts, Errors, and Background-Visible Text

{{BACKGROUND_TEXT_PLAN}}

### Hardcoded-String and Stale-Key Prevention

{{STRING_SCAN_PLAN}}

## 18. Accessibility Plan

| Capability | Implementation Responsibility | Runtime Verification |
|---|---|---|
| VoiceOver semantics and traversal | {{PLAN}} | {{VERIFY}} |
| Focus order and restoration | {{PLAN}} | {{VERIFY}} |
| Font scaling and text reflow | {{PLAN}} | {{VERIFY}} |
| Dynamic Type, Bold Text, and magnification | {{PLAN}} | {{VERIFY}} |
| Non-color differentiation | {{PLAN}} | {{VERIFY}} |
| Reduced/removed animations | {{PLAN}} | {{VERIFY}} |
| Contrast and visual adaptation | {{PLAN}} | {{VERIFY}} |
| Touch targets | {{PLAN}} | {{VERIFY}} |
| Hardware keyboard and pointer | {{PLAN}} | {{VERIFY}} |
| Switch Control | {{PLAN}} | {{VERIFY}} |
| Voice Control | {{PLAN}} | {{VERIFY}} |
| Error/state announcements | {{PLAN}} | {{VERIFY}} |
| Custom-control semantics | {{PLAN}} | {{VERIFY}} |

## 19. Error, Recovery, Offline, and Cancellation Design

{{ERROR_RECOVERY_PLAN}}

## 20. Permissions, Entitlements, Privacy Manifest, and Protected Capabilities

| Boundary | Entitlement / Runtime Ownership | Denial / Revocation / Failure Behavior | Evidence | Stop Condition |
|---|---|---|---|---|
| {{BOUNDARY}} | {{OWNERSHIP}} | {{FAILURE_BEHAVIOR}} | {{EVIDENCE}} | {{STOP}} |

Address applicable usage-description keys, entitlements, associated/universal links, background modes, notifications, HealthKit, camera/microphone/media/location/Bluetooth access, StoreKit, authentication, App Attest/DeviceCheck, analytics/crash reporting, privacy manifests, backup, retention, deletion, redaction, and release configuration.

## 20A. Mutation → Consumer Propagation

Required for STANDARD and COMPLEX and whenever a SMALL feature mutates durable state observed outside its local screen.

| Mutation | Authoritative Write | Affected Consumers | Active-Consumer Invalidation / Observation | Inactive / Recreated Consumer Catch-up | Expected Timing | Stale-State Risk | Verification |
|---|---|---|---|---|---|---|---|
| {{MUTATION}} | {{WRITE_BOUNDARY}} | {{CONSUMERS}} | {{ACTIVE_UPDATE_MECHANISM}} | {{REENTRY_CATCHUP_MECHANISM}} | {{TIMING}} | {{STALE_RISK}} | {{VM_ID_OR_SCENARIO}} |

For every durable mutation, trace producer → committed source of truth → resolver/read model → every affected visible consumer. Also define how a consumer that was inactive, destroyed, or reconstructed after the commit obtains the latest authoritative state. Do not accept local state replacement, navigation-triggered accidental reload, or app relaunch as the only refresh mechanism unless explicitly required by authority.

### Vertical Journey Closure

Every user-committable slice must have at least one executable journey proving: `commit → durable success → affected consumer refresh → correct origin-sensitive destination`. Where re-entry/recreation is material, include a journey proving a consumer that did not observe the original event still loads the latest committed state. Where a mutation intentionally does not affect a consumer, record that invariant and test it.

## 21. Testing Strategy

| Layer | Scope | Required Scenarios | Environment / Destination | Machine-Readable Output |
|---|---|---|---|---|
| Swift Testing / XCTest domain-unit | {{SCOPE}} | {{SCENARIOS}} | Host / iOS Simulator | {{OUTPUT}} |
| Observation/presentation state | {{SCOPE}} | {{SCENARIOS}} | MainActor test harness / iOS Simulator | {{OUTPUT}} |
| Repository/integration | {{SCOPE}} | {{SCENARIOS}} | Host / disk-backed / instrumented as required | {{OUTPUT}} |
| Persistence migration/relaunch | {{SCOPE}} | {{SCENARIOS}} | Host harness / iOS Simulator / device | {{OUTPUT}} |
| XCUITest / SwiftUI UI automation | {{SCOPE}} | {{SCENARIOS}} | iOS Simulator / device | {{OUTPUT}} |
| Scene recreation/process termination | {{SCOPE}} | {{SCENARIOS}} | iOS Simulator / device | {{OUTPUT}} |
| VoiceOver accessibility runtime | {{SCOPE}} | {{SCENARIOS}} | iOS Simulator / device / manual | {{OUTPUT}} |
| RTL/pseudo-locale/adaptive/iPad multitasking | {{SCOPE}} | {{SCENARIOS}} | iPhone/iPad Simulator / device | {{OUTPUT}} |
| Permission/background/universal-link/capability | {{SCOPE}} | {{SCENARIOS}} | iOS Simulator / device / staging | {{OUTPUT}} |
| App bundle/entitlement/privacy-manifest/signing inspection | {{SCOPE}} | {{SCENARIOS}} | Archive / release artifact | {{OUTPUT}} |

## 22. Evidence Plan

| Requirement / Scenario | Observable Contract | Evidence Layer | Timing | Blocking Scope | Cost Class | Exact Procedure / Command | Destination | Expected Result | Artifact Path | Limitation |
|---|---|---|---|---|---|---|---|---|---|---|
| {{REFERENCE}} | {{CONTRACT}} | {{LAYER}} | TASK-CLOSURE / FEATURE-CONVERGENCE / FINAL-READINESS | {{TASK_OR_GATE}} | LOW / MEDIUM / HIGH | {{PROCEDURE}} | {{DESTINATION}} | {{EXPECTED}} | {{PATH}} | {{LIMITATION}} |

Previews and screenshots may support visual review only and do not replace runtime evidence.

Evidence timing rules:
- `TASK-CLOSURE`: only evidence necessary to prove the bounded task's immediate behavioral/architectural outcome. Vertical journeys, directly changed persistence semantics, and directly changed migration behavior belong here when applicable.
- `FEATURE-CONVERGENCE`: whole-feature integration/regression evidence that requires multiple tasks to be assembled.
- `FINAL-READINESS`: expensive platform/device/security/privacy/performance/manual-runtime evidence that is required before acceptance/release but does not need to block ordinary implementation tasks unless the task directly changes that protected boundary.
- Prefer the cheapest deterministic evidence that proves the claim. Do not make unrelated file-protection, network-isolation, full manual accessibility, performance, signing, or device-reboot checks block a UI/domain task by default.
- A single valid artifact may satisfy multiple `VM-*` rows when its tests/scenarios cover them. Never rerun solely to create one unique file per VM ID.
- Long-running verification should produce a compact pass/fail summary plus artifact path; avoid workflows that require repeated full-log polling.
- Use manual final validation where it gives better confidence per cost (subjective design fidelity, real screen-reader flow, alternate input, representative RTL/adaptive quality, physical-device-only checks). Do not substitute manual checks for deterministic navigation/state/data correctness.
- Define a representative risk-based environment matrix instead of an exhaustive Cartesian product of screens × states × locales × devices × settings.

## 23. Verification Matrix

Use stable unique IDs (`VM-001`, `VM-002`, ...). Keep the detailed verification definitions in this plan; implementation tasks reference these IDs rather than duplicating the matrix. Include only applicable scenarios and do not create a per-row lifecycle status machine.

| ID | Requirement / Claim | Scenario | Timing | Blocking Scope | Environment / Destination | Preconditions | Expected Observable Result | Evidence Path | Method / Limitation |
|---|---|---|---|---|---|---|---|---|---|
| `VM-001` | {{REQUIREMENT_OR_CLAIM}} | {{SCENARIO}} | {{TIMING}} | {{BLOCKING_SCOPE}} | {{ENVIRONMENT}} | {{PRECONDITIONS}} | {{EXPECTED_RESULT}} | {{EVIDENCE_PATH}} | {{METHOD_OR_LIMITATION}} |

Rules:
- Every runtime-only claim must map to at least one runtime-capable `VM-*` scenario.
- Every row must trace to approved feature/architecture/design authority and must not invent behavior.
- Evidence paths must be concrete enough for later task execution and convergence review.
- If a scenario is not applicable, omit it rather than creating ceremonial rows.

## 24. Dependency-Ordered Implementation Sequence

1. {{STEP}}
2. {{STEP}}
3. {{STEP}}

This defines dependency order only, not implementation tasks, estimates, assignments, or code.

## 25. Technical Risks and Mitigations

| Risk | Trigger | Impact | Mitigation | Stop Condition |
|---|---|---|---|---|
| {{RISK}} | {{TRIGGER}} | {{IMPACT}} | {{MITIGATION}} | {{STOP}} |

## 26. Unresolved Technical Decisions

| ID | Decision | Supported Options | Recommendation | Status | Blocking Scope |
|---|---|---|---|---|---|
| TD-001 | {{DECISION}} | {{OPTIONS}} | {{RECOMMENDATION}} | Needs owner decision / Needs verification | {{SCOPE}} |

## 27. Readiness Implications

| Gate | Plan Impact | Current Status | Required Evidence / Remediation |
|---|---|---|---|
| {{GATE}} | {{IMPACT}} | PASS / BLOCKED / NEEDS VERIFICATION / N/A by owner authority | {{EVIDENCE}} |

## 28. Prohibited Patterns

{{PROHIBITED_PATTERNS}}

At minimum consider hardcoded strings, ad hoc dependencies, service locators, repositories/persistence contexts in leaf UI, side effects during SwiftUI body evaluation, state-holder recreation during view recomputation, duplicate state, unowned `Task` instances, unjustified `Task.detached`, unstructured/detached tasks contrary to authority, phone-only layouts, left/right assumptions, fixed-height text, previews as runtime proof, fake release services, in-memory release persistence substitutes, unapproved permissions/components, and silent simulated success.

## 29. Documentation Impact

{{DOCUMENTATION_IMPACT}}

## 30. Final Verdict

**Authoring verdict:** `{{AUTHORING_VERDICT}}`

Allowed values:

- `READY FOR PLAN REVIEW`
- `BLOCKED BY TECHNICAL DECISION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

This plan does not authorize task generation or implementation.


## Tier Scaling Rules

If classification was not run or is unavailable/stale, author this plan as COMPLEX. SMALL may collapse non-applicable specialist sections but must retain traceability, architecture placement, state/data flow, navigation, tests, and any triggered risk gate. STANDARD requires cross-feature propagation, durable-state coherence, origin-aware navigation, accessibility/localization, and applicable persistence/runtime verification. COMPLEX requires the full applicable plan including migration, historical integrity, concurrency/idempotency, protected boundaries, lifecycle/recovery, and named runtime evidence.
