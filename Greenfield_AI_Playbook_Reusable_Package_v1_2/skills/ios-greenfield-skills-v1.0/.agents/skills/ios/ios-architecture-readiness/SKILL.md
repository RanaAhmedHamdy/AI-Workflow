---
name: ios-architecture-readiness
description: Validates that required iOS architecture selections are decided before planning or implementation.
---

# iOS Architecture Readiness

## Inspect

- feature scope and protected boundaries;
- exact approved Xcode, Swift language mode, SDK, deployment targets;
- SwiftUI/UIKit/hybrid choice;
- observation/state model;
- concurrency and actor isolation;
- navigation and restoration;
- dependency composition;
- persistence and migration ownership;
- networking and external-service boundaries;
- background execution and extensions;
- privacy manifests, capabilities, entitlements, permissions;
- testing, simulator/device, archive, and release evidence.

## Block when

- a required selection is missing or contradictory;
- the plan silently chooses a framework, target, capability, or dependency;
- strict concurrency or language-mode changes lack migration scope;
- a protected platform boundary lacks authorization;
- external configuration lacks fail-closed behavior;
- tasks lack concrete evidence scenarios.

## Verdict

- `Ready for planning`
- `Ready with explicit limitations`
- `Blocked`
