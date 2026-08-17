# Phase 3 architecture map creation

Create exactly one Draft architecture map. This prompt is self-routing and can run directly with any repository-aware AI coding agent.

## Resolve the selected map

1. Read `docs/ai/architecture-docs.tsv` and `docs/ai/DOCUMENTATION_CHECKPOINT.md`.
2. Prefer the checkpoint's single next authorized architecture-map creation target and verify it exists in the manifest.
3. Correction exception: if the checkpoint currently authorizes review of exactly one existing `Draft` map and the current task context includes that map's completed review with recommendation `Revise`, select that same map for bounded correction. Do not select a different map.
4. If the checkpoint does not name a target, select the first manifest row in numeric order whose output does not exist, but only when all earlier required prerequisites are `Reviewed` and there is no conflicting authorized task.
5. From the selected row, resolve document ID, display name, output path, scope-spec path, and prerequisite path.
6. Verify the prerequisite exists and is `Reviewed` or `Reviewed orientation`.
7. If selection is ambiguous or out of sequence, stop without editing.

Record the current revision/worktree state before writing.

## Read first

Read `AGENTS.md`, repository context/index files, documentation-impact guidance when installed, checkpoint, Graphify policy/overrides, architecture manifest, selected scope specification, selected prerequisite, and only the reviewed project/feature/testing/product/architecture evidence routed by that scope specification.

## Evidence workflow

Use Graphify only as a scoped routing aid. Verify every material claim directly against current source, tests, build/configuration, reviewed documentation, or explicit owner decisions. Missing graph edges are not evidence of absence.

## Creation contract

- Create or revise only the selected manifest output path.
- Set/keep status `Draft`.
- Describe current architecture first; do not turn the map into a redesign plan.
- Follow the selected scope specification's required concerns, evidence limits, and non-goals.
- Include scope/authority, evidence limits, exclusions, inspected revision, current behavior, exceptions, protected boundaries, related reviewed pages, `Needs verification`, and provenance.
- Use repository-relative links only.
- Do not create another architecture map.

Update `docs/ai/DOCUMENTATION_CHECKPOINT.md` only to record that the selected map is Draft and authorize a separate read-only review of that same file. Do not authorize the next map during creation.

Do not edit source, tests, build/configuration, existing reviewed documents, policy/skills/checklists, manifests, hooks/CI, Graphify source, or generated Graphify output.

## Completion

Run `git diff --check` when available. Show the selected map/checkpoint diff, evidence inspected, exclusions, important `Needs verification`, and state that the exact next task is `docs/ai/prompts/architecture-map-review.md`. Stop without staging, committing, pushing, publishing, reviewing, or promoting.
