# {{FEATURE_NAME}} — Feature Readiness Report

**Feature ID:** `{{FEATURE_ID}}`  
**Feature Contract:** `{{FEATURE_CONTRACT_PATH}}`  
**Implementation Plan:** `{{IMPLEMENTATION_PLAN_PATH}}`  
**Implementation Tasks:** `{{IMPLEMENTATION_TASKS_PATH}}`  
**Implementation Revision:** `{{COMMIT_OR_REVISION}}`  
**Status:** Draft — owner acceptance required  
**Release Authorization:** NOT GRANTED

---

## 1. Authority and Status

- Contract approval: {{CONTRACT_STATUS}}
- Plan approval: {{PLAN_STATUS}}
- Task approval: {{TASK_STATUS}}
- Implementation authorization: {{IMPLEMENTATION_AUTHORIZATION}}
- Convergence verdict: `{{CONVERGENCE_VERDICT}}`
- Readiness-review verdict: `{{READINESS_REVIEW_VERDICT}}`
- Owner feature acceptance: `PENDING`
- Release authorization: `NOT GRANTED`

This report does not authorize release, signing, distribution, store submission, or production publication.

### 1.1 Convergence Blocker Classification

Do not collapse unrelated blockers into `IMPLEMENTATION DEFECT`. Classify each blocking finding by what it actually prevents.

| Finding ID | Category | Blocking Scope | Description | Required Remediation |
|---|---|---|---|---|
| {{FINDING_ID}} | IMPLEMENTATION / CI / EVIDENCE / DOCUMENTATION / REPOSITORY_STATE / OWNER_DECISION | {{SCOPE}} | {{DESCRIPTION}} | {{REMEDIATION}} |

A feature may be implementation-correct while still blocked from final readiness by evidence, documentation, CI, or repository-state requirements. The headline verdict must not mislabel those as production-code defects.

### 1.2 Evidence Reuse Rule

One real machine-readable/runtime artifact MAY satisfy multiple verification rows when the artifact actually contains the required scenarios and each row traces to it explicitly. Do not rerun the same suite only to manufacture a unique artifact filename per verification ID. Rerun only when evidence is absent, stale, invalid, or does not cover the required observable claim.

---

## 2. Implemented Scope

{{IMPLEMENTED_SCOPE}}

## 3. Explicitly Excluded Scope

{{EXCLUDED_SCOPE}}

## 4. Implementation Change Summary

{{CHANGE_SUMMARY}}

## 5. Task Completion Summary

| Task ID | Completion Status | Evidence Status | Completion Review | Limitations |
|---|---|---|---|---|
| {{TASK_ID}} | {{STATUS}} | {{EVIDENCE_STATUS}} | {{REVIEW_STATUS}} | {{LIMITATION}} |

## 6. Contract Coverage

| Contract Requirement | Implementation Location | Test/Evidence | Status | Limitation |
|---|---|---|---|---|
| {{REQ_ID}} | {{LOCATION}} | {{EVIDENCE}} | PASS / FAIL / NEEDS VERIFICATION | {{LIMITATION}} |

## 7. Scope-Fidelity Review

### In-Scope Behavior Implemented

{{IN_SCOPE_RESULT}}

### Excluded or Later-Feature Behavior Detected

{{SCOPE_DRIFT_RESULT}}

### Unsupported or Orphan Behavior

{{ORPHAN_BEHAVIOR}}

## 8. Plan and Architecture Conformance

| Area | Approved Authority | Implemented Outcome | Evidence | Status |
|---|---|---|---|---|
| Project/module structure | {{AUTHORITY}} | {{OUTCOME}} | {{EVIDENCE}} | {{STATUS}} |
| Dependency direction | {{AUTHORITY}} | {{OUTCOME}} | {{EVIDENCE}} | {{STATUS}} |
| Dependency composition | {{AUTHORITY}} | {{OUTCOME}} | {{EVIDENCE}} | {{STATUS}} |
| Presentation state | {{AUTHORITY}} | {{OUTCOME}} | {{EVIDENCE}} | {{STATUS}} |
| Concurrency/cancellation | {{AUTHORITY}} | {{OUTCOME}} | {{EVIDENCE}} | {{STATUS}} |
| Navigation/restoration | {{AUTHORITY}} | {{OUTCOME}} | {{EVIDENCE}} | {{STATUS}} |
| Persistence/migrations | {{AUTHORITY}} | {{OUTCOME}} | {{EVIDENCE}} | {{STATUS}} |
| Protected boundaries | {{AUTHORITY}} | {{OUTCOME}} | {{EVIDENCE}} | {{STATUS}} |

