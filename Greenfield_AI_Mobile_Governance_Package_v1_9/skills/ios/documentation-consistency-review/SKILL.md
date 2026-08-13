---
name: documentation-consistency-review
description: Detects stale or contradictory current specifications, plans, tasks, decisions, routing, and implementation authorization.
---

# Documentation Consistency Review

## Procedure

Compare the current authoritative chain:

`feature-input -> spec -> clarifications -> plan -> ADRs/decisions -> architecture spine -> tasks -> AI_CONTEXT -> implementation authorization -> evidence`

Check for:

- status mismatch;
- accepted ADRs whose old proposals remain canonical;
- stale package, target, dependency, or framework decisions;
- tasks that contradict the plan or source structure;
- implementation marked unblocked while a current artifact says blocked;
- evidence claims without artifacts;
- current documents that still describe superseded behavior;
- absolute local file links or broken routing;
- architecture selections described as both accepted and unresolved.

## Verdict

- **PASS**
- **PASS WITH NON-BLOCKING CLEANUP**
- **BLOCKED — CURRENT ARTIFACT CONTRADICTION**

Do not edit unless explicitly authorized.

## Convergence Ownership

Prefer one documentation convergence pass after the coherent feature diff is assembled. Reuse the documentation-impact result and architecture-coverage findings; do not independently re-read unchanged documents merely because another review skill already covered them.
