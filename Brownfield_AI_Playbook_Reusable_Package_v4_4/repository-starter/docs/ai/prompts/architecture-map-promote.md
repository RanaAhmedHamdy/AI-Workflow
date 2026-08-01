# Phase 3 architecture map promotion

Promote exactly one architecture map after its separate read-only review.

## Selected document

- ID: `{{DOCUMENT_ID}}`
- Name: `{{DOCUMENT_NAME}}`
- Target: `{{OUTPUT_PATH}}`
- Scope specification: `{{SPEC_PATH}}`
- Current prerequisite: `{{PREREQUISITE_PATH}}`
- Next planned map: `{{NEXT_OUTPUT_PATH}}`
- Next planned name: `{{NEXT_DOCUMENT_NAME}}`
- Revision at prompt generation: `{{GIT_REVISION}}`

## Required input and gate

Read `AGENTS.md`, `AI_CONTEXT.md`,
`docs/ai/DOCUMENTATION_CHECKPOINT.md`, `{{SPEC_PATH}}`, and
`{{OUTPUT_PATH}}`.

The conversation must contain the completed, separate read-only review of
`{{OUTPUT_PATH}}`.

- If that review recommended `Promote` with no blocking correction, continue.
- If it recommended `Revise` or `Blocked`, or the review result is unavailable,
  stop without editing and request the missing correction/review task.
- Do not silently perform the read-only review again in this promotion task.

Apply `documentation-impact-assessment` to the proposed status/checkpoint change.

## Promotion contract

When the gate passes:

1. Change only the target status from `Draft` to `Reviewed`.
2. Add or update its reviewed revision/scope only to the extent established by
   the completed review. Do not invent execution evidence.
3. Update `docs/ai/DOCUMENTATION_CHECKPOINT.md`:
   - record `{{OUTPUT_PATH}}` as Reviewed;
   - keep the current phase as Brownfield Phase 3;
   - authorize creation of `{{NEXT_OUTPUT_PATH}}` as the next single Draft map.
4. When `{{NEXT_OUTPUT_PATH}}` is `PHASE_3_4`, record that all planned maps are
   Reviewed and authorize only the Phase 3.4 architecture coverage review. Do
   not run it.

## Allowed edits

Edit only `{{OUTPUT_PATH}}` and
`docs/ai/DOCUMENTATION_CHECKPOINT.md`. Do not change document substance during
promotion. A required substantive correction must use a separate revision task
followed by another read-only review.

## Verification and completion

- Confirm the target status and checkpoint agree.
- Confirm the next path is present in `docs/ai/architecture-docs.tsv`, unless it
  is `PHASE_3_4`.
- Run `git diff --check`.
- Show the target/checkpoint diff.
- Report the review result relied upon, documentation-impact classification,
  and exact next authorized task.
- Stop without creating the next map, running Phase 3.4, staging, committing,
  pushing, or publishing.
