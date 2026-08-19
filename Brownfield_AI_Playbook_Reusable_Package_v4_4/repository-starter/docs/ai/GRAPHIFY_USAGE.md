# Graphify usage policy

Graphify is an **optional discovery and routing aid**. It is not architecture authority and it is not required to run the Brownfield workflow.

Current source, tests, build/configuration, reviewed repository documentation, and explicit owner decisions remain authoritative. Graphify output can help identify files, symbols, and relationships worth inspecting, but it must not replace direct verification of material claims.

## When Graphify is available

- Use Graphify for bounded discovery and context routing.
- Prefer scoped queries that narrow the files/symbols to inspect rather than treating a broad generated report as proof.
- Verify material dependency, ownership, lifecycle, persistence, security, runtime, and release claims directly against current repository evidence.
- Treat missing or incomplete graph relationships as **unknown**, not as evidence that the source relationship does not exist.
- Record the Graphify commands/queries used when they materially influenced document scope or provenance.

## When Graphify is unavailable

Continue the workflow using direct repository inspection. Do not block a documentation task solely because Graphify is not installed, has not been run, or has no usable output for the relevant scope.

Do not invent Graphify evidence or claim that a relationship is absent because no graph result is available.

## Optional project-specific overrides

`docs/ai/graphify-context-overrides.tsv` is optional. Create it only when a **verified, project-specific extraction or context gap** affects the current workflow and the missing/incorrect relationship has been confirmed directly from repository-relative evidence.

When an override file exists:

- apply only rows relevant to the current task;
- keep evidence paths repository-relative;
- record the reviewed revision/status according to the repository's documentation process;
- treat overrides as context-selection/review aids, not as modifications to Graphify itself;
- re-verify stale overrides when the relevant source changes.

If no verified gap exists, do not create an override file merely to satisfy the workflow.

## Version- and language-specific limitations

Do not encode observed parser/extractor limitations as universal reusable policy. Tool behavior can change by Graphify version, language, framework, repository structure, and extraction mode.

If a specific limitation matters to a project:

1. verify it against the Graphify version/output actually used;
2. verify the underlying relationship directly against source;
3. record the project-specific finding in repository-owned documentation or an override row;
4. avoid promoting that finding into reusable cross-project policy without independent evidence.

See `docs/ai/examples/GRAPHIFY_USAGE.project-example.md` and `docs/ai/examples/graphify-context-overrides.project-example.tsv` for **format/examples only**. Their paths, symbols, revisions, and limitations are not reusable truth.

## Generated-output boundary

Do not hand-edit generated Graphify output. Regeneration must remain safe. Project-owned corrections, review context, and verified exceptions belong in repository documentation and, when needed, `docs/ai/graphify-context-overrides.tsv`.

If source and Graphify output disagree, current source and other authoritative repository evidence win.
