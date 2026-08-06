# <Project> Android Architecture Spine

Status: [Draft / Approved]
Authority: [AGENTS.md, decision register, approved PRD/specs, design authority]
Scope: Shared cross-feature constraints and implementation gates.

## 1. Governance and authority
- Accountable owners:
- Platform/SDK baseline:
- Design authority:
- Protected boundaries:
- Unselected technical choices remain `Needs verification`.

## 2. Application structure and composition
- Application namespace/source roots:
- Module tree or intentionally single-module structure:
- Allowed dependency directions:
- Application/composition root:
- Thin Activity contract:
- DI/factory strategy:
- Test replacement strategy:

## 3. Presentation, navigation, and lifecycle
- ViewModel/state-owner default:
- Route/content boundary:
- Navigation ownership and leaf-screen restrictions:
- Read-only state/event contract:
- Ephemeral versus durable state:
- Recreation/resize/process-death reconstruction:

## 4. Data, persistence, offline, and integrity
- Source of truth:
- Persistence engine and migration ownership:
- Threading/transaction boundaries:
- Offline/degraded behavior:
- Backup/device-transfer rules:
- Sensitive-data lifecycle:

## 5. UI, design system, localization, RTL, and accessibility
- Design-system mapping:
- Resource-only user/accessibility strings:
- Required locales/fallback/key parity:
- RTL and mixed-direction behavior:
- Compact/medium/expanded and orientations:
- Insets, IME, input/focus:
- Accessibility and large-font obligations:
- Preview/runtime evidence matrix:

## 6. External services, permissions, background work, and configuration
- API/provider contracts:
- Fail-closed behavior:
- Permissions/platform capabilities:
- Background scheduler/reconciliation:
- Environment, secrets, flags:

## 7. Testing, evidence, observability, performance, release
- Test pyramid and runners:
- Evidence artifact format:
- Device/runtime matrix:
- Logging/privacy:
- Performance/reliability budgets:
- CI, signing, release, rollback:

## 8. Architecture selection register
| ID | Concern | Decision status | Owner | ADR/current home | Blocker | Required evidence |
|---|---|---|---|---|---|---|

## 9. Implementation stop rules
- Unresolved architecture is not permission to choose a mechanism.
- Contradictory current artifacts block implementation.
- File existence, compilation, previews, and evidence labels do not establish completion.
