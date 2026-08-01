# Cross-Feature Architecture Coverage Checklist

Use after Phase 3 maps are drafted and before owner questions or implementation audits. Do not infer `Not applicable` from absence.

## Classifications

- **Verified** - current reviewed evidence supports the conclusion within stated scope.
- **Needs verification** - material concern exists but evidence or accountable intent is incomplete/conflicting.
- **Not observed** - no relevant implementation/configuration found in inspected scope.
- **Not applicable** - accountable scope establishes the concern does not apply.

For every row capture: classification, evidence/scope, current document, gap, owner, blocker, next action.

| Concern | Classification | Evidence / scope | Current document | Gap / owner / blocker / next action |
|---|---|---|---|---|
| Application/module/target structure | | | | |
| Domain and feature ownership boundaries | | | | |
| Dependency direction, cycles, and isolation | | | | |
| Data flow and external integrations | | | | |
| API/backend contracts | | | | |
| Persistence, secure storage, cache, offline, migrations | | | | |
| State ownership, concurrency, lifecycle, restoration | | | | |
| Navigation, deep links, external entry points | | | | |
| Dependency injection/service location | | | | |
| Error, retry, recovery, degraded behavior | | | | |
| Design system and shared components | | | | |
| UI adaptation and supported form factors | | | | |
| Localization/internationalization | | | | |
| Accessibility | | | | |
| Permissions and platform capabilities | | | | |
| Background execution and sync | | | | |
| Notifications and platform integrations | | | | |
| Configuration and environment strategy | | | | |
| Feature flags, experiments, rollout, rollback | | | | |
| Analytics, consent, and privacy boundaries | | | | |
| Logging and diagnostics | | | | |
| Metrics, tracing, and operational observability | | | | |
| Crash/incident reporting and symbols/mappings | | | | |
| Performance, memory, rendering, network, battery | | | | |
| Security and sensitive-data boundaries | | | | |
| Build, signing, release, distribution, rollback | | | | |
| Testing/testability and runtime evidence | | | | |
| AI context, skills, hooks, documentation workflow | | | | |
| Project-specific cross-cutting concern | | | | |

## Living-review question

Are there material cross-cutting architectural concerns that are not represented above?

When yes: update the closest current document or create a focused one only when no suitable home exists; record why it matters, evidence boundary, owner, blocker, next action, and context-index routing.

## Gate result

- [ ] Every material concern has a current evidence home or explicit classification.
- [ ] Every `Needs verification` item has an owner, blocker, and next evidence layer.
- [ ] Owner questions are routed to Phase 3.5.
- [ ] Decision/source contradictions are routed to Phase 3.6.
- [ ] No empty/speculative documents were created to satisfy the checklist.
- [ ] New current documents are routed through the context index.

## UI adaptation sub-checks

- [ ] Supported device categories are explicitly decided.
- [ ] Supported orientations are explicitly decided.
- [ ] Compact, medium, and expanded behavior is documented.
- [ ] Navigation adaptation ownership is documented.
- [ ] Multi-window and resized-window behavior is classified.
- [ ] Foldable posture and hinge relevance is classified.
- [ ] ChromeOS and keyboard/mouse support is classified.
- [ ] State restoration across resize/orientation is classified.
- [ ] RTL, display scaling, and large-text behavior are classified.
- [ ] Insets, cutouts, IME, dialogs, sheets, camera/media, and platform components are classified where applicable.
- [ ] Preview, screenshot, UI-test, and runtime-test expectations are defined.
- [ ] The release/device verification matrix is defined.
- [ ] Static evidence is not presented as universal device compatibility proof.
