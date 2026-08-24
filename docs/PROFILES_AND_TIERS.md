# Profiles and feature tiers

Profiles answer **how much AI-Workflow infrastructure a repository adopts**. Feature tiers answer **how much process one change needs based on its risk**. They are deliberately independent.

| Profile | Intended use | Process weight |
|---|---|---|
| `skills` | Specialist mobile knowledge with explainable discovery | Minimal |
| `safety` | Recommended default for most mobile repositories | Light safety layer |
| `feature` | Proportional feature delivery without a mandatory Architecture Spine/ADR programme | Medium |
| `full` | Complete architecture and feature governance | Deep |

A repository on `full` may still deliver a SMALL change with one compact record. A repository on `safety` may encounter a migration, protected boundary, or unresolved behavior that routes to a STANDARD/COMPLEX recommendation and should be escalated rather than bypassed.

Feature tiers are `SMALL`, `STANDARD`, and `COMPLEX`. SMALL uses `SMALL_FEATURE_RECORD.md`; STANDARD uses the normal contract/plan/tasks flow proportionally; COMPLEX adds independent gates and the applicable advanced governance. The canonical trigger and route truth is [`routing/routes.json`](../routing/routes.json), not this explanatory document.
