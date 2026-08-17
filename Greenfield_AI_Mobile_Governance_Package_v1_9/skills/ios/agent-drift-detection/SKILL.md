---
name: agent-drift-detection
description: "Detects divergence between approved repository authority and generated specifications, plans, tasks, code, tests, documentation, or completion claims. Use after any iOS lifecycle phase when checking for scope, architecture, evidence, or governance drift."
---

# Skill: Agent Drift Detection

## Purpose

Detect divergence between approved repository authority and generated specifications, plans, tasks, code, tests, documentation, or completion claims.

This skill may be run after any lifecycle phase.

## Verdicts

- `PASS`
- `DRIFT DETECTED`
- `BLOCKED`
- `NEEDS OWNER DECISION`
- `NEEDS VERIFICATION`

## Drift Categories

### 1. Product Drift

Flag:

- behavior absent from approved product authority;
- candidate or deferred capability promoted into active scope;
- invented validation thresholds;
- invented pricing, quota, retention, retry, or entitlement behavior;
- changed offline behavior;
- sign-in made mandatory when local use is required;
- generated or estimated values presented as verified facts.

### 2. Architecture Drift

Flag:

- mechanisms contradicting accepted ADRs;
- ad hoc dependency construction;
- global service locators;
- feature logic in application or scene hosts;
- direct persistence or network access from leaf views;
- persistence entities exposed directly to presentation;
- weakened concurrency settings;
- unapproved targets, packages, extensions, SDKs, capabilities, or providers;
- unresolved decisions treated as permission.

### 3. Design Drift

Flag:

- approved exact artifacts omitted;
- generic platform layouts replacing approved composition;
- unsupported artifact copy implemented;
- candidate visual content treated as active behavior;
- information hierarchy changed;
- compact and wide compositions collapsed into one unreviewed layout;
- destructive, recovery, permission, purchase, or AI-review flows materially changed.

### 4. Adaptive UI Drift

Flag:

- phone-only implementation when tablet is in scope;
- fixed-size assumptions;
- missing reduced-width behavior;
- inaccessible keyboard-covered controls;
- clipped or unreachable content;
- orientation behavior invented from project defaults;
- unverified Stage Manager, external-display, or multi-window claims.

### 5. Localization and RTL Drift

Flag:

- hardcoded user-facing or accessibility-facing strings;
- sentence-fragment concatenation;
- left/right layout assumptions instead of leading/trailing;
- missing string-catalog or resource entries;
- incorrect plural, number, date, currency, measurement, or percentage formatting;
- damaged Arabic shaping;
- unmirrored layout;
- uppercase transformation applied to Arabic;
- mixed-direction units and values separated incorrectly.

### 6. Accessibility Drift

Flag:

- unlabeled controls;
- color-only status;
- clipped maximum text size;
- missing focus order;
- focus loss after state changes;
- missing error announcements;
- unhandled Button Shapes, Bold Text, Reduce Motion, Reduce Transparency, or Increased Contrast;
- static design title treated as accessibility proof;
- completion claimed without runtime evidence.

### 7. Persistence and Data-Integrity Drift

Flag:

- persistence mechanism selected before approval;
- in-memory substitute used for required durability;
- silent duplicate creation;
- historical snapshots rewritten;
- partial writes presented as success;
- failed writes corrupting prior valid state;
- migrations or deletion claimed without executed evidence;
- sensitive payloads mixed into normal storage;
- backup exclusions omitted;
- physical deletion overclaimed.

### 8. Protected-Boundary Drift

Flag:

- direct AI provider access;
- embedded secrets;
- permissive attestation fallback;
- unapproved capabilities or entitlements;
- production test receipts or fake entitlements;
- authentication tokens outside approved secure storage;
- silent external transfer;
- missing disclosure or consent;
- raw sensitive payload logging;
- unapproved release, signing, or distribution changes.

### 9. Task Drift

Flag tasks that omit:

- requirement IDs;
- architecture decisions;
- screen contracts;
- exact design artifacts;
- files or ownership;
- localization obligations;
- adaptive outcomes;
- accessibility outcomes;
- prohibited patterns;
- acceptance criteria;
- evidence layer;
- artifact path;
- stop condition.

Flag file-existence tasks that do not prove behavioral outcomes.

### 10. Evidence Drift

Flag:

- build success used as runtime proof;
- previews or snapshots used as accessibility proof;
- source inspection used as provider, signing, device, background, StoreKit, or attestation proof;
- claimed tests without commands and outcomes;
- missing environment and destination;
- missing artifact paths;
- stale evidence reused after behavior changes;
- limitations omitted.

### 11. Documentation Drift

Flag contradictions among:

- owner decisions;
- product authority;
- feature input;
- feature contract;
- architecture spine;
- ADRs;
- plan;
- tasks;
- readiness report;
- implementation;
- evidence;
- context router;
- playbook.

## Procedure

1. Identify the lifecycle artifact under review.
2. Load the smallest complete authority set.
3. Build a trace map:
   - product requirement;
   - feature contract;
   - design artifact;
   - architecture decision;
   - task or implementation;
   - evidence.
4. Compare each generated claim against authority.
5. Report only verified drift.
6. Mark uncertainty `Needs verification`.
7. Do not fix protected-boundary or owner-decision drift without authorization.

## Finding Format

- Drift ID;
- Category;
- Severity;
- Generated artifact and location;
- Conflicting or missing authority;
- Observed drift;
- Risk;
- Required remediation;
- Required evidence;
- Stop condition.

## Severity

- **Blocking:** changes product behavior, violates architecture, crosses protected boundaries, risks data loss/privacy, or makes false completion claims.
- **Major:** material design, adaptive, localization, accessibility, task, or evidence gap.
- **Minor:** wording, traceability, or documentation defect that does not alter behavior.

## Final Report

Include:

- verdict;
- blocking drift;
- major drift;
- minor drift;
- owner decisions required;
- verification required;
- files inspected;
- lifecycle phase that must be rerun;
- whether downstream artifacts are invalidated.
