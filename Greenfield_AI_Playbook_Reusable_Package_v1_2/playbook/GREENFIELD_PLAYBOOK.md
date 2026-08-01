# AI Greenfield Project Playbook — Mobile Generic v1.2

**Reusable specification-driven workflow for native Android and iOS teams**

**Define intent. Validate architecture. Build vertical slices. Verify reality. Publish evidence.**

This is the repository-operational Markdown edition of the human-readable Greenfield playbook. Material lifecycle or governance changes should be applied to both editions in the same release. Project-specific facts and decisions belong in the target repository, not in this reusable master.

---

# 1. Purpose and operating philosophy

This playbook is for new native Android and iOS products, major new applications, and genuinely new product surfaces where the team can establish architecture, design, testing, delivery, and AI-governance rules before legacy constraints dominate. It is specification-driven, evidence-aware, and human-controlled.

The central rule is:

> Do not let implementation outrun an agreed specification, architecture, or verification plan.

Greenfield does not mean “no risk.” It means that many risks are still choices. The workflow therefore makes choices explicit before they become expensive code, while still producing a working vertical slice early enough to expose mistaken assumptions.

The reusable order is:

```text
project principles
    -> product outcomes
    -> specification
    -> clarification
    -> experience/design direction
    -> technical plan
    -> cross-feature architecture coverage
    -> requirements checklist
    -> dependency-ordered tasks
    -> cross-artifact analysis
    -> walking skeleton
    -> bounded implementation slices
    -> convergence
    -> runtime/release verification
    -> explicit publication and human review
```

## 1.1 What “complete” means

A greenfield phase is complete only when its required artifacts are reviewable, contradictions are resolved or explicitly deferred, and the next phase can proceed without guessing about material behavior.

A feature is complete when:

- intended user behavior is present in the approved specification;
- architecture and platform constraints are reflected in the plan;
- implementation tasks trace to the spec and plan;
- relevant tests and runtime checks were actually executed;
- adaptive layout, localization, accessibility, privacy, security, performance, analytics, and release implications were addressed when applicable;
- implementation and specification converge;
- remaining uncertainty is owned, classified, and not hidden inside “done.”

## 1.2 Evidence and authority categories

| Category | Meaning | Allowed conclusion |
|---|---|---|
| Product decision | Approved behavior or business rule from an accountable owner | Defines intended behavior, not implementation correctness |
| Specification contract | Reviewed `spec.md` and accepted clarifications | Defines the functional contract within its stated scope |
| Technical decision | Reviewed plan, ADR, or constitution-backed decision | Defines an approved implementation direction |
| Design authority | Approved design-system or screen-flow evidence | Defines visual/interaction intent within the approved design scope |
| Test evidence | Named command or test actually ran and passed | Supports only the asserted behavior and environment |
| Runtime/device evidence | Observed on an approved simulator, emulator, or device | Supports the tested scenario and platform configuration |
| Release evidence | Built, signed, inspected, distributed, or store-stage evidence | Supports the exact artifact and release stage |
| Needs verification | Evidence is absent, stale, conflicting, or owner-dependent | Do not guess or convert it into a hidden default |

## 1.3 Authority model

Use this order when instructions conflict:

1. The current explicit task and accountable owner direction.
2. Root `AGENTS.md` mandatory policy and protected boundaries.
3. Approved product requirements and current Spec Kit feature artifacts.
4. Approved architecture decisions, design-system contracts, and platform constraints.
5. Current implementation and verification evidence.
6. `AI_CONTEXT.md` for context routing.
7. This playbook and repository skills as reusable procedures.
8. Imported vendor/platform skills as lower-authority guidance.

A skill explains how to work. It does not authorize the work.

---

# 2. Canonical greenfield lifecycle

| Phase | Main activity | Primary deliverable |
|---|---|---|
| 0 | Safe initialization and governance | Repository, branch policy, `AGENTS.md`, Spec Kit setup, protected boundaries, tool policy |
| 0.5 | Project constitution | `.specify/memory/constitution.md` and reviewable mandatory principles |
| 1 | Product framing and outcome discovery | Product brief, actors, journeys, success measures, constraints, non-goals |
| 1.5 | Experience exploration and design direction | Approved flow direction, design authority, design-system seed, prototype evidence |
| 2 | Feature specification | Spec Kit `spec.md` describing what and why |
| 2.5 | Clarification and requirements quality | Recorded clarifications, acceptance scenarios, specification checklist |
| 3 | Technical planning and architecture | Spec Kit `plan.md`, research, data model, contracts, architecture maps, ADRs |
| 3.4 | Cross-feature architecture coverage gate | Complete classification of all applicable architecture concerns |
| 4 | Task decomposition and consistency analysis | `tasks.md`, dependency order, `/speckit.analyze` clean or accepted findings |
| 4.5 | Implementation readiness audit | No-edit traceability, test plan, design handoff, protected-boundary approval |
| 5 | Walking skeleton and first vertical slice | Buildable app, navigation shell, one end-to-end slice, baseline CI and observability |
| 6 | Iterative feature implementation | Bounded Spec Kit implementation slices with tests and reviews |
| 7 | Expanded safety net and integration verification | Domain, UI, integration, contract, platform, and E2E evidence |
| 8 | Product and platform hardening | Accessibility, adaptive UI, localization, performance, security, privacy, resilience |
| 9 | Delivery and release verification | CI/CD, signing, artifacts, environments, store/release evidence |
| 10 | AI-assisted review and controlled publication | Diff review, documentation impact, explicit push/MR, no auto-merge |
| 11 | Launch, telemetry, and operational verification | Rollout, dashboards, crash/analytics validation, support readiness |
| 12 | Lessons, reusable assets, and handoff | Updated playbook lessons, templates, skills, ownership, maintenance plan |

