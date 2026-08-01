# UI Adaptation and Accessibility map specification

## Checklist coverage

- UI adaptation and supported form factors
- Localization/internationalization
- Accessibility
- Rendering/resource performance where it affects supported UI behavior

## Discovery question

What compact, medium, expanded, orientation, resize, multi-window, foldable,
ChromeOS, input, RTL, large-text, inset, IME, semantics, focus, and restoration
behavior is implemented, declared, tested, absent, or still owner-dependent?

## Required evidence

- `.agents/skills/adaptive-compose/SKILL.md` as procedure, not evidence
- `AGENTS.md` support requirements and `ai-context/DESIGN_SYSTEM.md`
- theme, components, navigation shell, representative Screens, dialogs/sheets,
  previews, and string resources
- manifest orientation/window declarations
- Compose/instrumented test sources and reviewed Testing Map
- reviewed Design System, Navigation, State Management, and feature pages

## Required content

- explicit support matrix with evidence status
- layout/reflow/container-width patterns
- navigation adaptation ownership
- orientation, resize, multi-window, foldable, and ChromeOS classification
- touch, keyboard, mouse, trackpad, focus, and IME classification
- RTL, localization resources, plurals/formatting, and hardcoded-string evidence
- font/display scaling, semantics, content descriptions, touch targets, and contrast
- insets, cutouts, system bars, dialogs, sheets, and sticky controls
- state preservation across configuration and process recreation
- preview, UI-test, screenshot, device, accessibility, and performance evidence

Do not infer universal device support from flexible Compose layouts or previews.
