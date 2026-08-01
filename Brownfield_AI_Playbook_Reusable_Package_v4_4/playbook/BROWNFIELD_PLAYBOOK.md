**AI Existing Project Playbook**

Mobile Generic v4.4

A reusable workflow for senior native Android and iOS developers working
in brownfield, inherited, legacy, or actively evolving mobile projects.

**Discover first. Verify decisions. Change selectively. Publish
evidence.**

**Consolidated edition**

Integrates the v3.1 skills/testing lessons, v3.2 hook/CI/MR workflow,
v3.3 decision-to-code audit model, v4.1 reusable AI-governance
architecture, v4.2 prompt ergonomics and verified gate responsibilities,
and v4.4 repository-owned prompt routing, checkpoint automation,
Graphify boundaries, and the transition from external prompt generation
to direct repository execution.

# 1. Purpose and operating philosophy

This playbook is for existing native mobile applications where
architecture, product intent, backend behavior, release process, and
test coverage may be incomplete, inconsistent, or only partly
documented. It is designed to make AI-assisted engineering safer without
pretending that documentation, source inspection, or unit tests alone
establish runtime or production truth.

Core rule: Never let AI change what it does not understand.

The reusable order is: evidence, questions, accountable decisions,
decision capture, implementation audit, classification, one authorized
action, verification, documentation, explicit publishing, and human/CI
review.

| **Use this when**                                                 | **Primary mindset**                                                                              | **Primary outcome**                                                                                               |
|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| You inherit or re-enter an old or active Android/iOS project.     | Act like a senior engineer joining a new company: discover first, change later.                  | A safer project, reviewed context, meaningful tests, explicit decisions, bounded changes, and repeatable handoff. |
| The repository contains unclear or conflicting behavior.          | Separate current implementation, approved contract, runtime truth, and desired future direction. | Fewer accidental rewrites, fewer invented requirements, and better review evidence.                               |
| AI tools are used for docs, tests, fixes, reviews, or automation. | Treat AI as an evidence-producing assistant, never as the authority.                             | Human-controlled changes with traceable scope and verification.                                                   |

## 1.1 What “complete” means

A brownfield project is never “fully known.” Completion is local and
evidence-based. A phase, feature, or risk area may be closed when:

- The material current contract is documented with provenance.

- Important contradictions are fixed, accepted, or explicitly deferred.

- Meaningful deterministic behavior is covered at the smallest useful
  test layer.

- Remaining uncertainty is classified as runtime, backend, device,
  security, release, or owner verification.

- The next local test or source change would not materially reduce risk.

- Useful evidence is recorded without duplicating status across every
  document.

Stop when the remaining work belongs to another evidence layer. Do not
manufacture more tests or setup artifacts merely to keep the workflow
moving.

## 1.2 Evidence categories

| **Category**              | **Meaning**                                                   | **Allowed conclusion**                                  |
|---------------------------|---------------------------------------------------------------|---------------------------------------------------------|
| Verified source fact      | Observed in current reviewed source/configuration.            | May describe the inspected implementation only.         |
| Existing test evidence    | A named test was actually run and passed.                     | May claim only the exact asserted contract.             |
| Owner/product decision    | An accountable person approved a behavior or policy.          | Defines intent, not implementation or runtime truth.    |
| Backend/platform contract | Confirmed by accountable service/platform evidence.           | May guide client behavior within the confirmed scope.   |
| Runtime/device evidence   | Observed on approved runtime, simulator, emulator, or device. | Supports the tested environment and scenario only.      |
| Release evidence          | Built, inspected, signed, or distributed artifact evidence.   | Supports the exact artifact and release stage verified. |
| Needs verification        | Evidence is incomplete or conflicting.                        | Do not guess, test as truth, or silently fix.           |

# 2. Canonical brownfield lifecycle

The lifecycle is intentionally sequential, but it is not a waterfall.
Teams may revisit earlier phases when new evidence changes the contract.
The critical rule is that each transition has a quality gate and that
decision-sensitive work uses the protected track described later.

| **Phase** | **Main activity**                    | **Primary deliverable**                                                                              |
|-----------|--------------------------------------|------------------------------------------------------------------------------------------------------|
| 0         | Safe setup                           | Branch/worktree safety, baseline commands, sensitive-file rules                                      |
| 1         | Repository discovery                 | Project overview, modules, features, dependencies, testing, technical debt                           |
| 1.5       | Documentation review and provenance  | Reviewed context, authority labels, context index                                                    |
| 1.6       | First testing foundation             | One or two meaningful low-risk characterization seams                                                |
| 2         | Feature-level understanding          | End-to-end feature docs, active/deferred paths, blockers                                             |
| 3         | Architecture/design validation       | Complete cross-feature architecture maps plus an explicit coverage review across applicable concerns |
| 3.4       | Architecture coverage gate           | Verified/Needs verification/Not observed/Not applicable classification and routed gaps               |
| 3.5       | Verification questions and decisions | Accountable answers captured before high-risk tests or fixes                                         |
| 3.6       | No-edit implementation audit         | Decision-to-source comparison and finding classification                                             |
| 4         | Skills and AI governance system      | Canonical skills, vendor separation, adapters, impact assessment, shared scripts, and hook strategy  |
| 5         | Expanded safety net                  | Risk-backed tests and deliberate test infrastructure                                                 |
| 6         | Controlled refactoring               | Small behavior-preserving changes protected by evidence                                              |
| 7         | Bounded feature or defect work       | One approved behavior change with acceptance criteria                                                |
| 8         | AI-assisted review and publish       | Diff review, documentation-impact evidence, explicit commit/push/MR, no auto-merge                   |
| 9         | CI/CD and release verification       | Shared deterministic gates, protected delivery, runtime/release evidence                             |
| 10        | Lessons extraction                   | Reusable prompts, skills, stop conditions, onboarding checklist                                      |

## 2.1 Two execution tracks

| **Track**                | **Use when**                                                                                                                                                               | **Sequence**                                                                                                                                                   |
|--------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Standard bounded track   | The requirement is clear, low risk, and does not cross protected or owner-sensitive boundaries.                                                                            | Context → current behavior → plan → focused implementation/test → verify → publish.                                                                            |
| Decision-sensitive track | The work affects auth, data integrity, persistence, signing, certificates, permissions, notifications, camera, release, backend contracts, or unresolved product behavior. | Evidence → architecture coverage review → questions → accountable answers → docs capture → no-edit audit → classify → authorize one action → verify → publish. |

# 3. AI context pipeline

The context pipeline limits what AI reads and prevents the entire
repository from becoming unreviewable prompt baggage. It begins only
after the context foundation has been reviewed.

| **Layer** | **Content**                                                               | **When used**                                                                                       |
|-----------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| 0         | AI context index and project overview                                     | Every session and task                                                                              |
| 1         | Architecture, design, module, dependency, testing, release, and debt maps | Planning, cross-feature review, refactoring                                                         |
| 2         | Feature map and feature-specific documents                                | Feature docs, bugs, tests, behavior changes                                                         |
| 3         | Project-specific and selected official platform skills                    | Testing, review, UI, tooling, platform work                                                         |
| 4         | Skills and AI governance system                                           | Canonical skills, vendor separation, adapters, impact assessment, shared scripts, and hook strategy |
| 5         | Only directly relevant current source and tests                           | Generation, editing, or code review                                                                 |

- Every task starts from the context index plus only the documents
  needed for that task.

- Feature work reads the feature document first when one exists.

- AI does not scan the entire repository unless the scope requires it
  and the user authorizes the larger inspection.

- Unclear claims remain Needs verification.

- Context documents explain provenance, authority, and evidence limits.

- Current source wins over stale orientation docs when the task requires
  current behavior.

## 3.1 Repository-owned prompt routing, checkpoints, and graph discovery

Once the initial context foundation exists, move repeated instructions
out of chat and into version-controlled repository artifacts. The
repository should become the durable task interface: an agent policy,
context index, checkpoint, focused scope specifications, prompt
templates, manifests, and deterministic runners.

A checkpoint records completed reviewed artifacts, the current phase,
the next single authorized task, blockers, and prohibited work. Create
it during Phase 1 or Phase 1.5, not after implementation begins. Advance
it only after the relevant review or promotion gate passes.

Use a manifest plus a runner when a phase contains a repeatable ordered
batch. The runner should resolve the next checkpoint-authorized item,
verify prerequisites and target status, render one task prompt, limit
allowed file changes, and stop without committing or publishing.

Graph tools such as Graphify may accelerate file and symbol discovery,
but they are not architecture authority. Verify every material
dependency, ownership, lifecycle, and runtime claim against current
source, tests, build/configuration, or reviewed documentation. Missing
graph edges are never evidence of absence.