## 2.1 Two execution tracks

### Standard product slice

Use when the feature is low-risk, fully specified, and does not alter protected or organization-wide architecture.

```text
specify -> clarify -> plan -> checklist -> tasks -> analyze
-> bounded implement -> focused tests -> converge -> review -> publish
```

### Decision-sensitive slice

Use when the work affects authentication, personal data, financial behavior, permissions, notifications, background execution, storage schema, public API contracts, analytics/privacy, signing, certificates, release configuration, or unresolved platform behavior.

```text
evidence -> owner questions -> decision capture -> plan/ADR update
-> protected-boundary preflight -> tasks -> analyze -> one authorized slice
-> focused verification -> converge -> review -> publish
```

---

# 3. Tool roles and boundaries

## 3.1 Spec Kit — workflow backbone

Use Spec Kit as the primary specification-driven artifact pipeline. Pin and verify the installed version. Do not assume every agent exposes identical command syntax; slash commands may appear as skills in some clients.

Recommended high-assurance sequence:

```text
/speckit.constitution
/speckit.specify
/speckit.clarify
/speckit.plan
/speckit.checklist
/speckit.tasks
/speckit.analyze
/speckit.implement
/speckit.converge
```

Use the commands as artifact generators and quality gates, not as an authorization system. Human review remains required at phase transitions.

### Spec Kit artifact ownership

| Artifact | Owns |
|---|---|
| `constitution.md` | durable project principles and mandatory engineering constraints |
| `spec.md` | intended user-visible behavior, actors, scenarios, acceptance outcomes, non-goals |
| `plan.md` | technical approach, platform choices, structure, constraints, research conclusions |
| `tasks.md` | dependency-ordered implementation work traceable to spec and plan |
| checklists | requirement quality and completeness questions, not test execution evidence |
| analyze report | cross-artifact gaps and contradictions; read-only findings |
| converge output | implementation-to-artifact completion gaps and newly appended work |

## 3.2 Stitch or similar generative design tool — optional exploration

Use Stitch-like design generation only during early experience exploration when the team needs rapid alternatives, flow sketches, or visual direction before a design source of truth exists.

Appropriate uses:

- explore competing screen structures;
- generate discussion prototypes from product scenarios;
- test information hierarchy and flow ideas;
- create disposable visual options for designer/product review;
- seed a design conversation before Figma or another authoritative design system exists.

Do not treat generated screens or generated front-end code as approved product requirements, accessibility evidence, platform architecture, or production-ready implementation. Promote only reviewed decisions into `spec.md`, the design authority, or the technical plan.

## 3.3 Figma MCP — authoritative design context when Figma is the source of truth

Use Figma MCP after the design team has established approved files, components, variables, auto-layout behavior, and screen states. It is most useful in Phases 1.5, 3, 4.5, 6, and 8.

Use it to:

- retrieve approved frames, components, variants, variables, and layout constraints;
- compare implementation against the design system;
- map design components to repository components and Code Connect where available;
- inspect loading, empty, error, disabled, permission, and localization states;
- write reviewed design content only when the project explicitly authorizes write-to-canvas workflows.

Never infer product behavior solely from a frame. A design file does not replace acceptance criteria, backend contracts, platform rules, or runtime evidence.

## 3.4 Graphify — optional code graph after meaningful source exists

Graphify is not required during blank-repository planning. It becomes useful after the project has a walking skeleton, imported foundations, generated modules, or enough source to form a meaningful dependency graph.

Recommended timing:

- **Phase 3:** optional when an existing organization starter, SDK, monorepo, or generated baseline already contains substantial code;
- **Phase 5:** build the first useful graph after the walking skeleton and foundational modules exist;
- **Phase 6:** query impact paths before cross-feature changes or module extraction;
- **Phase 10:** use graph-aware PR impact and overlap checks as supplementary review evidence;
- **Phase 12:** regenerate the graph after material architecture changes.

