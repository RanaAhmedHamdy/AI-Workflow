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
