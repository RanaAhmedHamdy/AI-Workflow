---
name: architecture-coverage-review
description: Reviews cross-cutting architecture coverage in bootstrap, feature-readiness, or convergence mode while keeping decision, implementation, and evidence status separate.
---

# Architecture Coverage Review

## Modes

- `BOOTSTRAP`: read PRD/design/governance authority, Spine, ADRs, Decision Register, coverage matrix, and directly relevant repository facts. Feature plan/tasks are not required.
- `FEATURE-READINESS`: include the approved feature contract/plan/tasks and implementation-readiness obligations.
- `CONVERGENCE`: include implementation and produced evidence.

## Procedure

1. Establish scope/revision and load only authorities relevant to active concerns.
2. Evaluate material concerns: structure/dependencies, state/concurrency/lifecycle, navigation, persistence/migrations, external services, localization/RTL/adaptation/accessibility, privacy/capabilities, background work, configuration, observability/performance, build/release, testing/evidence, production composition.
3. Record separately:
   - **Decision**: Decided / Deferred with conditions / Not applicable / Unresolved blocker.
   - **Implementation**: Not started / Partial / Implemented / Contradictory.
   - **Evidence**: None / Static / Host test / Instrumented / Runtime-device / External service / Release artifact.
4. Record the gap/owner/blocker/smallest next action.
5. Route current-document contradictions to `documentation-consistency-review`.
6. Do not infer `Not applicable` or runtime support from absence/static evidence.

In `BOOTSTRAP`, `Implementation: Not started` and `Evidence: None` are healthy when decision coverage is sufficient and no intended first-slice blocker is hidden.

## Output

Return concern matrix, contradictions, owner questions, next actions, and `PASS`, `PASS WITH LIMITATIONS`, or `BLOCKED`. A bootstrap pass means architecture coverage is sufficient for bounded feature intake only; it is not implementation readiness.