Maintain project-owned graph limitations and verified overrides outside
generated output. Never hand-edit generated graph files; regeneration
must remain safe and deterministic.

Why this saves time and tokens: stable policy and evidence instructions
are paid once in repository files; each session receives only the next
authorized scope and directly relevant context. Quality improves because
creation, review, promotion, and implementation do not silently collapse
into one conversation.

# 4. Phase 0 — Safe setup

Goal: Create a controlled environment where AI output can be inspected,
reverted, and measured before behavior changes begin.

- Dedicated focused branch or equivalent isolated worktree

- Known baseline build/test/lint/run commands

- Protected branch, secret, signing, certificate, production-data, and
  no-large-rewrite rules

- Decision about where AI instructions, docs, prompts, and temporary
  artifacts live

- Canonical agent policy, context routing, skill ownership, and
  client-adapter locations established before feature work.

- Repository-owned deterministic validation and documentation-impact
  classification planned as shared scripts, not duplicated client logic.

- Agent completion rules defined before relying on optional lifecycle
  hooks.

## Execution

1.  Start from the current integration branch unless explicitly told
    otherwise.

2.  Record worktree status and known pre-existing modifications.

3.  Run the application and baseline commands only when permitted and
    practical.

4.  Record failures as baseline failures, not AI-caused failures.

5.  Identify files that must never be shared, modified, staged, or
    committed.

6.  Do not refactor during setup.

## Quality gate

- The branch/worktree is safe and reviewable.

- Build/test status is known or explicitly unknown.

- Sensitive materials are excluded.

- Large rewrites and unrelated cleanup are prohibited.

> Prepare this existing mobile project for AI-assisted work. Record
> branch/worktree safety, baseline commands, sensitive files, protected
> areas, and no-rewrite rules. Do not modify app behavior.

# 5. Phase 1 — Repository discovery and context foundation

Goal: Teach humans and AI what exists before asking for improvements.

| **Artifact**         | **Purpose**                                                       | **Required?** |
|----------------------|-------------------------------------------------------------------|---------------|
| PROJECT_OVERVIEW.md  | Product surface, platforms, app/module structure, key risks       | Always        |
| MODULES.md           | Folders, packages/targets/modules, ownership boundaries           | Always        |
| FEATURE_MAP.md       | Visible features, entry points, state/data owners                 | Always        |
| ARCHITECTURE.md      | Observed high-level architecture, not an idealized target         | Always        |
| DEPENDENCIES.md      | Build tools, libraries, declared versions, dependency risks       | Always        |
| TESTING_MAP.md       | Existing tests, commands, gaps, infrastructure                    | Always        |
| TECH_DEBT.md         | Evidence-based risks and uncertainty, not a random cleanup list   | Usually       |
| Platform/build notes | Signing, entitlements, manifests, schemes, flavors/configurations | When relevant |

7.  Generate one document at a time.

8.  Keep discovery documentation-only.

9.  Cite inspected files and distinguish facts from assumptions.

10. Avoid unsupported design intent.

11. Commit or otherwise checkpoint the reviewed foundation before code
    planning.

> Act as a senior native mobile engineer joining this existing project.
> Generate only the requested discovery document. Cite inspected files,
> mark uncertainty, and do not modify code, tests, dependencies, or
> project configuration.

## Reusable foundation-document automation

For repeated discovery documents, use small create and read-only review
templates selected by a deterministic phase runner. Each task works on
one document, checks that its prerequisite is Reviewed or Reviewed
orientation, records the inspected revision, and stops before approval,
commit, or publication.

A reusable foundation set usually includes phase runner logic and
create/review templates for MODULES, FEATURE_MAP, TESTING_MAP,
DEPENDENCIES, PROJECT_OVERVIEW, and ARCHITECTURE. Copy the workflow
structure into another brownfield repository, but adapt platform names,
expected paths, product-authority files, and commands.

Do not ask a general chat model to regenerate these prompts for every
project run once the templates are checked into the repository.
Regenerate or revise a template only when the evidence contract,
repository topology, or phase gate changes.

# 6. Phase 1.5 — Documentation review, provenance, and context index

Goal: Make generated context safe enough to reuse.

- Review date and source revision/context

- Commands actually run

- Inspection scope and exclusions

- Authority level

- Worktree status when it affects evidence

- Explicit Needs verification for
  runtime/product/backend/security/release claims

## Review checks

- Unsupported or invented architecture, intent, business rules, or
  future plans

- Broken relative links

- Claims based on dirty or untracked files

- Declared dependency versions presented as resolved versions

- Static source claims presented as runtime truth

- Tests described more broadly than their assertions

- Documents that are too long or too generic to be useful context

## Quality gate

- The context index lists approved context files.

- Orientation docs do not claim final architectural truth.

- Material uncertainty is visible.

- Future tasks can select a small relevant context set.

> Review these generated documents as reusable AI context. Identify
> unsupported claims, broken links, stale assumptions, missing
> provenance, overconfident wording, and whether each file is safe as
> orientation context.

# 7. Phase 1.6 — First testing foundation

Goal: Add a minimal safety net before deeper feature work, refactoring,
or implementation.

12. Choose one or two important, low-risk, deterministic seams.

13. Plan before writing tests.

14. Protect current behavior, not ideal behavior.

15. Use current test tools and simple hand-written fakes where
    practical.

16. Run the narrow test and the project-level local test task.

17. Document blocked tests rather than forcing dependencies or
    production refactors.

| **Good first seam**                                                    | **Avoid initially**                                                  |
|------------------------------------------------------------------------|----------------------------------------------------------------------|
| Pure formatter, mapper, reducer, validation utility, state calculation | Authentication refresh, signing, certificates, production networking |
| Repository/data-source parameter forwarding with an existing interface | Camera, push delivery, permissions, secure storage runtime           |
| Resource parity or configuration-source-set checks                     | Large UI flows requiring new frameworks or broad seams               |

> Plan minimal characterization tests for current behavior only. Do not
> modify production code. Identify the smallest test layer, fakes,
> commands, risks, blockers, and the exact behavior each test would
> protect.

# 8. Phase 2 — Feature-level understanding

Goal: Map important features end to end and add selected safe tests only
where seams already exist.

- Entry points and navigation

- UI states and user-visible feedback

- ViewModel/controller/state ownership

- Repository/service/data-source flow

- Persistence, caching, secure storage, and transient state

- Threading, concurrency, lifecycle, and process-death behavior

- Permissions, notifications, camera, deep links, and external
  integrations

- Existing tests, risks, owner decisions, and next test candidates

Each feature document separates verified facts, owner decisions, Needs
verification, and recommendations.

## Phase 2 boundaries

- Do not mix refactoring, permission cleanup, auth/network changes,
  storage migrations, product behavior changes, or dependency additions
  into feature documentation.

- Do not test inactive or postponed paths merely because the code
  exists.

- A safe test may be added only when it requires no unapproved
  production refactor, new tooling, or protected-area change.

> Document this feature end to end from UI to data source. Include
> state, errors, navigation, persistence/networking,
> lifecycle/concurrency, active and deferred paths, existing tests,
> risks, and recommended next tests. Do not refactor or change behavior.

## Reusable feature-document batch

A feature manifest may define order, stable ID, feature name, and output
path. A runner may select the next missing page, launch one fresh agent
session for creation and another for review, permit edits only to the
selected page and—during review—the checkpoint, and stop when unexpected
files change.

The creation template should read the reviewed project maps, relevant
product authority, the feature’s directly related source/tests, and one
reviewed example page. It should separate current facts, owner intent,
executed evidence, static limitations, recommendations, and Needs
verification.

The review template should verify the page line by line against source
and tests, correct only that page, promote it only when material claims
are supported, and authorize exactly the next feature page in the
checkpoint.

This pattern is reusable across brownfield projects. Copy the
runner/template pattern as a baseline; adapt feature IDs, product
documents, source-language terminology, model/agent invocation, and
platform-specific evidence checks. Do not copy a project’s feature
manifest as universal truth.

# 9. Phase 3 — Architecture, design system, and cross-feature rules

Goal: Extract the material cross-feature architecture of the existing
system from real feature and source evidence, then prove that applicable
architecture concerns have either been documented, classified, or routed
before decision-sensitive work begins.

Phase 3 is not complete merely because a standard set of documents
exists. It is complete only when the repository’s applicable
cross-cutting concerns have a current evidence home and the Phase 3.4
coverage gate has been performed.

## 9.1 Required core architecture maps

Create or update only the maps supported by the inspected project. A
concern may share a document with a related concern when that keeps the
context smaller and clearer.

