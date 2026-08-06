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
