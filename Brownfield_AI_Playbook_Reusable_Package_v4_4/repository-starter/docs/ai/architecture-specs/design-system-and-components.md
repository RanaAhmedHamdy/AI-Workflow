# Design System and UI Components map specification

## Checklist coverage

- Design system and shared components
- Theming, tokens, reusable presentation states, and component ownership
- Design-authority-to-Compose evidence boundary

## Discovery question

How are the Warm Mentor product direction, Material theme tokens, typography,
shapes, icons, illustrations, shared components, and repeated feature states
implemented and reused, and where does source diverge from or incompletely
realize the design guidance?

## Required evidence

- `ai-context/DESIGN_SYSTEM.md`
- `ui/theme/`
- `ui/components/`
- navigation shell and representative feature Screens/previews
- local drawable/vector resources
- reviewed feature and Architecture pages
- relevant dependency declarations and current UI-test gaps

## Required content

- authority distinction between product design guidance and implemented source
- color, typography, shape, spacing, elevation, and icon ownership
- shared component inventory and reuse boundaries
- illustration/visual mapping
- component state patterns: selected, locked, success, safety, information,
  notebook/script, disabled
- screen-specific exceptions and duplication
- preview/test coverage and visual/runtime evidence limits
- remote/copyrighted asset and emoji restrictions

Keep device adaptation, localization, and accessibility detail in the dedicated
UI Adaptation and Accessibility map; cross-link rather than duplicate it.
