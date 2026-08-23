---
name: android-localization-rtl-readiness
description: Prevents hardcoded user-facing text, locale-key drift, RTL layout assumptions, and unverified mixed-direction/large-font behavior.
---
# Localization and RTL Readiness

Check user/accessibility text in Activities, Composables, ViewModels, workers, notifications, and error mapping. Require localized resources or approved localized domain content, plural/format APIs, start/end semantics, required locale folders, fallback behavior, deterministic key-parity validation, Arabic/RTL or applicable RTL preview/runtime, mixed text/numbers/units, and large-font reflow.

Return `PASS`, `PASS WITH LIMITATIONS`, or `FAIL` with exact literals/keys/layout assumptions and required evidence.
