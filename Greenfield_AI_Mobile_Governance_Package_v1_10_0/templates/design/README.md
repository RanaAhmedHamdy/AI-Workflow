# Design Authority — Optional Workflow

[← Greenfield start here](../../README.md) · [Architecture Bootstrap](../architecture/README.md) · [Feature Delivery](../mobile/README.md)

Use this workflow only when completed external designs already exist and the repository owner wants them to constrain downstream implementation. The source tool is not prescribed: Stitch, Figma, Sketch, exported images/PDFs/HTML, or another owner-approved source can be used.

No design-tool MCP/connector is required.

## Quick start

| Step | Goal | What you do | Result |
|---|---|---|---|
| 1 | Add completed designs | Export/copy the exact completed design artifacts into a stable repository path, or keep a deterministic external locator | Inspectable source artifacts |
| 2 | Approve them | Owner explicitly states which artifacts/revisions are approved | Design approval is explicit |
| 3 | Record authority | Update `DESIGN_AUTHORITY.md` and the artifact index; map relevant variants/screens | Canonical Design Authority |
| 4 | Consume downstream | Feature Contract/Plan/Tasks reference exact approved visuals; design-bound implementation inspects the actual visual before UI code | Approved design constrains implementation |

If your completed designs are already copied into the repository, you normally start at **Step 2**. Do not rewrite the exported design files merely to mark them approved.

## Step 1 — Add completed design artifacts

Prefer exact local exports when practical, for example:

```text
docs/design/approved/
  DESIGN_AUTHORITY.md
  DESIGN_ARTIFACT_INDEX.md
  artifacts/
    daily-dashboard.png
    meal-entry.png
    settings.png
```

Keep stable names/IDs/revisions where available. Do not duplicate full visual descriptions in Markdown when the actual artifact can be inspected directly.

## Step 2 — Owner approves the designs

Imported/downloaded files are not automatically authoritative. The owner must explicitly approve the identified artifacts or bounded set.

Example prompt:

```text
I approve all design artifacts currently listed in the Design Artifact Index as the
canonical visual and interaction design authority for their mapped screens/states.
Preserve their visual composition, hierarchy, grouping, emphasis, action placement,
and responsive/RTL intent except for documented required adaptations.
Update the repository design authority and decision/routing documentation accordingly.
Do not rewrite the source design artifacts themselves.
```

Approval may cover all artifacts or only a subset.

## Step 3 — Record Design Authority

Create/update:

- `docs/design/approved/DESIGN_AUTHORITY.md` from `DESIGN_AUTHORITY.template.md`
- `docs/design/approved/DESIGN_ARTIFACT_INDEX.md` from `DESIGN_ARTIFACT_INDEX.template.md`
- optional screen contracts/design-system docs when useful

Record only what downstream implementation needs, such as:

- source tool/project/revision where useful;
- exact local path or deterministic external locator;
- screen/state;
- compact/wide/RTL/state variants;
- approval scope;
- permitted adaptations.

The exact approved visual remains the authority for the visual composition it governs. Screen-contract and design-system Markdown supplements it; those files do not replace inspection of the actual visual.

## Step 4 — Use approved visuals in feature delivery

For a design-bound UI task, downstream artifacts should carry the exact design mapping:

```text
Plan
→ maps exact approved visual(s)

Task
→ carries concise Design Lock + exact artifact/variant

Implementation readiness
→ verifies the governing visual can actually be inspected

bounded-feature-implementation
→ opens/inspects the exact approved visual before writing UI code
```

The implementation agent must preserve approved composition, hierarchy, grouping, relative sizing, action placement, spacing rhythm, typography hierarchy, icon role/placement, and navigation composition within the declared authority.

Allowed differences are limited to documented platform-required behavior, accessibility, localization/RTL, supported responsive reflow, or explicit owner-approved adaptation. “More native,” framework defaults, subjective preference, or implementation convenience are not sufficient reasons for material redesign.

If the approved visual cannot be inspected, the design-bound task blocks rather than improvises from Markdown.

## Optional MCP / design-tool connector

Use an MCP/connector only when it saves work, for example to:

- retrieve a design that was not exported locally;
- inspect a missing variant;
- read source metadata;
- import a newly owner-approved revision.

External design-tool content never silently supersedes repository authority. A newer external revision must be explicitly approved before it becomes canonical.

## Optional visual review

A separate screenshot/fidelity comparison is **not mandatory for every screen**. Use it only when risk justifies the extra cost: owner concern, a high-value/high-complexity screen, regression, major visual refactor, or an explicit final-readiness requirement.

The default strategy is cheaper: prevent drift by requiring exact approved visual inspection before UI implementation.

## Efficiency rules

- Store/track only design artifacts downstream work needs.
- Inspect each unchanged governing visual once per coherent task execution and reuse that understanding.
- Do not load unrelated designs.
- Do not run per-screen image comparison by default.

**Next:** when architecture still needs to be established, continue with [Architecture Bootstrap](../architecture/README.md). If architecture is already ready for bounded feature intake, continue with [Feature Delivery](../mobile/README.md).