| **Map**                               | **Questions answered**                                                                                                                                                                                                                    |
|---------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ARCHITECTURE / MODULES                | Application composition, modules/packages/targets, dependency direction, ownership, feature/domain boundaries, shared infrastructure, cyclic-coupling risks                                                                               |
| DATA_FLOW                             | How data moves from UI through state owners, repositories/use cases, local/remote systems, platform services, and external integrations                                                                                                   |
| API_CONTRACTS                         | Observed endpoints, payloads, auth/header/error behavior, integration ownership, and unknown backend truth                                                                                                                                |
| PERSISTENCE_AND_CACHE                 | Data lifecycles, secure storage, caches, migrations, offline behavior, reset/logout behavior, process death, and consistency boundaries                                                                                                   |
| NAVIGATION                            | Graphs/stacks/routes/deep links, argument transport, restoration, session boundaries, external entry points, and form-factor navigation differences                                                                                       |
| STATE_MANAGEMENT                      | State owners, flows/publishers, concurrency, UI-local state, one-off events, restoration, and process/lifecycle boundaries                                                                                                                |
| ERROR_HANDLING                        | Error sources, mapping, user feedback, retry/backoff, degraded modes, recovery, and forced logout                                                                                                                                         |
| DEPENDENCY_INJECTION                  | Containers, scopes/lifetimes, manual construction, service location, feature isolation, and test seams                                                                                                                                    |
| DESIGN_SYSTEM / UI_COMPONENTS         | Observed tokens, shared components, repeated states, reuse rules, visual consistency, and theming                                                                                                                                         |
| UI_ADAPTATION_AND_PLATFORM            | Supported devices/form factors, compact/medium/expanded behavior, phone/tablet/foldable/multi-window/orientation strategy, iPad/Stage Manager/Catalyst/ChromeOS where applicable, platform-specific divergence, and runtime evidence gaps |
| LOCALIZATION_AND_ACCESSIBILITY        | Resources/catalogs, plural/format rules, RTL, Dynamic Type/font scaling, screen readers, semantics, focus, contrast, touch targets, and human-review boundaries                                                                           |
| BACKGROUND_EXECUTION                  | WorkManager/BGTaskScheduler/background fetch, foreground services/background modes, sync ownership, retries, cancellation, OS restrictions, battery, and process-death behavior                                                           |
| PERMISSIONS_AND_PLATFORM_CAPABILITIES | Permission-to-feature mapping, request timing, rationale, temporary/permanent denial, settings recovery, degraded behavior, lifecycle, intents/entitlements/capabilities                                                                  |
| CONFIGURATION_AND_ENVIRONMENTS        | Build configurations/flavors/schemes, endpoints, secrets delivery, local/staging/production separation, runtime configuration, remote config, and drift controls                                                                          |
| FEATURE_FLAGS_AND_ROLLOUT             | Local/remote flags, experiments, kill switches, rollout/rollback, ownership, defaults, expiry, and test coverage                                                                                                                          |
| ANALYTICS_AND_PRIVACY                 | Event ownership, taxonomy/naming, screen tracking, payloads, consent, PII/privacy boundaries, retention, debug/release behavior, and delivery evidence                                                                                    |
| OBSERVABILITY_AND_CRASH_REPORTING     | Logging, metrics, traces, diagnostics, crash reporters, metadata/privacy, symbol or mapping upload, alert/incident ownership, debug/release differences                                                                                   |
| PERFORMANCE_AND_RESOURCE_BEHAVIOR     | Startup, main-thread/actor blocking, rendering/recomposition, scrolling, memory, networking, persistence, battery, profiling evidence, and budgets where approved                                                                         |
| SECURITY_BOUNDARIES                   | Tokens, cookies, Keychain/Keystore, route/deep-link/intent boundaries, certificates, logging, sensitive data, platform capabilities, and threat-sensitive assumptions                                                                     |
| BUILD_AND_RELEASE                     | Schemes/configurations/build types, dependency resolution, signing/provisioning, artifacts, symbols/mappings, CI/release separation, distribution, rollback, telemetry, and environment controls                                          |
| TESTABILITY_ROADMAP                   | Existing seams, blockers, test layers, deterministic/runtime boundaries, infrastructure sequence, and evidence gaps                                                                                                                       |
| CODE_STYLE_AND_CONVENTIONS            | Observed naming, layering, concurrency, file organization, formatting, generated-source rules, and exceptions                                                                                                                             |
| AI_WORKFLOW_NOTES                     | Context routing, prompts that worked, overclaiming hazards, verification habits, protected boundaries, and documentation-impact workflow                                                                                                  |

## 9.2 Conditional maps and consolidation rule

Do not create empty documents to satisfy a template. For each concern:

- Extend the closest current architecture document when the concern is
  materially related and can remain easy to route.
- Create a focused document only when the concern is material,
  recurring, and has no clear current home.
- Record `Not observed` when no implementation/configuration was found
  within the stated inspection scope.
- Record `Not applicable` only when accountable scope establishes that
  the concern does not apply.
- Preserve `Needs verification` when evidence, runtime behavior, or
  owner intent is incomplete.
- Route every new current document through the context index and
  documentation index when those exist.

Examples:

- Analytics, observability, and crash reporting may share one
  `OBSERVABILITY.md` when ownership and evidence overlap.
- UI adaptation may be a section of design/localization architecture for
  a phone-only app, but a separate document for tablet/foldable/iPad
  support.
- Background execution may be a short `Not observed` row in the coverage
  review when the project has no workers, services, or background modes.
- Domain ownership may extend `ARCHITECTURE.md` or `MODULES.md` rather
  than introducing a DDD-specific document.

## 9.3 Execution

18. Create or refresh one map at a time from reviewed feature evidence
    and directly relevant current source/configuration.

19. For every map, state provenance, authority, inspection scope,
    exclusions, current facts, owner decisions, `Needs verification`,
    runtime/release limits, and related documents.

20. Document patterns and exceptions without converting recommendations
    into decisions.

21. Trace material cross-feature claims to concrete
    source/configuration, executed tests, runtime evidence, accountable
    decisions, or explicit `Needs verification`.

22. Do not create ADRs unless ownership, evidence, alternatives, and
    decision scope are clear.

23. Do not start a rewrite, dependency migration, module split,
    framework replacement, or test-infrastructure expansion while
    documenting architecture.

24. After the maps are complete, run Phase 3.4. Do not proceed directly
    to verification questions merely because the expected filenames
    exist.

> Validate architecture and design patterns across the documented
> features. Cover the applicable architecture dimensions in the Phase 3
> map set, extend or create only the smallest useful current documents,
> and preserve evidence boundaries. Then perform the Phase 3.4 coverage
> review. Do not refactor.

## 9.3.1 Reusable architecture-map pipeline

Use three separate tasks for every architecture map: create Draft,
perform a read-only review, then promote. Creation may update the
checkpoint only to authorize review of the same Draft. Review edits
nothing and returns Promote, Revise, or Blocked. Promotion changes
status/checkpoint only and must not perform substantive correction.

Use an architecture manifest with order, ID, name, output path, focused
scope specification, and reviewed prerequisite. A runner should reject
out-of-sequence work unless explicit authorization is supplied, verify
the checkpoint target, and render exactly one prompt.

Focused scope specifications are a high-value reusable pattern because
they reduce broad repository scans. Each specification defines the
discovery question, required evidence, required content, evidence
limits, and explicit non-goals. The specification names should be
reusable; their concrete paths and project contracts must be adapted.

Graph discovery is appropriate here for disputed or high-risk
relationships only. The create and review tasks must repeat that graph
output routes inspection but does not prove architecture.

# 9.4 Phase 3.4 — Cross-feature architecture coverage gate

Goal: Confirm that every material cross-cutting concern is represented,
classified, and routed before owner questions, decision capture, or
implementation auditing begin.

Use the reusable `architecture-coverage-review` skill and
`checklists/cross-feature-architecture-coverage.md` when available.

## Required classifications

| **Classification** | **Meaning**                                                                                                          |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| Verified           | Current reviewed evidence supports the stated conclusion within an explicit scope                                    |
| Needs verification | The concern is material but evidence, runtime behavior, or accountable intent is incomplete/conflicting              |
| Not observed       | No relevant implementation/configuration was found in the inspected scope; absence is not proof of non-applicability |
| Not applicable     | Accountable project scope establishes that the concern does not apply                                                |

For each applicable concern record:

- classification;
- evidence and inspection scope;
- current document or intended documentation home;
- material gap or stale claim;
- accountable owner;
- whether it blocks Phase 3.5, implementation, protected work, runtime
  verification, or release;
- smallest safe next action.

