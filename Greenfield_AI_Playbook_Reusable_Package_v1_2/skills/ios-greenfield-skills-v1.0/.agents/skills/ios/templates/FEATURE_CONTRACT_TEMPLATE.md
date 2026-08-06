# {{FEATURE_NAME}} — Feature Contract

**Feature ID:** `{{FEATURE_ID}}`  
**Platform:** {{PLATFORM}}  
**Classification:** {{CLASSIFICATION}}  
**Slice Type:** {{SLICE_TYPE}}  
**Status:** Draft — owner approval required  
**Feature Input:** `{{FEATURE_INPUT_PATH}}`  
**Output Path:** `{{OUTPUT_PATH}}`

---

## 1. Authority and Status

### 1.1 Authority Order

1. Current explicit owner direction.
2. Root repository policy.
3. Approved owner decisions.
4. Approved product authority and reviewed feature input.
5. Accepted architecture decisions and architecture spine.
6. Approved design authority and exact design artifacts.
7. Verified implementation and evidence.
8. Context routing, playbooks, skills, and imported guidance.

Unresolved conflicts must be marked `Needs owner decision` or `Needs verification`. They must not be resolved by invention.

### 1.2 Approval State

- Contract status: `DRAFT`
- Authoring verdict: `{{AUTHORING_VERDICT}}`
- Review verdict: `{{REVIEW_VERDICT}}`
- Owner approval: `PENDING`
- Implementation authorization: `NOT GRANTED`

---

## 2. Purpose and Bounded Outcome

### 2.1 Purpose

{{PURPOSE}}

### 2.2 User Outcome

{{USER_OUTCOME}}

### 2.3 Bounded Completion Outcome

{{BOUNDED_OUTCOME}}

---

## 3. Actors and Entry Points

### 3.1 Actors

{{ACTORS}}

### 3.2 Entry Points

{{ENTRY_POINTS}}

---

## 4. In-Scope Behavior

{{IN_SCOPE_BEHAVIOR}}

---

## 5. Explicit Exclusions and Non-Goals

{{EXCLUSIONS}}

---

## 6. Definitions and Terminology

| Term | Contract Meaning | Source |
|---|---|---|
| {{TERM}} | {{MEANING}} | {{SOURCE}} |

---

## 7. Preconditions

{{PRECONDITIONS}}

---

## 8. User Stories

### US-{{FEATURE_SHORT_ID}}-001 — {{STORY_TITLE}}

**As a** {{ACTOR}}  
**I want** {{GOAL}}  
**So that** {{OUTCOME}}

**Source:** {{SOURCE_REFERENCES}}

---

## 9. Functional Requirements

| ID | Requirement | Source | Verification Layer |
|---|---|---|---|
| {{FEATURE_SHORT_ID}}-FR-001 | {{OBSERVABLE_TESTABLE_REQUIREMENT}} | {{SOURCE}} | {{EVIDENCE_LAYER}} |

Requirements must be observable, testable, unambiguous, attributable, and free from unauthorized implementation detail.

---

## 10. Business Rules and Invariants

| ID | Invariant | Failure Consequence | Source |
|---|---|---|---|
| {{FEATURE_SHORT_ID}}-BR-001 | {{INVARIANT}} | {{CONSEQUENCE}} | {{SOURCE}} |

---

## 11. State Model

### 11.1 States

{{STATES}}

### 11.2 Events

{{EVENTS}}

### 11.3 Transition Matrix

| Current State | Event | Guard | Next State | Observable Result |
|---|---|---|---|---|
| {{STATE}} | {{EVENT}} | {{GUARD}} | {{NEXT_STATE}} | {{RESULT}} |

---

## 12. Validation Rules

| ID | Input or Condition | Valid Rule | Invalid Behavior | Recovery |
|---|---|---|---|---|
| {{FEATURE_SHORT_ID}}-VAL-001 | {{INPUT}} | {{RULE}} | {{ERROR_BEHAVIOR}} | {{RECOVERY}} |

---

## 13. Success Behavior

{{SUCCESS_BEHAVIOR}}

---

## 14. Failure Behavior

{{FAILURE_BEHAVIOR}}

---

## 15. Recovery Behavior

{{RECOVERY_BEHAVIOR}}

---

## 16. Offline Behavior

{{OFFLINE_BEHAVIOR}}

---

## 17. Cancellation and Destructive Behavior

{{DESTRUCTIVE_BEHAVIOR}}

---

## 18. Persistence and Durability Invariants

Describe observable durability and integrity outcomes only. Do not select a persistence engine, schema, ORM, storage context, or migration API unless an accepted architecture decision makes that mechanism mandatory.

| ID | Invariant | Evidence Required |
|---|---|---|
| {{FEATURE_SHORT_ID}}-PER-001 | {{DURABILITY_INVARIANT}} | {{EVIDENCE}} |

---

## 19. Screen-by-Screen Behavior

### {{SCREEN_CONTRACT_ID}} — {{SCREEN_NAME}}

**Purpose:** {{SCREEN_PURPOSE}}

**Product-authorized behavior:**  
{{PRODUCT_BEHAVIOR}}

**Approved visual and interaction intent:**  
{{DESIGN_INTENT}}

**Routine derivable states:**  
{{DERIVABLE_STATES}}

**Unsupported artifact content to exclude:**  
{{EXCLUDED_ARTIFACT_CONTENT}}

**Needs owner decision:**  
{{SCREEN_OWNER_DECISIONS}}

---

## 20. Design Traceability

### 20.1 Screen Contracts

{{DESIGN_CONTRACT_REFERENCES}}

