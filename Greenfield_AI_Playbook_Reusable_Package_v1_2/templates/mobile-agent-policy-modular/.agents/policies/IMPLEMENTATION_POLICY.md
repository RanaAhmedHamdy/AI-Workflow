# Implementation Policy

## 1. Working model

- Use one focused branch from the approved base branch.
- Keep unrelated changes visible.
- Do not hide, reset, discard, or rewrite unrelated work without authorization.
- Load only task-relevant current context through `AI_CONTEXT.md`.
- Implement only explicitly authorized tasks.
- Execute one coherent task slice at a time.
- Stop on authority, scope, architecture, design, or protected-boundary drift.

## 2. Separation of concerns

- Product behavior belongs in feature contracts.
- Technical mechanisms belong in plans and ADRs.
- Executable obligations belong in implementation tasks.
- Operational rules belong in repository policy.
- Runtime and release claims belong in evidence and readiness records.

Do not modify contracts merely to match an implementation mistake. Do not modify ADRs unless an approved technical decision changed.

## 3. Architecture conformance

Implementation must preserve applicable:

- module, target, package, and source-set boundaries;
- dependency direction;
- composition root;
- state ownership;
- lifecycle and concurrency ownership;
- navigation ownership;
- persistence boundaries;
- external-service boundaries;
- platform host thinness;
- design-system ownership;
- testability and release composition.

Do not introduce service locators, hidden globals, ad hoc dependency construction, UI-layer infrastructure access, broad unreviewed abstractions, or architecture changes without authority.

## 4. Cross-feature impact

Before finalizing changes that affect a cross-cutting concern, determine whether these remain current:

- architecture spine;
- ADRs;
- decision register;
- architecture-coverage matrix;
- readiness gates;
- `AI_CONTEXT.md`;
- project structure;
- CI and evidence paths;
- release rules.

Consider:

- lifecycle and state;
- concurrency;
- persistence and migration;
- adaptive UI;
- localization and RTL;
- accessibility;
- background work;
- permissions and capabilities;
- configuration and environments;
- analytics and observability;
- performance, memory, and energy;
- security and privacy;
- build, release, and testability.

Do not create empty architecture artifacts automatically.

## 5. Production integrity

Production code and release composition must not contain or silently select:

- fake repositories or providers;
- manufactured success;
- fixed successful identifiers;
- accept-all validation;
- placeholder authorization;
- no-op migrations, workers, schedulers, or lifecycle handling;
- in-memory substitutes for required durable state;
- preview or test dependencies;
- debug bypasses;
- dead routes;
- unused template models;
- future-feature placeholders;
- silent fallback from unavailable infrastructure to fake success.

Future configuration may remain in the repository only when its location, build inclusion, initialization behavior, privacy impact, authority, and inactive status are explicit.

## 6. Async and lifecycle ownership

Every asynchronous operation must define:

- owner;
- lifetime;
- cancellation;
- isolation or threading;
- terminal states;
- error mapping;
- duplicate-invocation behavior;
- durability expectations.

Presentation-scoped work should be lifecycle-owned. Durable work must not be cancelled merely because UI disappears.

## 7. Persistence integrity

Where applicable, implementation must preserve:

- system of record;
- schema/version ownership;
- migration and recovery;
- atomicity and rollback;
- logical idempotency;
- stale-write handling;
- date attribution;
- historical integrity;
- process termination and relaunch;
- backup, transfer, protection, deletion, and cache behavior;
- test-store isolation.

## 8. UI and design fidelity

User-facing implementation must:

- trace to approved design authority;
- implement material loading, empty, failure, recovery, disabled, and success states;
- preserve state across supported adaptation and lifecycle changes;
- keep required actions reachable;
- avoid hardcoded strings and hardcoded left/right assumptions;
- meet accessibility semantics, focus, scaling, motion, and non-color requirements;
- not treat previews or snapshots as runtime proof.

## 9. Documentation impact

Run `documentation-impact-assessment` before finalizing relevant plans and again after implementation.

After implementation, synchronize applicable:

- task status and evidence references;
- readiness report;
- `AI_CONTEXT.md` current phase;
- architecture coverage;
- evidence index;
- limitations;
- owner decisions;
- ADRs only when decisions changed;
- feature contract only when approved observable behavior changed;
- implementation plan only when an approved technical change altered it.

## 10. Review

Before readiness is declared:

- review the coherent diff against the target branch;
- run applicable platform and cross-cutting readiness procedures;
- run production-fake detection;
- run documentation review;
- record blockers, major findings, minor findings, test gaps, and unverified runtime layers;
- do not merge or publish.
