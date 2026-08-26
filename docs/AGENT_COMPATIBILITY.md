# Agent compatibility

The installer has one source of truth and thin client adapters:

```text
AGENTS.md                         canonical mandatory policy
AI_CONTEXT.md                     installed asset and routing index
.agents/skills/<...>/SKILL.md     canonical skill files
.claude/skills/<alias>            symlink to the canonical skill directory
CLAUDE.md                         Claude Code adapter importing AGENTS.md
```

`AGENTS.md` is generated for every workflow and profile. Greenfield and Brownfield may use different policy content, but they never require the recipient to load `AGENTS.common.md` plus a platform overlay. Brownfield source fragments remain package implementation details; the generated root file is merged and standalone.

`AI_CONTEXT.md` lists every installed skill, policy, prompt, template, routing file, and playbook/reference path. It is an index, not an instruction dump: route observable task facts first, then read only the relevant procedure or artifact template.

## Claude Code

Claude Code loads project memory from `CLAUDE.md`. The generated adapter imports `@AGENTS.md` and `@AI_CONTEXT.md`, so Claude receives the canonical policy without a duplicate policy file. The generated `.claude/skills/` entries are relative symlinks to `.agents/skills/` and are tracked by the installer manifest. On filesystems where symlink creation is unavailable, setup should be run in an environment that supports symlinks; the installer does not silently replace a requested adapter with a second copied skill tree.

Claude Code discovers project skills in `.claude/skills/<skill-name>/SKILL.md`. The aliases are prefixed for platform-specific skills (for example, `android-pr-review` and `ios-pr-review`) so Android/iOS and Brownfield/Greenfield copies cannot silently overwrite one another. Claude’s skill frontmatter uses the open Agent Skills shape (`name` and `description`), while the canonical skill body remains client-neutral.

## Nemotron, GLM, and other models

A model is not a filesystem integration. Nemotron, GLM, and other models can follow these skills when they are hosted inside a coding agent that loads `AGENTS.md`, `CLAUDE.md`, or Agent Skills, or when the host explicitly supplies the relevant files. The model name alone does not make repository skills discoverable.

No model-specific prompt or provider setup is required by this repository. For a host without native discovery, provide `AGENTS.md` and `AI_CONTEXT.md` as startup context, then expose the selected `.agents/skills/.../SKILL.md` files through that host’s system-prompt, project-instructions, or tool configuration. Do not paste every skill into context by default; use the deterministic route registry and the generated index to select the smallest relevant set.

The repository therefore supports two levels:

- Native discovery: Claude Code through `CLAUDE.md` and `.claude/skills/`; any Agent Skills-compatible host through the canonical skill directories.
- Adapter-required: hosts that only accept a raw model prompt or have their own project-instruction convention. Use a thin adapter that points to `AGENTS.md`, `AI_CONTEXT.md`, and the selected skill paths; do not fork the skill content.
