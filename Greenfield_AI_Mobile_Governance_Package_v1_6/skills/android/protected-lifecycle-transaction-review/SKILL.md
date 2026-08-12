---
name: protected-lifecycle-transaction-review
description: Audits atomic guarded lifecycle transitions, persistence, cancellation, expiry, result acceptance, and sensitive-data purge.
---
# Protected Lifecycle and Transaction Review

Verify explicit transaction boundaries for creation, authorization, cancellation/purge, expiry/purge, accepted result/transition/purge, stale/duplicate rejection, and dismissal cleanup. Guarded SQL/state transitions must check affected rows. Verify no queryable sensitive payload remains after required purge. Review before and after implementation. Return `PASS` or `FAIL`.
