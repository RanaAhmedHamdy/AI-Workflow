---
name: swift-concurrency-readiness
description: Audits Swift concurrency, actor isolation, Sendable correctness, cancellation, and async bridging.
---

# Swift Concurrency Readiness

Check:

- approved Swift language mode and strict-concurrency settings;
- main-actor ownership of UI-observable state;
- actor isolation for stores, caches, clients, and mutable services;
- `Sendable` correctness across isolation boundaries;
- cancellation propagation;
- structured versus detached tasks;
- continuation exactly-once resumption;
- delegate/callback bridging;
- reentrancy, ordering, idempotency, and duplicate side effects;
- async sequence lifetime;
- background expiration handling;
- typed error mapping and bounded terminal states.

Fail when:

- `@unchecked Sendable` lacks documented invariants/tests;
- broad `@MainActor` is used only to silence diagnostics;
- detached/unstructured tasks escape lifecycle ownership;
- continuations can resume zero or multiple times;
- compiler settings are weakened without migration authorization.

Output exact findings and verdict.
