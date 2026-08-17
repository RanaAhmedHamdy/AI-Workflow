# Brownfield repository starter kit

This is the **execution guide** for the v4.4 repository-owned documentation workflow.

Use it to answer: **what runs first, which prompt is selected, whether the script invokes the AI, what may change, what status to expect, and what to do next.**

You should not need the full playbook for the normal execution path. Use `../playbook/BROWNFIELD_PLAYBOOK.md` for rationale, governance details, and edge cases.

---

## 1. Know the three runners

They do not behave the same way.

| Workflow | Runner | Invokes AI? | Normal lifecycle |
|---|---|---|---|
| Foundation maps | `scripts/run-doc-phase.sh` | **No** | create Draft -> read-only review -> separate approval/promotion |
| Feature pages | `scripts/generate-feature-docs.sh` | **Only with `--execute`**; invokes OpenCode | create -> review/correct -> `Reviewed` + checkpoint |
| Phase 3 architecture maps | `scripts/run-architecture-doc.sh` | **No** | create Draft -> read-only review -> promote |

```text
Foundation
  runner -> printed prompt -> run agent yourself -> Draft
         -> printed review prompt -> fresh read-only review
         -> separate promotion/approval -> Reviewed

Features
  runner --execute -> fresh OpenCode create
                   -> fresh OpenCode review
                   -> Reviewed + checkpoint update

Phase 3 architecture maps
  runner -> rendered prompt -> run Codex yourself -> Draft
         -> fresh read-only review -> Promote / Revise / Blocked
         -> promotion prompt -> Reviewed + next checkpoint task
```

---

## 2. Two important v4.4 starter gaps

### `MODULES.md` must already be reviewed

The playbook expects `MODULES.md` as part of the reusable foundation, but this starter does **not** include:

```text
modules-create.md
modules-review.md
./scripts/run-doc-phase.sh modules ...
```

Before the first bundled foundation command, this must already exist:

```text
docs/wiki/project/MODULES.md
```

with a status accepted by the runner, normally:

```markdown
**Status:** Reviewed
```

or:

```markdown
**Status:** Reviewed orientation
```

For a new repository, create and independently review `MODULES.md` using the repository's approved documentation procedure. If you want the entire foundation flow automated, add MODULES create/review routing during adoption.

### Foundation review does not promote the Draft

The foundation `*-review.md` prompts are read-only. A successful review recommends promotion, but the v4.4 starter has no generic foundation promotion runner/template.

So foundation flow is:

```text
create Draft
-> separate read-only review
-> correct and re-review if needed
-> separately authorize/promote to Reviewed or Reviewed orientation
-> next document
```

Do not assume `./scripts/run-doc-phase.sh ... review` changes the file.

---

## 3. Adapt before the first run

Copy `scripts/` and `docs/ai/prompts/` only when the receiving repository uses the same directory contract. Review paths, product/platform terminology, model invocation, allowed-change rules, status parsing, and evidence sources before execution.

The files in `docs/ai/examples/` are **examples only**. Do not reuse their revisions, feature order, source paths, test counts, owner decisions, or checkpoint state as project truth.

Create/adapt live files such as:

```text
docs/ai/DOCUMENTATION_CHECKPOINT.md
docs/ai/feature-docs.tsv
docs/ai/architecture-docs.tsv
docs/ai/GRAPHIFY_USAGE.md
docs/ai/graphify-context-overrides.tsv
docs/ai/prompts/
docs/ai/architecture-specs/
```

`docs/ai/GRAPHIFY_USAGE.md` can be a policy baseline, but update the Graphify version/limitations for the receiving project. The architecture scope specs are reusable in structure, not in project-specific evidence or assumptions.

---

# Exact execution flow

## 4. Recommended order from a fresh repository

```text
1. Safe repository setup / baseline
2. MODULES.md reviewed                          <- bootstrap outside bundled runner
3. FEATURE_MAP.md reviewed
4. TESTING_MAP.md reviewed
5. DEPENDENCIES.md reviewed
6. PROJECT_OVERVIEW.md reviewed
7. high-level ARCHITECTURE.md reviewed
8. feature pages from feature-docs.tsv
9. focused Phase 3 architecture maps
10. Phase 3.4 architecture coverage review
11. owner verification/decisions when required
12. Phase 3.6 no-edit implementation audit
13. bounded implementation only after authorization
```

The foundation dependency shape is:

```text
MODULES
  ├─> FEATURE_MAP ─> TESTING_MAP
  └─> DEPENDENCIES
          └─> PROJECT_OVERVIEW
                  └─> ARCHITECTURE
```

