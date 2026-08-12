---
name: documentation-consistency-review
description: Detects stale or contradictory current specs, plans, tasks, ADRs, architecture maps, context routing, and authorization statements.
---
# Documentation Consistency Review

Compare current spec status, plan authorization, task authorization, accepted ADR canonical bodies, decision register, architecture spine, coverage matrix, `AI_CONTEXT.md`, build structure, and implementation. Flag accepted amendments not incorporated into canonical decisions, old proposals left active, stale package paths, unselected mechanisms described as selected (or vice versa), and evidence claims unsupported by artifacts.

Any material contradiction returns `BLOCKED`. Report the owning artifact and smallest authoritative edit sequence.
