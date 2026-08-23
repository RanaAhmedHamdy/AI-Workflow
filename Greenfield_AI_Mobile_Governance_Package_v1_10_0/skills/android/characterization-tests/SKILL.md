---
name: characterization-tests
description: Capture existing deterministic behavior at the smallest useful test layer before a focused change or refactor.
---

# Characterization Tests

1. Read the feature document, testing map, nearby source/tests, and protected rules.
2. State the observable contract and evidence source; mark ambiguity `Needs verification`.
3. Select the smallest established test layer; do not add frameworks or production seams without authorization.
4. Cover representative success, failure, boundary, and preservation behavior only where meaningful.
5. Keep production behavior unchanged; record suspicious behavior rather than fixing it.
6. Run the narrowest test and required repository gates; report exact commands/results.
7. Do not infer runtime/backend/device/accessibility/security/release truth from host-side tests.
