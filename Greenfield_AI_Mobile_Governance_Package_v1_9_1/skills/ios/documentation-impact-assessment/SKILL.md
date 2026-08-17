---
name: documentation-impact-assessment
description: Classifies documentation impact before finalizing plans and after implementation.
---

# Documentation Impact Assessment

1. Read task scope and authorization.
2. Inspect planned or final changed files.
3. Identify affected behavior, architecture, contracts, routing, evidence, protected boundaries, configuration, and release expectations.
4. Use `AI_CONTEXT.md` to locate only relevant current documents.
5. Return one:
   - `NO_DOCUMENTATION_IMPACT`
   - `DOCUMENTATION_REVIEW_REQUIRED`
   - `DOCUMENTATION_UPDATE_REQUIRED`
   - `NEEDS_VERIFICATION`
6. After authorized edits, search for stale terms and contradictions before closure.

Do not rewrite historical evidence or automatically edit every routed document.

## Bounded-Task Mode

During ordinary bounded implementation, this procedure should be lightweight: return documentation impact `YES`/`NO`, identify affected canonical files, and state whether immediate synchronization is required. Full cross-document consistency review belongs at convergence unless an authority document changed now.
