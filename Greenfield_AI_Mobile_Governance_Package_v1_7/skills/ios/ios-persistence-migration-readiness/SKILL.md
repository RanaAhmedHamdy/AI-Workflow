---
name: ios-persistence-migration-readiness
description: Validates iOS persistence choice, schema ownership, migration, isolation, backup, deletion, and recovery.
---

# iOS Persistence and Migration Readiness

Inspect:

- selected technology and rationale;
- system of record;
- schema/model ownership and versions;
- migration strategy;
- actor/context/queue isolation;
- atomic multi-record operations;
- guarded updates and stale-write behavior;
- backup and device transfer;
- file protection and encryption;
- Keychain boundaries;
- cache and temporary files;
- deletion/logout/account removal;
- test stores versus release stores;
- recovery after failed migration;
- representative production migration fixtures.

Do not assume SwiftData is always preferable to Core Data or vice versa.

Verdicts:

- `Ready`
- `Ready with migration evidence pending`
- `Blocked`
