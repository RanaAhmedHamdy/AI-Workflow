# {{FEATURE_NAME}} — Android Implementation Plan

**Feature ID:** `{{FEATURE_ID}}`  
**Feature Contract:** `{{FEATURE_CONTRACT_PATH}}`  
**Status:** Draft — plan review required  
**Implementation Authorization:** NOT GRANTED

## 1. Authority and Status

- Authoring verdict: `{{AUTHORING_VERDICT}}`
- Review verdict: `{{REVIEW_VERDICT}}`
- Owner approval: `PENDING`
- Implementation authorization: `NOT GRANTED`
- Android architecture baseline: {{ANDROID_ARCHITECTURE_BASELINE}}

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

| Contract Requirement | Planned Component / Responsibility | Design Reference | Android ADR Constraint | Test Layer(s) | Evidence |
|---|---|---|---|---|---|
| {{REQ_ID}} | {{COMPONENT}} | {{DESIGN_REF}} | {{ADR_REF}} | {{TEST_LAYER}} | {{EVIDENCE}} |

## 5. Android Toolchain and Build Baseline

| Concern | Accepted Decision | Authority | Feature Impact |
|---|---|---|---|
| Android Studio / JDK | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
| Gradle / AGP / Kotlin | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
| compileSdk / targetSdk / minSdk | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
| Namespace / application ID | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
| Build types / flavors | {{VALUE}} | {{AUTHORITY}} | {{IMPACT}} |
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

## 7. Module, Source-Set, Resource, and Manifest Ownership

| Module / Source Set / Resource Owner | Responsibility | Allowed Dependencies | Prohibited Responsibilities |
|---|---|---|---|
| {{MODULE}} | {{RESPONSIBILITY}} | {{ALLOWED}} | {{PROHIBITED}} |

Do not create modules, source sets, convention plugins, or shared abstractions merely for template compliance.

## 8. Domain Model and Value Semantics

| Domain Type | Responsibility | Invariants | Android Framework Exposure | Persistence Exposure |
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

### Repository, DAO, and Data-Source Boundaries

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

## 11. Presentation-State and ViewModel Design

| State Holder / ViewModel | Lifetime Owner | Owned State | Inputs | Events / Outputs | Execution / Isolation Boundary | Reconstruction Source |
|---|---|---|---|---|---|---|
| {{STATE_HOLDER}} | {{LIFETIME}} | {{STATE}} | {{INPUTS}} | {{OUTPUTS}} | {{BOUNDARY}} | {{RECONSTRUCTION}} |

### State Rules

{{STATE_RULES}}

Route-level workflows use an approved lifecycle-aware state holder when state spans recomposition, asynchronous work, validation, navigation, recreation, or durable recovery. Static leaf UI does not require ceremonial ViewModels.

## 12. Kotlin Coroutines and Flow Design

### Scope Ownership

{{SCOPE_OWNERSHIP}}

### Dispatcher Ownership and Injection

{{DISPATCHER_PLAN}}

### Flow Exposure and Lifecycle-Aware Collection

{{FLOW_PLAN}}

### Cancellation and Durable Work

{{CANCELLATION_PLAN}}

### Ordering, Retry, Reentrancy, and Duplicate Side Effects

{{ORDERING_IDEMPOTENCY_PLAN}}

### Error Mapping and Terminal States

{{ASYNC_ERROR_PLAN}}

Prohibit `GlobalScope`, unowned jobs, swallowed exceptions, and fire-and-forget production work.

## 13. Lifecycle, Recreation, and Restoration

### Recomposition and Local UI State

{{RECOMPOSITION_STATE}}

### Configuration Change and Activity/Fragment Recreation

{{CONFIGURATION_RECREATION}}

### Navigation Saved State

{{NAV_SAVED_STATE}}

### Process Death and App Relaunch

{{PROCESS_DEATH_RELAUNCH}}

### Device Reboot, Backup Restore, and Transfer Boundaries

{{REBOOT_BACKUP_TRANSFER}}

### Stale Restoration Recovery

{{STALE_RESTORATION}}

Keep each lifecycle class distinct. Do not store sensitive payloads in route arguments or saved state.

## 14. Navigation and Back Behavior

{{NAVIGATION_PLAN}}

Include top-level destinations, route ownership, minimal arguments, adaptive navigation, system back, predictive back where applicable, modal/dialog behavior, deep/app links if approved, discard protection, and restoration.

## 15. Screen-by-Screen Mapping

### {{SCREEN_CONTRACT_ID}} — {{SCREEN_NAME}}

- Exact artifacts: {{ARTIFACT_IDS}}
- Contract requirements: {{REQUIREMENTS}}
- Route/container boundary: {{ROUTE_BOUNDARY}}
- Render/content boundary: {{CONTENT_BOUNDARY}}
- ViewModel/state holder: {{STATE_HOLDER}}
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

### Split-Screen, Freeform, and Reduced Width

{{REDUCED_WIDTH_PLAN}}

### Foldable Posture and Hinge Behavior

{{FOLDABLE_PLAN}}

### Orientation

{{ORIENTATION_PLAN}}

### IME, Edge-to-Edge, System Bars, Cutouts, Insets, and Overflow

{{IME_INSETS_PLAN}}

