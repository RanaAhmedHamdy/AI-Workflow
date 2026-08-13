---
name: uikit-screen-readiness
description: Validates UIKit screens, controllers, coordinators, layout, lifecycle, and accessibility.
---

# UIKit Screen Readiness

Check:

- controller/coordinator ownership;
- view model or presentation model lifetime;
- dependency injection;
- Auto Layout and size-class behavior;
- trait/environment changes;
- child-controller containment;
- navigation/presentation/dismissal;
- keyboard and safe-area handling;
- state restoration;
- diffable data source or established collection/table pattern;
- localization, Dynamic Type, VoiceOver, focus, pointer/keyboard support;
- async cancellation on lifecycle transitions;
- tests and runtime evidence.

Flag massive view controllers, feature repositories created in controllers, hardcoded frames for adaptive UI, duplicated state across child controllers, and side effects without lifecycle ownership.

## Post-Mutation and Route-Origin Readiness (v1.7)
For any screen that commits durable state, identify dependent parent/sibling/cross-feature consumers and prove their render state updates from the authoritative source without relying on accidental navigation reload. Also prove that a dependent consumer created or re-entered after the mutation loads current committed state even if it did not observe the original event. For reusable screens entered from multiple origins, verify save/cancel/failure semantics per origin, including explicit separation of onboarding/setup completion from normal management and prevention of mode-to-mode return-state aliasing.
