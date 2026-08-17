# Foundation document promotion

Promote exactly one foundation document after its separate read-only review.

## Foundation order

1. `docs/wiki/project/MODULES.md`
2. `docs/wiki/project/FEATURE_MAP.md`
3. `docs/wiki/testing/TESTING_MAP.md`
4. `docs/wiki/project/DEPENDENCIES.md`
5. `docs/wiki/project/PROJECT_OVERVIEW.md`
6. `docs/wiki/project/ARCHITECTURE.md`

## Resolve the target

Use the completed read-only review available in the current conversation/task context.

- The review must identify exactly one foundation document and recommend `Promote` with no blocking correction.
- The target must currently be `Draft`.
- Earlier required foundation documents must already be `Reviewed` or `Reviewed orientation`.
- If the review result is unavailable, recommends `Revise`/`Blocked`, or more than one target is plausible, stop without editing.

Do not silently perform a new review inside this promotion task.

## Promotion contract

Edit only the selected foundation document and, if it already exists and is part of the repository workflow, `docs/ai/DOCUMENTATION_CHECKPOINT.md`.

1. Change only the selected document's review/status metadata needed to promote it from `Draft` to `Reviewed orientation` (or the repository's established equivalent reviewed status).
2. Do not change substantive documentation during promotion.
3. Preserve the review's evidence limits and unresolved `Needs verification` items.
4. If a checkpoint exists, record the promoted document and authorize only the next foundation creation task in the order above. After `ARCHITECTURE.md`, authorize only the next explicitly configured documentation phase.

If substantive correction is required, stop and route back to the matching `*-create.md` prompt, then repeat the read-only review.

## Completion

- Run `git diff --check` when available.
- Show the diff for only the promoted document and checkpoint, if changed.
- State the review result relied upon and the exact next authorized prompt.
- Do not stage, commit, push, publish, or start the next document.
