# Design System and UI Components map specification

## Checklist coverage

- Visual tokens, assets, typography, colors, spacing, and component ownership
- Shared UIKit/SwiftUI components and repeated presentation states
- Target/flavor theming and branded-resource boundaries
- Design-authority-to-implementation evidence boundary

## Discovery question

How are visual tokens, asset catalogs, colors, typography, images/icons, storyboards/XIBs, shared UIKit/SwiftUI components, and repeated feature states implemented and reused, including target/flavor variation, and where does current source diverge from documented design guidance?

## Required evidence

Inspect only applicable current evidence, including:

- reviewed design/product guidance that is explicitly authoritative, kept separate from implementation evidence
- asset catalogs, colorsets, imagesets, fonts, localization resources, and target membership
- shared UIKit views/view controllers, custom controls, cells, reusable XIBs/storyboards, appearance helpers, and SwiftUI components if present
- representative feature UI from Reviewed feature pages
- target/flavor-specific asset catalogs/storyboards/resources/configuration where present
- dependencies that materially provide UI components/theme behavior
- snapshots/UI tests/previews only where actually present
- reviewed Architecture, feature pages, and UI/accessibility context

## Required content

- authority distinction between design guidance and implemented source
- color, typography, spacing, shape, image/icon, and asset ownership
- shared component inventory and reuse boundaries
- storyboard/XIB/component relationships and target membership where material
- repeated UI state patterns: loading, empty, error, selected, disabled, success, warning, permission/degraded, etc., when observed
- target/flavor branding/theming boundaries
- screen-specific duplication and exceptions supported by evidence
- visual test/snapshot/preview/device evidence and gaps
- remote/licensed/copyright-sensitive asset boundaries where relevant
- `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Keep detailed device adaptation, localization, RTL, Dynamic Type, and accessibility behavior in the dedicated UI Adaptation and Accessibility map; cross-link instead of duplicating it.
- Do not invent a token system or design-system authority that is not present.
- Do not migrate storyboards/XIBs to SwiftUI or consolidate components merely for consistency.
- Do not move branded resources between targets or asset catalogs in this documentation task.
