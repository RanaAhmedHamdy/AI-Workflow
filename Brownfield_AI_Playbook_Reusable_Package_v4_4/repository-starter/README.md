# Brownfield repository starter kit

This starter is **prompt-first and AI-tool agnostic**. The top-level `ai-workflow` CLI may be used once to copy/bootstrap these reusable files into a repository, but the Brownfield workflow itself does not require any provider-specific CLI or bundled shell runner after installation.

Use a repository-aware AI coding agent and run the checked-in prompts directly. A normal instruction can be as small as:

```text
Follow docs/ai/prompts/modules-create.md exactly.
```

You can also paste a prompt's contents into your preferred agent. The agent must be able to inspect the repository evidence referenced by the prompt.

The full playbook explains rationale, governance, protected boundaries, and later implementation phases. This README is the execution path.

---

## 1. What is reusable vs project-specific

Reusable workflow files:

```text
docs/ai/prompts/
docs/ai/architecture-specs/
docs/ai/GRAPHIFY_USAGE.md
```

Project-specific workflow state that must be created or adapted from repository evidence when the corresponding phase is used:

```text
docs/ai/DOCUMENTATION_CHECKPOINT.md
docs/ai/feature-docs.tsv
docs/ai/architecture-docs.tsv
docs/ai/architecture-coverage-routing.tsv
```

Optional project-specific Graphify state, created **only when a verified extraction/context gap exists**:

```text
docs/ai/graphify-context-overrides.tsv
```

Files under `docs/ai/examples/` are examples only. Never copy their revisions, paths, feature order, decisions, test counts, Graphify limitations, override rows, or checkpoint state as project truth.

Before execution, adapt platform terminology, authoritative product/context paths, output paths, manifests, architecture scope specs, and repository policy. If Graphify is used, keep the reusable `GRAPHIFY_USAGE.md` policy and add project-specific overrides only when current evidence demonstrates a need.

---

## 2. Core rule: prompts are the workflow

There is no required script layer.

Each prompt either:
- names one fixed foundation document; or
- resolves one authorized feature/architecture target from the repository manifest + checkpoint.

The prompts enforce one-document scope, evidence boundaries, status transitions, and stop conditions. Optional local automation may be added later, but it must only select/render the same checked-in prompts and must not become a second source of workflow truth.

---

# Exact execution flow

## Before starting: repository root and optional Graphify setup

Run the workflow against the **root of the receiving repository**: the existing application/project being analyzed, not the AI-Workflow source repository. Open that repository as the working directory/root for your repository-aware AI agent.

Graphify is optional. The Brownfield prompts must continue to work when Graphify is not installed or has not produced usable output. Direct source/build/test inspection remains sufficient and authoritative.

If you choose to use Graphify, set it up **before the foundation sequence** so graph-assisted discovery is available from the first map. Use Graphify's current official installation/platform instructions:

- Official project/setup: <https://github.com/Graphify-Labs/graphify>
- PyPI package name: `graphifyy`; CLI command: `graphify`.

A typical project-scoped setup is:

```bash
# Run from the receiving repository root.
uv tool install graphifyy

# Register Graphify for the AI assistant you use. Examples:
graphify install --project                     # Claude Code default
graphify install --project --platform codex    # Codex
graphify install --project --platform agents   # generic Agent-Skills location
```

Then build the graph from that same repository root using the command appropriate to your assistant. Graphify's current documentation uses `/graphify .` on supported slash-command assistants and `$graphify .` on Codex. Follow the official README when platform commands differ.

If you expect a prompt to use graph-assisted discovery, first confirm Graphify generated usable output (currently including `graphify-out/graph.json`). If it did not, continue with direct repository inspection rather than blocking the workflow.

Do not hand-edit `graphify-out/`. Read and apply `docs/ai/GRAPHIFY_USAGE.md`. Create `docs/ai/graphify-context-overrides.tsv` only after a project-specific Graphify gap has been directly verified.

---

## 3. Foundation sequence

Run foundation documents in this order:

```text
MODULES
  -> FEATURE_MAP
  -> TESTING_MAP
  -> DEPENDENCIES
  -> PROJECT_OVERVIEW
  -> ARCHITECTURE
```

A foundation document uses three passes:

```text
create/revise Draft
-> fresh read-only review
-> promote status only
```

Do not combine review and promotion. If review returns `Revise`, rerun the matching create prompt against the existing Draft, then perform a fresh review again.