## Gate rules

1.  A missing current documentation home for a material concern blocks
    Phase 3 completion until the closest document is updated or a
    focused document is created.
2.  An owner-dependent ambiguity routes to Phase 3.5 as a concrete
    verification question tied to blocked work.
3.  A contradiction between an approved decision/current contract and
    source routes to Phase 3.6 for a no-edit audit.
4.  A runtime/device/backend/release uncertainty may remain
    `Needs verification` when the architecture map correctly records the
    boundary and next evidence layer.
5.  A `Not observed` concern does not require speculative implementation
    or an empty document.
6.  A `Not applicable` conclusion must state who or what authoritative
    scope supports it.
7.  Do not mark the gate complete while a material current claim is
    missing, duplicated inconsistently, or routed only through a
    historical document.

## Living-review question

Ask at the end of every coverage review:

> Are there material cross-cutting architectural concerns that are not
> represented in this review?

If yes:

- update the closest current architecture document, or create a focused
  document only when no suitable home exists;
- record why the concern matters and its evidence boundary;
- identify the accountable owner;
- state whether related implementation or release work is blocked;
- route the document through the current context index.

## Phase 3 quality gate

Phase 3 is complete only when:

- core and project-specific architecture concerns have current evidence
  homes;
- every coverage row is classified;
- material `Needs verification` items have owners and next evidence
  actions;
- owner questions are ready for Phase 3.5;
- decision/source contradictions are ready for Phase 3.6;
- no empty or speculative documents were created solely to satisfy the
  checklist;
- the context index routes every new current architecture document.

# 10. Phase 3.5 — Verification questions and accountable decisions

Goal: Resolve only the questions surfaced by feature evidence, the Phase
3.4 coverage gate, a backlog, or current-source conflict that block a
specific test, fix, refactor, protected change, bounded feature, runtime
verification, or release action.

Question generation is not a generic questionnaire exercise. Every
question must unlock or block a concrete engineering action.

25. Select a risk-backed area from the Phase 3.4 coverage review,
    backlog, defect, protected boundary, upcoming change, or meaningful
    test gap.

26. Generate only decision-relevant questions.

27. Name the accountable owner: product, backend, security, release,
    platform, design, accessibility, legal, or operations.

28. Record who decided, date, evidence/link, scope, what is now allowed,
    and what remains unresolved.

29. Capture decisions on a docs-only branch or equivalent isolated
    change before implementation whenever practical.

| **Decision capture field** | **Required content**                                               |
|----------------------------|--------------------------------------------------------------------|
| Decision                   | The approved behavior or policy, stated narrowly                   |
| Decided by                 | Accountable role/person                                            |
| Date                       | When the decision was made                                         |
| Evidence/link              | Ticket, meeting note, API contract, owner message, platform source |
| Scope/current phase        | Where the decision applies and where it does not                   |
| Tests/fixes now allowed    | Specific work unblocked                                            |
| Still Needs verification   | Runtime/backend/device/security/release uncertainty                |
| Docs to update             | Only documents future developers/AI will consult                   |

> Review the current feature, architecture maps, test map, backlog, and
> relevant source. Generate only owner/backend/security/release
> questions that block a specific test, fix, refactor, or feature. For
> each question state why it matters, owner needed, evidence available,
> blocked work, and safe next action. Do not answer by guessing.

# 11. Phase 3.6 — No-edit implementation audit

Goal: Compare approved decisions with the current active implementation
before changing code or tests.

28. Inspect the active runtime path and identify preserved, inactive,
    experimental, or postponed paths.

29. Trace normal, boundary, null, empty, malformed, error, and conflict
    cases.

30. Identify what existing tests actually prove.

31. Check whether opaque server values/order are preserved or normalized
    locally.

32. Identify crash, loop, corruption, privacy, security, or
    accidental-reactivation risks.

33. Determine whether a clean deterministic test seam exists.

34. Make no edits during the audit.

| **Classification**                 | **Meaning**                                                                    | **Default action**                               |
|------------------------------------|--------------------------------------------------------------------------------|--------------------------------------------------|
| Aligned and covered                | Implementation matches approved contract and focused evidence exists.          | No new test; preserve evidence.                  |
| Aligned but uncovered              | Important approved behavior lacks protection.                                  | Add one focused test if a clean seam exists.     |
| Partially aligned                  | Some cases match; others are incidental, unsafe, or undefined.                 | Split the finding; act only on approved portion. |
| Contradicts contract               | Source conflicts with accountable decision or safety rule.                     | Focused fix plus regression test.                |
| Not implemented                    | Approved behavior does not exist.                                              | Bounded feature/fix with acceptance criteria.    |
| Needs runtime/backend verification | Static evidence cannot establish actual behavior.                              | Gather the correct evidence; do not guess.       |
| Deferred/inactive path             | Code/design is preserved but outside active scope.                             | Do not reactivate, refactor, or test.            |
| No safe seam                       | Useful test requires brittle internals, broad refactor, or new infrastructure. | Document blocker and defer.                      |

> On a dedicated review branch, inspect the active path and nearby tests
> only. Make no edits. Classify each contract item as aligned/covered,
> aligned/uncovered, partial, contradiction, not implemented,
> runtime/backend verification, deferred, or no safe seam. Recommend
> exactly one next action.

## 11.1 Planning handoff after the no-edit audit

After Phase 3.6, the repository normally contains the owner answers,
reviewed architecture, the decision-to-source audit, classifications,
checkpoint, agent policy, and reusable skills. At this point, stop
switching to an external chat solely to generate increasingly detailed
Codex prompts.

Use the repository agent for the next plan because it can inspect the
current worktree, source, tests, reviewed contracts, and audit evidence
directly. The planning task should select one authorized audit item and
separate: already implemented, tests needed, behavior-preserving
seam/refactor, new behavior, runtime/device evidence, deferred work, and
blockers.

Approve the bounded plan when the task is material. Then use a fresh
implementation session and a separate fresh review session. The
implementation session follows the approved plan; the review session
independently checks the governing contract, diff, tests, documentation
impact, and stop condition.

Continue using an external general chat model only for unresolved
owner/product decisions, cross-project workflow design, comparison of
materially different strategies, or creation of a reusable
policy/template that does not yet exist in the repository.

Do not duplicate acceptance criteria, expected files, commands, or
output format in a new chat prompt when the reviewed plan, skill, or
checkpoint already owns them. A short execution envelope—authority, one
scope, boundaries, verification, durable evidence, and stop condition—is
sufficient.

# 12. Phase 4 — Skills system

Goal: Convert verified project patterns into concise reusable AI
behavior only after feature and architecture evidence exists.

## Phase 4A — Project-specific skills

- Protected-boundary preflight

- Characterization testing

- PR/diff review

- Documentation review

- Platform UI/resource parity

- ViewModel/state-owner changes

- Safe refactoring

- Feature planning

## Phase 4B — Selected official/platform skills

- Import only skills relevant to the project.

- Pin source repository and revision.

- Keep imported files separate from project-specific wrapper guidance.

- Do not install every available skill.

- Official skills remain lower authority than task scope and repository
  rules.

Each skill should contain: purpose, when to use, required context,
procedure, protected boundaries, verification, common mistakes, and
review checklist.

> Create a concise reusable AI skill for this project area. Base it on
> reviewed project patterns. Include purpose, when to use, required
> context, procedure, protected boundaries, verification, anti-patterns,
> and review checklist.

# 13. Reusable AI governance, skills, and agent hooks

Goal: Establish a reusable repository structure from the beginning so
policy, context, semantic skills, deterministic checks, client adapters,
hooks, publishing, and CI remain separate and maintainable.

The structure below is the recommended starting model for a new
brownfield project adopting this playbook. It is not a migration-only
layout and should not be introduced as an after-the-fact refactor when
the project can establish it during safe setup.

## 13.1 Recommended repository topology

AGENTS.md \# canonical mandatory agent policy  
AI_CONTEXT.md \# context and skill router  
AI_PLAYBOOK.md \# repository-specific advisory workflow  
CLAUDE.md \# thin Claude Code adapter, when used

.agents/  
├── skills/  
│ ├── protected-boundary-preflight/SKILL.md  
│ ├── characterization-tests/SKILL.md  
│ ├── documentation-review/SKILL.md  
│ ├── documentation-impact-assessment/SKILL.md  
│ ├── pr-review/SKILL.md  
│ ├── publish-ai-mr/SKILL.md  
│ └── official-\<provider\>-\<skill\> -\>
../vendor/\<provider\>/\<skill\>  
└── vendor/  
└── \<provider\>/  
├── README.md \# provenance and repository wrapper  
├── LICENSE  
└── \<imported-skill\>/

