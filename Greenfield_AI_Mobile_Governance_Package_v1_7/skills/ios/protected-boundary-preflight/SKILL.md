---
name: protected-boundary-preflight
description: Confirms authorization, owner, files, environment, and evidence before protected work.
---

# Protected-Boundary Preflight

## Universal protected classes

- identity, authentication, authorization, tokens, secrets;
- personal or sensitive data;
- destructive persistence, migrations, synchronization, deletion;
- public/backend contracts;
- permissions, capabilities, entitlements, background execution;
- signing, certificates, provisioning, production configuration, release;
- billing, financial, regulated, privacy, analytics, telemetry.

## Procedure

1. Read task, policy, routed context, and current implementation.
2. List proposed files and side effects.
3. Map each change to protected classes.
4. Separate inspection, local modification, runtime mutation, and remote side effects.
5. Confirm authorization, accountable owner, allowed files, forbidden files, test data, environment, cleanup, and evidence location.
6. Stop unclear or unauthorized work.
7. Reinspect the final diff for boundary drift.

This skill does not grant authorization.