### Keyboard, Mouse, Trackpad, D-pad, and ChromeOS Where In Scope

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
| TalkBack semantics and traversal | {{PLAN}} | {{VERIFY}} |
| Focus order and restoration | {{PLAN}} | {{VERIFY}} |
| Font scaling and text reflow | {{PLAN}} | {{VERIFY}} |
| Display scaling and magnification | {{PLAN}} | {{VERIFY}} |
| Non-color differentiation | {{PLAN}} | {{VERIFY}} |
| Reduced/removed animations | {{PLAN}} | {{VERIFY}} |
| Contrast and visual adaptation | {{PLAN}} | {{VERIFY}} |
| Touch targets | {{PLAN}} | {{VERIFY}} |
| Keyboard and D-pad | {{PLAN}} | {{VERIFY}} |
| Switch Access | {{PLAN}} | {{VERIFY}} |
| Voice Access | {{PLAN}} | {{VERIFY}} |
| Error/live-region announcements | {{PLAN}} | {{VERIFY}} |
| Custom-control semantics | {{PLAN}} | {{VERIFY}} |

## 19. Error, Recovery, Offline, and Cancellation Design

{{ERROR_RECOVERY_PLAN}}

## 20. Permissions, Manifest, Privacy, and Protected Capabilities

| Boundary | Manifest / Runtime Ownership | Denial / Revocation / Failure Behavior | Evidence | Stop Condition |
|---|---|---|---|---|
| {{BOUNDARY}} | {{OWNERSHIP}} | {{FAILURE_BEHAVIOR}} | {{EVIDENCE}} | {{STOP}} |

Address applicable permissions, exported components, intent filters, app links, services, receivers, providers, foreground-service types, notifications, alarms, WorkManager, Health Connect, billing, authentication, attestation, analytics/crash reporting, backup, retention, deletion, redaction, and release configuration.

## 21. Testing Strategy

| Layer | Scope | Required Scenarios | Environment / Destination | Machine-Readable Output |
|---|---|---|---|---|
| Kotlin/JVM domain/unit | {{SCOPE}} | {{SCENARIOS}} | Host JVM | {{OUTPUT}} |
| ViewModel/presentation state | {{SCOPE}} | {{SCENARIOS}} | Host JVM / accepted runtime | {{OUTPUT}} |
| Repository/integration | {{SCOPE}} | {{SCENARIOS}} | Host / disk-backed / instrumented as required | {{OUTPUT}} |
| Persistence migration/relaunch | {{SCOPE}} | {{SCENARIOS}} | Instrumented emulator/device | {{OUTPUT}} |
| Robolectric, if accepted | {{SCOPE}} | {{SCENARIOS}} | Host JVM | {{OUTPUT}} |
| Compose UI / View UI automation | {{SCOPE}} | {{SCENARIOS}} | Emulator/device | {{OUTPUT}} |
| Configuration change/process death | {{SCOPE}} | {{SCENARIOS}} | Emulator/device | {{OUTPUT}} |
| TalkBack accessibility runtime | {{SCOPE}} | {{SCENARIOS}} | Emulator/device/manual | {{OUTPUT}} |
| RTL/pseudo-locale/adaptive/foldable | {{SCOPE}} | {{SCENARIOS}} | Emulator/device | {{OUTPUT}} |
| Permission/background/app-link/service | {{SCOPE}} | {{SCENARIOS}} | Emulator/device/staging | {{OUTPUT}} |
| APK/AAB/manifest/R8/signing inspection | {{SCOPE}} | {{SCENARIOS}} | Release artifact | {{OUTPUT}} |

## 22. Evidence Plan

| Requirement / Scenario | Observable Contract | Evidence Layer | Exact Procedure / Command | Destination | Expected Result | Artifact Path | Limitation |
|---|---|---|---|---|---|---|---|
| {{REFERENCE}} | {{CONTRACT}} | {{LAYER}} | {{PROCEDURE}} | {{DESTINATION}} | {{EXPECTED}} | {{PATH}} | {{LIMITATION}} |

Previews and screenshots may support visual review only and do not replace runtime evidence.

## 23. Dependency-Ordered Implementation Sequence

1. {{STEP}}
2. {{STEP}}
3. {{STEP}}

This defines dependency order only, not implementation tasks, estimates, assignments, or code.

## 24. Technical Risks and Mitigations

| Risk | Trigger | Impact | Mitigation | Stop Condition |
|---|---|---|---|---|
| {{RISK}} | {{TRIGGER}} | {{IMPACT}} | {{MITIGATION}} | {{STOP}} |

## 25. Unresolved Technical Decisions

| ID | Decision | Supported Options | Recommendation | Status | Blocking Scope |
|---|---|---|---|---|---|
| TD-001 | {{DECISION}} | {{OPTIONS}} | {{RECOMMENDATION}} | Needs owner decision / Needs verification | {{SCOPE}} |

## 26. Readiness Implications

| Gate | Plan Impact | Current Status | Required Evidence / Remediation |
|---|---|---|---|
| {{GATE}} | {{IMPACT}} | PASS / BLOCKED / NEEDS VERIFICATION / N/A by owner authority | {{EVIDENCE}} |

## 27. Prohibited Patterns

{{PROHIBITED_PATTERNS}}

At minimum consider hardcoded strings, ad hoc dependencies, service locators, repositories/DAOs in leaf UI, side effects during composition, ViewModel recreation, duplicate state, `GlobalScope`, unowned jobs, hardcoded dispatchers contrary to authority, phone-only layouts, left/right assumptions, fixed-height text, previews as runtime proof, fake release services, in-memory release persistence substitutes, unapproved permissions/components, and silent simulated success.

## 28. Documentation Impact

{{DOCUMENTATION_IMPACT}}

## 29. Final Verdict

**Authoring verdict:** `{{AUTHORING_VERDICT}}`

Allowed values:

- `READY FOR PLAN REVIEW`
- `BLOCKED BY TECHNICAL DECISION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

This plan does not authorize task generation or implementation.