.claude/skills/\<skill\> -\> ../../.agents/skills/\<skill\>

docs/ai/  
├── SKILL_MAINTENANCE.md  
└── documentation-impact-map.tsv

scripts/  
├── check-documentation-impact.sh  
├── validate-ai-guidance.sh  
├── create-ai-mr.sh  
└── install-git-hooks.sh

.githooks/  
├── pre-commit  
└── pre-push

## 13.2 Authority and ownership layers

| **Layer**                                 | **Primary responsibility**                                                                    | **Must not do**                                                         |
|-------------------------------------------|-----------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| AGENTS.md                                 | Mandatory repository policy, protected boundaries, branch rules, and completion requirements. | Do not duplicate detailed skill procedures.                             |
| AI_CONTEXT.md                             | Select the smallest task-relevant documents and skills.                                       | Do not become an auto-load manifest or implementation authority.        |
| AI_PLAYBOOK.md                            | Explain the repository workflow and evidence model.                                           | Do not override AGENTS.md or verified current source.                   |
| .agents/skills/                           | Canonical project-owned skills and namespaced discovery adapters.                             | Do not duplicate imported content or silently grant authorization.      |
| .agents/vendor/                           | Pinned imported platform/provider content with provenance.                                    | Do not mix repository policy into imported skill bodies.                |
| .claude/skills/ and other client adapters | Thin exposure of canonical skills to a specific client.                                       | Do not duplicate business logic or become the source of truth.          |
| Deterministic scripts                     | Classify changed paths and validate structure.                                                | Do not invoke AI, edit docs, or make semantic correctness claims.       |
| Agent semantic skills                     | Interpret evidence, select documents, and perform read-only review.                           | Do not edit automatically or advance provenance without bounded review. |
| Git hooks                                 | Fast local hygiene, deterministic warnings, and objective blocking checks.                    | Do not create MRs, run LLMs, or hide remote side effects.               |
| CI/MR pipeline                            | Authoritative shared deterministic verification when available.                               | Do not replace human semantic approval or release evidence.             |
| Human approval                            | Authorize documentation edits, protected changes, and remote publication.                     | Do not treat unchecked AI output as evidence.                           |

## 13.3 Core reusable skills and evidence-derived skills

Recommended reusable core for most serious brownfield projects:

- protected-boundary-preflight — identify authorization, risk, owner,
  and evidence requirements before protected work.

- documentation-review — review selected current documents for evidence,
  provenance, currency, links, and overclaiming.

- documentation-impact-assessment — decide which current documents
  require review because of a planned or completed task.

- characterization-tests — protect existing deterministic behavior at
  the smallest useful seam.

- pr-review — review one focused diff for correctness, regressions,
  scope, verification, and protected-boundary drift.

- publish-ai-mr — prepare evidence in Stage 1, stop for approval, and
  perform deterministic publication only in Stage 2.

Project-, platform-, and architecture-specific skills should be created
only after reviewed evidence exists. Examples include Compose resource
parity, ViewModel/StateFlow conventions, SwiftUI localization parity,
state-owner conventions, camera workflows, or project-specific auth
refresh behavior. Do not copy these automatically into every repository.

## 13.4 Skill package and naming conventions

- Use lowercase-kebab-case directory names.

- For project-owned skills, the YAML frontmatter name must exactly match
  the directory name.

- Use direct functional names such as documentation-review or
  protected-boundary-preflight.

- Namespace imported adapters, for example official-android-camerax or
  official-apple-\<skill\>.

- Do not rename imported upstream frontmatter merely to match the
  adapter name.

- Each project-owned SKILL.md should state purpose, trigger conditions,
  required context, procedure, boundaries, verification, output
  contract, and common mistakes.

- Keep skills advisory; authorization still comes from the task and
  mandatory repository policy.

## 13.5 Documentation-impact workflow

Use four distinct layers rather than embedding semantic review in hooks:

Layer

Question answered

Typical result

Changed-path classifier

Which changed paths may affect which documentation surfaces?

none, possible, or definite candidate impact

Documentation-impact assessment

Which current documents actually require review, and why?

NO_DOCUMENTATION_IMPACT DOCUMENTATION_REVIEW_REQUIRED
DOCUMENTATION_UPDATE_REQUIRED NEEDS_VERIFICATION

Documentation review

Are the selected current documents accurate, evidenced, current, linked
correctly, and safe to reuse?

read-only findings and smallest required update scope

Human authorization

Should identified documentation changes or follow-up work proceed?

approved update, accepted no-edit result, explicit follow-up, or stop

- Do not assume AI_CONTEXT.md is the only affected document.

- Do not scan or rewrite the entire documentation tree by default.

- Do not edit historical evidence merely to remove old strings.

- Do not require documentation edits for every source change.

- Do not advance review dates or source revisions unless the stated
  bounded review actually occurred.

## 13.6 Planning and completion contracts

Before finalizing a relevant plan, the agent reports classification,
potentially affected current documents, historical documents to inspect
only, plan implications, and Needs verification. Before declaring an
implementation ready for review, the agent reports changed boundaries,
current documents reviewed, updates required or intentionally omitted,
evidence, and unresolved items.

This output contract is the portable cross-client baseline. It remains
effective even when a client has no reliable lifecycle-hook mechanism.

## 13.7 Agent lifecycle hooks and completion adapters

Agent hooks are optional early-warning and completion adapters. They
must call shared repository logic rather than implement a second review
system.

| **Lifecycle point**                         | **Agent-hook responsibility**                                                                                   | **Required behavior**                                                                                  |
|---------------------------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| After task understanding, before final plan | Run or consume the deterministic impact classifier and identify candidate documentation surfaces.               | Load only relevant context; flag protected boundaries; do not edit docs.                               |
| Before declaring implementation ready       | Require documentation-impact-assessment when candidate impact exists.                                           | Run documentation-review only for selected current docs; include the assessment in the final response. |
| Before creating completion artifacts        | Prevent unauthorized task.md, implementation_plan.md, walkthrough.md, raw reports, or repository scratch files. | Report artifacts rather than silently creating or deleting them.                                       |

- Codex baseline: AGENTS.md completion rule plus .agents/skills/. When
  the installed client exposes and the team verifies a project-local
  lifecycle contract, UserPromptSubmit may inject the standing reminder
  and Stop may run the classifier and validate the final-response
  contract. Trust and real-client acceptance remain required.

- Claude Code baseline: CLAUDE.md plus relative .claude/skills/
  adapters. A lifecycle hook may invoke the shared classifier and return
  its result to the active agent when supported.

- Antigravity baseline: shared completion rule plus explicit artifact
  prohibition. Its adapter should run the classifier before completion
  and must not create task or walkthrough artifacts unless requested.

- Other clients: implement only a thin adapter to shared policy, skills,
  and scripts.

- Client hooks must never edit documentation automatically, invoke
  publishing, or duplicate path mappings.

Agent-hook behavior is advisory and semantic. Repository correctness
must never depend only on a proprietary client hook.

### 13.7.1 Everyday prompt ergonomics

Once repository policy and a verified, trusted lifecycle adapter are
active, ordinary task prompts do not need to repeat the
documentation-impact instructions or name likely documents. The
repository workflow supplies the reminder, classification, semantic
assessment, selected-document review, completion check, and approval
request.

Example normal prompt: “Fix the locale persistence bug and add focused
regression coverage.”

- Mention documentation explicitly only when granting edit authority up
  front, naming an authoritative contract document, or supplying domain
  knowledge that deterministic path mappings may not contain.

- Smaller prompts are an intended benefit of the governance system, but
  only while the client hooks are enabled and trusted; AGENTS.md,
  publishing Stage 1, pre-push, and CI remain fallback layers.

### 13.7.2 Automatic workflow versus authorized editing

The workflow may perform these steps automatically:

- inject the standing documentation-impact reminder;

- run the deterministic changed-path classifier;

- ask the active agent to perform documentation-impact assessment;

- review only the selected current documents;

- validate that the final response reports the semantic result; and

- request approval when an unrequested documentation edit is required.

The workflow must not automatically authorize:

- documentation edits outside the task’s granted scope;

- changes to product, backend, security, release, or owner-controlled
  contracts;

- review-date or provenance advancement without a bounded review; or

- commit, push, MR creation, merge, or other remote effects.

Default approval behavior: read-only document review needs no extra
approval; an already-authorized relevant documentation update may
proceed in scope; an unrequested required update must stop for human
authorization.

## 13.8 Git hooks, CI, and shared deterministic scripts

