---
name: compose-screen-readiness
description: Runs before Compose implementation and before completion to enforce state ownership, route/content structure, localization, adaptation, accessibility, and evidence.
---
# Compose Screen Readiness

## Pre-implementation mode
For each screen verify:
- governing spec/design/screen contract;
- named ViewModel/state owner and lifecycle scope;
- route obtains state holder through approved composition;
- stateless content takes immutable state/callbacks only;
- navigation handled through callbacks at the correct boundary;
- resource key inventory and required locales;
- RTL/start-end behavior;
- compact/medium/expanded and orientation/resize contract;
- loading/empty/failure/recovery/disabled states;
- large-font, semantics, focus, touch targets, IME/insets;
- preview, test, and runtime matrix;
- prohibited patterns and stop conditions.

## Completion mode
Scan for hardcoded strings, manual ViewModel/dependency construction, Activity-owned feature state, public mutable state, domain work in Composables, leaf `NavController`, fixed phone roots, left/right assumptions, clipped large text, missing locale keys, absent semantics, and unsupported runtime claims.

Verdicts: `Ready for implementation`, `Blocked before implementation`, `Ready for runtime verification`, `Ready with limitations`, `Not ready`.

## Post-Mutation and Route-Origin Readiness (v1.6)
For any screen that commits durable state, identify dependent parent/sibling/cross-feature consumers and prove their render state updates from the authoritative source without relying on accidental navigation reload. For reusable screens entered from multiple origins, verify save/cancel/failure semantics per origin, including explicit separation of onboarding/setup completion from normal management.
