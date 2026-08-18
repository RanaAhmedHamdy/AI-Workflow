# Brownfield AI Playbook Reusable Package v4.4

Contents:

- `playbook/` — DOCX and Markdown editions of the v4.4 playbook.
- `checklists/` — reusable architecture-coverage checklist.
- `templates/` — AGENTS policy templates.
- `skills/` — reusable governance, testing, review, adaptive UI, and publishing skills.
- `repository-starter/` — **prompt-first, AI-tool-agnostic** documentation workflow, focused architecture specs, Graphify policy, and clearly labeled project-specific examples.

Start with `repository-starter/README.md` for the exact operational flow. The core starter requires **no provider-specific CLI or shell runner**: checked-in prompts are run directly with the repository-aware AI agent of your choice. Manifests and the documentation checkpoint provide ordered state for feature and architecture batches.

The full playbook is the deeper governance/rationale reference. Project-specific manifests, checkpoints, Graphify overrides, evidence paths, revisions, decisions, test counts, and project status must be regenerated or adapted from the receiving repository.

## Canonical brownfield lifecycle

Safe setup → repository discovery → documentation/provenance review → first characterization tests → feature understanding → architecture/design validation → architecture coverage gate → verification questions and accountable decisions → no-edit implementation audit → testing safety net → controlled refactor or bounded feature/defect work → independent review → documentation impact → explicit publish → CI/runtime/release verification.

## Package installation

When this package is used from the full `AI-Workflow` repository, bootstrap the reusable starter with the target platform:

```bash
python3 tools/install.py brownfield --platform android --target /path/to/repository
# or
python3 tools/install.py brownfield --platform ios --target /path/to/repository
```

The installer copies reusable prompts/specifications, composes the common + selected platform AGENTS policy, installs applicable reusable skills and the reusable architecture checklist/templates, and installs the Markdown playbook as `AI_PLAYBOOK.md`. It deliberately does not promote files under `docs/ai/examples/` into project truth or create project-specific manifests/checkpoints from guessed state. Use `--skills-only` when only the reusable skill layer is wanted.

Manual/bootstrap lifecycle:

1. Read `repository-starter/README.md` and adapt the project-specific example manifests/checkpoint.
2. Read the canonical playbook in `playbook/BROWNFIELD_PLAYBOOK.md` or the DOCX edition for governance and rationale.
3. Select/install the AGENTS template appropriate to the target repository.
4. Copy only the reusable skills that fit the repository workflow.
5. Run the repository-owned prompts directly, one authorized task at a time.
6. Do not copy example project state as current authority in a new repository.
