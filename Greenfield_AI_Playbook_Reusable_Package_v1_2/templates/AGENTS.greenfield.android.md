# AGENTS.md - Greenfield Native Android Overlay

Use with `AGENTS.common.md`. These are defaults, not inferred project facts. Record an explicit decision for material exceptions.

## Project defaults

- Kotlin, Gradle Kotlin DSL, and a Version Catalog for dependency versions.
- Compose-first UI unless product/platform constraints require Views.
- Coroutines and read-only StateFlow for observable screen state; event in, state out.
- Dependency direction and module boundaries defined before scaling beyond the first vertical slice.

## Adaptive UI and supported Android surfaces

Every new or materially changed Compose screen MUST support the project's approved Android surface matrix.

The default greenfield matrix includes compact, medium, and expanded windows; phones, tablets, foldables, and ChromeOS-capable devices; portrait, landscape, runtime orientation changes, split-screen, multi-window, resized windows, touch, keyboard, mouse, trackpad, RTL, font/display scaling, cutouts, IME, and system bars.

Implementation requirements:

- use window/adaptive information at the appropriate application or feature boundary;
- avoid phone-only and portrait-only assumptions;
- avoid fixed container dimensions that prevent reflow;
- use adaptive navigation and list-detail patterns only where information architecture requires them;
- preserve state across resize, orientation, and activity recreation;
- consider fold posture and display features when materially relevant;
- provide compact and expanded previews for representative states;
- add focused automated or runtime verification appropriate to the changed UI.

Material 3 adaptive APIs are preferred when compatible with the approved dependency and platform strategy. Their use does not authorize dependency additions or upgrades without review.

Static inspection and previews do not prove device compatibility. Unverified runtime configurations must be reported.

- Skill: `.agents/skills/adaptive-compose/SKILL.md`.

## Localization and accessibility

- No hardcoded user-facing strings; use resources, format/plural APIs, and start/end semantics.
- Preserve RTL, font scaling, semantics, focus behavior, touch targets, and accessible state descriptions.
- Exercise at least one RTL and one large-font configuration before a representative screen is considered complete.

## Testing defaults

- Select and document the test stack during Phase 0/1; do not hardcode JUnit 4 versus 5 in this template.
- Prefer domain/state tests, then component/semantics tests, then a small set of instrumented/E2E journeys where lower layers cannot prove the acceptance contract.
- Establish CI commands and artifact/runtime gates before release work.

## Architecture-changing decisions

Record decisions before adding a new DI framework, networking stack, persistence layer, analytics/crash system, feature-flag platform, background-work architecture, adaptive-navigation architecture, or module family.
