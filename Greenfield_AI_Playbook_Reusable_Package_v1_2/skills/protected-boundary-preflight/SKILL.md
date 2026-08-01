---
name: protected-boundary-preflight
description: Confirm authorization, evidence, files, owners, and verification requirements before work near protected repository boundaries.
---

# Protected-Boundary Preflight

## Universal protected classes

- identity, authentication, authorization, tokens, secrets, and sensitive data;
- destructive persistence, migrations, synchronization, and data integrity;
- backend/public contracts and externally visible behavior;
- permissions, intents/deep links, entitlements, background/platform capabilities;
- signing, certificates, provisioning, production configuration, distribution;
- financial, regulated, safety, legal, privacy, analytics, and telemetry boundaries.

Project-specific boundaries in `AGENTS.md` extend this list.

## Procedure

1. Read the task, relevant `AGENTS.md` rules, routed context, and current implementation.
2. List proposed files and behavior/configuration changes.
3. Map each change to universal and project-specific protected classes.
4. Separate read-only inspection from modification and remote/runtime side effects.
5. Confirm explicit authorization, accountable owner, allowed files, forbidden files, test data, environment, cleanup, and evidence location.
6. Stop unauthorized or unclear modifications and record `Needs verification`.
7. After work, inspect the final diff for boundary drift and report unrun evidence layers.

## Authority

This skill does not grant authorization. Documentation, tests, plans, or current source do not independently authorize protected changes.
