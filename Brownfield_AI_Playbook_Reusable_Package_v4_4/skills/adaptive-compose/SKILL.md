---
name: adaptive-compose
description: Design, implement, and review Jetpack Compose UI across supported Android devices, orientations, window sizes, input modes, RTL, and large-text configurations without introducing unauthorized architecture changes.
---

# Adaptive Compose

Use this skill for a new Compose screen, a material screen-layout change, navigation-shell work, tablet/foldable/ChromeOS/orientation/multi-window work, or an adaptive-layout audit.

## Read first

- `AGENTS.md`.
- The affected feature document selected through `AI_CONTEXT.md`.
- Current design-system, UI-component, localization/accessibility, and architecture-coverage documents.
- The affected screen, navigation shell, state holder, nearby previews/tests, and dependency/build rules.

## Establish the support contract

Record which configurations apply: compact, medium, and expanded windows; portrait and landscape; phones, tablets, foldables, and ChromeOS-capable devices; multi-window and resized windows; touch, keyboard, mouse, and trackpad; RTL, font/display scaling, cutouts, system bars, IME, and relevant fold posture.

Do not infer that an untested configuration is supported.

## Inspect current architecture

Determine where adaptive information is produced; whether navigation adapts; whether pane layouts exist; whether state survives resize/orientation/recreation; whether fixed container assumptions exist; whether content reflows, clips, overlaps, or stretches; and whether dialogs, sheets, forms, CameraX, or media behavior depends on window state.

## Implementation guidance

- Prefer flexible constraints, weights, adaptive grids, flow layouts, content-width limits, and pane arrangements over fixed screen-sized containers.
- Use compact versus expanded information architecture intentionally.
- Keep adaptive navigation at the correct application or feature-shell boundary.
- Preserve shared business state and semantics across layout variants.
- Handle insets, cutouts, IME, and system bars.
- Preserve localization, RTL, accessibility, and large-text behavior.
- Avoid broad shell, dependency, or architecture changes during a bounded screen task unless explicitly authorized.

Material 3 adaptive APIs are preferred only when compatible with the approved dependency and architecture strategy. This skill does not authorize adding or upgrading dependencies.

## Foldables

Consider posture and display features when a hinge can obscure content, a dual-pane arrangement materially improves the task, camera/media placement depends on posture, or foldable optimization is explicitly required. Do not add fold-specific architecture when responsive reflow is sufficient.

## Previews and tests

Prefer representative coverage for compact portrait, compact landscape, expanded width, RTL, large font, and relevant loading/empty/error/populated states. Use the repository's existing preview, screenshot, Compose UI, and instrumented-test stack.

Static previews do not replace runtime verification for recreation, multi-window, fold posture changes, keyboard/mouse interaction, CameraX, system UI, TalkBack, or actual device rendering.

## Anti-patterns

Flag fixed phone-sized roots, portrait assumptions, raw-pixel layout logic, duplicate business state per layout, shell navigation embedded in leaf UI, hardcoded left/right positioning, clipped large text, stretch-only tablet layouts, unapproved adaptive dependencies, and universal-support claims based only on previews or static review.

## Required output

Report support configurations assessed, current adaptive mechanism, files changed, previews/tests added, runtime checks performed, unsupported or unverified configurations, and architecture/dependency decisions still required.
