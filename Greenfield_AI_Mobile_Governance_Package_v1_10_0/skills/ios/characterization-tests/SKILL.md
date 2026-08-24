---
name: characterization-tests
description: Captures existing deterministic behavior before a behavior-preserving refactor.
---

# Characterization Tests

1. Read the feature contract or Brownfield change note, available testing map, nearby implementation/tests, and protected rules.
2. State the observable current behavior, source provenance, and evidence source.
3. Mark ambiguity `Needs verification`.
4. Select the smallest established test layer.
5. Cover representative success, failure, boundary, and preservation behavior.
6. Keep production behavior unchanged.
7. Run the narrowest test and required repository gates; report exact commands/results and any fixture/target limitations.
8. Do not infer simulator/device, VoiceOver, Dynamic Type, scene/background, privacy/capability, archive, or release truth from host tests.
