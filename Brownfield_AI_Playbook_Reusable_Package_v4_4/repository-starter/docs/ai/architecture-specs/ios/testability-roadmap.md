# Testability Roadmap specification

## Checklist coverage

- Existing test targets/layers, deterministic seams, doubles, and runtime evidence
- Cross-map contract coverage and material verification gaps
- Simulator/device/accessibility/security/performance/build/release evidence layers
- Smallest risk-backed sequence for improving confidence without speculative infrastructure

## Discovery question

Which deterministic seams and test layers already exist, which material feature/architecture contracts are covered or uncovered, what infrastructure or environment blocks stronger evidence, and what is the smallest risk-backed verification sequence using the repository's established testing stack?

## Required evidence

- all test targets/sources relevant to current scope
- Xcode schemes, test plans, `TEST_HOST`, host applications, destinations, and test build settings where material
- XCTest, XCUITest, Swift Testing, snapshots, integration harnesses, or other frameworks only if actually present
- reviewed `TESTING_MAP.md`
- all Reviewed Phase 3 maps available at the time this roadmap is created
- feature-page `Needs verification`, runtime gaps, and test candidates
- existing fakes/stubs/mocks/protocol seams and deterministic helpers
- CI/scripts/shared validation configuration actually present
- latest recorded test execution evidence, including environment workarounds, without silently rerunning tests

## Required content

- current test targets/layers/frameworks and execution paths
- contract-to-evidence matrix across important feature/architecture risks
- deterministic seams, injectable boundaries, and available doubles
- host/scheme/target/flavor execution constraints
- high-risk uncovered behavior and no-safe-seam cases
- UI/navigation/accessibility/adaptive/runtime gaps
- persistence/migration/cache/logout/process-relaunch gaps
- error/cancellation/concurrency/background/notification/permission gaps
- backend/security/privacy/performance/build/release evidence gaps
- prerequisite infrastructure versus focused tests
- prioritized roadmap with risk, smallest useful layer, owner/evidence dependency, and completion signal
- `Needs verification`, blocked-environment, and no-safe-seam classifications

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not add tests, targets, frameworks, dependencies, mocks, CI, or production seams in this documentation task.
- Do not prescribe Swift Testing, XCUITest, snapshot testing, or another framework unless a separate testing-strategy decision authorizes it.
- Do not use arbitrary coverage percentages as a roadmap objective.
- Do not present simulator/unit evidence as proof of device, accessibility, backend, security, performance, signing, or release behavior.
