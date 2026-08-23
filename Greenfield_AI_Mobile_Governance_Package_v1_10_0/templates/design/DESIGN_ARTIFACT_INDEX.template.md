# Design Artifact Index

> Keep this table compact. Store visual detail in the artifact itself, not duplicated prose.

| Artifact ID | Screen / State | Variant / Form Factor | Local Path or Deterministic Locator | Source Revision | Approval | Notes / Permitted Adaptation |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |

Rules:
- `Approved` must come from explicit owner authority, not file presence.
- Prefer a stable local artifact path when practical.
- If only an external locator exists, downstream implementation must be able to inspect the exact approved revision or return blocked.
- A newer external revision does not silently supersede the approved row.
