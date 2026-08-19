# Common rules

- Work on exactly one requested document.
- Graphify is a discovery aid, not architecture authority.
- Verify every material claim against current source, tests, build files, or reviewed project documents.
- Apply `docs/ai/GRAPHIFY_USAGE.md`. Graphify output is optional.
- If `docs/ai/graphify-context-overrides.tsv` exists, apply only directly relevant verified rows.
- Do not edit production code, tests, AGENTS.md, existing product documents, Graphify installation files, or `graphify-out/`.
- This review is read-only. Do not edit the target or change its status.
- Record provenance, inspected revision, commands run, exclusions, and Needs verification.
- Repository-relative paths only; never use `file://` links.
- You may use bounded research subagents. Subagents must not edit files. One main agent synthesizes and writes the target document.

# Task: Review FEATURE_MAP.md

Review only:

`docs/wiki/project/FEATURE_MAP.md`

Do not edit it.

Check:
- unsupported implementation claims;
- planned behavior presented as implemented;
- missing or incorrect routes, screens, ViewModels, repositories, persistence, or tests;
- Graphify omissions repeated as architecture omissions;
- placeholder capabilities presented as functional;
- missing provenance or Needs verification;
- duplication of PRD/README instead of implementation mapping;
- broken repository-relative paths;
- inconsistent feature statuses.

Return:
1. Blocking findings.
2. Non-blocking findings.
3. Smallest revision scope.
4. Promotion recommendation: `Promote`, `Revise`, or `Blocked`.
5. Evidence inspected and commands run.

Recommend `Promote` only when no blocking documentation correction is required.
