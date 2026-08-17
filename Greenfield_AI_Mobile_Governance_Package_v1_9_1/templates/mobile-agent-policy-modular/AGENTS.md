# AGENTS.md — Mobile Repository Policy

> Reusable template. Replace or remove every bracketed value. This file is the repository's constitution-equivalent stable-principles authority unless an owner-approved decision names another path.

## Status

- Product: [fill in]
- Mode: [greenfield / brownfield]
- Platforms: [Android / iOS / both]
- Accountable owner: [fill in]
- Base branch: [fill in]
- Initial locales and fallback: [fill in]
- Feature contract: `docs/features/<feature-id>/FEATURE_CONTRACT.md`
- Implementation plan: `docs/features/<feature-id>/IMPLEMENTATION_PLAN.md`
- Implementation tasks: `docs/features/<feature-id>/IMPLEMENTATION_TASKS.md`
- Readiness report: `docs/features/<feature-id>/READINESS_REPORT.md`
- Evidence root: `docs/verification/<feature-id>/`

This template must not be used to infer project facts.

## Authority

1. Current explicit task scope and accountable repository-owner direction.
2. This root `AGENTS.md`.
3. Approved owner decisions and current owner-approved feature contracts.
4. Accepted architecture decisions, architecture spine, and design contracts.
5. Verified implementation plus matching test, runtime, service, archive, and release evidence.
6. `AI_CONTEXT.md` for routing, current phase, canonical paths, and evidence status.
7. `AI_PLAYBOOK.md`, policy modules, templates, and installed skills.
8. Imported vendor guidance.

Skills explain procedures; they do not authorize work. Templates shape artifacts; they do not establish project facts. Unresolved conflicts are `Needs verification` or `Needs owner decision` and block any slice that would encode an arbitrary choice.

## Mandatory lifecycle

Feature input  
→ contract authoring  
→ independent contract review  
→ owner contract approval  
→ plan authoring  
→ independent plan review  
→ owner plan approval  
→ task authoring  
→ independent task review  
→ owner task approval  
→ readiness gate  
→ explicit implementation authorization  
→ bounded feature implementation  
→ task evidence closure  
→ implementation convergence  
→ `READINESS_REPORT.md`  
→ applicable final-readiness evidence closure  
→ independent readiness review  
→ owner feature acceptance  
→ separate release authorization.

No stage silently authorizes the next protected stage.

- Contract approval does not authorize implementation.
- Plan approval does not authorize task execution.
- Task approval does not authorize implementation.
- Implementation completion does not establish feature acceptance.
- Final-readiness evidence closure completes applicable deferred manual/device/platform proof; it does not authorize acceptance or release.
- Feature acceptance does not authorize signing, distribution, or publication.

## Core rules

- Start from [base branch] and use one focused task branch. Never work directly on protected branches.
- Load only task-relevant current context through `AI_CONTEXT.md`.
- Do not invent requirements, decisions, verification results, commands, files, owners, runtime behavior, support claims, evidence, or approval.
- Keep unrelated worktree changes visible. Never hide, reset, discard, rewrite, or absorb them without authorization.
- Keep product behavior in feature contracts, technical mechanisms in plans and ADRs, bounded executable obligations in tasks, and operational policy in `AGENTS.md`.
- Do not create production code, tests, schemas, migrations, targets, or project files while authoring contracts, plans, or tasks.
- Do not implement before explicit implementation authorization.
- Keep platform/application hosts thin.
- Keep production composition free of fakes, test bindings, previews, no-op mechanisms, dead routes, unused template code, and silent simulated success.
- Every completed task requires matching current evidence.
- Missing runtime evidence keeps runtime-only work open.
- Do not claim device, backend, accessibility, security, performance, signing, archive, or release behavior from static or unit evidence alone.

## Governance consistency

Before planning, task generation, implementation, convergence, feature acceptance, and release review, verify that current contracts, plans, tasks, owner decisions, ADRs, architecture maps, design authority, readiness gates, `AI_CONTEXT.md`, evidence paths, and authorization records agree.

A stale or contradictory current artifact blocks affected work.

## Protected boundaries

Identity, authentication, authorization, secrets, sensitive data, destructive persistence, public/backend contracts, permissions, capabilities, manifests, entitlements, external services, analytics, billing, health or regulated behavior, signing, production configuration, distribution, and release are protected.

Run `protected-boundary-preflight` before protected work. Missing protected configuration must fail closed.

A dependency, configuration file, manifest entry, plist, entitlement, or provider declaration does not itself authorize use.

## Required policy routing

Always read the root `AGENTS.md` and `AI_CONTEXT.md`. Then load only the policy modules needed for the current lifecycle stage:

- `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` — contract, plan, task, implementation, convergence, and readiness work.
- `.agents/policies/GOVERNANCE_LIFECYCLE.md` — contract/plan/task authoring or governance/status review.
- `.agents/policies/IMPLEMENTATION_POLICY.md` — production implementation and convergence.
- `.agents/policies/EVIDENCE_AND_COMPLETION.md` — task verification, convergence, readiness, or any evidence claim.
- `.agents/policies/PROTECTED_BOUNDARIES.md` — only when the feature/task touches a protected boundary or its risk signals require preflight.
- `.agents/policies/android/ANDROID_ENGINEERING_POLICY.md` — Android planning, implementation, or platform review.
- `.agents/policies/ios/IOS_ENGINEERING_POLICY.md` — iOS planning, implementation, or platform review.

Do not load every policy module ceremonially. `AI_CONTEXT.md` routes applicable skills, ADRs, design contracts, evidence, and platform policy. Missing required routed context is blocking; unrelated policy text is not required context.

## Required repository procedures

The repository must provide equivalent procedures for:

- feature-contract authoring and review;
- implementation-plan authoring and review;
- implementation-task authoring and review;
- architecture and project-structure readiness;
- localization and RTL readiness;
- adaptive and accessibility readiness;
- persistence and migration readiness;
- privacy and protected-boundary readiness;
- runtime-evidence readiness;
- production-fake detection;
- documentation-impact assessment and documentation review;
- PR review;
- bounded feature implementation;
- feature implementation convergence;
- feature readiness review.

A missing required procedure, or a `Blocked`, `Fail`, `Not ready`, or equivalent verdict, stops affected work unless the accountable owner explicitly authorizes a narrower non-blocked slice.

## Publishing

Publishing is two-stage:

1. read-only preparation and evidence;
2. separate explicit approval for remote side effects.

Never merge, auto-merge, force-push, bypass failed checks, expose credentials, sign, upload, promote, roll out, or publish without authorization.

## Completion report

Report:

- scope;
- files changed;
- behavior affected;
- authorities applied;
- protected boundaries touched or confirmed untouched;
- tests and checks actually run;
- exact commands or sessions;
- environments and destinations;
- expected and actual outcomes;
- evidence artifacts;
- documentation impact;
- architecture impact;
- blockers and limitations;
- remaining `Needs verification` items;
- current lifecycle verdict;
- what remains unauthorized.