The `PROJECT_OVERVIEW.md` creation prompt also expects the feature/testing maps, so the order above is the safest normal sequence.

---

# Foundation documents

## 5. What `run-doc-phase.sh` actually does

Usage:

```bash
./scripts/run-doc-phase.sh <phase> <create|review>
```

Supported phases:

```text
feature-map
testing-map
dependencies
project-overview
architecture
```

The script verifies the selected prerequisite, prints the prompt, and copies it to the clipboard when possible. It **does not invoke Codex/another agent, edit files, approve status, update the checkpoint, commit, or publish.**

After each command, run the printed prompt in the intended agent session yourself.

## 6. Exact foundation command sequence

### A. Feature map

Create:

```bash
./scripts/run-doc-phase.sh feature-map create
```

Uses:

```text
docs/ai/prompts/feature-map-create.md
```

Requires:

```text
docs/wiki/project/MODULES.md -> Reviewed / Reviewed orientation
```

Expected output:

```text
docs/wiki/project/FEATURE_MAP.md -> Draft
```

Then run a separate review:

```bash
./scripts/run-doc-phase.sh feature-map review
```

Uses `feature-map-review.md`. The review is read-only. Correct only the target if needed, re-review, then separately promote/approve it before continuing.

### B. Testing map

```bash
./scripts/run-doc-phase.sh testing-map create
./scripts/run-doc-phase.sh testing-map review
```

Uses:

```text
testing-map-create.md
testing-map-review.md
```

Requires reviewed `FEATURE_MAP.md`.

Expected target:

```text
docs/wiki/testing/TESTING_MAP.md -> Draft -> separately reviewed/promoted
```

### C. Dependencies

```bash
./scripts/run-doc-phase.sh dependencies create
./scripts/run-doc-phase.sh dependencies review
```

Uses:

```text
dependencies-create.md
dependencies-review.md
```

Runner requires reviewed `MODULES.md`.

Expected target:

```text
docs/wiki/project/DEPENDENCIES.md -> Draft -> separately reviewed/promoted
```

### D. Project overview

Run only after `MODULES.md`, `FEATURE_MAP.md`, `TESTING_MAP.md`, and `DEPENDENCIES.md` are reviewed.

```bash
./scripts/run-doc-phase.sh project-overview create
./scripts/run-doc-phase.sh project-overview review
```

Uses:

```text
project-overview-create.md
project-overview-review.md
```

Runner directly checks reviewed `DEPENDENCIES.md`; the prompt itself expects the other reviewed maps too.

Expected target:

```text
docs/wiki/project/PROJECT_OVERVIEW.md -> Draft -> separately reviewed/promoted
```

### E. High-level architecture

This is the **Phase 1 orientation architecture page**, not the later focused Phase 3 map pipeline.

```bash
./scripts/run-doc-phase.sh architecture create
./scripts/run-doc-phase.sh architecture review
```

Uses:

```text
architecture-create.md
architecture-review.md
```

Runner requires reviewed `PROJECT_OVERVIEW.md`. The create prompt expects the full reviewed foundation.

Expected target:

```text
docs/wiki/project/ARCHITECTURE.md -> Draft -> separately reviewed/promoted
```

At this point preserve/checkpoint the reviewed foundation before relying on it for deeper work.

## 7. Foundation lookup table

| Scenario | Command | Prompt | Runner invokes AI? |
|---|---|---|---|
| Create feature map | `run-doc-phase.sh feature-map create` | `feature-map-create.md` | No |
| Review feature map | `run-doc-phase.sh feature-map review` | `feature-map-review.md` | No |
| Create testing map | `run-doc-phase.sh testing-map create` | `testing-map-create.md` | No |
| Review testing map | `run-doc-phase.sh testing-map review` | `testing-map-review.md` | No |
| Create dependencies | `run-doc-phase.sh dependencies create` | `dependencies-create.md` | No |
| Review dependencies | `run-doc-phase.sh dependencies review` | `dependencies-review.md` | No |
| Create overview | `run-doc-phase.sh project-overview create` | `project-overview-create.md` | No |
| Review overview | `run-doc-phase.sh project-overview review` | `project-overview-review.md` | No |
| Create high-level architecture | `run-doc-phase.sh architecture create` | `architecture-create.md` | No |
| Review high-level architecture | `run-doc-phase.sh architecture review` | `architecture-review.md` | No |

---

# Feature documents

