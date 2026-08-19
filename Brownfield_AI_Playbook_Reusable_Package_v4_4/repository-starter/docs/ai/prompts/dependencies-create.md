# Common rules

- Work on exactly one requested document.
- Graphify is a discovery aid, not architecture authority.
- Verify every material claim against current source, tests, build files, or reviewed project documents.
- Apply `docs/ai/GRAPHIFY_USAGE.md`. Graphify output is optional.
- If `docs/ai/graphify-context-overrides.tsv` exists, apply only directly relevant verified rows.
- Do not edit production code, tests, AGENTS.md, existing product documents, Graphify installation files, or `graphify-out/`.
- Do not mark the target document reviewed during creation.
- Record provenance, inspected revision, commands run, exclusions, and Needs verification.
- Repository-relative paths only; never use `file://` links.
- You may use bounded research subagents. Subagents must not edit files. One main agent synthesizes and writes the target document.

# Task: Create DEPENDENCIES.md

Create only:

`docs/wiki/project/DEPENDENCIES.md`

Inspect Gradle settings, build files, version catalogs, plugins, manifests, and source usage.

Include:
- Gradle modules;
- plugins;
- Android/Kotlin/Compose versions;
- runtime libraries;
- DI, persistence, lifecycle, coroutine, and testing dependencies;
- declared versus directly observed usage;
- version source and ownership;
- upgrade-sensitive dependencies;
- unused or placeholder dependencies if evidenced;
- excluded/future technologies;
- build-tool dependencies;
- Needs verification;
- provenance and commands.

Rules:
- Distinguish declared versions from resolved artifacts.
- Do not claim runtime behavior from declaration alone.
- Do not invent backend, Room, billing, login, camera, or cloud dependencies.
- If the target already exists as `Draft`, revise only that file using current evidence and supplied review findings.
- Set status to Draft.
- Show the final diff.
