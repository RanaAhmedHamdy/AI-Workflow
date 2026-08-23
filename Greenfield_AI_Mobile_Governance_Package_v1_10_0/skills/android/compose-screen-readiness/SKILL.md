---
name: compose-screen-readiness
description: Runs before Compose implementation and before completion to enforce state ownership, route/content structure, localization, adaptation, accessibility, and evidence.
---
# Compose Screen Readiness

## Pre-implementation mode
For each screen verify:
- governing spec/design/screen contract;
- for a design-bound screen, exact approved visual artifact/variant is identified and actually inspectable;
- pre-code visual inspection is required; Markdown descriptions do not substitute for the approved visual;
- Design Lock and only permitted platform/accessibility/localization/RTL/responsive/owner-approved adaptations are explicit;
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

## Post-Mutation and Route-Origin Readiness (v1.9)
For any screen that commits durable state, identify dependent parent/sibling/cross-feature consumers and prove their render state updates from the authoritative source without relying on accidental navigation reload. Also prove that a dependent consumer created or re-entered after the mutation loads current committed state even if it did not observe the original event. For reusable screens entered from multiple origins, verify save/cancel/failure semantics per origin, including explicit separation of onboarding/setup completion from normal management and prevention of mode-to-mode return-state aliasing.
