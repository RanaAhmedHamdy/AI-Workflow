# {{FEATURE_NAME}} — Android Feature Contract

**Feature ID:** `{{FEATURE_ID}}`  
**Platform:** Native Android  
**Classification:** {{CLASSIFICATION}}  
**Slice Type:** {{SLICE_TYPE}}  
**Status:** Draft — owner approval required  
**Feature Input:** `{{FEATURE_INPUT_PATH}}`  
**Output Path:** `{{OUTPUT_PATH}}`

---

## 1. Authority and Status

### 1.1 Authority Order

1. Current explicit owner direction.
2. Root repository policy and protected boundaries.
3. Approved owner decisions.
4. Approved product authority and reviewed feature input.
5. Accepted Android architecture decisions and architecture spine.
6. Approved design authority and exact design artifacts.
7. Verified implementation and produced evidence.
8. Context routing, playbooks, skills, imported guidance, and Android samples.

Unresolved conflicts must be marked `Needs owner decision` or `Needs verification`. They must not be resolved by invention or by assuming Android conventions.

### 1.2 Approval State

- Contract status: `DRAFT`
- Authoring verdict: `{{AUTHORING_VERDICT}}`
- Review verdict: `{{REVIEW_VERDICT}}`
- Owner approval: `PENDING`
- Planning authorization: `NOT GRANTED`
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

| ID | Observable Requirement | Source | Required Evidence Layer(s) |
|---|---|---|---|
| {{FEATURE_SHORT_ID}}-FR-001 | {{OBSERVABLE_TESTABLE_REQUIREMENT}} | {{SOURCE}} | {{EVIDENCE_LAYER}} |

Requirements must be observable, testable, unambiguous, attributable, and free from unauthorized Android implementation detail.

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

| ID | Input or Condition | Valid Rule | Invalid Behavior | Recovery | Explicit Source |
|---|---|---|---|---|---|
| {{FEATURE_SHORT_ID}}-VAL-001 | {{INPUT}} | {{RULE}} | {{ERROR_BEHAVIOR}} | {{RECOVERY}} | {{SOURCE}} |

No validation rule is settled without an explicit approved source.

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

## 16. Offline and Local-Only Behavior

{{OFFLINE_BEHAVIOR}}

State exactly what remains available locally and what becomes unavailable. Do not promise synchronization or background delivery without approved authority.

---

## 17. Cancellation and Destructive Behavior

{{DESTRUCTIVE_BEHAVIOR}}

Back navigation, gesture dismissal, system back, or lifecycle transitions must not silently commit, discard, delete, purchase, transfer, or reassign data.

---

## 18. Persistence and Durability Invariants

Describe observable durability and integrity outcomes only. Do not select Room, DataStore, SQLite, an ORM, schema, DAO, storage context, migration API, or file location unless accepted architecture makes that mechanism mandatory.

Keep recomposition, configuration change, Activity/Fragment recreation, process death, app relaunch, device reboot, backup restore, and device transfer distinct.

| ID | Durability / Integrity Invariant | Required Evidence | Limitation |
|---|---|---|---|
| {{FEATURE_SHORT_ID}}-PER-001 | {{DURABILITY_INVARIANT}} | {{EVIDENCE}} | {{LIMITATION}} |

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

| Surface | Exact Artifact ID | Window/Locale Evidence | Scope Used | Unsupported Content Excluded |
|---|---|---|---|---|
| {{SURFACE}} | `{{ARTIFACT_ID}}` | {{WINDOW_LOCALE}} | {{SCOPE}} | {{EXCLUDED_CONTENT}} |

Static artifacts do not prove runtime, TalkBack, focus, text scaling, RTL, resizing, foldables, lifecycle, persistence, permissions, or device behavior.

---

## 21. Adaptive and Resizable UI Contract

### 21.1 Compact Window

{{COMPACT_LAYOUT_OUTCOME}}

### 21.2 Medium Window

{{MEDIUM_LAYOUT_OUTCOME}}

### 21.3 Expanded Window / Tablet

{{EXPANDED_LAYOUT_OUTCOME}}

### 21.4 Split-Screen, Freeform, and Reduced Width

{{REDUCED_WIDTH_OUTCOME}}

### 21.5 Orientation and Fold/Posture Changes

{{ORIENTATION_POSTURE_OUTCOME}}

### 21.6 IME, System Bars, Cutouts, Hinges, and Overflow

{{IME_INSETS_OVERFLOW_OUTCOME}}

### 21.7 State Preservation During Reflow

{{REFLOW_STATE_PRESERVATION}}

Do not use vague statements such as “make responsive.” Define information hierarchy, reflow, reachability, overflow, and state preservation without inventing breakpoints or content regions.

---

## 22. Localization and RTL Contract

### 22.1 Approved Locales and Fallback

{{LOCALE_SCOPE}}

### 22.2 User-Facing and Accessibility-Facing Copy Categories

{{COPY_CATEGORIES}}

### 22.3 Formatting, Plurals, and Grammar

{{FORMATTING_REQUIREMENTS}}

### 22.4 RTL and Bidirectional Content

{{RTL_REQUIREMENTS}}

