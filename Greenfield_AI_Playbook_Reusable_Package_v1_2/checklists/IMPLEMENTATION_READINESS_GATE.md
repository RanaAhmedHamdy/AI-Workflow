# Mandatory Android Implementation Readiness Gate

Run before `/speckit.plan`, before accepting `/speckit.tasks`, and before `/speckit.implement`. If any applicable gate fails, implementation stops for the affected slice.

Use only: `PASS`, `FAIL`, `NOT APPLICABLE`, `BLOCKED - OWNER DECISION`, or `BLOCKED - EVIDENCE/PREREQUISITE`.

| Gate | Condition that must be satisfied |
|---|---|
| GOV-01 | `spec.md`, `plan.md`, `tasks.md`, accepted ADRs, architecture maps, and `AI_CONTEXT.md` agree on status and authorization. |
| GOV-02 | Feature specification is approved for the requested implementation slice. |
| GOV-03 | Applicable protected-boundary authorization is recorded. |
| ARCH-01 | Required architecture decisions are accepted and canonical bodies contain no active superseded contradiction. |
| ARCH-02 | Application namespace, source roots, package/module boundaries, and allowed dependency directions are decided. |
| ARCH-03 | `MainActivity`/Activity responsibilities are explicitly thin and exclude feature state and dependency construction. |
| ARCH-04 | Composition root/DI/factory strategy is approved and mapped to concrete ownership. |
| STATE-01 | Every meaningful screen/workflow has a named lifecycle-retained state owner. |
| STATE-02 | ViewModel/state-holder construction mechanism and scope are decided. |
| STATE-03 | Durable versus ephemeral state and process-death reconstruction are defined. |
| UI-01 | Every screen task maps to an approved screen/design contract and user acceptance outcomes. |
| UI-02 | Route/content split, navigation callback ownership, and prohibited dependency parameters are stated. |
| UI-03 | All user/accessibility strings are resource-backed; required locales and fallback are stated. |
| UI-04 | Locale-key parity check is planned and owned. |
| UI-05 | RTL behavior and start/end semantics are in acceptance criteria. |
| UI-06 | Compact/medium/expanded and applicable orientation/resize behavior are defined. |
| UI-07 | Large-font, accessibility semantics, focus, touch targets, IME, and inset behavior are defined. |
| UI-08 | Preview and runtime matrix is named, with unsupported/unverified configurations explicit. |
| DATA-01 | Persistence, transaction, migration, backup, and data-lifecycle decisions are resolved where applicable. |
| BG-01 | Background scheduler, uniqueness, constraints, cancellation, expiry, and reconciliation are resolved where applicable. |
| EXT-01 | External prerequisites exist or the plan defines an approved fail-closed boundary. |
| FAKE-01 | No production fake, no-op, sentinel, accept-all, or silent simulated-success behavior is planned. |
| TASK-01 | Tasks specify behavioral outcomes, not only file creation. |
| TASK-02 | Every task identifies requirement, ADR, boundary, package/module location, prohibited patterns, stop condition, and dependencies. |
| EVID-01 | Every task names exact evidence scenarios and expected outcomes. |
| EVID-02 | Completion format requires evidence artifact path, command/session, environment, result, and limitations. |
| TEST-01 | Test stack/runners and deterministic baseline commands are available or explicitly block implementation. |
| DOC-01 | Documentation consistency and impact reviews have no unresolved stale current artifact. |

## Report format

```markdown
# Implementation Readiness Audit: <feature/slice>

- Result: PASS / BLOCKED
- Reviewed revision/worktree:
- Scope:

## Failed gates
- <gate>: <exact blocker>
  - Owner/action:
  - Narrower safe slice, if any:

## Next action
Implementation is ALLOWED / BLOCKED for <scope>.
```
