# Cross-Feature Architecture Coverage Checklist

> Reusable template. Do not infer `Not applicable` from absence.

## Status model

### Decision status
- Decided
- Deferred with conditions
- Not applicable
- Unresolved blocker

### Implementation status
- Not started
- Partial
- Implemented
- Contradictory / stale

### Evidence status
- None
- Static inspection
- Host / JVM / unit test
- Integration / migration test
- Instrumented / UI automation
- Simulator / emulator runtime
- Physical-device runtime
- Accessibility runtime
- Background / lifecycle runtime
- External-service evidence
- Performance / memory / energy evidence
- Archive / package inspection
- Signing / distribution evidence

### Lifecycle impact
- Planning blocker
- Implementation-authorization blocker
- Convergence blocker
- Feature-acceptance blocker
- Release blocker
- Non-blocking limitation

## Coverage matrix

| Concern | Decision | Implementation | Evidence | Lifecycle impact | Current home / scope | Gap / owner / blocker / next action |
|---|---|---|---|---|---|---|
| Application namespace, roots, module/target/package structure | | | | | | |
| Domain and feature ownership | | | | | | |
| Dependency direction and isolation | | | | | | |
| Host/composition-root ownership | | | | | | |
| Presentation state and lifecycle | | | | | | |
| Cross-feature state propagation and inactive/recreated consumer coherence | | | | | | |
| Navigation and restoration | | | | | | |
| Persistence, migrations, backup, deletion | | | | | | |
| Localization and RTL | | | | | | |
| Accessibility and adaptive UI | | | | | | |
| Permissions, capabilities, manifests, entitlements | | | | | | |
| External services and dormant future configuration | | | | | | |
| Background execution | | | | | | |
| Privacy, analytics, logging, observability | | | | | | |
| Performance, memory, energy | | | | | | |
| Build, signing, release, rollback | | | | | | |
| Testing and runtime evidence | | | | | | |
| Production composition and fake prevention | | | | | | |
| Implementation authorization synchronization | | | | | | |
| Task evidence closure | | | | | | |
| Convergence and readiness report | | | | | | |
| Owner acceptance | | | | | | |
| Separate release authorization | | | | | | |

## Android sub-checks

- [ ] Compact/medium/expanded behavior classified.
- [ ] Foldables/hinge classified.
- [ ] ChromeOS/resizable support classified.
- [ ] IME, system bars, cutouts, multi-window classified.
- [ ] Keyboard, mouse, trackpad, D-pad, Switch Access, Voice Access classified.
- [ ] Activity recreation and process death classified.

## iOS sub-checks

- [ ] iPhone and iPad classes/orientations classified.
- [ ] Split View, Stage Manager, reduced width classified.
- [ ] Multiple scenes/windows classified.
- [ ] Safe areas, keyboard, sheets, popovers classified.
- [ ] Full Keyboard Access, pointer, Switch Control, Voice Control classified.
- [ ] Process termination/relaunch and scene recreation classified.

## Gate result

Return `PASS`, `PASS WITH LIMITATIONS`, or `BLOCKED`.

`PASS` does not authorize implementation, establish feature acceptance, or authorize release.
