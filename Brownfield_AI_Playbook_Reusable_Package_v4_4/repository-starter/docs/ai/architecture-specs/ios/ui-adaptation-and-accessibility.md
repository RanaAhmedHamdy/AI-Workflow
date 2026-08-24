# UI Adaptation and Accessibility map specification

## Checklist coverage

- Supported iPhone/iPad/form-factor behavior and adaptive layout strategy
- Orientation, size classes, split view, multitasking, scene/window, safe-area, keyboard, and input behavior
- Localization, RTL, Dynamic Type, VoiceOver, focus, contrast, motion, and accessibility semantics
- Rendering/resource behavior where it materially affects supported UI

## Discovery question

What device/form-factor, orientation, size-class, resize/multitasking, scene/window, keyboard/input, safe-area, localization/RTL, large-text, VoiceOver, focus, contrast, motion, and restoration behavior is declared or implemented, and which support claims remain runtime/device/accessibility `Needs verification`?

## Required evidence

Inspect only applicable current evidence, including:

- `AGENTS.md`, approved support requirements, and relevant project-owned iOS skills as procedures rather than proof
- target device-family/deployment/build settings and app/scene configuration
- UIKit storyboards/XIBs, Auto Layout constraints, size-class variations, trait handling, split-view/tab/navigation structures, custom layout code, and SwiftUI layout only if present
- representative feature UI, reusable components, dialogs/sheets/popovers, scroll views, keyboard handling, and safe-area behavior
- localization resources, string catalogs/`.strings`/`.stringsdict`, locale-aware formatting, and RTL-sensitive layout code
- accessibility labels/values/traits/actions, focus behavior, Dynamic Type/font scaling, content-size handling, contrast/motion behavior where implemented
- iPad/multitasking/pointer/keyboard support code where present
- UI/snapshot/accessibility tests and recorded simulator/device evidence actually available
- reviewed Design System, Navigation, State, Testing, and feature pages

## Required content

- supported-device/form-factor matrix with evidence status
- Auto Layout/size-class/trait/adaptive-container patterns
- iPhone/iPad/split-view/multitasking/orientation/resizing classification
- scene/window/safe-area/keyboard behavior and ownership
- touch, hardware keyboard, pointer/trackpad, focus, and text-input classification where relevant
- localization resources, formatting, plurals, hardcoded-string findings, and RTL behavior
- Dynamic Type/font scaling and accessibility-size behavior
- VoiceOver labels/values/traits/actions/headings/focus evidence
- contrast, touch target, Reduce Motion, animation, and degraded/permission-state accessibility where evidenced
- state preservation across rotation/resizing/scene transitions/relaunch where evidenced
- UI-test/snapshot/simulator/device/human accessibility evidence and gaps
- `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not infer universal iPhone/iPad support from Auto Layout or target device-family settings alone.
- Do not claim VoiceOver, Dynamic Type, RTL, keyboard, pointer, multitasking, or restoration behavior without matching runtime/human evidence where required.
- Do not introduce `NavigationSplitView`, new layout architecture, new accessibility frameworks, or broad storyboard rewrites.
- Do not change constraints, size classes, localization resources, or target support in this documentation task.
