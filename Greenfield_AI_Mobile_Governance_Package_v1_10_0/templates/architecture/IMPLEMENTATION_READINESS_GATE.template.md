# Mobile Implementation Readiness Gate

> A `PASS` result means the slice is eligible for repository-owner implementation authorization. This gate does not itself authorize implementation.
>
> This gate is **not** the architecture-bootstrap exit check. Do not execute it to PASS before an approved Feature Contract, Implementation Plan, and Implementation Tasks exist.

## Allowed statuses

- PASS
- FAIL
- NOT APPLICABLE
- BLOCKED — OWNER DECISION
- BLOCKED — EVIDENCE / PREREQUISITE

## Required authorities

- `AGENTS.md`
- `AI_CONTEXT.md`
- `AI_PLAYBOOK.md`
- owner decision register
- approved feature contract
- approved implementation plan
- approved implementation tasks
- accepted ADRs
- architecture spine
- architecture coverage
- design authority and screen contracts
- protected-boundary decisions
- evidence paths

## Gates

| Gate | Condition |
|---|---|
| GOV-01 | Contract, plan, tasks, decisions, ADRs, architecture maps, readiness records, and `AI_CONTEXT.md` agree. |
| GOV-02 | Contract passed independent review and is owner-approved. |
| GOV-03 | Plan passed independent review and is owner-approved. |
| GOV-04 | Tasks passed independent review and are owner-approved. |
| GOV-05 | Protected-boundary authorization is recorded where applicable. |
| GOV-06 | One canonical implementation-authorization record is identified. |
| GOV-07 | Canonical artifact and evidence paths agree. |
| ARCH-01 | Required architecture decisions are accepted and current. |
| ARCH-02 | Structure, boundaries, and dependency direction are decided. |
| ARCH-03 | Platform hosts are thin. |
| ARCH-04 | Composition strategy is approved. |
| STATE-01 | Every meaningful workflow has a named state owner. |
| STATE-02 | Durable versus ephemeral state is defined. |
| STATE-03 | Recreation/process reconstruction is defined. |
| CONC-01 | Async ownership, lifetime, cancellation, isolation, terminal states, and duplicate behavior are defined. |
| DESIGN-01 | Every screen maps to approved design authority and screen contract. |
| DESIGN-02 | Every design-bound UI task identifies an exact approved visual artifact that is locally inspectable or deterministically retrievable before implementation. |
| DESIGN-03 | Every design-bound UI task carries a Design Lock: binding composition plus only documented permitted platform/accessibility/localization/responsive/owner-approved adaptations. |
| UI-01 | Route/container and render/content boundaries are defined. |
| UI-02 | Localization, RTL, accessibility, adaptation, keyboard/insets are defined. |
| NAV-01 | Navigation, dismissal, restoration, and external entry points are defined. |
| DATA-01 | System of record, schema ownership, migration, rollback, idempotency, backup, deletion, and relaunch are defined. |
| EXT-01 | External prerequisites exist or fail closed. |
| CONFIG-01 | Future configuration has explicit location, build inclusion, initialization behavior, privacy impact, and active/dormant status. |
| FAKE-01 | No production fake, no-op, sentinel, placeholder authorization, dead route, unused template model, or silent simulated success is planned. |
| TASK-01 | Tasks define behavioral outcomes and an acyclic dependency graph. |
| EVID-01 | Every task names exact evidence scenarios, procedures, environments, expected results, and artifact paths. |
| EVID-02 | Invalid or stale evidence reopens the task. |
| CONV-01 | Readiness report template and convergence/readiness-review procedures exist. |
| DOC-01 | Current documentation has no unresolved contradiction. |

## Report format

```markdown
# Implementation Readiness Audit: <feature/slice>

- Reviewed revision/worktree:
- Scope:
- Platform:
- Result: PASS / FAIL / BLOCKED
- Eligible for owner implementation authorization: YES / NO
- Implementation authorization: GRANTED / NOT GRANTED / PENDING
- Canonical authorization record:

## Failed or blocked gates

- <gate>: <exact blocker>
  - Owner/action:
  - Required evidence:

## Next action

The slice is ELIGIBLE / NOT ELIGIBLE for repository-owner implementation authorization.

This gate does not itself authorize implementation.
```
