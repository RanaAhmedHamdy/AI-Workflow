# Phase 3 architecture map promotion

Promote exactly one architecture map after its separate read-only review. No runner is required.

## Required review gate

The completed read-only review must be available in the current conversation/task context and must recommend `Promote` with no blocking correction. If the review result is unavailable, recommends `Revise`/`Blocked`, or does not identify exactly one target, stop without editing.

Do not silently repeat the review.

## Resolve the target and next item

1. Read `docs/ai/DOCUMENTATION_CHECKPOINT.md` and `docs/ai/architecture-docs.tsv`.
2. Confirm the review target is the single Draft map currently authorized for promotion/review completion.
3. Resolve its manifest row and scope specification.
4. Resolve the next manifest row in numeric order. If none exists, the next step is `PHASE_3_4` architecture coverage review.

## Promotion contract

Edit only the selected map and `docs/ai/DOCUMENTATION_CHECKPOINT.md`.

1. Change only the target status from `Draft` to `Reviewed` and update review metadata only to the extent established by the completed review.
2. Do not make substantive corrections during promotion.
3. Record the selected map as Reviewed in the checkpoint.
4. Authorize creation of exactly the next manifest map; if none remains, authorize only Phase 3.4 architecture coverage review.

If a substantive correction is needed, stop and route back to `architecture-map-create.md` for correction of the same Draft, followed by another fresh `architecture-map-review.md`.

## Completion

Run `git diff --check` when available. Show the target/checkpoint diff, the review result relied upon, and exact next authorized prompt/task. Stop without creating the next map, running Phase 3.4, staging, committing, pushing, or publishing.
