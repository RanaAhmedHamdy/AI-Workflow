\
# Feature documentation review prompt

Review one generated Android feature document against current repository
evidence. This is a documentation-only review.

## Inputs supplied by the runner

- Feature ID: `{{FEATURE_ID}}`
- Feature name: `{{FEATURE_NAME}}`
- Document: `{{OUTPUT_PATH}}`
- Current Git revision: `{{GIT_REVISION}}`
- Next feature path: `{{NEXT_OUTPUT_PATH}}`
- Next feature name: `{{NEXT_FEATURE_NAME}}`

## Read first

1. `AGENTS.md`
2. `docs/ai/GRAPHIFY_USAGE.md`
3. `docs/ai/DOCUMENTATION_CHECKPOINT.md`
4. `docs/wiki/project/FEATURE_MAP.md`
5. `docs/wiki/project/ARCHITECTURE.md`
6. `docs/wiki/testing/TESTING_MAP.md`
7. `{{OUTPUT_PATH}}`
8. Relevant authoritative `ai-context/` documents
9. The exact source and test files cited by the document

## Review task

Review `{{OUTPUT_PATH}}` line by line and correct it where required.

Check:

- every material current-state statement against source;
- route patterns, parsing, callback destinations, and navigation ownership;
- constructor-injected dependencies and repository bindings;
- data derivation and persistence behavior;
- active versus partial, placeholder, and deferred classifications;
- test names, commands, execution status, and assertion boundaries;
- protected Version 1 boundaries;
- stale absolute file links or invented symbols;
- review status, revision, scope, provenance, and Needs verification items;
- consistency with the reviewed project maps and authoritative product docs.

Graphify is a discovery aid only. Verify dependency-sensitive claims directly
against source.

## Allowed edits

You may edit only:

- `{{OUTPUT_PATH}}`
- `docs/ai/DOCUMENTATION_CHECKPOINT.md`

Do not modify source, tests, Gradle, resources, generated Graphify output,
`AGENTS.md`, `ai-context/`, other feature pages, Git history, or remotes.

## Approval rule

Set the feature document status to `Reviewed` only when its material claims are
supported and its uncertainty is honestly classified.

After successful review, update `docs/ai/DOCUMENTATION_CHECKPOINT.md`:

- add `{{OUTPUT_PATH}}` to completed feature documents if absent;
- keep the current phase as detailed feature documentation;
- set the next authorized task to create and review
  `{{NEXT_OUTPUT_PATH}}` for **{{NEXT_FEATURE_NAME}}`;
- state that only that next page may be created in the next task.

When `{{NEXT_OUTPUT_PATH}}` is `NONE`, record that the planned feature-document
batch is complete and route the next task to a human-reviewed architecture
coverage assessment. Do not create that assessment in this task.

## Completion

Show:

- `git diff -- {{OUTPUT_PATH}} docs/ai/DOCUMENTATION_CHECKPOINT.md`
- corrections made;
- evidence inspected;
- unresolved Needs verification items.

Stop after reviewing this one feature document and updating the checkpoint.