### 20.2 Exact Design Artifacts

| Surface | Exact Artifact ID | Scope Used | Unsupported Content Excluded |
|---|---|---|---|
| {{SURFACE}} | `{{ARTIFACT_ID}}` | {{SCOPE}} | {{EXCLUDED_CONTENT}} |

---

## 21. Adaptive UI Contract

### 21.1 Compact Phone

{{COMPACT_LAYOUT_OUTCOME}}

### 21.2 Regular-Width Tablet

{{WIDE_LAYOUT_OUTCOME}}

### 21.3 Reduced Tablet Width / Multitasking

{{REDUCED_WIDTH_OUTCOME}}

### 21.4 Keyboard, Safe Areas, and Overflow

{{KEYBOARD_SAFE_AREA_OUTCOME}}

Do not use vague statements such as “make responsive.” Define information hierarchy, reflow, reachability, and interaction outcomes.

---

## 22. Localization and RTL Contract

### 22.1 User-Facing Copy Categories

{{COPY_CATEGORIES}}

### 22.2 Formatting

{{FORMATTING_REQUIREMENTS}}

### 22.3 RTL

{{RTL_REQUIREMENTS}}

All user-facing and accessibility-facing strings must be localizable. Sentence-fragment concatenation is prohibited.

---

## 23. Accessibility Contract

| Area | Required Outcome | Runtime Evidence |
|---|---|---|
| VoiceOver / screen reader | {{OUTCOME}} | {{EVIDENCE}} |
| Focus order | {{OUTCOME}} | {{EVIDENCE}} |
| Dynamic Type / text scaling | {{OUTCOME}} | {{EVIDENCE}} |
| Bold Text | {{OUTCOME}} | {{EVIDENCE}} |
| Differentiate Without Color | {{OUTCOME}} | {{EVIDENCE}} |
| Button Shapes | {{OUTCOME}} | {{EVIDENCE}} |
| Reduce Transparency | {{OUTCOME}} | {{EVIDENCE}} |
| Increased Contrast | {{OUTCOME}} | {{EVIDENCE}} |
| Reduce Motion | {{OUTCOME}} | {{EVIDENCE}} |
| Touch targets | {{OUTCOME}} | {{EVIDENCE}} |
| Error announcement | {{OUTCOME}} | {{EVIDENCE}} |

---

## 24. Privacy and Protected Boundaries

{{PROTECTED_BOUNDARIES}}

| Boundary | Rule | Stop Condition | Evidence |
|---|---|---|---|
| {{BOUNDARY}} | {{RULE}} | {{STOP_CONDITION}} | {{EVIDENCE}} |

---

## 25. Acceptance Scenarios

### AC-{{FEATURE_SHORT_ID}}-001 — {{SCENARIO_TITLE}}

**Given** {{PRECONDITION}}  
**When** {{ACTION}}  
**Then** {{OBSERVABLE_RESULT}}  
**And** {{ADDITIONAL_RESULT}}

**Evidence layer:** {{EVIDENCE_LAYER}}  
**Required destination/environment:** {{ENVIRONMENT}}  
**Artifact path:** {{ARTIFACT_PATH}}

---

## 26. Evidence Requirements

| Requirement or Scenario | Evidence Layer | Environment | Artifact Path | Limitation |
|---|---|---|---|---|
| {{REFERENCE}} | {{EVIDENCE_LAYER}} | {{ENVIRONMENT}} | {{PATH}} | {{LIMITATION}} |

The contract defines required evidence. It does not claim evidence has already been produced.

---

## 27. Clarification Register

| ID | Source of Ambiguity | Affected Area | Supported Options | Recommended Answer | Status |
|---|---|---|---|---|---|
| CL-{{FEATURE_SHORT_ID}}-001 | {{SOURCE}} | {{AREA}} | {{OPTIONS}} | {{RECOMMENDATION}} | `Resolved from authority` / `Needs owner decision` |

Only material observable-behavior questions belong here. Technical mechanism questions belong in later planning or feasibility work.

---

## 28. Requirements-to-Source Traceability

| Contract Requirement | Product Source | Feature Input | Screen Contract | Exact Artifact | ADR / Architecture Constraint |
|---|---|---|---|---|---|
| {{REQUIREMENT_ID}} | {{PRD_REFERENCE}} | {{INPUT_REFERENCE}} | {{SCREEN_REFERENCE}} | `{{ARTIFACT_ID}}` | {{ADR_REFERENCE}} |

---

## 29. Dependencies

{{DEPENDENCIES}}

---

## 30. Out-of-Scope, Candidate, and Deferred Items

{{OUT_OF_SCOPE_ITEMS}}

---

## 31. Owner Review

### 31.1 Decisions Required

{{OWNER_DECISIONS_REQUIRED}}

### 31.2 Recommended Dispositions

{{RECOMMENDED_DISPOSITIONS}}

### 31.3 Risks of Acceptance or Deferral

{{DECISION_RISKS}}

---

## 32. Approval Record

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Repository owner |  | Pending |  |  |

An agent must not mark this contract approved.

---

## 33. Change-Control Rule

Any change to approved observable behavior, scope, design authority, protected boundaries, or architecture traceability requires:

1. source authority update;
2. contract amendment;
3. review rerun;
4. owner approval;
5. downstream plan, tasks, and evidence synchronization.

---

## 34. Final Verdict

**Authoring verdict:** `{{AUTHORING_VERDICT}}`

Allowed values:

- `READY FOR OWNER APPROVAL`
- `BLOCKED BY PRODUCT CLARIFICATION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

This verdict does not authorize implementation.
