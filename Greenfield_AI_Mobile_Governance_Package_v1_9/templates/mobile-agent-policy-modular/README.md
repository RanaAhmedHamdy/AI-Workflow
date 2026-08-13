# Modular Mobile Agent Policy Pack

This package refactors one very large repository policy into a small authoritative root file plus six routed policy modules.

## Structure

```text
AGENTS.md
.agents/policies/
  GOVERNANCE_LIFECYCLE.md
  IMPLEMENTATION_POLICY.md
  EVIDENCE_AND_COMPLETION.md
  PROTECTED_BOUNDARIES.md
  android/
    ANDROID_ENGINEERING_POLICY.md
  ios/
    IOS_ENGINEERING_POLICY.md
```

## Intended use

- `AGENTS.md` is always loaded and remains the constitution-equivalent authority.
- `AI_CONTEXT.md` routes only the policy modules relevant to the current work.
- Skills provide procedures.
- Templates provide artifact structures.
- ADRs and feature artifacts provide project-specific decisions and behavior.

## Suggested AI_CONTEXT routing

| Work type | Required policy |
|---|---|
| Any governed work | `AGENTS.md` |
| Contract, plan, task, approval, acceptance | `.agents/policies/GOVERNANCE_LIFECYCLE.md` |
| Implementation | `.agents/policies/IMPLEMENTATION_POLICY.md` |
| Verification, convergence, completion | `.agents/policies/EVIDENCE_AND_COMPLETION.md` |
| Protected work | `.agents/policies/PROTECTED_BOUNDARIES.md` |
| Android work | `.agents/policies/android/ANDROID_ENGINEERING_POLICY.md` |
| iOS work | `.agents/policies/ios/IOS_ENGINEERING_POLICY.md` |

Replace every bracketed placeholder and synchronize paths with `AI_CONTEXT.md`, `AI_PLAYBOOK.md`, templates, skills, readiness gates, and the owner decision register.

- `.agents/policies/FEATURE_DELIVERY_INVARIANTS.md` centralizes complexity, journey coherence, mutation propagation, evidence timing/reuse, and representative/manual runtime rules used by both platforms.