Use Graphify to answer structural questions such as module dependencies, callers, feature ownership, shortest dependency paths, and potential change impact. Treat graph edges as derived evidence that must be checked against source when the conclusion is material. Do not commit generated graph output unless the repository explicitly chooses to version it.

## 3.5 Tool selection rule

```text
Need product intent?              -> Spec Kit spec and accountable owners
Need design exploration?          -> Stitch-like tool, optional and disposable
Need approved design context?      -> Figma MCP or approved design source
Need source dependency insight?    -> Graphify after meaningful source exists
Need platform truth?               -> current official platform documentation
Need implementation authorization? -> current task + AGENTS.md + approved decisions
```

---

# 4. Phase 0 — Safe initialization and governance

## Goal

Create a repository where specifications, implementation, review, and publication are controlled before feature code begins.

## Required outputs

- initialized repository and integration branch strategy;
- root `AGENTS.md` assembled from `AGENTS.common.md` plus the selected greenfield platform overlay;
- `AI_CONTEXT.md` routing index;
- `AI_PLAYBOOK.md` task workflow summary;
- Spec Kit initialized and version recorded;
- protected-boundary list;
- canonical skill and adapter structure;
- branch, commit, review, and publication rules;
- hooks policy and deterministic shared scripts;
- documentation-impact workflow;
- initial CI skeleton or explicit CI plan.

## Execution

1. Create the repository and establish protected branches.
2. Initialize Spec Kit with the selected agent integration.
3. Record the installed Spec Kit version and upgrade policy.
4. Assemble one root `AGENTS.md`; do not leave competing platform templates active.
5. Establish `.agents/skills/` as canonical project skills and separate imported vendor content.
6. Define which files contain secrets, signing material, production configuration, or personal data.
7. Define local hooks as reminders or deterministic checks only. Hooks must not silently publish, merge, authorize protected changes, or replace CI.
8. Establish focused branches and explicit remote-side-effect approval.
9. Create `AI_CONTEXT.md` with placeholders for future product, design, architecture, feature, testing, and release documents.
10. Decide whether design authority will be Figma, another design system, or repository-owned design documentation.
11. Decide whether Graphify will be adopted later; do not create an empty graph simply to satisfy the playbook.

## Quality gate

- The repository has one authority model.
- Spec Kit runs and its version is known.
- Agent instructions do not conflict.
- Remote publication requires explicit approval.
- Secrets and release boundaries are protected.
- Hooks and skills are advisory or deterministic, not hidden authorities.

---

# 5. Phase 0.5 — Project constitution

## Goal

Create durable principles before feature specifications and technical choices begin.

Run `/speckit.constitution` and review the result manually.

## Constitution topics

- product quality and acceptance discipline;
- platform support and minimum OS policy;
- native UI and architecture direction;
- adaptive layout and supported form factors;
- localization and accessibility requirements;
- privacy and data minimization;
- security and protected boundaries;
- state and concurrency rules;
- dependency and architecture-change policy;
- test pyramid and evidence rules;
- performance budgets and startup expectations;
- analytics, crash reporting, and observability boundaries;
- CI, review, release, and publication controls;
- documentation and specification maintenance;
- exceptions and decision-record requirements.

## Rule

The constitution should contain stable principles. Feature-specific behavior belongs in `spec.md`; implementation details belong in `plan.md`; project-specific operational rules belong in `AGENTS.md`.

## Quality gate

- Every mandatory principle is testable, reviewable, or tied to a named decision process.
- The constitution does not contain placeholders presented as decisions.
- Android and iOS rules match the chosen target platform and minimum OS.
- Existing starter defaults have been confirmed, replaced, or removed.

---

# 6. Phase 1 — Product framing and outcome discovery

## Goal

Define the product problem and success boundaries before creating detailed features.

## Required artifacts

| Artifact | Purpose |
|---|---|
| `PRODUCT_BRIEF.md` | problem, target users, value proposition, scope, non-goals |
| `ACTORS_AND_JOURNEYS.md` | actors, primary journeys, edge journeys, support journeys |
| `SUCCESS_MEASURES.md` | product and operational outcomes, measurement ownership |
| `DOMAIN_GLOSSARY.md` | shared terminology and disputed terms |
| `CONSTRAINTS.md` | legal, privacy, commercial, platform, schedule, integration constraints |
| `RISKS_AND_ASSUMPTIONS.md` | assumptions requiring validation and early risk experiments |

## Execution

1. Separate outcomes from proposed screens.
2. Identify the first releasable product slice and explicit non-goals.
3. Record data categories, identity model, payments, regulated behavior, and external integrations early.
4. Identify assumptions that require prototypes, backend confirmation, user research, or legal/security review.
5. Define analytics only after product outcomes and privacy boundaries are understood.
6. Do not choose architecture merely because a starter template provides it.