## 9. Design Conformance

| Screen / Surface | Screen Contract | Exact Artifacts | Implemented States | Unsupported Content Excluded | Status |
|---|---|---|---|---|---|
| {{SCREEN}} | {{SCREEN_CONTRACT}} | {{ARTIFACTS}} | {{STATES}} | {{EXCLUDED_CONTENT}} | {{STATUS}} |

## 10. Automated Test Results

| Layer | Command / Procedure | Environment | Expected Result | Actual Result | Artifact | Limitation |
|---|---|---|---|---|---|---|
| Domain/unit | {{COMMAND}} | {{ENVIRONMENT}} | {{EXPECTED}} | {{ACTUAL}} | {{PATH}} | {{LIMITATION}} |
| State/presentation | {{COMMAND}} | {{ENVIRONMENT}} | {{EXPECTED}} | {{ACTUAL}} | {{PATH}} | {{LIMITATION}} |
| Repository/integration | {{COMMAND}} | {{ENVIRONMENT}} | {{EXPECTED}} | {{ACTUAL}} | {{PATH}} | {{LIMITATION}} |
| Persistence/migration | {{COMMAND}} | {{ENVIRONMENT}} | {{EXPECTED}} | {{ACTUAL}} | {{PATH}} | {{LIMITATION}} |
| UI automation | {{COMMAND}} | {{ENVIRONMENT}} | {{EXPECTED}} | {{ACTUAL}} | {{PATH}} | {{LIMITATION}} |
| Full CI | {{COMMAND}} | {{ENVIRONMENT}} | {{EXPECTED}} | {{ACTUAL}} | {{PATH}} | {{LIMITATION}} |

## 11. Runtime Evidence

| Scenario | Destination / OS | Command or Session | Expected Result | Actual Result | Artifact | Limitation |
|---|---|---|---|---|---|---|
| {{SCENARIO}} | {{DESTINATION}} | {{SESSION}} | {{EXPECTED}} | {{ACTUAL}} | {{PATH}} | {{LIMITATION}} |

## 12. Persistence and Data Integrity

