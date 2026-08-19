# Phase 3 architecture map read-only review

Perform a separate read-only review of exactly one Draft architecture map. No runner is required.

## Resolve the target

1. Read `docs/ai/DOCUMENTATION_CHECKPOINT.md` and `docs/ai/architecture-docs.tsv`.
2. Select the single Draft map the checkpoint authorizes for review.
3. Verify its manifest row, scope specification, and reviewed prerequisite.
4. If the checkpoint does not authorize exactly one Draft map review, stop without editing.

Read the repository policy/context, documentation-review guidance when installed, checkpoint, Graphify policy and any existing verified overrides, manifest, selected scope specification, selected Draft, and only directly relevant reviewed evidence/current source.

## Review procedure

Verify material claims directly against source, tests, build/configuration, reviewed documents, or explicit owner decisions. Use scoped Graphify discovery only for disputed/high-risk relationships. Check every required concern/source group in the scope specification, current-versus-planned separation, ownership/dependency direction, lifetimes, fallback/error behavior, protected boundaries, test-evidence limits, runtime/release limits, links, provenance, and `Needs verification`.

## No-edit contract

Do not edit any file. Do not fix the Draft, change status, update checkpoint, create review artifacts, or authorize the next map.

Return:
- blocking findings;
- non-blocking findings;
- unsupported/stale claims;
- missing material coverage;
- provenance/link issues;
- smallest required correction scope;
- promotion recommendation: `Promote`, `Revise`, or `Blocked`;
- exact evidence inspected and commands run;
- unverified runtime/device/backend/security/release layers.

Recommend `Promote` only when no blocking documentation correction is required. If `Promote`, the next task is `docs/ai/prompts/architecture-map-promote.md` and it must have access to this review result. Stop without editing, staging, committing, pushing, publishing, promoting, or reviewing another map.
