---
name: runtime-evidence-readiness
description: Requires exact evidence scenarios and concrete artifacts before tasks can be completed.
---
# Runtime Evidence Readiness

Every task must specify scenario, evidence layer, environment, expected result, and planned artifact. Generic labels such as `Runtime` or `TalkBack Review` are insufficient.

Before closure, completed tasks must cite actual command/session, device/emulator/environment, timestamp/result, artifact path, and limitations. Reopen tasks lacking matching evidence.

Evidence layers: host unit, integration, instrumented, emulator/device runtime, manual accessibility, external-service/attestation, release artifact.

Return `PASS` or `FAIL` with improperly completed tasks.
