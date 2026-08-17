---
name: ios-privacy-capability-readiness
description: Audits privacy manifests, required-reason APIs, usage descriptions, capabilities, entitlements, and sensitive Apple frameworks.
---

# iOS Privacy and Capability Readiness

Review:

- Privacy Manifest and third-party manifests;
- required-reason API declarations;
- `Info.plist` usage descriptions;
- data categories, purpose, minimization, consent, retention, deletion;
- analytics, tracking, advertising, crash reporting;
- entitlements and capabilities;
- App Groups and Keychain groups;
- associated domains, URL schemes, universal links;
- push notifications and background modes;
- camera, microphone, photos, contacts, location, Bluetooth, HealthKit, HomeKit, and other permissioned frameworks;
- StoreKit and entitlement state;
- signing/provisioning impact.

A framework import does not authorize a permission or capability. Missing configuration must fail closed.

Return exact protected boundaries, required owner decisions, evidence, and verdict.
