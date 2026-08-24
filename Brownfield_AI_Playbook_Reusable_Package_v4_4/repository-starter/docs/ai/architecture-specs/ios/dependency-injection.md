# Dependency Injection map specification

## Checklist coverage

- Dependency construction, injection, service location, and composition roots
- Scope/lifetime, dependency direction, isolation, cycles, and shared mutable dependencies
- Test/preview seams and target-specific composition

## Discovery question

How are application services, feature objects, routers/coordinators, presenters/interactors/view models, repositories, networking/storage clients, and platform integrations constructed, passed, scoped, and replaced for tests/previews, and where does service location or hidden global state occur?

## Required evidence

Inspect current evidence where applicable:

- application/scene entry points and root composition
- routers/coordinators/factories/builders/assemblers and feature creation paths
- initializer/property/delegate injection
- singleton/static/shared-instance/service-locator patterns
- dependency containers or third-party DI frameworks only if actually present
- presenter/interactor/view-model/controller constructors and mutable dependencies
- repositories/services/network/storage/platform clients
- target/flavor-specific composition or registration
- XCTest setup, fakes, stubs, mocks, protocol abstractions, preview composition, and test-only factories
- reviewed Data Flow, Modules, Dependencies, Architecture, Testing, and feature pages

## Required content

- composition roots and feature-assembly paths
- provider/factory/container/manual-construction inventory
- dependency direction and ownership
- singleton/application/scene/feature/view-controller/UI-local lifetimes where evidenced
- initializer/property/delegate/service-locator patterns and exceptions
- target/flavor-specific dependency differences
- test/preview replacement seams and hard-to-replace dependencies
- possible cycles or shared mutable state supported by evidence
- static construction evidence versus runtime lifecycle evidence
- isolation/testability observations and `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not assume Swinject, Resolver, Factory, Needle, or any DI framework exists.
- Do not introduce a DI container, service locator, protocol layer, or factory merely to improve testability.
- Do not label manual construction as defective by default; document the verified current pattern and its consequences.
- Do not infer successful runtime construction solely from declarations or project references.
