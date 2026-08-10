# AGENTS.md — Common Mobile Repository Policy

> Reusable template. Replace or remove every bracketed value. This file must not be used to infer project facts.
>
> This repository may use this file as the constitution-equivalent stable-principles authority. If so, `AI_CONTEXT.md` and the owner decision register must say so explicitly. Do not create a duplicate constitution that repeats the same rules.

## 1. Authority and precedence

1. Current explicit task scope and accountable repository-owner direction.
2. Root `AGENTS.md` mandatory operating, safety, and stable-principles rules.
3. Approved owner decisions and current owner-approved feature contracts.
4. Approved product authority, architecture decisions, architecture spine, and design contracts.
5. Verified implementation plus matching test, runtime, external-service, archive, and release evidence.
6. `AI_CONTEXT.md` for routing, current phase, canonical paths, and evidence status.
7. `AI_PLAYBOOK.md`, repository templates, and installed skills as mandatory procedures where routed.
8. Imported vendor guidance and model suggestions.

Skills explain how to work; they do not authorize work. Templates shape artifacts; they do not establish project facts. Unresolved conflicts are `Needs verification` or `Needs owner decision` and block any slice that would encode an arbitrary choice.

## 2. Project mode, scope, and evidence boundary

- Mode: [greenfield / brownfield].
- Product: [fill in].
- Platforms and supported form factors: [fill in].
- Approved product-behavior source: [fill in].
- Feature-input path: [fill in].
- Feature-contract path pattern: `docs/features/<feature-id>/FEATURE_CONTRACT.md`.
- Implementation-plan path pattern: `docs/features/<feature-id>/IMPLEMENTATION_PLAN.md`.
- Implementation-task path pattern: `docs/features/<feature-id>/IMPLEMENTATION_TASKS.md`.
- Feature-readiness path pattern: `docs/features/<feature-id>/READINESS_REPORT.md`.
- Accountable owner(s): [fill in].
- Constitution-equivalent authority: [AGENTS.md / another approved path].
- Initial locales and fallback: [fill in].
- Release channels: [fill in].

Current source and configuration describe implementation only. Tests prove only their assertions. Compilation, previews, snapshots, host tests, simulator/emulator runs, physical-device runs, external-service checks, archive inspection, and release evidence are distinct evidence classes. Runtime, accessibility, backend, security, privacy, performance, signing, distribution, and release claims require matching evidence.

## 3. Canonical lifecycle

The repository uses this controlled feature-delivery sequence:

1. Governance initialization and authority routing.
2. Product input and design authority.
3. Cross-feature architecture and accepted ADRs.
4. Feature input.
5. Feature-contract authoring.
6. Independent feature-contract review.
7. Repository-owner feature-contract approval.
8. Implementation-plan authoring.
9. Independent implementation-plan review.
10. Repository-owner implementation-plan approval.
11. Implementation-task authoring.
12. Independent implementation-task review.
13. Repository-owner task-set approval.
14. Pre-implementation readiness review.
15. Explicit implementation authorization.
16. Dependency-ordered implementation.
17. Task-level verification and evidence closure.
18. Feature implementation convergence.
19. Canonical `READINESS_REPORT.md`.
20. Independent feature-readiness review.
21. Repository-owner feature acceptance.
22. Separate release authorization.
23. Archive, signing, distribution, release verification, and post-release learning.

No stage silently authorizes the next protected stage. In particular:

- contract approval does not authorize planning or implementation by itself;
- plan approval does not authorize task execution;
- task approval does not authorize implementation;
- implementation completion does not establish feature acceptance;
- feature acceptance does not authorize release, signing, or distribution.

## 4. Working rules

- Start from [base branch] and use one focused task branch. Never work directly on protected branches.
- Load only task-relevant current context through `AI_CONTEXT.md`; do not scan the whole repository by default.
- Do not invent requirements, decisions, verification results, commands, files, owners, runtime behavior, dependency versions, support claims, evidence, or approval.
- Keep unrelated worktree changes visible. Never hide, reset, discard, rewrite, or absorb them without explicit authorization.
- Add dependencies, frameworks, modules, targets, environments, services, capabilities, or architecture patterns only with explicit scope and a recorded decision when they change the architecture surface.
- Keep product behavior in feature contracts, technical choices in implementation plans and ADRs, bounded executable obligations in implementation tasks, and operational policy in `AGENTS.md`.
- Do not create production code, tests, schemas, migrations, targets, or project files while authoring contracts, plans, or tasks.
- Do not reopen accepted architecture during task implementation unless the approved plan contains an explicit decision task.
- Do not preserve future-feature placeholders, dead routes, no-op workers, unused template models, dormant production bindings, or release-path stubs merely because they may be useful later. Future work must be reintroduced through approved scope. Configuration files may be retained for later features only when their repository location, target membership, initialization behavior, and protected-boundary status are explicit.

