---
name: pr-review
description: Review one coherent task diff for defects, regressions, scope drift, protected-boundary violations, documentation impact, adaptive-UI issues, and missing evidence.
---

# PR Review

Read `AGENTS.md`, routed context, PR description, complete target-branch diff, and nearby tests. Confirm scope; trace changed behavior through callers/state/data/platform boundaries; prioritize concrete defects and regressions; check architecture-coverage effects; verify documentation-impact evidence; flag unapproved protected work; cite tight file/line ranges; separate blockers, non-blockers, questions, and test gaps. Report commands actually run and unverified runtime layers. Do not merge or authorize publication.

## Adaptive UI review

When the diff changes a Compose screen, shared component, navigation shell, dialog, sheet, camera/media UI, or screen-level state:

- identify the approved device/window/orientation support contract;
- check for phone-only, portrait-only, fixed-container, and stretch-only assumptions;
- inspect compact and expanded arrangements;
- check resize/orientation state preservation and lifecycle effects;
- check RTL, large text, insets, cutouts, IME, and relevant keyboard/mouse/focus behavior;
- verify adaptive navigation changes occur at the correct architecture level;
- review relevant previews, screenshot/UI tests, and runtime evidence;
- distinguish static review from device compatibility proof.

Do not require every leaf composable to receive `WindowSizeClass` directly. Review effective screen and application behavior.