| **Control**      | **Recommended responsibility**                                                                                                             | **Blocking policy**                                                                          |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| Pre-commit       | Fast branch/staged hygiene, secrets/sensitive files, prohibited artifacts, and diff checks.                                                | Block only objective local hygiene failures.                                                 |
| Pre-push         | Deterministic AI-guidance validation, documentation-impact classification, accepted-cost local verification, and protected-branch blocking | Block structural/script failures; warn for possible or definite semantic impact.             |
| CI/MR pipeline   | Run the same shared scripts using the real target branch and publish a stable summary.                                                     | Fail structural or malformed-output checks; do not fail solely for possible/definite impact. |
| Release pipeline | Perform protected signing, artifact, distribution, telemetry, and rollback verification.                                                   | Use protected credentials and owner-controlled approvals.                                    |

Centralize checks in reusable scripts such as
check-documentation-impact.sh and validate-ai-guidance.sh. Hooks, CI,
manual workflows, and publishing preparation should call those scripts
instead of copying their logic.

Each gate protects a different boundary:

- Agent lifecycle hook — protects task completion and final-response
  completeness.

- Publishing Stage 1 — protects the current branch evidence package and
  proposed MR description.

- Git pre-push — protects the exact local push with objective repository
  checks.

- CI/MR pipeline — protects the shared repository independently of local
  clients and hook installation.

When the publishing script executes git push, Git fires the configured
pre-push hook automatically. The temporary MR description file does not
trigger the hook, and the publishing script must not run semantic skills
itself.

If CI is unavailable, publishing Stage 1 plus pre-push and human MR
review provide a strong local fallback, but the missing shared
clean-environment result must remain Needs verification. An agent hook
alone is never a publication gate.

## 13.9 Two-stage explicit publishing

A reusable publishing skill should separate evidence preparation from
remote side effects:

- Stage 1: verify branch, worktree, committed scope, structural
  guidance, documentation-impact classification, semantic assessment
  status, actual tests/checks, risks, and reviewer focus.

- Stage 1: write the proposed MR description to an external temporary
  path and stop for explicit approval.

- Stage 2: rerun deterministic checks, invoke the repository publishing
  script, push without force, and create or reuse the MR.

- Never create the MR from pre-push, never merge, never enable
  auto-merge, and never store credentials in skills or descriptions.

## 13.10 Vendor and adapter conventions

- Store imported source under .agents/vendor/\<provider\>/.

- Pin source repository and revision, preserve license, record import
  date, and maintain a repository wrapper README.

- Keep repository precedence and routing in the wrapper README, not in
  imported SKILL.md files.

- Expose only selected imported skills through namespaced relative links
  under .agents/skills/.

- Point client adapters to .agents/skills/, not directly to vendor
  content.

- Use deterministic checksums or an equivalent integrity comparison
  during vendor refreshes.

- Do not import or expose every available upstream skill.

## 13.11 Reusable documentation automation package

The following artifacts are reusable patterns and may be copied as a
starter kit when the receiving repository adopts the same directory
contract:

Foundation phase runner plus one-document create/review templates.

Feature-document manifest, creation template, review template, and
guarded runner.

Architecture-map manifest, focused scope specifications,
create/read-only-review/promotion templates, and checkpoint-aware
runner.

Documentation checkpoint format and status vocabulary.

Graph discovery usage policy stating that generated relationships are
routing aids only.

Copy-as-is is appropriate only for truly platform-neutral policy text
and shell mechanics whose paths and command dependencies match the new
repository. In most projects, copy the files as a baseline commit and
immediately adapt repository paths, platform terminology, authority
documents, model invocation, status parsing, test commands, and
allowed-change rules.

Never copy these as universal project facts: feature manifests,
architecture ordering, graph override rows, source paths, product
contracts, test counts, reviewed revisions, checkpoint state, or
model/provider defaults. These are project-specific and must be
regenerated or edited from evidence.

Prefer a small reusable package over prompts pasted from chat history.
Version it, review changes to it like code, and let runners render the
current task from repository state.

## 13.12 Adoption rule for future projects

Use the governance capabilities in most brownfield projects, but do not
blindly copy every implementation-specific skill.

| **Adopt during safe setup**                                                                                                                                                                                          | **Add after discovery and evidence**                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Mandatory policy, context router, documentation review, documentation-impact assessment, protected-boundary preflight, PR review, explicit publishing, deterministic validator/classifier, and thin client adapters. | Characterization-testing refinements, platform skills, architecture-specific skills, feature-specific skills, imported official skills, client lifecycle hooks, and CI integrations appropriate to the repository. |

The goal is a small, enforceable, reusable control system—not the
largest possible skill catalog.

# 14. Phase 5 — Expanded testing safety net

Goal: Grow coverage around important behavior after seams, decisions,
and risks are understood.

35. Prioritize business, security, data integrity, lifecycle, and
    user-risk boundaries.

36. Use the smallest layer that can establish the desired evidence.

37. Introduce test infrastructure only with an explicit plan.

38. Use hand-written fakes when they are clearer than a framework.

39. Keep tests focused on approved or existing behavior.

40. Update test maps only when meaningful coverage was actually added
    and run.

| **Select a test because…**                                  | **Do not select a test because…**                                          |
|-------------------------------------------------------------|----------------------------------------------------------------------------|
| It protects a known risk or owner decision.                 | The phase number says “add more tests.”                                    |
| It supports an upcoming refactor or feature.                | A file exists and is currently untested.                                   |
| It characterizes a bug-adjacent edge case.                  | Coverage percentage alone would increase.                                  |
| It closes a verification backlog item through a clean seam. | It requires new dependencies or broad production changes without approval. |

> Identify the next safest tests for this feature or layer. Prefer
> risk-backed behavior, approved decisions, existing seams, and
> understandable fakes. List any required infrastructure separately
> before adding dependencies or production seams.

# 15. Phase 6 — Controlled refactoring

Goal: Improve one isolated area without changing public behavior.

41. Explain current behavior before proposing changes.

42. Confirm or add protecting tests first.

43. Use small reversible steps.

44. Edit only authorized files.

45. Do not mix feature work, dependency upgrades, or unrelated cleanup.

46. Review the complete diff and run required checks.

> I want to refactor this code safely. First explain current behavior,
> identify smells, propose reversible steps, identify tests required
> before editing, and explain risks. Preserve public behavior.

# 16. Phase 7 — Bounded feature or defect implementation

Goal: Implement one approved behavior change using the established
context, decision, testing, and review workflow.

47. Write acceptance criteria before coding.

48. Confirm active and deferred paths.

49. Choose the safest option that fits existing architecture.

50. List exact allowed and forbidden files.

51. Add regression or behavior tests.

52. Implement in small reviewable steps.

53. Update only useful documentation after behavior stabilizes.

> Implement this bounded feature or fix in the existing architecture.
> Restate the requirement, acceptance criteria, approved decision,
> active path, files likely to change, protected boundaries, test plan,
> and safest implementation option before coding.

# 17. Phase 8 — AI-assisted review and explicit publishing

Goal: Make every AI-assisted change reviewable and ensure remote side
effects are explicit.

## Review the diff, not the whole project

- Confirm scope matches changed files.

- Trace changed behavior through callers, state/data boundaries, and
  tests.

- Prioritize defects, regressions, security, lifecycle/concurrency, data
  integrity, performance, accessibility, and missing verification.

- Separate blocking findings, non-blocking improvements, questions, and
  Needs verification.

- Verify branch, files, tests, commit, push, and MR from actual tool
  output.

## Explicit publish model

| **Layer**              | **Responsibility**                                                                                                                         |
|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Local command          | Fast feedback while editing                                                                                                                |
| Pre-commit             | Fast branch/staged hygiene and scratch/sensitive-file checks                                                                               |
| Pre-push               | Deterministic AI-guidance validation, documentation-impact classification, accepted-cost local verification, and protected-branch blocking |
| Publish script/command | Clean-worktree validation, safe push, duplicate-MR detection, explicit MR creation, no auto-merge                                          |
| MR pipeline            | Authoritative shared deterministic verification before merge; semantic documentation review remains explicit                               |
| Release pipeline       | Protected signing, upload, and delivery verification                                                                                       |

- Never hide MR creation inside pre-push.

- Never force-push by default.

- Never auto-merge or auto-approve.

- Create temporary MR descriptions outside the repository.

- Detect and reuse an existing open MR instead of creating duplicates.

- Require the MR description to state purpose, scope, files, protected
  areas, actual verification, blockers, risk, and reviewer focus.

> Review this diff as a senior native mobile engineer. Return must-fix
> findings, should-fix findings, optional suggestions, test gaps,
> questions, protected-boundary concerns, and final risk level. Cite
> tight file and line ranges.

