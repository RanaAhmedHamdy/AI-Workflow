# Feature documentation review prompt

Review exactly one Draft feature document against current repository evidence. This prompt runs directly; no runner is required.

## Resolve the target

1. Read `docs/ai/feature-docs.tsv` and `docs/ai/DOCUMENTATION_CHECKPOINT.md` when present.
2. Select the single manifest page currently awaiting review: prefer the checkpoint-authorized review target; otherwise use the first manifest row whose page exists with status `Draft` and whose predecessors are already `Reviewed`.
3. If zero or multiple pages are plausible, stop without editing and report the ambiguity.
4. Determine the next manifest row after the selected page. If none exists, treat the next path as `NONE`.

## Read first

Read `AGENTS.md`, Graphify policy, any existing verified overrides, checkpoint when present, the manifest, reviewed project/testing maps, the selected feature page, relevant product/context authority, and the exact source/test files cited by the page.

## Review and correction task

Review the selected page line by line. Verify current-state statements, navigation, constructor dependencies, data/persistence behavior, active/partial/deferred classifications, test assertions/execution limits, protected boundaries, links, status metadata, provenance, and `Needs verification`.

Graphify is discovery only; verify dependency-sensitive claims directly against source.

You may edit only:
- the selected feature page;
- `docs/ai/DOCUMENTATION_CHECKPOINT.md` when that file exists.

Do not modify source, tests, build/configuration, resources, generated Graphify output, `AGENTS.md`, product/context authority, other feature pages, Git history, or remotes.

## Approval rule

Correct the selected page only where required. Set its status to `Reviewed` only when all material claims are supported and uncertainty is honestly classified. If a blocking claim cannot be corrected from available evidence, leave it `Draft`, record the blocker in the response, do not advance the checkpoint, and stop.

On successful review, update the checkpoint when present:
- record the selected page as completed/reviewed if absent;
- keep the feature-documentation phase active;
- authorize creation of exactly the next manifest page;
- if there is no next row, record the feature-document batch complete and authorize only the next explicitly configured architecture/coverage step.

## Completion

Show the diff for the selected page and checkpoint, corrections made, evidence inspected, unresolved `Needs verification`, and the exact next authorized prompt. Stop after one feature review.
