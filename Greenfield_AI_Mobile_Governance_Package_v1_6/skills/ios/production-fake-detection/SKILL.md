---
name: production-fake-detection
description: Detects fake, demo, preview, test, or simulated behavior in release paths.
---

# Production Fake Detection

Inspect release/production composition for:

- manufactured provider responses;
- fixed success IDs;
- accept-all validation;
- placeholder receipts, tokens, signatures, or authorization;
- no-op repositories, schedulers, workers, migrations, or background handlers;
- in-memory substitutes for required durability;
- preview/test bindings in release composition;
- debug bypasses or menus;
- silent fallback from unavailable infrastructure to simulated success.

Also inspect target membership, build configurations, conditional compilation, dependency containers, environment values, generated configuration, and package products.

## Verdict

- **PASS**
- **FAIL — RELEASE FAKE OR BYPASS FOUND**
- **NEEDS VERIFICATION — BUILD COMPOSITION NOT PROVEN**
