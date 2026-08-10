# Skill: Bounded Feature Implementation v1

## Purpose

Execute an explicitly authorized, dependency-valid group of Android implementation tasks and produce the task-level verification and evidence required to close that group.

This skill is the production-code mutation procedure. It applies already-approved product and technical authority; it does not create or approve that authority.

It is intentionally narrower than `feature-implementation-convergence`. This skill implements only the authorized task group and performs the immediate checks needed to know whether those tasks can be honestly marked complete. `feature-implementation-convergence` remains the independent, whole-feature post-implementation audit across the complete coherent diff and all evidence.

## Preconditions

Verify before editing production code:

- feature contract is owner-approved;
- implementation plan is owner-approved and independently reviewed;
- implementation task set is owner-approved and independently reviewed;
- `IMPLEMENTATION_READINESS_AUDIT.md` is current and permits the authorized slice;
- explicit implementation authorization is recorded for the exact feature/slice and task IDs;
- all dependencies for the selected tasks are complete or explicitly included in the same authorized coherent group;
- applicable protected-boundary and platform preflights are satisfied;
- current authority documents do not contradict one another;
- the worktree and branch state are understood and unrelated changes will not be overwritten.

If any prerequisite is missing or contradictory, do not implement the affected task.

## Required Inputs

Read only the inputs needed for the authorized task group, including as applicable:

- `AGENTS.md` and required policy modules;
- `AI_CONTEXT.md` and active playbook routing;
- owner decision and implementation-authorization record;
- approved feature contract;
- approved implementation plan;
- approved implementation tasks;
- current `IMPLEMENTATION_READINESS_AUDIT.md`;
- architecture spine and applicable ADRs;
- approved design authority, screen contracts, and exact artifacts;
- applicable Android readiness skills;
- current source, tests, project configuration, package graph, and evidence policy.

Do not load unrelated feature material merely because it exists.

## Required Output

Modify only artifacts authorized by the selected tasks. These may include, when the task explicitly requires them:

- production Kotlin/Java source;
- tests and fixtures;
- resources and localization catalogs;
- persistence schemas and migrations;
- project, target, package, entitlement, plist, or capability configuration that has already passed the required protected-boundary authorization;
- task-status and evidence references;
- verification artifacts and implementation-impacted documentation.

Return exactly one execution verdict:

- `TASK GROUP IMPLEMENTED`
- `TASK GROUP PARTIALLY IMPLEMENTED`
- `BLOCKED BY AUTHORITY OR SCOPE`
- `BLOCKED BY DEPENDENCY`
- `BLOCKED BY IMPLEMENTATION DEFECT`
- `BLOCKED BY PROTECTED BOUNDARY`
- `BLOCKED BY MISSING EVIDENCE`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

`TASK GROUP IMPLEMENTED` means only that the selected authorized tasks satisfy their own completion gates with matching evidence. It does not mean feature convergence, owner acceptance, merge approval, signing approval, or release authorization.

## Execution Procedure

### 1. Bind the Authorized Task Group

Record:

- feature ID;
- exact task IDs;
- authorization source;
- included and excluded scope;
- prerequisite task state;
- required stop conditions;
- protected boundaries involved;
- exact evidence obligations.

Do not expand the group because adjacent work appears convenient.

### 2. Inspect Before Editing

Inspect the current repository implementation at every affected boundary before making changes.

Confirm:

- actual module/source-set/package ownership;
- existing dependency direction;
- existing state, navigation, persistence, and composition patterns;
- current tests and fixtures;
- unrelated worktree changes;
- whether task assumptions still match repository facts.

If the repository materially contradicts the approved plan or task, stop instead of improvising a new architecture.

### 3. Run Only Applicable Preflights

Before the relevant mutation, run the readiness procedure required by the selected task, such as:

- `android-project-structure-readiness`;
- `kotlin-coroutines-readiness`;
- `compose-screen-readiness` or `android-views-screen-readiness`;
- `android-persistence-migration-readiness`;
- `android-localization-rtl-readiness`;
- `android-adaptive-accessibility-readiness`;
- `android-permission-capability-readiness`;
- `protected-boundary-preflight`.

Do not rerun unrelated whole-feature review procedures as ritual.

### 4. Implement the Smallest Coherent Change

For each task, implement only the approved behavior and mechanism.

Preserve:

- accepted module/source-set/package ownership;
- dependency direction and composition root;
- presentation-state ownership and lifecycle-aware state ownership;
- structured concurrency and cancellation;
- navigation/restoration ownership;
- repository and persistence boundaries;
- approved localization, adaptive, accessibility, privacy, and capability behavior;
- fail-closed protected configuration.

