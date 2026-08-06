# Cross-Feature Architecture Coverage Checklist

Use after Phase 3 architecture maps are drafted and before owner questions or implementation audits. Do not infer `Not applicable` from absence.

## Status model

Record three independent dimensions for every concern.

### Decision status
- **Decided** - approved direction exists with accountable authority.
- **Deferred with conditions** - deferred with trigger, owner, impact, and revisit condition.
- **Not applicable** - accountable scope establishes that the concern does not apply.
- **Unresolved blocker** - a material decision is missing or conflicting.

### Implementation status
- **Not started**
- **Partial**
- **Implemented**
- **Contradictory/stale**

### Evidence status
- **None**
- **Static inspection**
- **Host test**
- **Instrumented test**
- **Emulator/device runtime**
- **External-service evidence**
- **Release-artifact evidence**

For every row capture evidence/scope, current document, gap, owner, blocker, next action, and required next evidence.

| Concern | Decision | Implementation | Evidence | Current home / scope | Gap / owner / blocker / next action |
|---|---|---|---|---|---|
| Application namespace, source roots, module/target structure | | | | | |
| Domain and feature ownership boundaries | | | | | |
| Dependency direction, cycles, and isolation | | | | | |
| Activity/application/composition-root ownership | | | | | |
| Presentation state and ViewModel ownership | | | | | |
| Route/content and navigation boundaries | | | | | |
| Data flow and external integrations | | | | | |
| API/backend contracts | | | | | |
| Persistence, secure storage, cache, offline, migrations | | | | | |
| State, concurrency, lifecycle, process-death reconstruction | | | | | |
| Error, retry, recovery, degraded behavior | | | | | |
| Design system and shared components | | | | | |
| UI adaptation and supported form factors | | | | | |
| Localization, locale parity, and RTL | | | | | |
| Accessibility, focus, semantics, large text | | | | | |
| Permissions and platform capabilities | | | | | |
| Background execution and sync | | | | | |
| Notifications and platform integrations | | | | | |
| Configuration and environment strategy | | | | | |
| Feature flags, experiments, rollout, rollback | | | | | |
| Analytics, consent, and privacy boundaries | | | | | |
| Logging and diagnostics | | | | | |
| Metrics, tracing, operational observability | | | | | |
| Crash reporting and symbols/mappings | | | | | |
| Performance, memory, rendering, network, battery | | | | | |
| Security and sensitive-data boundaries | | | | | |
| Build, signing, release, distribution, rollback | | | | | |
| Testing/testability and runtime evidence | | | | | |
| AI context, skills, hooks, documentation workflow | | | | | |
| Project-specific cross-cutting concern | | | | | |

## UI adaptation sub-checks

- [ ] Supported device categories and exclusions are explicitly decided.
- [ ] Supported orientations are explicitly decided.
- [ ] Compact, medium, and expanded behavior is documented per relevant screen/shell.
- [ ] Navigation adaptation ownership is documented.
- [ ] Multi-window and resized-window behavior is classified.
- [ ] Foldable posture/hinge relevance is classified.
- [ ] ChromeOS and keyboard/mouse support is classified.
- [ ] State restoration across resize/orientation/recreation is classified.
- [ ] RTL, display scaling, and large-text behavior are classified.
- [ ] Insets, cutouts, IME, dialogs, sheets, camera/media, and platform components are classified where applicable.
- [ ] Preview, screenshot, UI-test, and runtime-test expectations are defined.
- [ ] Release/device verification matrix is defined.
- [ ] Static evidence is not presented as universal compatibility proof.

## Gate result

Return `PASS`, `PASS WITH LIMITATIONS`, or `BLOCKED`. `PASS` means every material decision has an approved home; it does not mean implementation or runtime evidence is complete.
