# Greenfield AI Mobile Governance Package

**Version:** 1.4  
**Platforms:** Native Android and native iOS  
**Model:** Repository-owned, contract-first, architecture-synchronized, evidence-gated

This package provides reusable governance policies, playbooks, architecture templates, feature templates, platform-specific skills, readiness gates, convergence procedures, and owner-acceptance controls for greenfield mobile delivery.

## Canonical lifecycle

Feature input → feature contract → independent contract review → owner approval → implementation plan → independent plan review → owner approval → implementation tasks → independent task review → owner approval → implementation readiness audit → explicit owner implementation authorization → bounded feature implementation → task evidence closure → feature convergence → `READINESS_REPORT.md` → independent readiness review → owner feature acceptance → separate release authorization.

## Playbooks

- `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v2_1_Agent_Native.docx` is the latest agent-native playbook and does not use Spec Kit. It is updated to use `IMPLEMENTATION_TASKS.md`, a pre-implementation `IMPLEMENTATION_READINESS_AUDIT.md`, and a post-implementation `READINESS_REPORT.md`.
- `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v2_0_Agent_Native.docx` and `playbook/AI_Greenfield_Project_Playbook_Mobile_Generic_v1_5_iOS_Android.docx` are retained unchanged as earlier editions. They are not the canonical agent-native workflow.
- `Mobile_Feature_Delivery_Governance_Pipeline.docx` is the human-readable end-to-end lifecycle reference.

## Package structure

```text
templates/
  mobile-agent-policy-modular/
  governance/
  architecture/
  mobile/
skills/
  android/
  ios/
historical/
  policies/
playbook/
```

Android and iOS skills remain separate even when they share a skill name. Their required inputs, platform contracts, evidence layers, and verdict semantics may differ. Do not merge them solely by name.

## Canonical repository artifacts

- `FEATURE_CONTRACT.md`
- `IMPLEMENTATION_PLAN.md`
- `IMPLEMENTATION_TASKS.md`
- `IMPLEMENTATION_READINESS_AUDIT.md`
- `READINESS_REPORT.md`

## Important semantics

- Skills and templates do not authorize work.
- ADR acceptance does not authorize implementation.
- Readiness `PASS` means eligible for owner implementation authorization only.
- Implementation completion does not establish feature acceptance.
- Feature acceptance does not authorize release.
- Runtime-only claims require matching runtime evidence.
- Configuration retained for future features must have explicit target/source-set inclusion, runtime initialization, privacy impact, and active/dormant status.

## Installation

1. Copy `templates/mobile-agent-policy-modular/AGENTS.md` to the repository root and install its `.agents/policies/` modules.
2. Select the relevant platform policy and skills from `skills/android/` or `skills/ios/`.
3. Copy governance, architecture, and mobile templates into the repository template location.
4. Create `AI_CONTEXT.md` from `templates/governance/AI_CONTEXT.template.md`.
5. Replace every placeholder and record canonical paths and owners.
6. Do not install files under `historical/` as active authority.

## Hooks

No hooks are included. Hook execution is repository-specific and must be added only through explicit repository policy.
