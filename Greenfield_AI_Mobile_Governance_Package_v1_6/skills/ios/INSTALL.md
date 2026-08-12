# Installation

Copy the package's `.agents/skills/` structure into the repository root.

Recommended repository layout:

```text
.agents/
  skills/
    README.md
    shared/
    ios/
AI_CONTEXT.md
AGENTS.md
```

Then:

1. Add the routing rows from `AI_CONTEXT.skill-routing.template.md` to the project `AI_CONTEXT.md`.
2. Ensure `AGENTS.md` references the required iOS skills and stop behavior.
3. Replace no placeholders in the skills themselves; project-specific facts belong in `AGENTS.md`, ADRs, architecture maps, and `AI_CONTEXT.md`.
4. Run `documentation-consistency-review` after installation.
5. Treat any missing required skill or failing verdict as an implementation-readiness blocker.
