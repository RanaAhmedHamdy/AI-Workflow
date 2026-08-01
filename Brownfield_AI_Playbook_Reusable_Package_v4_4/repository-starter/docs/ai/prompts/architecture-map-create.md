# Phase 3 architecture map creation

Create exactly one Draft architecture map.

## Selected document

- ID: `{{DOCUMENT_ID}}`
- Name: `{{DOCUMENT_NAME}}`
- Output: `{{OUTPUT_PATH}}`
- Scope specification: `{{SPEC_PATH}}`
- Required reviewed prerequisite: `{{PREREQUISITE_PATH}}`
- Inspected revision at prompt generation: `{{GIT_REVISION}}`

## Read first

1. `AGENTS.md`
2. `AI_CONTEXT.md`
3. `.agents/skills/documentation-impact-assessment/SKILL.md`
4. `docs/ai/DOCUMENTATION_CHECKPOINT.md`
5. `docs/ai/GRAPHIFY_USAGE.md`
6. `docs/ai/graphify-context-overrides.tsv`
7. `docs/ai/architecture-docs.tsv`
8. `{{SPEC_PATH}}`
9. `{{PREREQUISITE_PATH}}`
10. Only the reviewed project, feature, testing, product, and architecture documents routed by the scope specification

Apply `documentation-impact-assessment` before writing. The expected authorized
surface is `{{OUTPUT_PATH}}` plus
`docs/ai/DOCUMENTATION_CHECKPOINT.md`; stop if the assessment requires an
unapproved current-document change.

## Evidence workflow

1. Record the current revision and worktree state. Preserve unrelated changes.
2. Run a scoped Graphify query using the discovery question in `{{SPEC_PATH}}`.
3. Treat Graphify only as a routing aid. Verify every material claim directly
   against current source, tests, build/configuration files, or reviewed
   documentation.
4. Inspect only the files needed for this map. Absence of a graph edge is not
   evidence that a dependency or behavior is absent.
5. Distinguish current implementation, approved product constraints,
   recommendations, historical execution evidence, and `Needs verification`.

## Creation contract

- Create only `{{OUTPUT_PATH}}`.
- Set its status to `Draft`.
- Describe current architecture first; do not turn the map into a redesign plan.
- Include scope, authority, evidence limits, exclusions, inspected revision,
  current behavior, exceptions, protected boundaries, related reviewed pages,
  `Needs verification`, and provenance.
- Use repository-relative links only.
- Use the smallest useful diagrams or tables. Do not duplicate entire feature
  documents.
- Do not create empty sections to satisfy the checklist. For absent concerns,
  record `Not observed` only when the scope specification assigns that concern
  to this document and current inspection supports the classification.
- Do not mark the map Reviewed during creation.

## Checkpoint update

Update `docs/ai/DOCUMENTATION_CHECKPOINT.md` only to record that
`{{OUTPUT_PATH}}` was created as Draft and that the next authorized task is a
separate read-only review of the same file.

Do not authorize `{{NEXT_OUTPUT_PATH}}` during creation.

## Prohibited changes

Do not edit source, tests, Gradle/configuration, existing reviewed documents,
`AGENTS.md`, `AI_CONTEXT.md`, skills, checklists, scripts, manifests, hooks, CI,
Graphify source, or generated Graphify output. Do not create another
architecture map.

## Verification and completion

- Check all material claims against cited evidence.
- Check repository-relative links.
- Run `git diff --check`.
- Do not run Android builds or tests unless the scope specification identifies a
  claim that cannot be made honest without current execution evidence.
- Show the diff for `{{OUTPUT_PATH}}` and the checkpoint.
- Report evidence inspected, documentation-impact classification, exclusions,
  important `Needs verification`, and the exact next authorized task.
- Stop without staging, committing, pushing, publishing, reviewing, or promoting
  the Draft.