## Quality gate

- A reviewer can explain who the product serves and which problem the first release solves.
- Non-goals are explicit.
- Material assumptions have owners.
- Success measures do not require unauthorized data collection.

---

# 7. Phase 1.5 — Experience exploration and design direction

## Goal

Turn product journeys into reviewed interaction direction without allowing visual prototypes to become hidden requirements.

## Tool routing

### Use Stitch-like tools when

- no authoritative design exists;
- the team needs rapid alternatives;
- outputs are explicitly exploratory;
- a designer/product owner will review and promote selected decisions.

### Use Figma MCP when

- Figma is the approved design authority;
- components, variables, and flows already exist;
- the agent needs precise layout/design-system context;
- implementation will map to approved components.

## Required outputs

- information architecture and navigation concept;
- key user flows and state diagrams;
- design-system seed: color, typography, spacing, elevation, motion, icon, and component principles;
- compact and expanded layout direction when applicable;
- accessibility and localization assumptions;
- required screen states: loading, empty, error, offline, permission denied, disabled, success;
- design authority declaration;
- prototype decision log showing what was accepted, rejected, or left exploratory.

## Quality gate

- Prototypes do not contain unreviewed product rules.
- Every accepted design behavior is reflected in the specification or a design contract.
- Responsive/adaptive behavior is represented, not inferred from a single phone frame.
- Accessibility and localization are included before implementation.

---

# 8. Phase 2 — Feature specification with Spec Kit

## Goal

Describe what the feature must do and why, without prematurely choosing the implementation.

Run `/speckit.specify` for each bounded feature or release slice.

## Specification content

- actors and preconditions;
- prioritized user stories;
- acceptance scenarios;
- success, error, empty, offline, permission, and recovery behavior;
- data visible to the user;
- privacy and consent behavior;
- analytics requirements only when approved;
- localization and accessibility behavior;
- supported platforms and form factors;
- non-functional outcomes expressed as observable requirements;
- explicit non-goals;
- unresolved questions.

## Rules

- Do not encode framework names, dependency choices, or file structures in the functional specification unless they are true product constraints.
- Do not treat a Figma frame or generated prototype as a complete specification.
- Do not create one enormous application-wide spec. Use bounded feature directories and cross-link shared contracts.
- Treat the spec as the intent source. When behavior changes, update it before or together with downstream artifacts.

## Quality gate

- Every user story has observable acceptance outcomes.
- Important failure and recovery behavior is specified.
- Ambiguities are visible rather than hidden in implementation notes.
- The scope is small enough to plan and implement safely.

---

# 9. Phase 2.5 — Clarification and requirements quality

## Goal

Remove expensive ambiguity before technical planning.

## Execution

1. Run `/speckit.clarify`, focusing on the highest-risk areas first.
2. Record owner answers in the specification rather than leaving them only in chat.
3. Review design states against the clarified specification.
4. Run `/speckit.checklist` to generate requirement-quality questions.
5. Add focused checklists for security, accessibility, payments, data retention, permissions, or offline behavior when applicable.
6. Return to `/speckit.specify` or clarification whenever the checklist finds missing behavior.

## Clarification priorities

- identity and authorization;
- data ownership and lifecycle;
- destructive actions;
- error and retry behavior;
- offline and synchronization behavior;
- permission denial and recovery;
- notification and background behavior;
- analytics/privacy boundaries;
- financial or regulated behavior;
- multi-device and multi-account behavior;
- supported platforms and form factors;
- release and rollout expectations.

## Quality gate

- No material requirement is answered only by “use the normal behavior.”
- Checklist failures are fixed at the specification source.
- Remaining questions have owners and do not silently pass into planning.

---

# 10. Phase 3 — Technical planning and architecture

## Goal

Convert approved intent into a coherent, testable, platform-appropriate implementation strategy.

Run `/speckit.plan` after specification clarification.

## Required plan outputs

Spec Kit may generate feature-level research, data model, contracts, and quickstart artifacts. In addition, the project must establish current architecture documents that cover the application as a whole.

### Always-required architecture outputs

