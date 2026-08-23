---
name: adr-lifecycle-governance
description: "Controls ADR status transitions so repository facts and agent proposals cannot become accepted architecture without explicit owner authority, and accepted decisions can be amended, provisional, deferred, rejected, or superseded safely."
---

# ADR Lifecycle Governance

## Purpose

Validate and apply ADR lifecycle transitions. This skill governs status/authority; it does not independently choose architecture.

## Allowed lifecycle states

- `Proposed`
- `Accepted`
- `Accepted with amendments`
- `Accepted provisionally`
- `Deferred`
- `Rejected`
- `Superseded`
- `Deprecated`

## Non-negotiable rules

1. Repository/tool/build settings are evidence, not owner approval.
2. Agent recommendations remain proposals until explicit owner direction accepts/amends them.
3. `Proposed → Accepted*` requires explicit owner authority naming or clearly covering the decision.
4. `Accepted with amendments` means the current canonical decision changed materially but remains owner-approved. Contradictory old accepted wording must not remain current authority; retain it only as `Superseded — historical only` when useful.
5. `Accepted provisionally` requires:
   - approved direction;
   - exact blocking evidence/spike;
   - pass/fail exit criteria;
   - lifecycle impact while unproven.
   It must not be treated as implementation-ready when the required proof is still open.
6. `Deferred` requires a reason/trigger or condition for reconsideration when material.
7. `Superseded` requires a successor reference when one exists.
8. ADR acceptance never authorizes feature implementation or release.

## Procedure

For each requested status change:

1. Identify the current status and canonical decision body.
2. Identify the explicit owner decision source. If absent, do not promote authority.
3. Separate verified facts from the owner decision and agent recommendation.
4. Validate the requested transition and any provisional/deferred/supersession metadata.
5. Update the canonical decision body so current authority is unambiguous.
6. Mark obsolete conflicting wording historical/superseded rather than leaving two current decisions.
7. Return the downstream reconciliation set: Spine, coverage, Decision Register, routing/gates/policies/feature docs only where affected.
8. Run or route `documentation-consistency-review` after synchronization.

## Verdicts

- `TRANSITION VALID — SYNCHRONIZE`
- `NO STATUS CHANGE REQUIRED`
- `BLOCKED — EXPLICIT OWNER AUTHORITY REQUIRED`
- `BLOCKED — PROVISIONAL EXIT CRITERIA MISSING`
- `BLOCKED — CURRENT AUTHORITY CONTRADICTION`
- `NEEDS VERIFICATION`

## Efficiency

Do not rewrite unaffected ADR sections or downstream files. Preserve concise historical context only when it helps future decision review.
