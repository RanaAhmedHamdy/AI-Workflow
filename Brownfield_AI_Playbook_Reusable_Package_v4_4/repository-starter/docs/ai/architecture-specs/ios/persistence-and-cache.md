# Persistence and Cache map specification

## Checklist coverage

- Durable persistence, secure storage, caches, transient files, and server-authoritative state
- Offline/read-through/write-through behavior and invalidation
- Logout/reset/destructive operations, migrations, backup, protection, and consistency boundaries

## Discovery question

What data is persisted, securely stored, cached, derived, downloaded, or discarded; which technology and owner is responsible for each lifetime; and what migration, backup, corruption, deletion, offline, protection, and consistency behavior is implemented or still `Needs verification`?

## Required evidence

Inspect only storage mechanisms actually present, including where applicable:

- `UserDefaults` suites/keys/wrappers
- Keychain wrappers/access groups
- file-system paths, caches, documents/application-support/temp directories, downloaded files, and cleanup code
- Core Data models/stores/migrations, SwiftData, SQLite, Realm, or other databases only if present
- `URLCache`, image caches, in-memory caches, or third-party cache libraries actually present
- repository/service ownership and server-authoritative refresh/sync behavior
- logout/reset/delete/account-switch behavior
- entitlements, App Groups, iCloud/document-container, backup/file-protection configuration where material
- existing persistence/cache tests and Reviewed feature pages
- reviewed Data Flow, State Management, Security, Configuration, and Testing maps

## Required content

- persistence/cache inventory with owner, technology, sensitivity, lifetime, and source-of-truth relationship
- key/file/store naming and isolation boundaries where useful
- read/write/update/delete/clear/invalidation behavior
- cache refresh, stale-data, offline, and fallback behavior where evidenced
- logout/account-switch/reset/destructive-data boundaries
- concurrency/queue/actor/context ownership where applicable
- file protection, backup/device-transfer, App Group/iCloud boundaries where applicable
- migration/schema/versioning/corruption/recovery behavior and gaps
- process termination/relaunch persistence expectations supported by evidence
- test evidence versus runtime/migration/backup/security gaps
- `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not assume Core Data, SwiftData, Keychain, iCloud, Realm, or another storage technology exists.
- Do not migrate storage technology, add encryption, change backup rules, clear data, or alter file locations.
- Do not claim sensitive data is secure merely because it is stored locally or in Keychain without the relevant configuration/runtime evidence.
- Do not infer server consistency, offline guarantees, or migration safety from client interfaces alone.