| Document | Coverage |
|---|---|
| `ARCHITECTURE.md` | system shape, layers, dependency direction, application composition |
| `MODULES_AND_OWNERSHIP.md` | module/target boundaries, domain ownership, allowed dependencies |
| `DATA_FLOW.md` | UI-to-domain-to-data flows, synchronization, data ownership |
| `API_AND_INTEGRATION_CONTRACTS.md` | endpoints, SDKs, external systems, error and versioning contracts |
| `STATE_AND_CONCURRENCY.md` | state ownership, lifecycle, threading/actors/coroutines, cancellation |
| `NAVIGATION_AND_DEEP_LINKS.md` | graph, argument rules, back-stack/state restoration, external entry points |
| `PERSISTENCE_OFFLINE_SYNC.md` | local storage, caching, encryption, migrations, offline and conflict policy |
| `ERROR_RECOVERY.md` | error classification, retries, user feedback, forced recovery, support diagnostics |
| `DEPENDENCIES_AND_DI.md` | dependency strategy, DI/service construction, architecture-surface approvals |
| `DESIGN_SYSTEM_AND_COMPONENTS.md` | tokens, components, states, design-to-code mapping |
| `LOCALIZATION_ACCESSIBILITY_ADAPTATION.md` | languages, RTL, semantics, dynamic type/font scale, windows/form factors |
| `SECURITY_PRIVACY_PERMISSIONS.md` | threats, personal data, credentials, permissions, consent, protected boundaries |
| `CONFIGURATION_ENVIRONMENTS_FLAGS.md` | environments, secrets delivery, build variants/schemes, remote config, feature flags |
| `BACKGROUND_NOTIFICATIONS_PLATFORM.md` | background work, notifications, platform services, lifecycle and restrictions |
| `ANALYTICS_OBSERVABILITY_CRASH.md` | event ownership, logging, metrics, tracing, crash metadata, privacy limits |
| `PERFORMANCE_RELIABILITY.md` | startup, rendering, memory, battery, networking, resilience budgets |
| `BUILD_RELEASE_DISTRIBUTION.md` | build graph, signing, artifacts, CI/CD, store channels, rollback |
| `TESTABILITY_AND_VERIFICATION.md` | seams, pyramid, contract/integration/UI/runtime strategy, device matrix |
| `AI_WORKFLOW_AND_DOCUMENTATION.md` | context routing, skills, hooks, artifact maintenance, review and publishing |

### Conditional focused documents

Create a separate document only when the concern is material enough that the combined document would become unclear. Examples include payments, cryptography, healthcare data, media pipelines, maps/location, BLE/hardware, camera/vision, or cross-platform shared code.

## ADR rules

Create an ADR for architecture choices that are hard to reverse, affect multiple features, add an architecture-surface dependency, or materially change security, data, delivery, or operational behavior.

Typical ADR candidates:

- state architecture;
- navigation model;
- local database and migration policy;
- networking/client stack;
- authentication model;
- module boundaries;
- dependency injection approach;
- analytics/crash/observability provider;
- feature-flag provider;
- design-system integration;
- background execution strategy;
- minimum OS and adaptation scope.

## Figma MCP in Phase 3

Use Figma MCP to extract approved variables, components, variants, and layout behavior into the design-system mapping. Record design file/frame identifiers or stable links in project documentation, but do not copy secrets or large generated dumps into prompts.

## Graphify in Phase 3

Use only when the project already contains substantial generated or starter code. Otherwise defer graph creation to Phase 5.

## Quality gate

- The plan passes the constitution check.
- Architecture decisions trace to requirements and constraints.
- The project has no unnamed architecture surface.
- The test strategy can validate the chosen design.
- Protected boundaries have owners and approval requirements.
- The Phase 3.4 architecture coverage review is ready to run.

---

# 11. Phase 3.4 — Cross-feature architecture coverage gate

## Goal

Prevent architecture concerns from disappearing between the specification, plan, design files, and implementation tasks.

Use `checklists/cross-feature-architecture-coverage.md` and the `architecture-coverage-review` skill.

## Statuses

| Status | Meaning |
|---|---|
| Decided and documented | Approved direction exists with evidence and an accountable owner |
| Deferred with conditions | Intentionally deferred with trigger, owner, and impact |
| Not applicable | Project scope establishes that the concern does not apply |
| Unresolved blocker | Material concern is unresolved and blocks planning or implementation |

Do not use “not observed” as a final greenfield status. In a new project, absence usually means the team has not decided yet.

## Required concern groups

- product/domain ownership;
- modules and dependency direction;
- state and concurrency;
- data flow and contracts;
- persistence/offline/sync;
- navigation and external entry points;
- design system and component mapping;
- adaptive UI and supported form factors;
- localization and accessibility;
- permissions and platform capabilities;
- notifications and background execution;
- security, privacy, and sensitive data;
- configuration, environments, secrets, and flags;
- analytics, logging, metrics, tracing, and crash reporting;
- performance, reliability, and resource budgets;
- build, signing, distribution, and rollback;
- testing, runtime verification, and device matrix;
- AI workflow, context, hooks, skills, and publication.

## Closure rule

For every unresolved item:

- fix the specification if behavior is unclear;
- fix the plan or ADR if architecture is unclear;
- update the design authority if experience behavior is unclear;
- create an owner question if a decision is missing;
- mark implementation blocked when proceeding would encode an arbitrary choice.