### 3.1 MODULES

Create:

```text
Follow docs/ai/prompts/modules-create.md exactly.
```

Expected target:

```text
docs/wiki/project/MODULES.md -> Draft
```

Fresh read-only review:

```text
Follow docs/ai/prompts/modules-review.md exactly.
```

The review returns `Promote`, `Revise`, or `Blocked` and edits nothing.

If it returns `Promote`, in a context that contains that completed review run:

```text
Follow docs/ai/prompts/foundation-promote.md exactly.
```

Expected status:

```text
docs/wiki/project/MODULES.md -> Reviewed orientation
```

### 3.2 FEATURE_MAP

Create/revise:

```text
Follow docs/ai/prompts/feature-map-create.md exactly.
```

Review:

```text
Follow docs/ai/prompts/feature-map-review.md exactly.
```

Promote only after a `Promote` verdict:

```text
Follow docs/ai/prompts/foundation-promote.md exactly.
```

Expected target:

```text
docs/wiki/project/FEATURE_MAP.md
```

### 3.3 TESTING_MAP

```text
Follow docs/ai/prompts/testing-map-create.md exactly.
Follow docs/ai/prompts/testing-map-review.md exactly.
Follow docs/ai/prompts/foundation-promote.md exactly.   # only after Promote
```

Expected target:

```text
docs/wiki/testing/TESTING_MAP.md
```

### 3.4 DEPENDENCIES

```text
Follow docs/ai/prompts/dependencies-create.md exactly.
Follow docs/ai/prompts/dependencies-review.md exactly.
Follow docs/ai/prompts/foundation-promote.md exactly.   # only after Promote
```

Expected target:

```text
docs/wiki/project/DEPENDENCIES.md
```

### 3.5 PROJECT_OVERVIEW

Run only after MODULES, FEATURE_MAP, TESTING_MAP, and DEPENDENCIES are reviewed.

```text
Follow docs/ai/prompts/project-overview-create.md exactly.
Follow docs/ai/prompts/project-overview-review.md exactly.
Follow docs/ai/prompts/foundation-promote.md exactly.   # only after Promote
```

Expected target:

```text
docs/wiki/project/PROJECT_OVERVIEW.md
```

### 3.6 High-level ARCHITECTURE

```text
Follow docs/ai/prompts/architecture-create.md exactly.
Follow docs/ai/prompts/architecture-review.md exactly.
Follow docs/ai/prompts/foundation-promote.md exactly.   # only after Promote
```

Expected target:

```text
docs/wiki/project/ARCHITECTURE.md
```

At this point the reusable foundation is complete.

---

## 4. Feature-document batch

Before starting, create/adapt:

```text
docs/ai/feature-docs.tsv
```

Use `docs/ai/examples/feature-docs.project-example.tsv` only as a format example.

Recommended columns:

```text
order<TAB>feature_id<TAB>display_name<TAB>output_path
```

Also maintain `docs/ai/DOCUMENTATION_CHECKPOINT.md` so it names the single next authorized task whenever possible.

### Create one feature page

Start a fresh creation session:

```text
Follow docs/ai/prompts/feature-doc-create.md exactly.
```

The prompt resolves exactly one feature from the manifest/checkpoint. It creates or corrects only that page and leaves it `Draft`. It does **not** advance the checkpoint.

### Review one feature page

Start a fresh review session:

```text
Follow docs/ai/prompts/feature-doc-review.md exactly.
```

The review prompt resolves the single Draft page awaiting review, verifies/corrects only that page, and may mark it `Reviewed` when evidence supports promotion. On success it updates the checkpoint to authorize exactly the next manifest item.

Repeat create -> review until the feature manifest batch is complete.

If selection is ambiguous, the prompts stop instead of guessing. Fix the checkpoint/manifest state, then rerun the same prompt.

---

## 5. Phase 3 focused architecture maps

Before starting, create/adapt:

```text
docs/ai/architecture-docs.tsv
docs/ai/architecture-specs/
docs/ai/DOCUMENTATION_CHECKPOINT.md
```

Use the project example manifest only as a format example:

```text
order<TAB>document_id<TAB>display_name<TAB>output_path<TAB>spec_path<TAB>prerequisite_path
```

Every focused architecture map uses three separate passes.

### Create Draft

```text
Follow docs/ai/prompts/architecture-map-create.md exactly.
```

