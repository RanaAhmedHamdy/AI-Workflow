---
name: architecture-coverage-review
description: Review completed architecture maps for missing, fragmented, unobserved, inapplicable, owner-blocked, or runtime-only cross-cutting concerns before verification questions and implementation audits.
---

# Architecture Coverage Review

## Read first

- Current task and `AGENTS.md`.
- `AI_CONTEXT.md` and current Phase 3 architecture/design maps.
- Feature docs and directly relevant current source/configuration only where needed.
- The repository's canonical cross-feature architecture coverage checklist.

## Procedure

1. Establish review scope and reviewed revision/worktree state.
2. Evaluate every checklist concern that could materially apply.
3. Classify each as `Verified`, `Needs verification`, `Not observed`, or `Not applicable`.
4. For UI adaptation, explicitly classify device categories, orientations, compact/medium/expanded windows, resize/multi-window, foldables, ChromeOS, input modes, RTL, large text, state restoration, previews/tests, and runtime evidence.
5. Identify the current documentation home. Extend the closest current document; propose a new focused document only when no suitable home exists.
6. Record evidence, gap, owner, blocker, and smallest safe next action.
7. Route owner-dependent ambiguity to the decision register and source/decision contradiction to a no-edit implementation audit.
8. Keep runtime/backend/device/security/release uncertainty explicit rather than manufacturing static conclusions.
9. Ask whether any material cross-cutting concern is not represented.
10. Return a gate result; do not edit files unless the task authorizes documentation changes.

## Safety

Do not create empty documents, infer `Not applicable` from absence, convert recommendations into decisions, authorize implementation, scan the entire repository by default, or claim universal support from static source, previews, or dependency presence.

## Output

Return scope, classification table, missing/stale current documents, owner questions, audit candidates, runtime/release handoffs, living-review answer, adaptive-support evidence matrix, and pass/block result.
