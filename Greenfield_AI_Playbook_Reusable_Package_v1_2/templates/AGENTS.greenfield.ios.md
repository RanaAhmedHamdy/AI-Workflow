# AGENTS.md - Greenfield Native iOS Overlay

Use with `AGENTS.common.md`. These are defaults, not inferred project facts. Record an explicit decision for material exceptions.

## Project defaults

- Define deployment targets, project generation, dependency management, concurrency, observation, navigation, persistence, and testing choices during Phase 0/1.
- Prefer Swift Concurrency and a single observable-state approach compatible with the deployment target; do not mandate `@Observable` when the target cannot support it.
- Prefer Swift Package Manager unless a documented dependency constraint requires another manager.

## Adaptive and accessible UI

- Define iPhone/iPad/multitasking/Stage Manager/Catalyst/orientation scope before the first representative screen is complete.
- Use size-aware navigation/layout only for approved form factors; support Dynamic Type, VoiceOver semantics/focus, RTL/localization catalogs, and representative previews/tests.
- Avoid fixed-height text containers and sentence concatenation across localized fragments.

## Testing defaults

- Select and document XCTest/test-plan/snapshot/UI-test strategy during Phase 0/1.
- Prefer domain/state tests, then component/semantics or snapshot evidence, then a small set of XCUITest journeys where lower layers cannot prove the acceptance contract.

## Architecture-changing decisions

Record decisions before adding a new dependency manager, observation/concurrency framework, networking stack, persistence layer, analytics/crash system, feature-flag platform, background-task architecture, or target family.