The prompt resolves the checkpoint-authorized manifest row, verifies its reviewed prerequisite, creates exactly one Draft map, and updates the checkpoint only to authorize review of that same Draft.

### Fresh read-only review

```text
Follow docs/ai/prompts/architecture-map-review.md exactly.
```

This edits nothing and returns:

```text
Promote | Revise | Blocked
```

If `Revise`, run `architecture-map-create.md` again to correct the same Draft, then perform another fresh read-only review.

### Promote

Only after a review returned `Promote`, run the promotion prompt in a context that contains that completed review result:

```text
Follow docs/ai/prompts/architecture-map-promote.md exactly.
```

Promotion changes only review metadata/status + checkpoint. It must not make substantive corrections. The checkpoint then authorizes exactly the next architecture-map row, or Phase 3.4 when the manifest is complete.

Repeat create -> review -> promote one map at a time.

---

## 6. Prompt routing reference

| Scenario | Prompt | Edits files? | Expected result |
|---|---|---:|---|
| Build module topology | `modules-create.md` | Yes | `MODULES.md` Draft |
| Review module topology | `modules-review.md` | No | Promote / Revise / Blocked |
| Create feature map | `feature-map-create.md` | Yes | `FEATURE_MAP.md` Draft |
| Review feature map | `feature-map-review.md` | No | Promote / Revise / Blocked |
| Create testing map | `testing-map-create.md` | Yes | `TESTING_MAP.md` Draft |
| Review testing map | `testing-map-review.md` | No | Promote / Revise / Blocked |
| Create dependency map | `dependencies-create.md` | Yes | `DEPENDENCIES.md` Draft |
| Review dependency map | `dependencies-review.md` | No | Promote / Revise / Blocked |
| Create project overview | `project-overview-create.md` | Yes | `PROJECT_OVERVIEW.md` Draft |
| Review project overview | `project-overview-review.md` | No | Promote / Revise / Blocked |
| Create high-level architecture | `architecture-create.md` | Yes | `ARCHITECTURE.md` Draft |
| Review high-level architecture | `architecture-review.md` | No | Promote / Revise / Blocked |
| Promote reviewed foundation Draft | `foundation-promote.md` | Status/checkpoint only | Reviewed orientation |
| Create next feature page | `feature-doc-create.md` | Yes | One feature page Draft |
| Review next feature page | `feature-doc-review.md` | Yes, bounded | Reviewed page + next checkpoint |
| Create next focused architecture map | `architecture-map-create.md` | Yes | One map Draft + review checkpoint |
| Review focused architecture map | `architecture-map-review.md` | No | Promote / Revise / Blocked |
| Promote focused architecture map | `architecture-map-promote.md` | Status/checkpoint only | Reviewed + next checkpoint |

---

## 7. What happens after the documentation maps

After the feature and focused architecture maps are reviewed:

1. Run the Phase 3.4 cross-feature architecture coverage review using the reusable `architecture-coverage-review` skill/checklist.
2. Route unresolved owner-sensitive behavior to explicit verification questions/decisions.
3. Run the Phase 3.6 no-edit implementation audit for one bounded feature/contract.
4. Use protected-boundary preflight when applicable.
5. Implement only one authorized bounded item.
6. Run focused verification and documentation-impact assessment.
7. Run independent implementation/documentation review as applicable.
8. Publish only after explicit human authorization.

See the full playbook for these later phases and their rationale.

---

## 8. Failure/stop cases

Stop rather than guessing when:

- a required reviewed prerequisite is missing;
- a manifest/checkpoint names different targets;
- more than one Draft could be the review target;
- a promotion prompt cannot see the completed review result;
- a review returns `Revise` or `Blocked`;
- repository evidence cannot support a material claim;
- the prompt would need to edit outside its allowed boundary;
- runtime/backend/device/release evidence is required but unavailable.

Classify unresolved claims as `Needs verification` and route them to the correct evidence owner/layer.

---

## 9. Optional automation

You may add local shell/CI/client automation later, but it is optional. Good automation may:

- choose the same next manifest row the prompt would choose;
- verify prerequisite/status state;
- open/copy the checked-in prompt;
- detect unexpected file changes.

It should **not** embed a specific AI provider as a requirement, duplicate the prompt's policy, automatically approve/promote content, commit/push, or silently advance workflow state.

The checked-in prompt + manifest + checkpoint remain the durable workflow contract.
