# Android Persistence and Migration Readiness

## Purpose
Review Android durable-data architecture and evidence before and after implementation.

## Required inputs
- system-of-record decision
- Room/DataStore/file/secure-storage ADRs
- schema and migration plan
- repository and transaction boundaries
- backup, deletion, process-death, and test-store rules

## Checks
- schema/version ownership and representative fixtures
- migration and failed-migration recovery
- transactions, rollback, idempotency, duplicate prevention, stale writes
- process termination/relaunch durability
- backup/restore/device transfer/deletion
- test isolation and production-store separation
- no in-memory release substitute

## Verdicts
`PASS`, `FAIL`, `BLOCKED`, or `NEEDS VERIFICATION`.