# 18. Phase 9 — CI/CD, runtime, and release verification

Goal: Make verification repeatable while keeping merge verification
separate from delivery and signing.

54. Document local commands before automating them.

55. Centralize shared checks in reusable scripts rather than duplicating
    logic in hooks and CI.

56. Keep pre-commit fast.

57. Allow pre-push to run heavier checks only when the team accepts the
    cost.

58. Treat the MR pipeline as the authoritative merge gate.

59. Restrict signing, beta upload, store delivery, and production
    credentials to protected release workflows.

60. Do not claim release readiness from source or local unit tests
    alone.

| **Evidence stage**        | **Typical mobile evidence**                                                               |
|---------------------------|-------------------------------------------------------------------------------------------|
| Source/configuration      | Build settings, manifests/entitlements, code paths, resource/source-set layout            |
| Local deterministic tests | Unit, mapper, reducer, repository/data-source, resource/config tests                      |
| Simulator/emulator/device | Lifecycle, permissions, camera, notifications, accessibility, UI, navigation              |
| Backend/integration       | Real error shapes, auth refresh, push association, remote ordering/cursors                |
| Artifact inspection       | APK/AAB/IPA contents, dependency/resource packaging, symbols, minification/stripping      |
| Release delivery          | Signing/provisioning, TestFlight/internal track, telemetry, rollout and rollback evidence |

> Analyze this CI/CD and release setup. Explain current local and remote
> gates, missing evidence, safe improvements, local reproduction
> commands, protected secrets/signing boundaries, and what remains
> runtime or release verification. Do not rewrite the pipeline until the
> plan is approved.

# 19. Platform mapping — Android and iOS

The core workflow is platform-neutral. Use platform-specific evidence
and commands only in the companion mapping below.

| **Concern**         | **Android examples**                                         | **iOS examples**                                                            |
|---------------------|--------------------------------------------------------------|-----------------------------------------------------------------------------|
| Build system        | Gradle, AGP, build types, flavors, version catalogs          | Xcode, xcodebuild, schemes, configurations, Swift Package Manager/CocoaPods |
| UI                  | Jetpack Compose, Views                                       | SwiftUI, UIKit                                                              |
| State/lifecycle     | ViewModel, StateFlow/Flow, SavedStateHandle                  | Observable/Observation, Combine, async/await, actors, view lifecycle        |
| Persistence         | DataStore, Room, SharedPreferences, Android Keystore         | UserDefaults, Core Data/SwiftData/SQLite, Keychain                          |
| Networking          | Retrofit/OkHttp, interceptors/authenticators                 | URLSession, middleware/client abstractions, authentication refresh          |
| Navigation          | Navigation Compose, intents, deep links                      | NavigationStack/coordinators, URL schemes, universal links                  |
| Notifications       | FCM, notification permission, services/channels              | APNs, UNUserNotificationCenter, background modes                            |
| Camera/scanning     | CameraX, ML Kit                                              | AVFoundation, Vision/VisionKit                                              |
| Accessibility       | TalkBack, font scale, semantics, RTL                         | VoiceOver, Dynamic Type, accessibility traits, RTL                          |
| Testing             | JUnit, Compose UI tests, instrumented tests, emulator/device | XCTest, XCUITest, simulator/device                                          |
| Signing/release     | Keystores, signing configs, Play tracks, APK/AAB             | Certificates, provisioning profiles, entitlements, TestFlight, IPA          |
| Security boundaries | Exported components, PendingIntent, network security config  | Entitlements, keychain access groups, ATS, URL handling                     |

## 18.1 Platform-neutral verification wording

| **Avoid generic playbook wording** | **Prefer**                                                         |
|------------------------------------|--------------------------------------------------------------------|
| Run ./gradlew testDebugUnitTest    | Run the project’s full local unit-test task                        |
| Run assembleDebug                  | Run the project’s application compile/build gate                   |
| Inspect APK/AAB                    | Inspect the signed or unsigned application artifact as appropriate |
| Use emulator                       | Use an approved simulator, emulator, or physical device            |
| Check Compose strings              | Check the platform’s localized resource and visible-text parity    |
| Verify Play Store release          | Verify the approved beta/store distribution workflow               |

# 20. Artifact and documentation matrix

| **Artifact class**           | **Examples**                                                                                                                                                        | **Lifecycle**                                                                                     |
|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| Mandatory operating context  | Agent rules, context index, project overview, modules, testing map                                                                                                  | Long-lived; keep concise and current                                                              |
| Feature context              | Feature docs, active/deferred path notes                                                                                                                            | Update when behavior/evidence/risk changes                                                        |
| Architecture context         | Core maps plus adaptation, background work, permissions, configuration, rollout, analytics/observability, performance, and domain-boundary coverage when applicable | Update only when cross-feature evidence changes                                                   |
| Architecture coverage record | Phase 3.4 cross-feature classifications, owners, blockers, and routing                                                                                              | Refresh after material architecture discovery or before a major architecture-sensitive workstream |
| Decision records             | Verification questions, accountable answers                                                                                                                         | Keep while decision remains relevant                                                              |
| Audit outputs                | No-edit implementation evidence table                                                                                                                               | Usually temporary or summarized into durable docs                                                 |
| Implementation plans         | Refactor or feature plan                                                                                                                                            | Task-scoped; remove/archive when no longer useful                                                 |
| Testing evidence             | Testing map, foundation summary, manual QA checklist                                                                                                                | Update only for meaningful verified coverage                                                      |
| Workflow assets              | Skills, prompts, shared scripts, MR template                                                                                                                        | Long-lived if reused and validated                                                                |
| Temporary artifacts          | Scratch notes, generated reports, raw logs, MR description files                                                                                                    | Keep outside repo unless explicitly approved; delete after use                                    |

# 21. Minimum verification matrix

| **Change type**   | **Minimum evidence**                                                                      | **Important note**                                                  |
|-------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Docs only         | Diff/format/link checks appropriate to documentation                                      | Do not run expensive builds unless docs tooling requires them.      |
| Focused unit test | Narrow test, full local unit task, compile/build gate, diff check                         | Use project-specific commands and report actual results.            |
| Production fix    | Regression test where practical, focused test, full unit task, build, diff review         | Add lint/integration/device checks when the boundary requires them. |
| Refactor          | Protecting tests, focused/full suite, build, complete diff review                         | Public behavior must remain unchanged.                              |
| Workflow script   | Syntax/static checks, help/dry-run, safe rejection cases, diff check                      | Avoid remote side effects during initial validation.                |
| Protected area    | Approved preflight, narrow tests, and required runtime/security/device/release validation | Static unit evidence is often insufficient.                         |
| Release change    | Artifact, signing/provisioning, distribution, telemetry, rollback evidence                | Requires explicit owner approval and protected credentials.         |

# 22. Stop conditions and anti-patterns

- Stop when the next test duplicates existing coverage.

- Stop Phase 3 progression when a material cross-cutting concern lacks a
  current evidence home, classification, owner, or routing decision.

- Stop when a test requires reflection, brittle internals, broad
  production refactoring, or new infrastructure without approval.

- Stop when remaining behavior requires backend, runtime, device,
  security, accessibility, or release evidence.

- Stop when the owner has deferred the path or feature.

- Do not apply every audit finding as a fix.

- Do not treat current implementation as correct merely because it
  exists.

- Do not treat owner intent as implemented merely because it is
  documented.

- Do not combine decision capture, audit, multiple fixes, refactoring,
  dependency changes, CI changes, and release automation in one MR.

- Do not trust AI claims about files, tests, branches, commits, pushes,
  or MRs without actual tool output.

- Do not create task.md, walkthrough.md, scratch files, generated audit
  exports, or artifact metadata in the repository unless explicitly
  intended.

- Do not paste live tokens, credentials, certificates, private keys,
  production data, or reusable authorization headers into prompts or
  docs.

## 22.1 Stop generating detailed external prompts

Stop using ChatGPT as a prompt-writing intermediary when all of the
following are true:

AGENTS.md or equivalent defines authority, safety boundaries, and
completion behavior.

The context index routes the agent to reviewed project, feature,
architecture, and testing evidence.

The checkpoint names exactly one next authorized task.

A reviewed decision contract and Phase 3.6 audit classify the relevant
gap.

An approved implementation plan or reusable planning skill defines
acceptance and verification.

At that point, start a fresh repository session with a compact
instruction to execute the next authorized task. More detail can reduce
quality by freezing guessed file lists, duplicating stale criteria, and
consuming context that should be used for source inspection.

Resume external prompt design only when the repository lacks one of
those control artifacts or when a human decision must be made outside
the coding agent.

# 23. Master checklists

## Before closing Phase 3