| Concern | Expected Outcome | Procedure | Result | Evidence | Status |
|---|---|---|---|---|---|
| Store initialization | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Schema/version ownership | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Migration | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Failed-migration recovery | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Atomic operations | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Rollback | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Logical idempotency | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Duplicate/stale-write prevention | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Relaunch durability | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Date attribution/historical stability | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Test-store isolation | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |
| Backup/protection/deletion | {{EXPECTED}} | {{PROCEDURE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |

## 13. Localization and Bidirectional Layout

| Check | Environment | Result | Evidence | Limitation |
|---|---|---|---|---|
| Hardcoded-string scan | {{ENVIRONMENT}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Resource validation | {{ENVIRONMENT}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Approved locales | {{ENVIRONMENT}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Plurals/substitutions | {{ENVIRONMENT}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Locale-aware formatting | {{ENVIRONMENT}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| RTL runtime | {{ENVIRONMENT}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Mixed-direction content | {{ENVIRONMENT}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Long translation/truncation | {{ENVIRONMENT}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |

## 14. Accessibility Runtime

| Capability | Environment | Expected Outcome | Actual Result | Evidence | Limitation |
|---|---|---|---|---|---|
| Screen reader | {{ENVIRONMENT}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Focus order/restoration | {{ENVIRONMENT}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Text scaling/reflow | {{ENVIRONMENT}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Non-color differentiation | {{ENVIRONMENT}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Reduced motion | {{ENVIRONMENT}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Contrast/transparency adaptation | {{ENVIRONMENT}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Touch targets | {{ENVIRONMENT}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Alternative input | {{ENVIRONMENT}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Error/state announcements | {{ENVIRONMENT}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |

## 15. Adaptive, Window, and Lifecycle Runtime

| Scenario | Device / Window / OS | Expected Outcome | Actual Result | Evidence | Limitation |
|---|---|---|---|---|---|
| Compact window | {{DESTINATION}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Expanded/tablet window | {{DESTINATION}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Reduced/split/resized window | {{DESTINATION}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Orientation/posture change | {{DESTINATION}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Keyboard/IME and insets | {{DESTINATION}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Reflow/state preservation | {{DESTINATION}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Background/foreground | {{DESTINATION}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |
| Process termination/relaunch | {{DESTINATION}} | {{EXPECTED}} | {{RESULT}} | {{PATH}} | {{LIMITATION}} |

## 16. Privacy and Protected Boundaries

| Boundary | Expected Rule | Inspection / Runtime Result | Evidence | Status |
|---|---|---|---|---|
| {{BOUNDARY}} | {{RULE}} | {{RESULT}} | {{PATH}} | {{STATUS}} |

## 17. Production-Fake Detection

- Verdict: `{{PRODUCTION_FAKE_VERDICT}}`
- Release composition inspected: {{INSPECTION_SCOPE}}
- Fake/test/preview bindings found: {{RESULT}}
- Manufactured provider success found: {{RESULT}}
- Fixed success identifiers found: {{RESULT}}
- No-op infrastructure found: {{RESULT}}
- Debug bypasses found: {{RESULT}}
- Silent simulated fallback found: {{RESULT}}
- Evidence: {{PATH}}

## 18. Documentation Synchronization

| Document | Required Change | Status | Evidence / Commit |
|---|---|---|---|
| Feature contract | {{CHANGE_OR_NONE}} | {{STATUS}} | {{EVIDENCE}} |
| Implementation plan | {{CHANGE_OR_NONE}} | {{STATUS}} | {{EVIDENCE}} |
| Implementation tasks | {{CHANGE_OR_NONE}} | {{STATUS}} | {{EVIDENCE}} |
| ADRs | {{CHANGE_OR_NONE}} | {{STATUS}} | {{EVIDENCE}} |
| Architecture spine | {{CHANGE_OR_NONE}} | {{STATUS}} | {{EVIDENCE}} |
| Architecture coverage | {{CHANGE_OR_NONE}} | {{STATUS}} | {{EVIDENCE}} |
| Evidence index | {{CHANGE_OR_NONE}} | {{STATUS}} | {{EVIDENCE}} |
| Authorization records | {{CHANGE_OR_NONE}} | {{STATUS}} | {{EVIDENCE}} |

## 19. PR Review

- Review verdict: `{{PR_REVIEW_VERDICT}}`
- Blocking findings: {{BLOCKING_FINDINGS}}
- Non-blocking findings: {{NON_BLOCKING_FINDINGS}}
- Test gaps: {{TEST_GAPS}}
- Runtime layers not proven: {{UNPROVEN_LAYERS}}
- Commands run: {{COMMANDS}}
- Review record: {{PATH}}

## 20. Known Limitations and Unverified Claims

{{LIMITATIONS}}

## 21. Owner Decisions Required

{{OWNER_DECISIONS}}



## Blocker Classification

Classify each blocker as `IMPLEMENTATION`, `CI`, `EVIDENCE`, `DOCUMENTATION`, `REPOSITORY_STATE`, or `OWNER_DECISION`. Do not use `BLOCKED BY IMPLEMENTATION DEFECT` for missing evidence, documentation drift, or an uncommitted working tree unless there is also a production defect.

## Evidence Reuse Summary

Map each current evidence artifact to all requirements/verification rows it validly proves. List only genuinely missing/stale scenarios as rerun work; do not demand one unique execution/artifact per verification ID.

## Final-Readiness Manual Checks

List applicable manual/device-only checks separately from implementation defects, with environment, steps, actual result, artifact/notes, and limitations.

## 22. Final Readiness Verdict

**Verdict:** `{{VERDICT}}`

Allowed values:

- `READY FOR FINAL READINESS`
- `READY FOR FEATURE READINESS REVIEW`
- `READY FOR OWNER ACCEPTANCE`
- `BLOCKED BY IMPLEMENTATION DEFECT`
- `BLOCKED BY ARCHITECTURE DRIFT`
- `BLOCKED BY SCOPE DRIFT`
- `BLOCKED BY CI`
- `BLOCKED BY MISSING EVIDENCE`
- `BLOCKED BY DOCUMENTATION SYNC`
- `BLOCKED BY REPOSITORY STATE`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

This verdict does not authorize release, signing, distribution, TestFlight, App Store submission, Play Console deployment, or production publication.

## 23. Owner Acceptance Record

| Role | Name | Decision | Date | Notes |
|---|---|---|---|---|
| Repository owner |  | Pending |  |  |
