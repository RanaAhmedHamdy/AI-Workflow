---
name: android-runtime-evidence-readiness
description: Requires exact evidence scenarios and concrete artifacts before tasks can be completed.
---
# Runtime Evidence Readiness

Every task must specify scenario, evidence layer, environment, expected result, and planned artifact. Generic labels such as `Runtime` or `TalkBack Review` are insufficient.

Before closure, completed tasks must cite actual command/session, device/emulator/environment, timestamp/result, artifact path, and limitations. Reopen tasks lacking matching evidence.

Evidence layers: host unit, integration, instrumented, emulator/device runtime, manual accessibility, external-service/attestation, release artifact.

Return `PASS` or `FAIL` with improperly completed tasks.
## Verification-Matrix Executability

When the approved implementation plan contains `VM-*` scenarios, verify before evidence execution that each applicable scenario is runnable: the ID exists and traces to approved authority; the named emulator/device/window/OS/locale/accessibility condition is available or has an approved equivalent; preconditions are reproducible; the procedure is concrete; the expected observable result is explicit; the evidence path is usable; and runtime-only claims use runtime-capable evidence. Report unavailable scenarios as blocked/needs verification rather than silently substituting evidence.

This skill checks executability only. It does not maintain a second per-scenario lifecycle status system and does not manufacture `PASS` evidence.