Do not:

- invent product behavior or validation;
- reopen accepted ADRs;
- introduce later-feature placeholders;
- create service locators or hidden global state;
- perform side effects from declarative rendering;
- introduce unowned tasks or lifecycle-escaping async work;
- use preview/test/demo dependencies in production composition;
- manufacture provider success, identifiers, authorization, receipts, attestation, or durable behavior;
- silently fall back to simulated success;
- broaden cleanup/refactoring beyond what the task requires.

### 5. Implement Task-Named Verification

Add or update only the tests and evidence mechanisms required to prove the selected tasks.

Prefer the narrowest valid layer first. Run the exact task-defined command/procedure and environment. Record actual results, not intended results.

Examples may include focused unit/state tests, repository or migration tests, UI tests, simulator/device scenarios, TalkBack checks, lifecycle/relaunch checks, or platform configuration inspection when the task requires them.

Do not substitute source inspection, previews, snapshots, compilation, or host tests for runtime-only claims.

### 6. Fix Defects Inside the Authorized Task Scope

When task verification exposes an implementation defect caused by the selected work, repair it if the repair stays within the authorized task boundary and accepted plan.

Stop and escalate when the fix would require:

- new product behavior;
- architecture or ADR amendment;
- a new protected permission/capability/service;
- expansion into an unauthorized task;
- changing an owner-approved acceptance criterion;
- fabricating or weakening evidence.

### 7. Perform Task-Closure Checks

Before marking a selected task complete, verify only that task's completion contract:

- objective and acceptance criteria are satisfied;
- required tests/procedures actually ran;
- environment/destination is named;
- expected and actual result are recorded;
- evidence exists at the declared path;
- limitations and unrun layers are explicit;
- no prohibited scope entered the task diff;
- no obvious production fake, bypass, or test/preview binding was introduced by the selected changes;
- protected changes match their approved authorization;
- documentation impact from the selected task is synchronized where required.

This is a local execution sanity check, not the independent whole-feature convergence review.

### 8. Review the Bounded Diff

Inspect the coherent diff created for the selected task group for:

- accidental unrelated edits;
- generated, Gradle, manifest, or project-file churn;
- duplicated mechanisms;
- obvious ownership/dependency violations;
- incomplete call-site updates;
- missing tests/evidence;
- secrets or sensitive values;
- temporary debug/sample code.

Do not claim that this bounded diff review satisfies `feature-implementation-convergence` or final `pr-review`.

### 9. Update Task Evidence and Stop

Update only permitted task/evidence/documentation fields with verified facts.

For each task report:

- status;
- files changed;
- behavior implemented;
- tests/checks actually run;
- exact commands/sessions;
- environment/destination;
- expected and actual outcome;
- evidence artifacts;
- limitations and unrun layers;
- blockers or follow-up task IDs.

Then stop at the authorized task-group boundary.

## Separation from Feature Implementation Convergence

`bounded-feature-implementation` owns:

- production mutation for explicitly authorized tasks;
- task-local preflights required before those mutations;
- focused tests and runtime procedures named by those tasks;
- fixing defects discovered within the same authorized task scope;
- task-level evidence capture and truthful task closure;
- bounded diff hygiene.

`feature-implementation-convergence` owns, after implementation:

- independent whole-feature task-completion audit;
- end-to-end contract-to-implementation traceability;
- complete plan/architecture/design conformance review;
- cross-task and cross-cutting completeness;
- broad production-composition/fake detection;
- whole-feature localization/RTL, accessibility, adaptive, lifecycle, persistence, privacy, and runtime evidence review;
- coherent feature diff and documentation synchronization assessment;
- creation/update of `READINESS_REPORT.md` and the convergence verdict.

Do not duplicate those convergence duties during each implementation slice unless the selected task explicitly requires the same check for its own completion or a newly introduced change creates an immediate safety/integrity risk.

## Stop Conditions

Stop immediately for:

- missing or mismatched implementation authorization;
- failed prerequisite or dependency;
- stale/contradictory contract, plan, task, ADR, design, or readiness authority;
- required protected-boundary approval not present;
- task requiring behavior not defined by authority;
- required repository target/path/contract not existing as planned;
- verification exposing a fix outside authorized scope;
- inability to produce required evidence;
- request to merge, sign, upload, distribute, release, access production, or mutate a remote protected system without separate authorization.

## Completion Rule

A task may be marked complete only when its approved outcome exists and its own named verification/evidence obligations are satisfied. Otherwise leave it open or blocked.
