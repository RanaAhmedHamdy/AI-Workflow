# Design Authority Workflow — Optional Operational Guide

Use this workflow when externally created designs already exist and the repository owner wants them to constrain downstream implementation. The source tool is not prescribed: Stitch, Figma, Sketch, exported images/PDFs/HTML, or another owner-approved source may be used.

This workflow can be used independently of the architecture and feature-delivery workflows.

## Core authority rule

An imported design artifact is **source material**, not repository authority by file existence alone.

```text
Completed external design
        ↓
Preserve/import the exact artifact
        ↓
Explicit owner approval
        ↓
Record approval + exact artifact identity/path
        ↓
Approved design authority
```

Do not rewrite exported visual artifacts merely to mark them approved. Record approval in repository governance documents.

## Recommended minimal files

- `docs/design/approved/DESIGN_AUTHORITY.md` from `DESIGN_AUTHORITY.template.md`
- `docs/design/approved/DESIGN_ARTIFACT_INDEX.md` from `DESIGN_ARTIFACT_INDEX.template.md`
- exact approved visual artifacts under a stable repository path when practical
- optional screen contracts/design-system documents when the project needs them

## Procedure

1. **Preserve exact source artifacts.** Keep stable filenames/IDs and revisions where available.
2. **Inventory only what downstream work needs.** Record screen/state, form factor/variant, local path or deterministic external locator, and approval state.
3. **Obtain explicit owner approval.** Approval may cover all listed artifacts or a bounded subset. Do not infer approval from import/download.
4. **Record design authority.** State what is binding: visual composition, hierarchy, grouping, emphasis, action placement, spacing rhythm, typography hierarchy, tokens, interaction behavior, responsive variants, etc.
5. **Record permitted adaptations.** Platform-required behavior, accessibility, localization/RTL, and responsive reflow may adapt the source only within the approved authority. “More native,” framework defaults, or implementation convenience are not sufficient reasons for material redesign.
6. **Map features/screens to exact artifacts.** Feature Contracts, Plans, and Tasks should cite the exact approved artifacts that govern each design-bound screen/state.
7. **Do not require a separate post-hoc visual review by default.** Instead, the implementation procedure must inspect the exact approved visual artifact before writing UI code for a design-bound task.

## Design-bound implementation rule

For a UI task with approved visual authority:

> Referencing an artifact is not the same as inspecting it. The implementation agent MUST inspect the exact approved visual artifact before implementing that screen/state. Markdown screen contracts and design-system documents supplement the visual authority; they do not replace it.

If the approved visual cannot be inspected, the task is blocked rather than free to improvise.

The task must preserve the approved composition unless a documented permitted adaptation applies. Material reordering, regrouping, substitution of framework-default composition, or redesign for subjective platform preference requires explicit owner approval.

## Local artifacts and MCP / design-tool connectors

A design-tool MCP/connector is **optional**.

Preferred when practical: keep exact approved exports locally in the repository so downstream work is deterministic and does not depend on network access or external permissions.

Use an MCP/connector only when useful to retrieve missing artifacts/variants, inspect source metadata, or import a newly approved revision. External content never silently supersedes the repository-approved revision. A newly retrieved revision requires explicit owner approval before it becomes canonical.

## Efficiency rules

- Keep the artifact index compact; do not duplicate full design descriptions in Markdown.
- For a coherent task group, inspect each unchanged governing visual once and reuse that understanding during the task.
- Do not run image-comparison/fidelity review for every screen by default. Reserve manual/fidelity review for high-risk screens, owner concerns, regressions, or explicit final-readiness requirements.
- Do not load unrelated design artifacts.