Ask at the end:

> Are there material cross-cutting concerns not represented in this review?

If yes, add them to the closest architecture document and the reusable checklist only when they are broadly reusable.

---

# 12. Phase 4 — Tasks and cross-artifact analysis

## Goal

Create an executable, dependency-ordered implementation plan that remains faithful to specification and architecture.

## Execution

1. Run `/speckit.tasks`.
2. Ensure setup and foundational tasks precede feature stories.
3. Keep tests inside the user-story phase they protect rather than postponing all testing.
4. Add explicit tasks for adaptive layouts, localization, accessibility, analytics, observability, error states, and documentation where they are part of acceptance.
5. Add migration, rollout, rollback, and operational tasks when applicable.
6. Run `/speckit.analyze` before implementation.
7. Fix findings at their owning artifact: specification, plan, or tasks.
8. Re-run until remaining findings are consciously accepted and recorded.

## Task quality rules

Each task should identify:

- intended outcome;
- files or module boundary when known;
- prerequisite tasks;
- tests or verification evidence;
- design source or acceptance scenario;
- protected boundaries;
- stop condition and unresolved items.

## Quality gate

- Every requirement maps to plan coverage and implementation tasks.
- No task introduces behavior absent from the specification.
- No architecture decision exists only as an implementation task.
- The task set is small enough for bounded implementation and review.

---

# 13. Phase 4.5 — Implementation readiness audit

## Goal

Perform a read-only preflight before code generation begins.

## Review inputs

- constitution;
- product brief and current feature spec;
- clarifications and checklists;
- technical plan and ADRs;
- architecture coverage review;
- design authority and component mapping;
- tasks and analyze output;
- protected-boundary rules;
- baseline test/build/CI environment.

## Audit questions

- Does each task have an approved requirement?
- Does each design state have a specification outcome?
- Does the plan conflict with platform support or constitution rules?
- Are architecture-changing dependencies explicitly approved?
- Are adaptive, localization, and accessibility tasks present from the first slice?
- Are test seams and verification environments available?
- Are secrets, signing, backend, and external systems ready or explicitly deferred?
- Can the first vertical slice run without placeholder security or production credentials?
- Which tasks require protected-boundary preflight?

## Quality gate

Implementation begins only when blockers are resolved or the owner has authorized a narrower slice that avoids them.

---

# 14. Phase 5 — Walking skeleton and first vertical slice

## Goal

Prove the architecture, toolchain, and delivery path with the smallest end-to-end user outcome.

## Walking skeleton contents

- application boots on an approved simulator/emulator/device;
- navigation shell and dependency composition work;
- one representative screen renders approved design-system components;
- one state flow reaches a fake, local, or approved service boundary;
- error/loading/empty behavior exists;
- localization and accessibility foundations work;
- compact and expanded behavior is demonstrated when in support scope;
- baseline domain/state test and UI semantics test exist;
- CI builds and runs deterministic checks;
- sanitized logging and crash initialization are verified in non-production scope;
- configuration and secrets do not rely on developer-local accidents.

## Graphify timing

After the skeleton contains meaningful modules and dependencies:

1. generate the repository graph locally;
2. inspect module and feature dependency direction;
3. compare the graph with `MODULES_AND_OWNERSHIP.md`;
4. record contradictions as plan or implementation issues;
5. keep graph output uncommitted unless versioning it is an explicit repository decision.

## Quality gate

- The architecture is buildable, not only documented.
- The first slice traces from spec to design to code to tests.
- CI and local commands agree on the deterministic baseline.
- No prototype code or generated design code bypasses repository conventions.

---

# 15. Phase 6 — Iterative feature implementation

## Goal

Implement one bounded user-story slice at a time while keeping artifacts and code aligned.

## Execution loop

```text
select task phase
-> read smallest relevant context
-> protected-boundary preflight if needed
-> retrieve Figma context if design-authoritative
-> query Graphify if impact is cross-feature
-> implement the bounded slice
-> add focused tests
-> run verification
-> review diff
-> update affected artifacts
-> run converge at agreed checkpoints
```

Use `/speckit.implement` in scoped phases for large features rather than asking one agent to implement the entire product in one context window.

## Design-to-code rules

- Prefer existing repository components mapped to Figma components.
- Do not generate duplicate components merely because a frame can be translated directly.
- Preserve semantic roles, focus behavior, content descriptions/labels, Dynamic Type/font scale, RTL, and window adaptation.
- Treat generated Stitch or Figma code as reference material requiring normal review, not privileged source.

## Convergence

Run `/speckit.converge` after meaningful slices and before feature completion. If it appends tasks, review them; do not auto-accept tasks that conflict with owner decisions or scope.

---

# 16. Phase 7 — Expanded safety net and integration verification

