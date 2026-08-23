---
name: documentation-impact-assessment
description: Routes planned or completed changes to current documents without editing automatically.
---
# Documentation Impact Assessment

Inspect task/final diff, affected behavior, architecture, contracts, routing, skills/hooks, evidence, protected boundaries, configuration, release, adaptation, localization/RTL, accessibility, state ownership, and project structure. Use `AI_CONTEXT.md` for current homes. Return `NO_DOCUMENTATION_IMPACT`, `DOCUMENTATION_REVIEW_REQUIRED`, `DOCUMENTATION_UPDATE_REQUIRED`, or `NEEDS_VERIFICATION`.

## Bounded-Task Mode

During ordinary bounded implementation, this procedure should be lightweight: return documentation impact `YES`/`NO`, identify affected canonical files, and state whether immediate synchronization is required. Full cross-document consistency review belongs at convergence unless an authority document changed now.
