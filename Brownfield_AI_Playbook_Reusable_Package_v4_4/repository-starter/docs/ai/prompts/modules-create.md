# Common rules

- Work on exactly one requested document.
- Graphify is a discovery aid, not architecture authority.
- Verify every material claim against current source, build files, tests, or reviewed project documents.
- Apply `docs/ai/GRAPHIFY_USAGE.md`. Graphify output is optional.
- If `docs/ai/graphify-context-overrides.tsv` exists, apply only directly relevant verified rows.
- Do not edit production code, tests, AGENTS.md, product documents, Graphify installation files, or generated graph output.
- Do not mark the target document reviewed during creation.
- Record provenance, inspected revision, commands run, exclusions, and Needs verification.
- Use repository-relative paths only; never use `file://` links.
- You may use bounded research subagents. Subagents must not edit files. One main agent synthesizes and writes the target document.

# Task: Create or revise MODULES.md

Create or revise only:

`docs/wiki/project/MODULES.md`

Inspect the repository structure and build configuration directly. For Android projects, start with settings/build files, version catalogs, module build files, manifests, source sets, and directly relevant tests. For another platform, use the equivalent project/workspace/module definition files.

Include:
- repository/module inventory;
- module type and responsibility;
- important source sets or targets;
- direct module-to-module dependencies supported by build configuration;
- app/library boundaries and primary entry points;
- test modules/source sets and where they attach;
- generated, vendor, tooling, or sample modules when materially relevant;
- ownership or protected boundaries when evidenced;
- important exceptions or unusual topology;
- Needs verification;
- provenance and inspected revision.

Rules:
- Describe the current repository topology, not a desired modularization.
- Distinguish build-declared dependencies from runtime behavior.
- Do not infer feature ownership solely from folder names.
- Do not turn this into a feature map or dependency-library inventory.
- If the target already exists as `Draft`, revise only that file using current evidence and any supplied review findings.
- Set status to `Draft`.
- Show the final diff.
