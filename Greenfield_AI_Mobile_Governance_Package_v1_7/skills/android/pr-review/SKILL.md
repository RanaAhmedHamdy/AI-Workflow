---
name: pr-review
description: Reviews a coherent Android diff for defects, architecture drift, UI structure, localization, adaptive/accessibility issues, protected-boundary violations, stale docs, and missing evidence.
---
# PR Review

Trace changed behavior through callers, ViewModels/state, navigation, domain/data/platform boundaries. For Compose changes inspect thin Activity, route/content split, construction boundaries, immutable state, hardcoded strings, locale parity, RTL, compact/expanded arrangements, resize/recreation, large text, semantics/focus, IME/insets, and evidence artifacts. Separate blockers, non-blockers, questions, and unverified runtime layers. Do not merge or authorize publication.
