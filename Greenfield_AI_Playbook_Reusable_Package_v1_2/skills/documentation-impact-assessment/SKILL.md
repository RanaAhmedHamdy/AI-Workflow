---
name: documentation-impact-assessment
description: Assess which current documents require review or updates because of planned or completed work, without editing automatically.
---

# Documentation Impact Assessment

## Procedure

1. Read task scope and authorization boundary.
2. Inspect proposed files or final changed-file set.
3. Run the repository changed-path classifier when available; treat output as candidate routing only.
4. Identify affected behavior, architecture, contracts, routing, skills/hooks, verification evidence, protected boundaries, configuration, release expectations, and architecture-coverage dimensions.
5. Consider UI adaptation, background work, permissions, environments, feature flags, analytics/privacy, observability/crash reporting, performance, and domain/module ownership when relevant.
6. Use `AI_CONTEXT.md` to locate only task-relevant current documents; distinguish current guidance from historical evidence and unexecuted plans.
7. Apply `documentation-review` semantically.
8. Return one classification: `NO_DOCUMENTATION_IMPACT`, `DOCUMENTATION_REVIEW_REQUIRED`, `DOCUMENTATION_UPDATE_REQUIRED`, or `NEEDS_VERIFICATION`. Stop before editing.

## Closure review

After authorized documentation edits, reassess the final diff, rerun candidate routing, search for old behavior/path/contract terms, review newly discovered current documents, and do not declare completion while a material stale claim remains.

## Safety

Do not require edits for every source change, rewrite historical evidence, edit vendor content, advance provenance beyond the actual review, or claim automatic invocation in every client.