## 5. Governance consistency

Before planning, task generation, implementation, convergence, feature acceptance, and release review, verify that current feature contracts, implementation plans, implementation tasks, owner decisions, accepted ADRs, architecture maps, design authority, `AI_CONTEXT.md`, readiness gates, and authorization records do not contradict one another.

A stale or contradictory current artifact blocks the affected work. Typical blockers include:

- conflicting implementation-authorization status;
- stale persistence or feasibility-spike status;
- mismatched canonical task filenames;
- evidence paths that do not exist;
- a context router describing an earlier lifecycle phase;
- an architecture coverage matrix that contradicts an accepted ADR;
- a task marked complete without matching evidence.

Accepted amendments must be incorporated into canonical authority documents. Historical proposals must be clearly marked `Superseded — historical only` and must not remain implementation-authoritative.

## 6. Cross-feature architecture impact

Before finalizing a plan or implementation that introduces or changes a cross-cutting concern, determine whether the architecture spine, ADRs, decision register, architecture-coverage matrix, readiness gates, and context routing remain accurate.

Consider:

- project, module, target, and package boundaries;
- dependency direction and composition;
- presentation state and lifecycle;
- concurrency and cancellation;
- navigation and restoration;
- persistence, migrations, backup, transfer, and deletion;
- adaptive UI, supported surfaces, localization, RTL, and accessibility;
- background execution, notifications, workers, widgets, extensions, and external entry points;
- permissions, capabilities, manifests, entitlements, and exported components;
- configuration, environments, feature flags, analytics, privacy, and observability;
- authentication, authorization, billing, entitlement, and regulated behavior;
- external services, attestation, secrets, and network boundaries;
- performance, memory, energy, startup, and scalability;
- build, CI, signing, archive, release, and testability.

Use `AI_CONTEXT.md` to select only relevant current documents. Do not create empty architecture documents or ADRs automatically. Record unsupported or owner-dependent claims as `Needs verification` or `Needs owner decision`.

## 7. Documentation impact

Run `documentation-impact-assessment` before finalizing relevant plans and again after implementation.

Changed-path routing is only a candidate signal. Documentation edits require authority and must not overstate the review actually performed.

After implementation, synchronize at least the applicable:

- implementation-task status and evidence references;
- `READINESS_REPORT.md`;
- `AI_CONTEXT.md` current phase and authorized next actions;
- architecture-coverage matrix;
- evidence index;
- known limitations;
- owner decision register;
- ADRs only when a technical decision changed;
- feature contract only when approved observable behavior changed;
- implementation plan only when an approved technical change altered the plan.

Run `documentation-review` or the repository-equivalent procedure before feature acceptance.

## 8. Protected boundaries

Treat the following as protected unless the repository explicitly narrows or extends the list:

- identity, authentication, authorization, and entitlement;
- secrets, keys, tokens, certificates, and production configuration;
- user data, sensitive data, destructive persistence, deletion, backup, and transfer;
- public APIs, backend contracts, provider schemas, and externally visible identifiers;
- permissions, platform capabilities, manifests, entitlements, exported components, app links, and external entry points;
- background execution, notifications, workers, extensions, and scheduled operations;
- signing, provisioning, release credentials, distribution, and store publication;
- financial, billing, medical, health, regulated, child-safety, and privacy-sensitive behavior;
- analytics, tracking, crash reporting, telemetry, and raw-data logging;
- external AI, attestation, provider access, and client-visible configuration.

Invoke `protected-boundary-preflight` before protected work. Missing protected configuration must fail closed into an explicit unavailable, recoverable, queued, or approved local/manual-fallback state. A framework import, dependency declaration, configuration file, manifest entry, or entitlement does not itself authorize use.

## 9. Feature-contract rules