- Every material cross-cutting concern has a current documentation home
  or an explicit `Not observed` / `Not applicable` classification.

- UI adaptation, background execution, permissions,
  configuration/environments, feature flags, analytics/privacy,
  observability/crash reporting, performance, and domain/module
  ownership were explicitly considered.

- Each `Needs verification` item names the owner, blocked work, and next
  evidence layer.

- New current documents are routed through the context index.

- The living-review question found no unrepresented material concern, or
  each discovered concern was routed.

## Before generating verification questions

- A documented risk, backlog item, protected concern, upcoming change,
  or test gap exists.

- Relevant reviewed docs, the Phase 3.4 coverage record, and current
  source are selected through the context pipeline.

- Each question will unlock a concrete action.

- Accountable owners are known or named.

## Before editing code

- Decision documentation is available when required.

- The active path and nearby deferred paths were identified.

- Audit findings were classified.

- One focused action is selected.

- Allowed and forbidden files are explicit.

- Required tests and runtime evidence are known.

## Before publishing

- Every changed line was reviewed.

- Only intended files are staged.

- Actual verification commands and results are recorded.

- No secrets, signing materials, private data, or unsafe logs were
  added.

- Protected areas are declared.

- Known blockers remain visible.

- The branch is pushed explicitly and the MR is not auto-merged.

# 24. Reusable prompt chain

## A. Brownfield onboarding

> Act as a senior native mobile engineer joining this existing project.
> Do not modify code. Explain what the project does, how it is
> organized, what is verified, and what needs verification. Cite
> evidence for material claims.

## B. Documentation review

> Review these generated documents as reusable AI context. Identify
> unsupported claims, broken links, missing provenance, stale
> assumptions, overconfident wording, and whether each file is safe as
> orientation context.

## C. Feature documentation

> Explain this feature end to end from UI to data source. Include state,
> errors, navigation, persistence, lifecycle/concurrency, active and
> deferred paths, existing tests, risks, and recommended next evidence.
> Do not suggest improvements until current behavior is documented.

## D. Architecture coverage review

> Review the completed Phase 3 maps against the reusable cross-feature
> architecture coverage checklist. For each concern classify Verified,
> Needs verification, Not observed, or Not applicable; cite the evidence
> home; identify the owner and blocker; and route missing current
> documentation, owner questions, and decision/source contradictions. Do
> not create empty documents or infer non-applicability from absence.

## E. Generate verification questions

> Review the current feature, architecture, test map, backlog, and
> relevant source. Generate only questions that block a specific test,
> fix, refactor, feature, or protected action. Name the owner and safe
> next action. Do not answer by guessing.

## F. Record decisions

> On a docs-only change, record accountable answers in the decision
> register, backlog, and only the feature/architecture/testing documents
> whose sequencing or contract changed. Preserve remaining uncertainty.
> Do not modify code or tests.

## G. Audit decisions against code

> Inspect the active path and nearby tests only. Make no edits. Return
> an evidence table with contract item, implementation evidence, test
> evidence, classification, risk, and exactly one recommended next
> action.

## H. Implement one fix or test

> Make the smallest authorized change on the correct focused branch. Add
> regression or characterization coverage. Do not broaden contracts or
> reactivate deferred paths. Run focused and project-required checks and
> update only useful docs.

## I. Bug investigation

> Given this report, logs, decisions, and relevant files, produce ranked
> hypotheses with evidence, counter-evidence, and the smallest
> experiment for each. Do not jump directly to a fix.

## J. PR review

> Review this diff as a senior native mobile engineer. Return blocking
> findings, non-blocking improvements, optional suggestions, test gaps,
> questions, protected-boundary concerns, and final risk level.

## K. Publish handoff

> After human diff review, stage intended files, commit conventionally,
> push safely, and create or reuse an MR with an external reviewed
> description file. Do not force-push, duplicate, approve, or merge the
> MR.

## L. Plan the next authorized audit item

> Read the agent policy, context index, checkpoint, reviewed decision
> contract, Phase 3.6 audit, applicable skills, and directly relevant
> source/tests. Produce a plan only. Select one authorized item;
> classify existing implementation, tests, behavior-preserving
> refactor/seam work, new behavior, runtime evidence, deferred work, and
> blockers. Define verification and stop conditions. Do not edit.

## M. Execute an approved repository plan

> Implement the next approved incomplete task from the checkpoint and
> reviewed plan. Inspect current source before editing. Modify only
> files necessary for the authorized contract, preserve unrelated work,
> run focused and repository-required verification, update durable
> evidence, and stop at the approved boundary. Do not publish unless
> separately authorized.

## N. Independent implementation review

> In a fresh session, independently review the completed task against
> the decision contract, Phase 3.6 audit, approved plan, agent policy,
> and diff. Verify tests and documentation impact, identify blocking and
> non-blocking findings, classify remaining runtime or owner evidence,
> and update the checkpoint only when completion is supported. Do not
> broaden the implementation.

## O. Advance the checkpoint

> Update only the durable workflow checkpoint after the required review
> gate passes. Record the completed artifact or batch, evidence summary,
> remaining Needs verification, the next single authorized task, and
> prohibited work. Do not create or implement the next task in the same
> checkpoint-advance operation.

# 25. Suggested working cadence

| **Time**  | **Activity**             | **Example**                                                        |
|-----------|--------------------------|--------------------------------------------------------------------|
| 10–15 min | Load reviewed context    | Context index, feature doc, decision record, relevant skill        |
| 30–60 min | Perform one bounded task | One doc, one audit, one focused test, one fix, or one diff review  |
| 15–30 min | Validate evidence        | Inspect diff, run checks, review runtime artifact if required      |
| 10 min    | Update durable context   | Record useful decision, evidence, blocker, prompt, or skill lesson |

# 26. Example adoption sequence

| **Stage** | **Focus**                       | **Proof of progress**                                                                               |
|-----------|---------------------------------|-----------------------------------------------------------------------------------------------------|
| 1         | Safe setup and discovery        | Reviewed overview/modules/features/testing/debt docs                                                |
| 2         | Provenance and first tests      | Context index plus one or two meaningful passing seams                                              |
| 3         | Feature and architecture maps   | Important active/deferred paths and protected boundaries understood                                 |
| 4         | Skills and AI governance system | Canonical skills, vendor separation, adapters, impact assessment, shared scripts, and hook strategy |
| 5         | Selective implementation        | One focused test/fix/refactor/feature closes a real risk                                            |
| 6         | Review and automation           | Explicit MR publish flow and shared merge verification                                              |
| 7         | Reusable extraction             | Project lessons become generic prompts/skills without project-specific leakage                      |

# 27. Final rule

For an existing mobile project, AI should first become a reader, then a
documenter, then a tester, then an architecture and decision auditor,
then a skill/tooling assistant, and only after that a refactoring or
feature-coding assistant.

The workflow succeeds when it reduces uncertainty and risk—not when it
produces the largest number of documents, tests, skills, or changes. Use
it on legacy and active production-style Android and iOS projects,
review every AI output, and stop when the next evidence belongs to a
different owner or verification layer.

# Appendix A — What changed in v4.4

- Integrated architecture completeness into Phase 3 rather than
  appending a detached checklist.
- Added Phase 3.4 as a coverage gate before verification questions and
  no-edit auditing.
- Expanded Phase 3 outputs to cover UI adaptation, background execution,
  permissions, configuration/environments, feature flags/rollout,
  analytics/privacy, observability/crash reporting, performance,
  domain/feature ownership, and dependency isolation when applicable.
- Added four evidence-aware classifications: Verified, Needs
  verification, Not observed, and Not applicable.
- Added routing rules from coverage gaps to documentation updates, Phase
  3.5 owner questions, Phase 3.6 audits, or later runtime/release
  evidence.
- Updated lifecycle, artifacts, prompts, master checklists, and stop
  conditions so the coverage gate cannot be bypassed by merely
  generating expected filenames.
- Preserved the anti-sprawl rule: extend the closest current document
  and create a new document only when the concern is material and has no
  suitable home.

Integrated repository-owned documentation runners, manifests, focused
scope specifications, and checkpoint sequencing into Phases 1–3 rather
than treating them as optional appendices.

Added Graphify guidance: discovery/routing only, direct source
verification, project-owned limitation supplements, and no edits to
generated graph output.

Defined the Phase 3.6 transition point at which external prompt
generation should stop and Codex/repository agents should plan,
implement, and review from durable context.

Added reusable cross-project prompts for planning, implementation,
independent review, and checkpoint advancement.

Classified workflow files into reusable starter-kit artifacts versus
project-specific manifests, overrides, paths, revisions, and contracts.