## Goal

Move from a working slice to a reliable product without replacing evidence with test volume.

## Test layers

1. Domain and pure-state tests.
2. Repository/data-source and contract tests.
3. Persistence and migration tests on the required runtime.
4. UI component and semantics tests.
5. Navigation and deep-link tests.
6. Integration tests using approved fakes or test services.
7. Small end-to-end journey set on device/simulator.
8. Release-candidate smoke tests.

## Rules

- Use the repository’s established framework unless a decision authorizes a change.
- Test the smallest useful layer first.
- Do not use production services, personal data, signing credentials, or real payment instruments in automated tests.
- Record exactly what each test does not prove.
- Include failure, cancellation, process death/state restoration, permission denial, offline, and retry behavior when applicable.

---

# 17. Phase 8 — Product and platform hardening

## Goal

Verify cross-cutting quality against real platform behavior before release.

## Hardening areas

### Adaptive UI

- compact, medium, expanded windows;
- orientation and resize behavior;
- tablets/iPad, foldables, multi-window, split view, Stage Manager where applicable;
- large text and content reflow;
- keyboard, pointer, and external display where in support scope.

### Localization and accessibility

- all visible and accessibility strings localized;
- plural/format parity;
- RTL and pseudo-locale review;
- screen-reader traversal and announcements;
- focus order, touch targets, contrast, motion, switch/keyboard access;
- human translation review.

### Performance and reliability

- cold/warm startup;
- scrolling and rendering;
- recomposition/invalidation;
- memory pressure and leaks;
- battery and background limits;
- networking latency, retries, and payloads;
- database performance;
- crash-free and ANR/hang goals.

### Security and privacy

- threat review;
- permission minimization;
- sensitive logging and crash metadata;
- local encryption/keychain/keystore behavior;
- transport security and certificate policy;
- exported components, deep links, URL schemes, and intents;
- consent, retention, deletion, and account lifecycle;
- dependency and supply-chain review.

## Quality gate

Static inspection alone is insufficient. Record device/runtime, backend, telemetry, and release evidence separately.

---

# 18. Phase 9 — Delivery and release verification

## Goal

Prove that the exact intended artifact can be built, signed, distributed, observed, and rolled back safely.

## Required evidence

- deterministic CI checks;
- environment and configuration resolution;
- dependency resolution and lockfiles;
- debug, test, staging, and release artifact separation;
- signing/provisioning ownership;
- secrets delivery without repository leakage;
- symbol/mapping upload for crash reporting;
- artifact inspection and checksums;
- release logging behavior;
- backend and feature-flag readiness;
- store metadata, privacy declarations, permissions, and entitlements;
- staged rollout and rollback plan;
- support and incident ownership.

## Rule

Authorization to build is not authorization to sign, upload, distribute, or access production systems. Treat each remote or release side effect as separately controlled.

---

# 19. Phase 10 — Review and controlled publication

## Goal

Publish only a reviewed, committed, evidence-backed change.

## Procedure

1. Run `pr-review` against the complete task diff.
2. Run documentation-impact assessment.
3. Run deterministic repository guidance validation and impact classification when available.
4. Record commands actually run and checks not run.
5. Review Spec Kit artifact changes together with code changes.
6. Review Graphify impact output only as supplementary evidence.
7. Prepare the MR description outside the repository.
8. Stop for explicit approval before push or MR creation.
9. Never merge, auto-merge, force-push, or bypass failed gates.

## Completion report

- specification/plan/tasks affected;
- files changed;
- tests and tier;
- design authority used;
- architecture coverage affected;
- protected boundaries touched;
- documentation impact;
- runtime/release checks;
- review findings;
- remaining Needs verification.

---

# 20. Phase 11 — Launch and operational verification

## Goal

Verify the product in real operational conditions after artifact correctness is established.

## Launch checks

- staged rollout and feature-flag state;
- analytics event receipt and privacy review;
- crash symbolication and sanitized metadata;
- logs, metrics, traces, and dashboards;
- backend capacity and error rates;
- push/background behavior;
- support playbook and escalation;
- rollback and kill-switch readiness;
- product success measures and anomaly thresholds.

Do not claim launch success from build success alone.

---

# 21. Phase 12 — Lessons, maintenance, and handoff

## Goal

Turn project experience into reusable assets without copying project-specific secrets or assumptions into generic templates.

## Outputs

- updated onboarding and `AI_CONTEXT.md`;
- maintained constitution and `AGENTS.md`;
- current architecture and design maps;
- decision and verification backlog;
- reusable skills and prompts;
- known stop conditions;
- Spec Kit version/upgrade notes;
- design-tool and MCP provenance;
- Graphify regeneration policy;
- ownership and maintenance schedule;
- lessons proposed for the generic Greenfield or Brownfield playbook.

