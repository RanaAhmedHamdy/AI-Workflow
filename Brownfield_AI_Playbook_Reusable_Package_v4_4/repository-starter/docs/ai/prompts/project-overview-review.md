# Common rules

- Work on exactly one requested document.
- Graphify is a discovery aid, not architecture authority.
- Verify every material claim against current source, tests, build files, or reviewed project documents.
- Apply `docs/ai/GRAPHIFY_USAGE.md` and `docs/ai/graphify-context-overrides.tsv`.
- Do not edit production code, tests, AGENTS.md, existing product documents, Graphify installation files, or `graphify-out/`.
- This review is read-only. Do not edit the target or change its status.
- Record provenance, inspected revision, commands run, exclusions, and Needs verification.
- Repository-relative paths only; never use `file://` links.
- You may use bounded research subagents. Subagents must not edit files. One main agent synthesizes and writes the target document.

# Task: Review PROJECT_OVERVIEW.md

Review only:

`docs/wiki/project/PROJECT_OVERVIEW.md`

Do not edit it.

Check:
- duplication instead of summary;
- product intent presented as implementation;
- missing current boundaries;
- missing links to reviewed maps;
- stale statuses;
- unsupported maturity claims;
- unresolved items omitted;
- weak provenance.

Return:
1. Blocking findings.
2. Non-blocking findings.
3. Smallest revision scope.
4. Promotion recommendation: `Promote`, `Revise`, or `Blocked`.
5. Evidence inspected and commands run.

Recommend `Promote` only when no blocking documentation correction is required.
