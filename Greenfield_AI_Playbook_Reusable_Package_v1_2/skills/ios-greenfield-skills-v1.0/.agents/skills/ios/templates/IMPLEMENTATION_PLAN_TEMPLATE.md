# {{FEATURE_NAME}} — Implementation Plan

**Feature ID:** `{{FEATURE_ID}}`  
**Feature Contract:** `{{FEATURE_CONTRACT_PATH}}`  
**Status:** Draft — plan review required  
**Implementation Authorization:** NOT GRANTED

## 1. Authority and Status
- Authoring verdict: `{{AUTHORING_VERDICT}}`
- Review verdict: `{{REVIEW_VERDICT}}`
- Owner approval: `PENDING`
- Implementation authorization: `NOT GRANTED`

## 2. Scope and Exclusions
### In Scope
{{IN_SCOPE}}

### Explicitly Excluded
{{EXCLUSIONS}}

## 3. Assumptions and Preconditions
| ID | Assumption / Precondition | Source | Status |
|---|---|---|---|
| AP-001 | {{ASSUMPTION}} | {{SOURCE}} | Confirmed / Needs verification |

## 4. Requirements-to-Plan Traceability
| Contract Requirement | Planned Component | Design Reference | ADR Constraint | Test Layer | Evidence |
|---|---|---|---|---|---|
| {{REQ_ID}} | {{COMPONENT}} | {{DESIGN_REF}} | {{ADR_REF}} | {{TEST_LAYER}} | {{EVIDENCE}} |

## 5. Architecture Mapping
### Feature Boundary
{{FEATURE_BOUNDARY}}

### Dependency Direction
{{DEPENDENCY_DIRECTION}}

### Protected Boundaries
{{PROTECTED_BOUNDARIES}}

## 6. Module and Target Ownership
| Module / Target | Responsibility | Allowed Dependencies | Prohibited Responsibilities |
|---|---|---|---|
| {{MODULE}} | {{RESPONSIBILITY}} | {{ALLOWED}} | {{PROHIBITED}} |

## 7. Domain Model and Value Semantics
| Domain Type | Responsibility | Invariants | Persistence Exposure |
|---|---|---|---|
| {{TYPE}} | {{RESPONSIBILITY}} | {{INVARIANTS}} | None / Adapter-only |

## 8. Persistence Design
### Accepted Architecture
{{PERSISTENCE_ARCHITECTURE}}

### Repository Boundaries
{{REPOSITORY_BOUNDARIES}}

### Transactions and Atomicity
{{TRANSACTION_RULES}}

### Duplicate Prevention and Idempotency
{{IDEMPOTENCY_RULES}}

### Migration and Recovery
{{MIGRATION_RULES}}

### Date Attribution and Historical Integrity
{{DATE_RULES}}

### Sensitive Data Separation
{{SENSITIVE_DATA_RULES}}

## 9. Presentation-State Design
| State Holder | Owned State | Inputs | Events / Outputs | Actor Boundary |
|---|---|---|---|---|
| {{STATE_HOLDER}} | {{STATE}} | {{INPUTS}} | {{OUTPUTS}} | {{BOUNDARY}} |

## 10. Navigation and Restoration
{{NAVIGATION_PLAN}}

## 11. Screen-by-Screen Mapping
### {{SCREEN_CONTRACT_ID}} — {{SCREEN_NAME}}
- Exact artifacts: {{ARTIFACT_IDS}}
- Contract requirements: {{REQUIREMENTS}}
- Composition: {{COMPOSITION}}
- State mapping: {{STATE_MAPPING}}
- Actions/events: {{ACTIONS}}
- Failure/recovery: {{FAILURE_RECOVERY}}
- Unsupported content excluded: {{EXCLUDED_CONTENT}}

## 12. Adaptive UI Plan
### Compact
{{COMPACT_PLAN}}

### Regular Width / Tablet
{{WIDE_PLAN}}

