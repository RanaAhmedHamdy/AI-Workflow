---
name: swiftui-screen-readiness
description: Validates a SwiftUI screen before implementation and before completion.
---

# SwiftUI Screen Readiness

## Pre-implementation

Require:

- governing spec and design contract;
- state owner and lifetime;
- dependency composition path;
- route/container boundary;
- render/content boundary where practical;
- navigation, sheet, popover, dismissal, and restoration contract;
- loading, empty, failure, recovery, disabled, and success states;
- localization and formatting inventory;
- iPhone/iPad/size-class/multitasking behavior;
- Dynamic Type and VoiceOver expectations;
- preview and runtime matrix;
- evidence paths and stop conditions.

## Completion scan

Flag:

- network, persistence, authorization, or domain work in `body`;
- feature model recreation during view recomputation;
- unowned `Task` side effects;
- application routers or repositories passed to leaf views;
- hardcoded strings;
- fixed-height text;
- hardcoded left/right behavior;
- compact-only or portrait-only assumptions;
- inaccessible custom controls;
- previews presented as runtime evidence.

## Verdicts

- `Ready for implementation`
- `Blocked before implementation`
- `Ready for runtime verification`
- `Not ready`

## Post-Mutation and Route-Origin Readiness (v1.7)
For any screen that commits durable state, identify dependent parent/sibling/cross-feature consumers and prove their render state updates from the authoritative source without relying on accidental navigation reload. Also prove that a dependent consumer created or re-entered after the mutation loads current committed state even if it did not observe the original event. For reusable screens entered from multiple origins, verify save/cancel/failure semantics per origin, including explicit separation of onboarding/setup completion from normal management and prevention of mode-to-mode return-state aliasing.
