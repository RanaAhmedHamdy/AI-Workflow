---
name: ios-localization-rtl-readiness
description: Enforces iOS localization, String Catalog, formatting, RTL, and mixed-direction correctness.
---

# iOS Localization and RTL Readiness

Verify:

- approved localization source: String Catalog, `.strings`, generated resources, or equivalent;
- zero hardcoded user-facing and accessibility-facing strings;
- stable keys and fallback locale;
- plurals, substitutions, grammatical variants, and comments/context;
- locale-aware dates, times, numbers, measurements, lists, currencies;
- no translated sentence-fragment concatenation;
- leading/trailing semantics;
- Arabic/Hebrew or other approved RTL runtime;
- mixed-direction text, numbers, units, punctuation;
- long translation and truncation behavior;
- notifications, widgets, intents, extensions, and error mapping;
- deterministic stale/missing-key validation.

Return concrete missing keys, layout risks, evidence requirements, and verdict.