### Reduced Width / Multitasking
{{REDUCED_WIDTH_PLAN}}

### Keyboard, Safe Areas, Overflow
{{KEYBOARD_PLAN}}

## 13. Localization and RTL Plan
### String Ownership
{{STRING_PLAN}}

### Formatting
{{FORMATTING_PLAN}}

### RTL and Bidirectional Content
{{RTL_PLAN}}

### Hardcoded-String Prevention
{{STRING_SCAN_PLAN}}

## 14. Accessibility Plan
| Capability | Implementation Responsibility | Verification |
|---|---|---|
| VoiceOver | {{PLAN}} | {{VERIFY}} |
| Focus order | {{PLAN}} | {{VERIFY}} |
| Dynamic Type | {{PLAN}} | {{VERIFY}} |
| Bold Text | {{PLAN}} | {{VERIFY}} |
| Differentiate Without Color | {{PLAN}} | {{VERIFY}} |
| Button Shapes | {{PLAN}} | {{VERIFY}} |
| Reduce Transparency | {{PLAN}} | {{VERIFY}} |
| Increased Contrast | {{PLAN}} | {{VERIFY}} |
| Reduce Motion | {{PLAN}} | {{VERIFY}} |
| Touch targets | {{PLAN}} | {{VERIFY}} |
| Error announcement | {{PLAN}} | {{VERIFY}} |

## 15. Error, Recovery, Offline, and Cancellation Design
{{ERROR_RECOVERY_PLAN}}

## 16. Testing Strategy
| Layer | Scope | Required Scenarios | Environment |
|---|---|---|---|
| Domain / unit | {{SCOPE}} | {{SCENARIOS}} | Host |
| Repository / integration | {{SCOPE}} | {{SCENARIOS}} | Host / disk-backed |
| Persistence relaunch | {{SCOPE}} | {{SCENARIOS}} | Simulator host |
| UI automation | {{SCOPE}} | {{SCENARIOS}} | Simulator |
| Accessibility runtime | {{SCOPE}} | {{SCENARIOS}} | Simulator / device |
| RTL and adaptive runtime | {{SCOPE}} | {{SCENARIOS}} | Simulator / device |

## 17. Evidence Plan
| Requirement / Scenario | Evidence Layer | Procedure | Destination | Artifact Path | Limitation |
|---|---|---|---|---|---|
| {{REFERENCE}} | {{LAYER}} | {{PROCEDURE}} | {{DESTINATION}} | {{PATH}} | {{LIMITATION}} |

## 18. Dependency-Ordered Implementation Sequence
1. {{STEP}}
2. {{STEP}}
3. {{STEP}}

This defines order only, not implementation tasks.

## 19. Technical Risks and Mitigations
| Risk | Trigger | Impact | Mitigation | Stop Condition |
|---|---|---|---|---|
| {{RISK}} | {{TRIGGER}} | {{IMPACT}} | {{MITIGATION}} | {{STOP}} |

## 20. Unresolved Technical Decisions
| ID | Decision | Supported Options | Recommendation | Status |
|---|---|---|---|---|
| TD-001 | {{DECISION}} | {{OPTIONS}} | {{RECOMMENDATION}} | Needs owner decision / Needs verification |

## 21. Readiness Implications
| Gate | Plan Impact | Current Status | Required Evidence |
|---|---|---|---|
| {{GATE}} | {{IMPACT}} | PASS / BLOCKED / NEEDS VERIFICATION | {{EVIDENCE}} |

## 22. Prohibited Patterns
{{PROHIBITED_PATTERNS}}

## 23. Documentation Impact
{{DOCUMENTATION_IMPACT}}

## 24. Final Verdict
**Authoring verdict:** `{{AUTHORING_VERDICT}}`

Allowed values:
- `READY FOR PLAN REVIEW`
- `BLOCKED BY TECHNICAL DECISION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

This plan does not authorize implementation.
