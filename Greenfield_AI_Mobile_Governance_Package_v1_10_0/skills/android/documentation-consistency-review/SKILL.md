---
name: documentation-consistency-review
description: Detects stale or contradictory current product/design/architecture/feature authority, including ADR lifecycle and implementation-authorization mismatches.
---

# Documentation Consistency Review

Compare only current authoritative artifacts relevant to scope: product/design authority, Decision Register, ADR canonical bodies/statuses, Architecture Spine, coverage, `AI_CONTEXT`, feature artifacts when they exist, build structure, authorization, implementation, and evidence.

Flag:

- repository/Gradle evidence or agent recommendation presented as owner approval;
- ADR promotion without explicit owner authority;
- provisional decisions represented as fully proven or missing exit criteria;
- accepted amendments not reflected in current canonical decisions;
- superseded text left active;
- stale package/module/dependency paths or unselected mechanisms described as selected;
- plan/tasks contradicting accepted architecture or design authority;
- contradictory readiness/authorization claims;
- evidence claims unsupported by artifacts.

Historical wording explicitly labeled `Superseded — historical only` is allowed.

Any material contradiction returns `BLOCKED`. Report the owning artifact and smallest authoritative edit sequence. Reuse unchanged prior findings; do not reread unrelated documents solely for ceremony.