Feature contracts must:

- remain bounded by the approved feature input;
- distinguish explicitly in-scope behavior, strictly necessary supporting behavior, later-feature behavior, exclusions, and clarification candidates;
- source every observable validation rule, required-field rule, range, uniqueness rule, destructive threshold, date rule, decimal policy, exact copy requirement, and save-eligibility condition;
- describe observable product behavior rather than selecting UI frameworks, state-holder APIs, persistence engines, schemas, DI frameworks, SDK classes, or test frameworks;
- define failure, recovery, offline, cancellation, destructive, durability, adaptive, localization, RTL, accessibility, privacy, and evidence outcomes where applicable;
- map screens to approved screen contracts and exact design artifacts;
- exclude unsupported artifact content;
- state evidence obligations without claiming evidence already exists;
- remain unapproved and implementation-unauthorized until the repository owner decides.

## 10. Implementation-plan rules

Implementation plans must:

- require an owner-approved feature contract and closed material product clarifications;
- apply accepted ADRs without silently selecting alternatives;
- separate domain, presentation, data, platform, navigation, and host ownership;
- define dependency composition, state ownership, lifecycle, concurrency, cancellation, persistence, migrations, restoration, protected boundaries, testing, and runtime evidence;
- map every planned component to contract requirements;
- map every screen to exact design authority;
- define adaptive, localization, RTL, accessibility, failure, recovery, offline, and destructive behavior;
- define dependency order only, not implementation tasks, assignments, estimates, or code;
- record unresolved technical decisions honestly;
- never claim implementation authorization.

## 11. Implementation-task rules

Implementation tasks must:

- be generated only from an owner-approved contract and owner-approved implementation plan that passed independent review;
- define one bounded, independently reviewable outcome;
- form an explicit acyclic dependency graph;
- trace to contract requirements, plan sections, and architecture/design authority;
- state allowed scope and prohibited scope;
- name acceptance criteria, verification layer, exact procedure or command, environment, artifact path, limitation, and stop condition;
- include localization, approved RTL locales, accessibility, adaptive behavior, lifecycle, persistence integrity, privacy, production composition, documentation, and evidence as first-class work;
- not reopen accepted architecture;
- not create giant “implement feature” tasks or trivial evidence-free tasks;
- remain non-executable until explicit implementation authorization is granted.

## 12. Implementation authorization

Implementation may begin only when:

- the feature contract is owner-approved;
- the implementation plan is owner-approved and independently reviewed;
- the task set is owner-approved and independently reviewed;
- applicable readiness gates are `PASS` or explicitly owner-authorized `N/A`;
- material contradictions are resolved;
- implementation authorization is explicitly recorded.

Authorization must have one canonical record. Copies in plans, tasks, context routing, and readiness reports must remain synchronized.

## 13. Implementation rules

During implementation:

- execute one coherent task slice at a time;
- preserve contract and plan boundaries;
- stop on architecture drift, protected-boundary drift, unsupported product behavior, or missing authority;
- use the approved composition path and state ownership model;
- keep hosts thin and leaf UI free of infrastructure dependencies;
- use structured lifecycle-owned asynchronous work;
- keep production composition free of fakes, previews, test bindings, no-op mechanisms, and silent simulated success;
- update evidence as each task closes rather than deferring all proof to the end;
- do not tick task completion gates until acceptance criteria and evidence are actually satisfied.

## 14. Testing and verification

- Use the repository-approved test stack unless a testing-strategy decision authorizes a change.
- Choose the smallest useful test layer that proves the required contract.
- Every task must name a concrete observable scenario and expected result, not only an evidence category.
- A completed task must cite an actual evidence artifact, command or session, environment, expected result, actual outcome, and limitations.
- Report only commands actually run and exact results.
- Do not claim device, backend, accessibility, security, performance, lifecycle, persistence, background, signing, archive, or release behavior from static or unit evidence alone.
- Evidence paths must exist and correspond to the final source revision. Stale or pre-correction artifacts cannot prove final readiness.
- Previews and snapshots are development or bounded visual evidence only. They do not prove runtime behavior.
- A task marked complete without matching evidence must be reopened.

## 15. Post-implementation convergence

Completion of implementation tasks does not establish feature completion.

After implementation, run `feature-implementation-convergence` or the repository-equivalent procedure. It must verify:

