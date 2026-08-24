# State Management map specification

## Checklist coverage

- State ownership, lifetime, observation, concurrency, lifecycle, and restoration
- Persisted versus cached versus derived versus transient UI state
- Cross-feature shared state and one-off events
- Dependency boundaries that influence state lifetime

## Discovery question

Which objects own application/session/navigation/feature/UI state, how is state observed and mutated, what thread/actor/queue/lifecycle rules apply, what is persisted or reconstructed, and where are restoration, cancellation, concurrency, or shared-state behavior unverified?

## Required evidence

Inspect current mechanisms actually present, including where applicable:

- view controllers/views/cells and their mutable state
- presenters/interactors/view models/controllers/state structs/models
- app/scene delegates and shared/session/global managers
- routers/coordinators/navigation state
- repositories/services and persisted/cache-backed state
- callbacks/delegates, NotificationCenter, KVO, GCD/OperationQueue, Combine, async/await/actors, ObservableObject, Observation, SwiftUI state, or other observation/concurrency mechanisms actually present
- lifecycle methods, notification observers, cancellation/cleanup, and scene transitions
- state-related tests and Reviewed feature pages
- reviewed Data Flow, Persistence, Navigation, DI, Architecture, and Testing maps

## Required content

- state-owner inventory by scope/lifetime
- persisted, cached, derived, transient, navigation, and one-off-event state
- observation/update mechanisms and dependency relationships
- main-thread/MainActor/queue/actor expectations where evidenced
- callback/delegate/notification/publisher/task lifetimes and cancellation behavior
- UI/controller versus presenter/interactor/view-model/service state boundaries
- application/session/shared mutable state and isolation risks supported by evidence
- scene/background/foreground/restoration/relaunch behavior and gaps
- rapid action, duplicate request, reentrancy, concurrent edit, and ordering behavior where relevant
- error/loading/action-in-progress representation
- test seams and runtime evidence limits
- `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not prescribe `ObservableObject`, Observation, Combine, async/await, actors, `@MainActor`, SwiftUI state, or another state model.
- Do not introduce a second application-wide observation/concurrency model.
- Do not claim process/scene restoration from static state declarations alone.
- Do not refactor singleton/shared state, callback chains, or presenter/interactor ownership in this documentation task.
