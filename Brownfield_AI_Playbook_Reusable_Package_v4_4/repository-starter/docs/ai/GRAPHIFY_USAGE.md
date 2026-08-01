# Graphify usage and limitation supplement

**Status:** Draft  
**Source review revision:** `fcfd4afeb846775f01fa02321e1aa5d1e39cf33d`  
**Reviewed architecture page:** `docs/wiki/project/MODULES.md` (Reviewed orientation at revision `944e430101050520cfbc5b9201880d285a47a299`)

Graphify is a discovery and routing aid, not architecture authority. Its output can identify useful files and symbols to inspect, but architectural conclusions remain grounded in the repository source and reviewed project documentation.

## Known Graphify v0.9.22 Kotlin limitations

Graphify v0.9.22 can omit or incompletely represent relationships involving:

- top-level properties;
- constructor parameter types;
- Hilt/`@Inject` dependencies;
- qualified property access;
- some explicit Compose calls.

Absence of a graph edge is not evidence of absence. Agents must consult `docs/ai/graphify-context-overrides.tsv` when working in scopes affected by these limitations and must verify dependency-sensitive claims against current source.

The override file records only relationships directly verified from repository-relative source paths. It supplements Codex context selection and review; it does not change Graphify queries, extraction, traversal, or generated output.

## Generated-output boundary

Generated Graphify files must not be hand-edited. Full rebuilds overwrite generated output, so corrections and review context belong in this project-owned supplement rather than in `graphify-out/graph.json` or other generated files.

## Reviewed evidence

The current override rows were checked against:

- `app/src/main/java/com/stemcampathome/data/FakeCampData.kt` for `FakeLessonRepository` access to `CanonicalLessonOrder` and `LessonContentDays.byDayNumber`;
- the ViewModel constructor declarations under `app/src/main/java/com/stemcampathome/navigation/` and `app/src/main/java/com/stemcampathome/ui/screens/` listed row-by-row in `docs/ai/graphify-context-overrides.tsv`;
- `docs/wiki/project/MODULES.md`, especially “Directly inspected ViewModel dependencies” and “Known Graphify limitations affecting this page.”

When source and generated Graphify output differ, treat the current source as the evidence for dependency-sensitive claims and record any project-owned contextual supplement here or in the TSV rather than editing generated output.
