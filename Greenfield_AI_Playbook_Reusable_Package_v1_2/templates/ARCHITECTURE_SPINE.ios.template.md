# <Project> iOS Architecture Spine

- Status: Draft / Approved
- Accountable owner:
- Authority:
- Scope:
- Applicable readiness gate:
- Architecture coverage:
- Current lifecycle phase:

Architecture approval does not authorize implementation or release.

## 1. Governance and authority
## 2. Application structure and composition
## 3. Presentation state and Observation
## 4. Swift concurrency
## 5. Navigation, restoration, scenes, and external entry points
## 6. Data, persistence, offline, and integrity
## 7. UI, localization, RTL, adaptive UI, and accessibility
## 8. External services, privacy, capabilities, and configuration
## 9. Background execution and extensions
## 10. Build, dependencies, testing, evidence, and release

## 11. Lifecycle matrix

| Scenario | Source of truth | Reconstruction / recovery | Required evidence | Status |
|---|---|---|---|---|
| State-owner recreation | | | | |
| Process termination/relaunch | | | | |
| Scene recreation | | | | |
| Background/foreground | | | | |
| Rotation/resize/multitasking | | | | |
| App upgrade/migration | | | | |

## 12. Architecture selection register

| ID | Concern | Decision status | Implementation status | Evidence status | Lifecycle impact | Owner | ADR/current home | Blocker | Next action | Required evidence |
|---|---|---|---|---|---|---|---|---|---|---|

## 13. Governance lifecycle integration

- Features implementation-authorized:
- Features in convergence:
- Readiness reports:
- Owner acceptance:
- Release authorization:
- `Needs verification` items:

## 14. Stop rules

- Unresolved architecture is not permission to choose.
- Contradictions block affected work.
- Missing protected-boundary authority blocks affected work.
- Compilation/previews do not establish completion.
- Readiness `PASS` means eligible for owner authorization only.
