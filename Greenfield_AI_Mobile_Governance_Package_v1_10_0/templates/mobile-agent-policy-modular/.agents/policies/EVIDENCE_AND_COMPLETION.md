# Evidence and Completion Policy

## 1. Evidence classes

Treat these as distinct:

- static inspection;
- compilation;
- lint/static analysis;
- unit tests;
- integration tests;
- migration tests;
- UI automation;
- previews;
- snapshots;
- simulator/emulator runtime;
- physical-device runtime;
- accessibility-service runtime;
- external-service or backend runtime;
- background/lifecycle runtime;
- performance, memory, and energy evidence;
- archive/package inspection;
- signing and release evidence.

One class does not automatically prove another.


## 1.1 Evidence timing and blocking scope

Every planned verification must declare one timing class:

- `TASK-CLOSURE` — necessary to prove the bounded task's immediate behavioral/architectural outcome.
- `FEATURE-CONVERGENCE` — cross-task integration/regression evidence executed after the feature is assembled.
- `FINAL-READINESS` — expensive platform/device/security/privacy/performance/manual-runtime evidence required before acceptance/release but not normally before ordinary task closure.

`bounded-feature-implementation` executes `TASK-CLOSURE` evidence only, unless the selected task explicitly owns a later gate or directly changes the protected boundary that makes earlier evidence necessary.

Evidence should run at the earliest stage where it is necessary, but not earlier.

Final-readiness closure occurs after convergence and before independent feature-readiness review. Use existing applicable platform runtime/accessibility/privacy/persistence/performance readiness procedures; do not create a new ceremonial skill solely for this gate. Update `READINESS_REPORT.md` with actual results and remaining limitations.

## 1.2 Evidence reuse and compact execution

- One valid artifact may satisfy multiple requirements or `VM-*` rows when it contains the required scenarios and is traceable to the current revision.
- Never rerun a test solely to create a unique artifact filename.
- Prefer one coherent test result bundle over many identical reruns when coverage is equivalent.
- Long-running verification should emit a compact summary (verdict, failing scenario, artifact path, limitations). Agents should not repeatedly poll or ingest full logs when exit status plus summary/artifact is sufficient.

## 1.3 Manual validation and representative matrices

Manual validation is preferred where automation adds high cost but weak extra confidence, including subjective visual fidelity, real screen-reader flow/focus, alternate-input ergonomics, representative RTL/adaptive quality, and physical-device-only checks. Record named device/runtime, steps, expected/actual result, artifact/notes, and limitation.

Manual validation must not replace deterministic automated proof for domain rules, transaction atomicity, idempotency/duplicate prevention, migration correctness, required navigation destinations, or mutation-to-consumer propagation.

Use a representative risk-based runtime matrix instead of the Cartesian product of every screen, state, locale, device, orientation, text size, and accessibility setting. Add configurations when feature risk or explicit product support requires them.

## 2. Required evidence record

Every completed task must identify:

- task and requirement;
- observable contract;
- evidence layer;
- command or procedure;
- environment or destination;
- expected result;
- actual result;
- artifact path;
- source revision;
- limitations;
- verdict.

Report only commands and sessions actually run.

## 3. Evidence validity

Evidence is invalid when:

- the path does not exist;
- it references a stale location;
- it predates material source corrections;
- it belongs to a different source revision;
- it does not exercise the claimed scenario;
- it relies on static evidence for runtime-only behavior;
- it omits environment or actual outcome;
- it claims a broader result than observed.

Regenerate evidence after material production changes.

## 4. Task completion

File, class, target, module, route, preview, screenshot, build, or test existence is not completion.

A task closes only when:

- all acceptance criteria are satisfied;
- prohibited scope is absent;
- required evidence exists;
- limitations are recorded;
- completion review passes;
- task checkboxes and status accurately reflect reality.

A task marked complete without matching evidence must be reopened.

## 5. Runtime-only claims

Compilation, previews, snapshots, and host tests do not prove applicable:

- process termination and relaunch;
- accessibility-service behavior;
- focus and announcements;
- adaptive resizing and multitasking;
- permissions and external entry points;
- background execution;
- device-only behavior;
- provider, billing, attestation, or backend behavior;
- signing, archive, or distribution.

Unsupported runtime layers remain `Needs verification`.

## 6. Persistence evidence

Where applicable, produce named evidence for:

- clean-store initialization;
- representative migration;
- failed-migration recovery;
- atomic multi-record operations;
- rollback;
- logical idempotency;
- duplicate prevention;
- stale-write behavior;
- date attribution;
- historical integrity;
- process termination and relaunch;
- isolated test stores.

## 7. Accessibility and adaptive evidence

Each required scenario must be recorded separately with environment, procedure, expected result, actual result, artifact, limitation, and verdict.

Applicable scenarios may include:

- screen-reader or TalkBack traversal;
- focus order and restoration;
- validation announcements;
- maximum text scaling;
- bold text or equivalent;
- non-color differentiation;
- contrast settings;
- reduced motion/transparency or equivalent;
- alternative input;
- RTL and mixed-direction text;
- long translations;
- compact and expanded layouts;
- resize and multitasking;
- keyboard/IME and safe areas/insets;
- state preservation across reflow.

A generic summary log cannot satisfy individually named acceptance criteria.

## 8. Production-fake evidence

Inspect applicable:

- source sets and targets;
- conditional compilation;
- dependency injection bindings;
- environment/configuration selection;
- test and preview dependencies;
- workers and schedulers;
- persistence implementation;
- package/archive contents;
- runtime initialization.

Allowed verdicts:

- `PASS`
- `FAIL — RELEASE FAKE OR BYPASS FOUND`
- `NEEDS VERIFICATION — BUILD COMPOSITION NOT PROVEN`

## 9. Documentation evidence

Documentation review must check:

- authority;
- currency;
- provenance;
- evidence limits;
- contradictions;
- approval and authorization language;
- historical proposals;
- canonical filenames;
- artifact paths;
- current lifecycle phase.

## 10. PR review

Review the complete coherent diff, not isolated files.

Cover:

- contract behavior;
- scope;
- architecture;
- lifecycle and concurrency;
- persistence;
- localization and RTL;
- accessibility;
- adaptation;
- privacy and protected boundaries;
- production integrity;
- documentation;
- evidence;
- unverified layers.

The review must not merge, publish, or self-approve.

## 11. Convergence output

The convergence record must include:

- files read;
- files changed;
- decisions applied;
- source corrections;
- commands run;
- test results;
- runtime scenarios;
- evidence paths;
- tasks closed;
- tasks still open;
- limitations;
- production-fake verdict;
- protected-boundary verdict;
- convergence verdict;
- readiness-review verdict.

## 12. Completion reporting

Every completion report states:

- scope;
- files changed;
- behavior affected;
- authorities applied;
- protected boundaries touched or untouched;
- exact commands/sessions;
- environments;
- expected and actual outcomes;
- evidence paths;
- documentation impact;
- architecture impact;
- blockers;
- limitations;
- remaining `Needs verification`;
- current verdict;
- what is not authorized.

If FINAL-READINESS manual evidence remains:
- convergence returns READY FOR FINAL READINESS;
- notify the user with only the pending check names and short PASS criteria;
- do not run feature-readiness-review until resolved.
