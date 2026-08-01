# Persistence and Cache map specification

## Checklist coverage

- Persistence, secure storage, cache, offline behavior, and migrations
- Destructive data handling and reset boundaries
- Backup, process-death, and consistency boundaries

## Discovery question

What data is persisted, cached, derived, or discarded, how are the two
Preferences DataStores keyed and scoped, and what migration, backup, failure,
offline, and consistency behavior is implemented or unverified?

## Required evidence

- progress and notebook repository contracts and implementations
- DataStore providers, qualifiers, filenames, and keys
- fake repositories
- Parent Settings reset/clear flows
- Android backup/data-extraction configuration
- manifest and application initialization
- DataStore repository tests and relevant ViewModel tests
- reviewed Data Flow, State Management, Notebook, Progress, Parent Settings,
  Architecture, and Testing pages

## Required content

- persisted data inventory and ownership
- progress/notebook key formats and independent stores
- write, replace, blank-removal, clear, and recreation behavior
- IOException fallback and other exception behavior
- cache/offline classification
- destructive action boundaries and confirmation ownership
- backup, restore, corruption, migration, app-upgrade, and process-death gaps
- security/sensitivity classification without inventing encryption requirements
- current JVM evidence versus Android runtime evidence

Record Room, cloud sync, image persistence, and settings DataStore as absent or
deferred, not as current architecture.
