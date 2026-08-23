---
name: documentation-consistency-review
description: Detects stale or contradictory current product/design/architecture/feature authority, including ADR lifecycle and implementation-authorization mismatches.
---

# Documentation Consistency Review

Compare only the current authoritative chain relevant to the reviewed scope: product/design authority, Decision Register, ADRs, Architecture Spine, coverage, `AI_CONTEXT`, feature artifacts when they exist, implementation authorization, and evidence.

Check for:

- repository evidence or agent recommendation presented as explicit owner approval;
- ADR status changes without owner authority;
- `Accepted provisionally` decisions whose blocker/exit criteria disappeared or are represented as fully proven;
- accepted amendments not incorporated into the canonical decision/Spine;
- superseded historical text still presented as current authority;
- stale package/target/dependency/framework decisions;
- feature plan/tasks contradicting accepted architecture or design authority;
- implementation marked unblocked while a current artifact says blocked;
- evidence claims without artifacts;
- architecture selections described as both accepted and unresolved;
- absolute local links or broken routing.

Historical text explicitly labeled `Superseded — historical only` is not a contradiction by itself.

## Verdict

- `PASS`
- `PASS WITH NON-BLOCKING CLEANUP`
- `BLOCKED — CURRENT ARTIFACT CONTRADICTION`

Do not edit unless explicitly authorized. Prefer one reconciliation pass after a coherent decision/implementation batch; reuse prior unchanged findings rather than rereading everything ceremonially.
