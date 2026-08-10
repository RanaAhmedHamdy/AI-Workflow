---
name: characterization-tests
description: Captures existing deterministic behavior before a behavior-preserving refactor.
---

# Characterization Tests

1. Read the feature contract, nearby implementation/tests, and protected rules.
2. State the observable current behavior and evidence source.
3. Mark ambiguity `Needs verification`.
4. Select the smallest established test layer.
5. Cover representative success, failure, boundary, and preservation behavior.
6. Keep production behavior unchanged.
7. Run the narrowest test and report exact commands/results.
8. Do not infer device, accessibility, security, background, or release truth from host tests.