## 8. Prepare the feature batch

Before execution:

- foundation pages referenced by `feature-doc-create.md` should be reviewed;
- adapt `docs/ai/feature-docs.tsv` from the example;
- adapt `docs/ai/DOCUMENTATION_CHECKPOINT.md` to the real project state;
- verify the feature prompts' `AGENTS.md`, `ai-context/`, source, and platform assumptions;
- prefer a clean Git worktree.

Manifest format:

```text
# order<TAB>feature_id<TAB>display_name<TAB>output_path
10<TAB>today<TAB>Today<TAB>docs/wiki/features/TODAY.md
```

Use real tab characters.

## 9. Dry run first

```bash
./scripts/generate-feature-docs.sh --next
```

Without `--execute`, the script selects the first missing feature and prints the OpenCode create/review commands it would run. It does not change files.

## 10. Execute one feature

Recommended normal command:

```bash
./scripts/generate-feature-docs.sh --next --execute
```

With `--execute`, the script invokes OpenCode itself.

For the selected feature it:

1. reads `feature-docs.tsv` and selects the first missing page;
2. renders `feature-doc-create.md` with feature/revision values;
3. runs a fresh `opencode run` creation session;
4. allows only the selected feature page to change;
5. verifies the page was created;
6. renders `feature-doc-review.md`;
7. runs a separate fresh `opencode run` review session;
8. allows only the selected page plus `DOCUMENTATION_CHECKPOINT.md` to change;
9. requires the normal successful review pass to mark the page `Reviewed`;
10. leaves changes uncommitted for human review.

The feature review is intentionally different from foundation review: it may **correct the selected feature page, promote it to `Reviewed`, and advance the checkpoint**.

If unexpected files change, automation stops.

### Other useful feature scenarios

Specific feature:

```bash
./scripts/generate-feature-docs.sh --feature today --execute
```

Create only, no review:

```bash
./scripts/generate-feature-docs.sh --next --create-only --execute
```

Review an existing page:

```bash
./scripts/generate-feature-docs.sh --feature today --review-only --execute
```

All missing pages:

```bash
./scripts/generate-feature-docs.sh --all          # dry run
./scripts/generate-feature-docs.sh --all --execute
```

For first adoption, prefer repeated `--next --execute` so each resulting page/checkpoint can be inspected before continuing.

Default model/agent are defined in the script and may be overridden by `--model`, `--agent`, `OPENCODE_DOC_MODEL`, and `OPENCODE_DOC_AGENT`.

## 11. End of feature batch

On the final feature, the rendered review receives `NEXT_OUTPUT_PATH=NONE`. It records the feature batch as complete and routes the checkpoint onward; it does **not** automatically perform the Phase 3.4 coverage review.

Before the focused architecture pipeline, adapt the architecture manifest, scope specs, and checkpoint to the actual project.

---

# Phase 3 focused architecture maps

## 12. Do not confuse the two architecture workflows

```bash
./scripts/run-doc-phase.sh architecture create
```

is for:

```text
docs/wiki/project/ARCHITECTURE.md
```

The later focused maps use:

```bash
./scripts/run-architecture-doc.sh ...
```

with project-specific entries from `docs/ai/architecture-docs.tsv`, such as `DATA_FLOW.md`, `STATE_MANAGEMENT.md`, `SECURITY_BOUNDARIES.md`, or `TESTABILITY_ROADMAP.md`.

## 13. Prepare the architecture pipeline

Before execution:

- adapt `docs/ai/architecture-docs.tsv`;
- adapt the matching files under `docs/ai/architecture-specs/`;
- make sure every manifest prerequisite exists and is reviewed;
- make sure the checkpoint's `## Next authorized task` contains the exact authorized `docs/wiki/...md` path;
- verify paths such as `AI_CONTEXT.md`, required skills, and Graphify files referenced by the prompts exist.

Manifest columns:

```text
order<TAB>document_id<TAB>display_name<TAB>output_path<TAB>spec_path<TAB>prerequisite_path
```

## 14. List state first

```bash
./scripts/run-architecture-doc.sh --list
```

This is read-only and shows each manifest document's current status.

## 15. Exact lifecycle for every focused map

### Create

```bash
./scripts/run-architecture-doc.sh --next create
```

The runner verifies checkpoint order, manifest entry, scope spec, reviewed prerequisite, and that the target does not already exist. It renders:

```text
docs/ai/prompts/architecture-map-create.md
```

It **does not invoke Codex**. Paste/run the rendered prompt yourself.

