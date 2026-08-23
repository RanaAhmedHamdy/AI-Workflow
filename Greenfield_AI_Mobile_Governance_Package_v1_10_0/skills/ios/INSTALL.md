# Installation

For a normal repository bootstrap, prefer the top-level AI-Workflow CLI through `uvx`. You do **not** need a local AI-Workflow clone.

Change into the **root of the receiving iOS repository** and run:

```bash
cd /path/to/your/ios-project
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow greenfield --platform ios
```

Because `--target` defaults to the current working directory, the command above installs into `/path/to/your/ios-project`. If you are not inside the receiving repository, specify it explicitly instead:

```bash
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow greenfield --platform ios \
  --target /path/to/your/ios-project
```

Use `--dry-run` first when you want to inspect the destinations. The full bootstrap installs the iOS skills **and** the Greenfield governance policies/templates/context scaffold required by the package workflow. Use `--skills-only` only when those other bootstrap assets are already installed and owned by the receiving repository.

For manual or skills-only installation, install the iOS package under a platform-scoped skill directory so it remains self-contained and can coexist with the Android package.

Recommended repository layout:

```text
.agents/
  skills/
    ios/
      README.md
      INSTALL.md
      AI_CONTEXT.skill-routing.template.md
      <skill-name>/SKILL.md
AI_CONTEXT.md
AGENTS.md
```

If the repository also contains native Android, install that package separately under `.agents/skills/android/`. Do not flatten the two platform packs into the same directory because several cross-cutting skill names intentionally exist in both packs so either platform can be installed independently.

Then:

1. Copy the contents of this package's `skills/ios/` directory to `.agents/skills/ios/` in the receiving repository.
2. Add or adapt the routing rows from `AI_CONTEXT.skill-routing.template.md` in the project `AI_CONTEXT.md`.
3. Ensure the root `AGENTS.md` and modular policies route the required iOS procedures and stop behavior.
4. Keep project-specific facts in `AGENTS.md`, ADRs, architecture maps, and `AI_CONTEXT.md`; do not rewrite reusable skill procedures with project facts.
5. Run `documentation-consistency-review` after installation.
6. Treat any missing required skill or failing verdict as an implementation-readiness blocker.
