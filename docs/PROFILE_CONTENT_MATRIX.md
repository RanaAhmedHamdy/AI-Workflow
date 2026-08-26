# Profile content matrix

This matrix is the profile-content authority consumed by installer tests. Platform skill packs remain namespaced and self-contained.

<!-- profile-test-authority: {"skills":{"agents":true,"small_record":false,"architecture":false,"brownfield_playbook":false},"safety":{"agents":true,"small_record":false,"architecture":false,"brownfield_playbook":false},"feature":{"agents":true,"small_record":true,"architecture":false,"brownfield_playbook":false},"full":{"agents":true,"small_record":true,"architecture":true,"brownfield_playbook":true}} -->

| Asset group | Skills | Safety | Feature | Full | Workflow / platform | Reason |
|---|---:|---:|---:|---:|---|---|
| Selected platform specialist skills | Yes | Yes | Yes | Yes | Both / Android+iOS | Deep mobile procedures remain available, but routing selects them. |
| `AGENTS.md`, `CLAUDE.md`, `AI_CONTEXT.md`, `FIRST_SAFE_CHANGE.md`, routing registry | Yes | Yes | Yes | Yes | Both / Android+iOS | One canonical policy plus thin client adapter, discoverability, and explainable deterministic routing. |
| Protected-boundary and evidence policies | No | Yes | Yes | Yes | Greenfield; generated equivalent context for Brownfield | Safety layer. |
| Feature tier policy and SMALL record | No | No | Yes | Yes | Both / Android+iOS | Proportional feature delivery. |
| Feature Input/Contract/Plan/Tasks/readiness templates | No | No | Yes | Yes | Both / Android+iOS | STANDARD/COMPLEX path. |
| Architecture Spine, ADR, architecture coverage/readiness, design templates, decision register | No | No | No | Yes | Greenfield / Android+iOS | Full governance only. |
| Brownfield source-first playbook, repository-starter templates and architecture checklist | No | No | No | Yes | Brownfield / Android+iOS | Advanced mapping/governance only. |
| Brownfield composed source-first policy | No | Yes | Yes | Yes | Brownfield / Android+iOS | First safe change without mandatory full mapping. |
