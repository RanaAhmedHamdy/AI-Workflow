# Kotlin Coroutines Readiness

## Purpose
Review Android coroutine and Flow ownership before planning, implementation, and convergence.

## Required inputs
- Android engineering policy
- accepted concurrency/state ADRs
- feature contract, plan, and tasks
- ViewModel, repository, worker, and lifecycle boundaries
- test and runtime evidence

## Checks
- structured scopes and explicit owners
- no `GlobalScope` or silent fire-and-forget work
- cancellation propagation and durable-work distinction
- dispatcher ownership and deterministic tests
- `StateFlow`/Flow sharing policy
- duplicate side-effect prevention
- bounded terminal states and explicit error mapping
- lifecycle-aware collection

## Verdicts
`PASS`, `FAIL`, `BLOCKED`, or `NEEDS VERIFICATION`.
