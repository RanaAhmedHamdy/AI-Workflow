# Governance Lifecycle Policy

## Purpose

This policy defines how a feature advances from input to owner acceptance and, separately, to release. It does not establish project-specific facts or grant approval.

## 1. Governance initialization

Before feature work:

- identify the accountable repository owner;
- record the constitution-equivalent authority;
- define canonical artifact paths;
- identify product, design, architecture, and evidence authorities;
- establish `AI_CONTEXT.md` routing;
- install required skills and templates;
- record toolchain, platform, branch, CI, and evidence locations;
- resolve contradictions before planning.

## 2. Feature input

A feature input must define or cite:

- feature identity and purpose;
- user-visible outcomes;
- actors and permissions;
- required and excluded scope;
- product rules and data semantics;
- design authority;
- platform and form-factor assumptions;
- privacy, regulatory, and protected-boundary implications;
- known open questions.

Unsupported assumptions remain clarification candidates. Do not silently convert them into requirements.

## 3. Feature contract

Feature contracts must:

- remain bounded by the approved feature input;
- distinguish in-scope behavior, strictly necessary support, later-feature behavior, exclusions, and clarification candidates;
- source every observable validation rule, required field, range, uniqueness rule, destructive threshold, date rule, decimal rule, exact-copy requirement, and save-eligibility condition;
- describe observable product behavior rather than framework or implementation choices;
- define applicable failure, recovery, offline, cancellation, destructive, durability, adaptive, localization, RTL, accessibility, privacy, and evidence outcomes;
- map screens to approved screen contracts and exact design artifacts;
- exclude unsupported artifact content;
- state evidence obligations without claiming evidence exists;
- remain unapproved until owner decision.

### Required gate

Feature-contract authoring  
→ independent feature-contract review  
→ repository-owner approval.

A review pass means ready for owner approval only.

## 4. Implementation plan

Plans require an owner-approved contract and closed material product clarifications.

Plans must:

- apply accepted ADRs without silently selecting alternatives;
- separate presentation, domain, data, platform, navigation, and host ownership;
- define dependency composition;
- define state ownership, lifecycle, concurrency, and cancellation;
- define persistence, migrations, transactions, restoration, backup, and deletion where applicable;
- define protected boundaries and fail-closed behavior;
- map planned components to contract requirements;
- map screens to exact design authority;
- define adaptive, localization, RTL, accessibility, failure, recovery, offline, and destructive behavior;
- define testing and runtime-evidence strategy;
- state dependency order only;
- avoid implementation tasks, assignments, estimates, and code;
- record unresolved technical decisions honestly;
- never claim implementation authorization.

### Required gate

Implementation-plan authoring  
→ independent implementation-plan review  
→ repository-owner approval.

## 5. Implementation tasks

Tasks require an owner-approved contract and owner-approved plan that passed independent review.

Tasks must:

- define one bounded, independently reviewable outcome;
- form an explicit acyclic dependency graph;
- trace to contract requirements, plan sections, ADRs, and design authority;
- state allowed and prohibited scope;
- define behavioral acceptance criteria;
- define verification layer, procedure or command, environment, expected result, artifact path, limitation, and stop condition;
- include applicable localization, RTL, accessibility, adaptive behavior, lifecycle, persistence integrity, privacy, production composition, documentation, and evidence work;
- not reopen accepted architecture;
- not collapse the feature into one giant task;
- remain non-executable until implementation authorization.

### Required gate

Implementation-task authoring  
→ independent implementation-task review  
→ repository-owner task approval.

## 6. Pre-implementation readiness

Before authorization, verify:

- contract approval;
- plan approval and review pass;
- task approval and review pass;
- accepted ADRs and architecture coverage;
- design authority and screen contracts;
- closed material clarifications;
- applicable protected-boundary preflight;
- applicable platform readiness procedures;
- canonical evidence locations;
- no current contradictions.

Allowed outcomes:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

## 7. Implementation authorization

Implementation begins only after explicit authorization is recorded.

Authorization must identify:

- feature/slice;
- approved contract, plan, and tasks;
- authorized scope;
- excluded scope;
- date;
- accountable owner;
- conditions and limitations.

There must be one canonical authorization record. Copies in other documents must remain synchronized.

## 8. Implementation

Execute dependency-ordered tasks one coherent slice at a time.

During implementation:

- preserve contract and plan boundaries;
- stop on scope, architecture, or protected-boundary drift;
- do not add later-feature placeholders;
- do not self-authorize amendments;
- attach evidence as tasks close;
- leave unsupported runtime work open;
- do not mark completion from file existence or compilation alone.

## 9. Feature implementation convergence

After implementation, run `feature-implementation-convergence` or an equivalent procedure.

It must verify:

1. task completion integrity;
2. contract-to-implementation traceability;
3. scope fidelity;
4. plan and architecture conformance;
5. design conformance;
6. state, lifecycle, concurrency, cancellation, navigation, and restoration;
7. persistence, migration, rollback, idempotency, relaunch, backup, and deletion where applicable;
8. localization, approved RTL, and formatting;
9. accessibility and adaptive runtime evidence;
10. privacy and protected-boundary integrity;
11. production-fake and release-composition integrity;
12. current evidence;
13. documentation synchronization;
14. coherent-diff PR review.

Allowed convergence verdicts:

- `READY FOR FEATURE READINESS REVIEW`
- `BLOCKED BY IMPLEMENTATION DEFECT`
- `BLOCKED BY ARCHITECTURE DRIFT`
- `BLOCKED BY SCOPE DRIFT`
- `BLOCKED BY MISSING EVIDENCE`
- `NEEDS VERIFICATION`

Convergence does not approve the feature or authorize release.

## 10. Readiness report

Create or update:

`docs/features/<feature-id>/READINESS_REPORT.md`

The report must include:

- approval and authorization state;
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

## 11. Independent readiness review

Run `feature-readiness-review` or equivalent.

Allowed verdicts:

- `PASS`
- `FAIL`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

`PASS` means ready for repository-owner feature acceptance only.

## 12. Owner feature acceptance

The repository owner may:

- accept the feature;
- reject it;
- require correction;
- require more evidence;
- approve a documented limitation;
- amend scope through controlled change.

Acceptance must be recorded canonically.

## 13. Release authorization

Feature acceptance does not authorize:

- production signing;
- provisioning or entitlements;
- archive/export;
- TestFlight or App Store Connect;
- Play Console or staged rollout;
- production configuration;
- remote upload, promotion, or publication.

Release requires separate explicit authorization.

## 14. Release verification

After authorization, verify applicable:

- clean build and complete test results;
- archive/package contents;
- signing and entitlement state;
- privacy declarations;
- production dependency graph;
- environment configuration;
- store metadata;
- release notes;
- rollout and rollback plan;
- evidence paths;
- post-release monitoring and learning.

Release review must not self-publish.