### 22.5 Long Translation and Text Expansion

{{TEXT_EXPANSION_REQUIREMENTS}}

All user-facing and accessibility-facing strings must be localizable. Sentence-fragment concatenation and absolute left/right assumptions are prohibited.

---

## 23. Accessibility Contract

| Capability | Required Observable Outcome | Applicable Modes | Runtime Evidence |
|---|---|---|---|
| TalkBack / screen-reader semantics | {{OUTCOME}} | TalkBack | {{EVIDENCE}} |
| Focus order and restoration | {{OUTCOME}} | Touch exploration / keyboard / D-pad | {{EVIDENCE}} |
| Font scaling and text reflow | {{OUTCOME}} | Approved font-scale matrix | {{EVIDENCE}} |
| Display scaling / magnification | {{OUTCOME}} | Approved display-size and magnification matrix | {{EVIDENCE}} |
| Non-color differentiation | {{OUTCOME}} | Color correction/inversion where applicable | {{EVIDENCE}} |
| Reduced or removed animations | {{OUTCOME}} | System animation settings | {{EVIDENCE}} |
| Contrast and visual-effect adaptation | {{OUTCOME}} | Approved system/device settings | {{EVIDENCE}} |
| Touch targets | {{OUTCOME}} | Touch / Switch Access | {{EVIDENCE}} |
| Keyboard and D-pad navigation | {{OUTCOME}} | Hardware keyboard / D-pad | {{EVIDENCE}} |
| Switch Access | {{OUTCOME}} | Switch Access | {{EVIDENCE}} |
| Voice Access | {{OUTCOME}} | Voice Access | {{EVIDENCE}} |
| Error and live-state announcement | {{OUTCOME}} | TalkBack/live-region behavior | {{EVIDENCE}} |
| Custom-control semantics | {{OUTCOME}} | TalkBack/alternative input | {{EVIDENCE}} |

Static design, source inspection, lint, previews, and screenshots do not establish runtime accessibility verification.

---

## 24. Privacy, Permissions, and Protected Boundaries

{{PROTECTED_BOUNDARIES}}

| Boundary | Observable Rule | Stop Condition / Fail-Closed Outcome | Required Evidence |
|---|---|---|---|
| {{BOUNDARY}} | {{RULE}} | {{STOP_CONDITION}} | {{EVIDENCE}} |

A dependency, SDK, manifest merge, sample, or design artifact does not authorize a permission, exported component, service, receiver, provider, app link, notification, foreground service, Health Connect integration, billing flow, authentication flow, attestation mechanism, analytics SDK, or external data transfer.

---

## 25. Acceptance Scenarios

### AC-{{FEATURE_SHORT_ID}}-001 — {{SCENARIO_TITLE}}

**Given** {{PRECONDITION}}  
**When** {{ACTION}}  
**Then** {{OBSERVABLE_RESULT}}  
**And** {{ADDITIONAL_RESULT}}

**Evidence layer(s):** {{EVIDENCE_LAYER}}  
**Required destination/environment:** {{ENVIRONMENT}}  
**Artifact path:** {{ARTIFACT_PATH}}  
**Known limitation:** {{LIMITATION}}

---

## 26. Evidence Requirements

| Requirement or Scenario | Evidence Layer | Environment | Procedure | Artifact Path | Limitation |
|---|---|---|---|---|---|
| {{REFERENCE}} | {{EVIDENCE_LAYER}} | {{ENVIRONMENT}} | {{PROCEDURE}} | {{PATH}} | {{LIMITATION}} |

Possible Android evidence layers include JVM/unit, ViewModel/state, repository/integration, disk-backed migration, instrumented, Compose/View UI automation, emulator runtime, physical-device runtime, TalkBack/manual accessibility, RTL/pseudo-locale, multi-window/foldable, configuration-change/process-death/relaunch, background/service, external-service/attestation, and APK/AAB/manifest/signing/release inspection.

The contract defines required evidence. It does not claim evidence has already been produced.

---

## 27. Clarification Register

| ID | Source of Ambiguity | Affected Area | Supported Options | Recommended Disposition | Status |
|---|---|---|---|---|---|
| CL-{{FEATURE_SHORT_ID}}-001 | {{SOURCE}} | {{AREA}} | {{OPTIONS}} | {{RECOMMENDATION}} | `Resolved from authority` / `Needs owner decision` / `Needs verification` / `Authority conflict` |

Only material observable-behavior questions belong here. Android technical mechanism questions belong in planning, ADRs, or feasibility work.

---

## 28. Requirements-to-Source Traceability

| Contract Requirement | Product Source | Feature Input | Screen Contract | Exact Artifact | Android ADR / Architecture Constraint |
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
3. independent contract review rerun;
4. owner approval;
5. downstream plan, tasks, readiness, and evidence synchronization.

---

## 34. Final Verdict

**Authoring verdict:** `{{AUTHORING_VERDICT}}`

Allowed values:

- `READY FOR OWNER APPROVAL`
- `BLOCKED BY PRODUCT CLARIFICATION`
- `BLOCKED BY AUTHORITY CONFLICT`
- `NEEDS VERIFICATION`

This verdict does not authorize planning or implementation.
