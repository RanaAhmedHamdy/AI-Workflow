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
