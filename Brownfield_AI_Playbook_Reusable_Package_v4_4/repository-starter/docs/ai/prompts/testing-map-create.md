# Common rules

- Work on exactly one requested document.
- Graphify is a discovery aid, not architecture authority.
- Verify every material claim against current source, tests, build files, or reviewed project documents.
- Apply `docs/ai/GRAPHIFY_USAGE.md` and `docs/ai/graphify-context-overrides.tsv`.
- Do not edit production code, tests, AGENTS.md, existing product documents, Graphify installation files, or `graphify-out/`.
- Do not mark the target document reviewed during creation.
- Record provenance, inspected revision, commands run, exclusions, and Needs verification.
- Repository-relative paths only; never use `file://` links.
- You may use bounded research subagents. Subagents must not edit files. One main agent synthesizes and writes the target document.

# Task: Create TESTING_MAP.md

Create only:

`docs/wiki/testing/TESTING_MAP.md`

Use actual test files and commands, not roadmap intentions.

Include:
- test source sets;
- test commands;
- actual test files grouped by behavior;
- behavior each test proves;
- tests confirmed run in this task;
- tests present but not run;
- device/runtime-only gaps;
- persistence test coverage;
- navigation and guided-flow coverage;
- ViewModel coverage;
- fragile or missing seams;
- high-risk untested behavior;
- Needs verification;
- provenance and exclusions.

Rules:
- Never claim a test passes unless run successfully in this task or supported by current verified evidence.
- Separate existence, execution, and behavioral proof.
- Do not infer UI correctness from local JVM tests.
- If the target already exists as `Draft`, revise only that file using current evidence and supplied review findings.
- Set status to Draft.
- Show the final diff.
