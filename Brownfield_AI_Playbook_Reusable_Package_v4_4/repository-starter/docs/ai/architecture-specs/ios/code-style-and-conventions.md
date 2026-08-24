# Code Style and Conventions map specification

## Checklist coverage

- Naming, file/type organization, layering, and dependency conventions
- UIKit/SwiftUI boundary and presentation conventions where observed
- State, concurrency, dependency-construction, resource, test, generated-source, and documentation conventions
- Formatting/lint/tooling conventions and material exceptions

## Discovery question

What naming, file organization, layering, UI, routing, state, concurrency, dependency-construction, resource, localization, testing, formatting, and generated-source conventions are consistently observed in this native iOS repository, and what material exceptions exist?

## Required evidence

Inspect representative current evidence from the major application and test areas, including where applicable:

- Swift and Objective-C source across major features/layers/targets
- view controllers, views, storyboards/XIBs, SwiftUI views, routers/coordinators, presenters/interactors/view models, services/repositories, and shared utilities actually present
- concurrency/observation patterns such as callbacks/delegates, NotificationCenter, GCD, OperationQueue, Combine, async/await, actors, ObservableObject, Observation, or other mechanisms actually present
- dependency construction/composition patterns
- asset catalogs, localization resources, generated-resource/source mechanisms, and target-specific resources
- XCTest/XCUITest/Swift Testing sources and test doubles actually present
- SwiftFormat, SwiftLint, compiler warnings, scripts, editor configuration, or other formatting/lint evidence actually present
- generated/build exclusions and Graphify/generated-output boundaries
- reviewed Modules, Architecture, State, DI, Design System, Testing, and feature documentation

## Required content

- directory/file/type/function/property naming conventions
- feature/layer/ownership and dependency-direction conventions
- UIKit/storyboard/XIB/SwiftUI boundaries and repeated presentation patterns actually observed
- router/coordinator/navigation ownership conventions where present
- presenter/interactor/view-model/state-owner conventions where present
- callback/delegate/notification/concurrency conventions and thread/actor expectations where evidenced
- dependency-construction, initializer/property injection, container, singleton, and service-locator conventions where observed
- resource, localization, accessibility-facing string, asset, and target-membership conventions
- test naming, organization, doubles, fixtures, assertions, and execution-boundary conventions
- generated source/resource, comments, documentation, formatting/lint, and graph-output rules
- observed exceptions, inconsistencies, mandatory policy versus common practice, and `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not convert frequent patterns into mandatory policy unless `AGENTS.md`, reviewed decisions, or equivalent authority establishes them.
- Do not prescribe UIKit-to-SwiftUI, callback-to-async/await, Combine-to-Observation, XCTest-to-Swift-Testing, or other modernization.
- Do not normalize folders, rename types, reformat unrelated code, or create lint/format tooling in this documentation task.
