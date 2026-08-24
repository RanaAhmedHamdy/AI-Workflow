# Data Flow map specification

## Checklist coverage

- End-to-end cross-feature data flow and ownership
- Remote/API, local persistence/cache, and external-integration boundaries
- Identity/argument transport and transformation boundaries
- Target/flavor divergence where material

Application/module structure remains owned by the reviewed project `ARCHITECTURE.md` and `MODULES.md`; cross-link rather than duplicating them.

## Discovery question

How does application data move from user/system entry points through the repository's actual UI/state/business layers into services, networking, local persistence/cache, platform services, and external integrations, and where are ownership, transformation, error, lifetime, and evidence boundaries unclear?

## Required evidence

Use the completed Reviewed feature pages as the primary routing source, then inspect only directly relevant current evidence, including where applicable:

- UIKit view controllers/views/storyboards/XIBs or SwiftUI views actually present
- routers/coordinators/navigation callbacks and argument transport
- presenters/interactors/view models/controllers/state owners actually present
- repositories/services/managers/data sources and their interfaces
- `URLSession`, Alamofire, Socket.IO, Firebase, or other network/integration code actually present
- `UserDefaults`, Keychain, files/caches, Core Data, SQLite/Realm/SwiftData, or other storage actually present
- dependency construction/composition points
- target/flavor configuration that changes source, resources, endpoints, or flow
- existing tests that prove transformations, forwarding, state transitions, or persistence behavior
- reviewed Architecture, Modules, Dependencies, Testing, and relevant feature pages

## Required content

- major data owners and their lifetimes
- representative end-to-end flows from entry/UI to final local/remote/platform boundary
- user input, route/argument, identifier, model/DTO/domain/view-data transformations
- source-of-truth and derived-data relationships where evidenced
- local versus remote ownership and cache/persistence interaction
- callbacks/delegates/notifications/publishers/async-completion/concurrency boundaries actually observed
- write ordering, refresh/sync, invalidation, and consistency behavior where evidenced
- target/flavor divergence and shared-flow boundaries
- external API/backend/platform integration boundaries and contract uncertainty
- error/degraded paths and missing evidence
- small diagrams/tables that improve routing without duplicating feature pages
- `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not invent repository/service/domain layers that are not present.
- Do not infer backend semantics, transaction guarantees, ordering, or production source-of-truth from client code alone.
- Do not refactor, introduce repositories/use cases, replace networking libraries, or redesign data flow.
- Do not duplicate detailed feature narratives already owned by Reviewed feature pages.