1. task completion integrity;
2. contract-to-implementation traceability;
3. scope fidelity and absence of later-feature drift;
4. plan and architecture conformance;
5. exact design conformance;
6. lifecycle, state, concurrency, cancellation, navigation, and restoration;
7. persistence, migrations, rollback, idempotency, relaunch, date attribution, backup, and deletion where applicable;
8. localization, approved RTL locales, formatting, and hardcoded-string prevention;
9. accessibility and adaptive runtime evidence;
10. privacy, permissions, capabilities, external transfer, and protected-boundary integrity;
11. production-fake detection and release-composition hygiene;
12. current automated, runtime, external-service, archive, and release evidence;
13. documentation synchronization;
14. coherent-diff PR review.

Allowed convergence verdicts:

- `READY FOR FEATURE READINESS REVIEW`
- `BLOCKED BY IMPLEMENTATION DEFECT`
- `BLOCKED BY ARCHITECTURE DRIFT`
- `BLOCKED BY SCOPE DRIFT`
- `BLOCKED BY MISSING EVIDENCE`
- `NEEDS VERIFICATION`

A convergence verdict does not approve the feature or authorize release.

## 16. Feature readiness and owner acceptance

Create or update:

`docs/features/<feature-id>/READINESS_REPORT.md`

The report must include:

- approvals and authorization state;
- implemented and excluded scope;
- task completion summary;
- contract coverage;
- plan and architecture conformance;
- automated-test results;
- runtime evidence;
- persistence and data-integrity evidence;
- localization and RTL evidence;
- accessibility evidence;
- adaptive/window/device evidence;
- privacy and protected-boundary evidence;
- production-fake verdict;
- documentation synchronization;
- PR-review result;
- known limitations and unverified claims;
- owner decisions required;
- final readiness verdict.

Run an independent `feature-readiness-review` or equivalent procedure.

Allowed review verdicts:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

`PASS` means ready for repository-owner feature acceptance only.

The repository owner may then accept, reject, or require correction. Owner feature acceptance must be recorded in the readiness report or another canonical acceptance record.

## 17. Release authorization and publishing

Feature acceptance does not authorize release.

Release work requires separate explicit authorization before any protected side effect involving:

- production signing or certificates;
- provisioning or entitlements;
- archive/export;
- TestFlight, App Store Connect, Play Console, internal testing, staged rollout, or production publication;
- release credentials;
- production configuration;
- store metadata;
- remote upload, promotion, rollout, or publication.

Publishing is two-stage:

1. read-only preparation and evidence;
2. separate explicit approval for remote side effects.

Never merge, auto-merge, force-push, bypass failed checks, expose credentials, or publish without authorization.

## 18. Review requirements

- Run independent review for contracts, plans, tasks, feature readiness, and release readiness where applicable.
- Invoke `pr-review` for the coherent target-branch diff before readiness is declared.
- Review findings must distinguish blockers, major findings, minor findings, questions, test gaps, and unverified runtime layers.
- Review procedures must not merge, publish, self-approve, or grant owner authorization.

## 19. Required repository procedures

The repository must install or provide equivalent procedures for:

- feature-contract authoring and review;
- implementation-plan authoring and review;
- implementation-task authoring and review;
- architecture readiness;
- project-structure readiness;
- localization and RTL readiness;
- adaptive and accessibility readiness;
- persistence and migration readiness;
- privacy and protected-boundary readiness;
- runtime-evidence readiness;
- production-fake detection;
- documentation-impact assessment and documentation review;
- PR review;
- feature implementation convergence;
- feature readiness review.

A missing required procedure, or a `Blocked`, `Fail`, `Not ready`, or equivalent verdict, stops the affected work unless the accountable owner explicitly authorizes a narrower non-blocked slice.

## 20. Completion contract

For every completed task or review, report:

- scope;
- files changed;
- behavior affected;
- authorities read;
- contract, plan, task, architecture, and design references;
- protected boundaries touched or confirmed untouched;
- tests and checks actually run;
- exact commands or sessions;
- environments and destinations;
- expected and actual outcomes;
- evidence artifacts;
- documentation-impact classification;
- architecture-coverage impact;
- known blockers;
- remaining `Needs verification` items;
- owner and next evidence step;
- current lifecycle verdict;
- explicit statement of what is not authorized.