## Reuse rule

Promote a lesson into the reusable playbook only when it is broadly applicable. Keep product-specific behavior, provider choices, credentials, and organization policy in the project repository.

---

# 22. Repository file model

Recommended structure:

```text
AGENTS.md
AI_CONTEXT.md
AI_PLAYBOOK.md

.specify/
  memory/constitution.md
  templates/
  scripts/

specs/
  001-feature-name/
    spec.md
    plan.md
    research.md
    data-model.md
    contracts/
    checklists/
    tasks.md

docs/
  product/
  design/
  architecture/
  decisions/
  testing/
  release/
  review/
  ai/

.agents/
  skills/
  vendor/

.claude/skills/          # optional compatibility exposure
.codex/hooks/            # optional client-specific adapter
scripts/                 # deterministic shared repository scripts
```

## Canonical ownership

- `AGENTS.md`: mandatory repository policy.
- Spec Kit artifacts: current product intent and derived implementation plan for each feature.
- `docs/architecture/`: cross-feature architecture truth and evidence boundaries.
- Figma or selected design authority: approved visual/component source, with repository mapping.
- Skills: procedures only.
- Hooks: reminders or deterministic checks only.
- CI: authoritative shared execution gate when configured.

---

# 23. Hooks and automation

Keep the same safe hook principles used by the Brownfield package.

Hooks may:

- inject documentation-impact guidance at prompt start;
- check documentation-impact completion at stop;
- remind the agent about review or protected boundaries;
- run deterministic read-only validators with bounded timeouts.

Hooks must not:

- authorize implementation or protected changes;
- edit specifications or documentation automatically;
- push, publish, merge, sign, upload, or access production systems;
- run a full review on every file save;
- claim that optional client hook behavior works everywhere.

Spec Kit extensions and workflows may orchestrate steps, but human approval boundaries remain external and mandatory.

---

# 24. Common failure modes

| Failure | Correction |
|---|---|
| Starting implementation from a vague prompt | Create and clarify a bounded specification first |
| Treating generated design as approved behavior | Promote reviewed decisions into spec/design authority |
| Putting architecture in `spec.md` | Move technical choices to plan/ADR |
| Generating tasks before architecture coverage | Complete Phase 3 and Phase 3.4 first |
| Running `/speckit.implement` for the whole product | Scope implementation by task phase or user story |
| Using Graphify before code exists | Defer until the walking skeleton or substantial starter code |
| Treating Figma as backend/product truth | Cross-check against spec and contracts |
| Copying generated Stitch/Figma code directly | Apply repository architecture, components, tests, and review |
| Adding every tool to every project | Adopt only tools with clear value and ownership |
| Creating broad tests without risk | Tie tests to acceptance, architecture, or release risk |
| Letting specs become stale after discoveries | Flow changes back to spec/plan/tasks, analyze, and converge |
| Allowing hooks to publish or modify | Keep remote side effects explicit and human-approved |

---

# 25. Starter adoption checklist

## Before the first feature

- [ ] Select Android or iOS Greenfield `AGENTS.md` overlay.
- [ ] Merge with `AGENTS.common.md` into one root `AGENTS.md`.
- [ ] Replace or remove every bracketed placeholder.
- [ ] Initialize and pin Spec Kit.
- [ ] Create the project constitution.
- [ ] Declare design authority and tool policy.
- [ ] Establish product brief, success measures, and constraints.
- [ ] Establish CI, protected branches, and publication approval.

## Before implementation

- [ ] Specification created and clarified.
- [ ] Requirement checklist reviewed.
- [ ] Technical plan and ADRs reviewed.
- [ ] Cross-feature architecture coverage gate passed.
- [ ] Tasks generated and analyzed.
- [ ] Design states and components mapped.
- [ ] Test and runtime strategy exists.
- [ ] Protected-boundary approvals recorded.

## Before feature completion

- [ ] Implementation converged with spec, plan, and tasks.
- [ ] Tests actually ran.
- [ ] Adaptive, localization, accessibility, privacy, analytics, and performance work completed when applicable.
- [ ] Documentation impact closed.
- [ ] PR review completed.
- [ ] Runtime/release evidence classified.
- [ ] Publication explicitly approved.

---

# 26. External tool verification notes

Tool capabilities and command names change. Before adopting or upgrading:

- verify the current Spec Kit installation and command reference;
- verify Graphify installation, graph format, MCP tools, and local-data policy;
- verify Figma MCP availability, permissions, client support, and read/write scope;
- verify Stitch or any generative design tool’s current export, privacy, and ownership terms;
- pin versions or record dates where reproducibility matters;
- keep external tools lower-authority than repository policy and approved artifacts.

This playbook intentionally describes tool roles and decision boundaries rather than hardcoding one vendor workflow as permanent architecture.
