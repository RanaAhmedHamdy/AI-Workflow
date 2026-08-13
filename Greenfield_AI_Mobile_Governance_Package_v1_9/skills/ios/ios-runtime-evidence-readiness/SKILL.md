---
name: ios-runtime-evidence-readiness
description: Classifies and validates iOS evidence across tests, simulators, devices, services, archives, and release artifacts.
---

# iOS Runtime Evidence Readiness

## Evidence classes

- Swift Testing
- XCTest
- XCUITest
- snapshot/visual regression
- simulator runtime
- physical-device runtime
- VoiceOver/manual accessibility
- Dynamic Type and RTL runtime
- background execution
- universal-link/deep-link verification
- StoreKit test/staging evidence
- privacy manifest/entitlement artifact inspection
- archive/export/signing evidence
- external-service attestation

Every task must name:

- observable contract;
- environment/destination and OS;
- command/session;
- expected result;
- artifact path;
- actual outcome;
- limitations.

A task marked complete without matching evidence is improperly closed and must be reopened.
## Verification-Matrix Executability

When the approved implementation plan contains `VM-*` scenarios, verify before evidence execution that each applicable scenario is runnable: the ID exists and traces to approved authority; the named simulator/device/OS/locale/accessibility condition is available or has an approved equivalent; preconditions are reproducible; the procedure is concrete; the expected observable result is explicit; the evidence path is usable; and runtime-only claims use runtime-capable evidence. Report unavailable scenarios as blocked/needs verification rather than silently substituting evidence.

This skill checks executability only. It does not maintain a second per-scenario lifecycle status system and does not manufacture `PASS` evidence.

## Runtime Evidence Optimization

Classify runtime checks by timing. Keep critical behavior/lifecycle checks at task closure only when the task changes them; run cross-feature journeys at convergence; reserve expensive device/manual/platform-hardening checks for final readiness unless directly affected.

Use a representative risk matrix rather than exhaustive combinations. For a typical UI feature, one primary phone configuration, one approved RTL locale, one maximum-text/accessibility layout configuration, one representative tablet/adaptive configuration, and one critical screen-reader journey are usually sufficient unless product/risk authority requires more.

Prefer manual validation for real screen-reader focus/announcements, subjective final visual fidelity, alternate-input ergonomics, representative adaptive/RTL quality, and physical-device-only behavior. Keep deterministic automation for navigation, state propagation, data correctness, transactions, idempotency, and migrations.