Expected result:

```text
selected map -> Draft
DOCUMENTATION_CHECKPOINT.md -> authorize review of the same Draft only
```

### Review in a separate fresh session

```bash
./scripts/run-architecture-doc.sh --next review
```

The target must exist with status exactly `Draft`. The runner renders:

```text
docs/ai/prompts/architecture-map-review.md
```

Run it in a fresh review session. The review is **no-edit** and returns:

```text
Promote
Revise
Blocked
```

### If review says `Promote`

```bash
./scripts/run-architecture-doc.sh --next promote
```

This renders:

```text
docs/ai/prompts/architecture-map-promote.md
```

Run the promotion task with the completed separate review result available. Promotion may only change status/review metadata and the checkpoint; it must not make substantive corrections.

Expected result:

```text
selected map -> Reviewed
checkpoint -> next map create authorization
```

Then repeat from `--list` / `--next create`.

### If review says `Revise`

Do not promote. Make only the separately authorized corrections to the Draft, then run another fresh:

```bash
./scripts/run-architecture-doc.sh --next review
```

Promote only after a review returns `Promote` with no blocking correction.

### If review says `Blocked`

Stop and resolve the blocker. Do not force promotion and do not create the next map.

## 16. Architecture runner lookup

| Scenario | Command | Prompt | Runner invokes AI? | Files expected to change after agent task |
|---|---|---|---|---|
| Inspect state | `run-architecture-doc.sh --list` | None | No | None |
| Create authorized map | `run-architecture-doc.sh --next create` | `architecture-map-create.md` | No | Draft map + checkpoint |
| Review Draft | `run-architecture-doc.sh --next review` | `architecture-map-review.md` | No | **None** |
| Promote passed Draft | `run-architecture-doc.sh --next promote` | `architecture-map-promote.md` | No | status/review metadata + checkpoint |

A specific ID can be used instead of `--next`, but the runner still enforces the checkpoint target by default. `--allow-out-of-sequence` bypasses that sequence guard and should be used only with explicit authorization.

When the final planned map is promoted, the promotion prompt routes the checkpoint to `PHASE_3_4`; it does not run the coverage gate itself.

---

# What happens after these runners

## 17. Documentation completion is not coding authorization

After applicable focused maps are reviewed:

```text
Phase 3.4 architecture coverage review
-> verification questions / accountable owner decisions when needed
-> Phase 3.6 no-edit implementation audit
-> protected-boundary preflight when applicable
-> one bounded authorized implementation item
-> verification
-> documentation impact
-> independent PR review
-> explicit publish
```

The three documentation runners do not automatically perform those later stages.

Do not treat “all expected files exist” as permission to implement.

---

# Common questions

## “I ran `run-doc-phase.sh` and nothing changed.”

Expected. It only prints/copies the selected prompt. Run that prompt in the agent yourself.

## “Foundation review passed but the page is still Draft.”

Expected. Foundation review is read-only. Separately promote/approve the page before the next prerequisite-dependent phase.

## “Which script actually invokes an AI?”

Only this runner, and only with `--execute`:

```bash
./scripts/generate-feature-docs.sh ... --execute
```

The foundation and architecture runners only render/print/copy prompts.

## “Why does `feature-map create` fail immediately?”

Most likely `docs/wiki/project/MODULES.md` is missing or not marked `Reviewed` / `Reviewed orientation`. MODULES automation is not bundled in v4.4.

## “Why does architecture `--next` fail?”

The checkpoint's authorized output must match a row in `architecture-docs.tsv`, and that row's prerequisite must be reviewed. Fix/adapt workflow state deliberately instead of bypassing the guard.

## “Architecture review says `Revise`. Can promotion fix it?”

No. Revision and promotion are separate. Correct the Draft, run another read-only review, then promote only after `Promote`.

---

# Final safety reminders

- Start with dry runs when supported.
- Prefer a clean worktree.
- Work on one document or one bounded task at a time.
- Keep create/review/promotion separate where the workflow defines them separately.
- Preserve `Needs verification` instead of inventing certainty.
- Treat Graphify as routing/discovery support, not architecture authority.
- Stop on unexpected file changes or state mismatches.
- Never copy example manifests/checkpoints/revisions as project truth.
- Do not let documentation automation silently become refactoring or feature implementation.
- Commit, push, merge, sign, release, and publish only when separately authorized.

For normal execution, start here. Open the full playbook when you need the reasoning behind a gate, a non-standard path, or the later brownfield governance procedures.
