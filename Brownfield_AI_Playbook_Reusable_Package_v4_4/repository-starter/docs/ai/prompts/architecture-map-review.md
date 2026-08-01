# Phase 3 architecture map read-only review

Perform a separate read-only review of exactly one Draft architecture map.

## Selected document

- ID: `{{DOCUMENT_ID}}`
- Name: `{{DOCUMENT_NAME}}`
- Target: `{{OUTPUT_PATH}}`
- Scope specification: `{{SPEC_PATH}}`
- Reviewed prerequisite: `{{PREREQUISITE_PATH}}`
- Revision at prompt generation: `{{GIT_REVISION}}`

## Read first

1. `AGENTS.md`
2. `AI_CONTEXT.md`
3. `.agents/skills/documentation-review/SKILL.md`
4. `.agents/skills/documentation-impact-assessment/SKILL.md`
5. `docs/ai/DOCUMENTATION_CHECKPOINT.md`
6. `docs/ai/GRAPHIFY_USAGE.md`
7. `docs/ai/graphify-context-overrides.tsv`
8. `docs/ai/architecture-docs.tsv`
9. `{{SPEC_PATH}}`
10. `{{OUTPUT_PATH}}`
11. Only the directly relevant reviewed evidence and current source/configuration

Apply `documentation-review` to the target. Use
`documentation-impact-assessment` only to identify stale current documents
affected by a material finding; it does not authorize edits.

## Review procedure

1. Record current revision, worktree state, review scope, and exclusions.
2. Run a scoped Graphify query for disputed or high-risk relationships only.
3. Verify material claims directly against source, tests, build/configuration,
   reviewed documents, or explicit owner decisions.
4. Check every required concern and source group in `{{SPEC_PATH}}`.
5. Check current-versus-planned separation, ownership, dependency direction,
   lifetimes, error/fallback behavior, protected boundaries, test-evidence
   limits, runtime/release limits, links, provenance, and `Needs verification`.
6. Identify checklist concerns that are missing, fragmented, duplicated, or
   incorrectly classified, but do not run the Phase 3.4 coverage gate.

## No-edit contract

Do not edit any file. Do not fix the Draft, change its status, update the
checkpoint, create review artifacts, or authorize the next map.

Return:

- blocking findings;
- non-blocking findings;
- unsupported or stale claims;
- missing material coverage;
- provenance/link issues;
- smallest required correction scope;
- promotion recommendation: `Promote`, `Revise`, or `Blocked`;
- exact evidence inspected and commands run;
- unverified runtime, device, backend, security, or release layers.

If the recommendation is `Promote`, state explicitly that no blocking
documentation correction is required. A later promotion task must still update
status and checkpoint.

Stop without staging, committing, pushing, publishing, promoting, or reviewing
another map.
