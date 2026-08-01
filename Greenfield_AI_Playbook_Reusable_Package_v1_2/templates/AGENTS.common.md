# AGENTS.md - Common Mobile Repository Policy

> Starter template. Replace or remove every bracketed value. This file must not be used to infer project facts.

## Authority and precedence

1. Current task scope and accountable repository-owner direction.
2. This file's mandatory operating and safety rules.
3. Verified current product contracts and implementation at the affected boundary.
4. `AI_CONTEXT.md` for context routing and evidence status.
5. Playbooks and `.agents/skills/` as advisory procedures.

Skills explain how to perform work; they do not authorize it. Unresolved conflicts are `Needs verification`.

## Project mode and evidence

- Mode: [greenfield / brownfield].
- Platforms and supported form factors: [fill in].
- Source of approved product behavior: [fill in].
- Current source/configuration describes implementation only; tests prove only their assertions; runtime and release claims require matching evidence.

## Working rules

- Start from [base branch] and use one focused task branch. Never work directly on protected branches.
- Load only task-relevant context through `AI_CONTEXT.md`; do not scan the whole repository by default.
- Do not invent requirements, verification results, commands, files, owners, or runtime behavior.
- Keep unrelated worktree changes visible; never hide, reset, discard, or rewrite them without explicit authorization.
- Add dependencies, frameworks, modules, environments, or architecture patterns only with explicit scope and a recorded decision when they change the architecture surface.

## Cross-feature architecture impact

Before finalizing a plan or implementation that materially introduces or changes a cross-cutting concern, determine whether the current architecture maps and coverage review remain accurate. Consider, when applicable: module/domain boundaries, dependency direction, UI adaptation, background execution, permissions, configuration/environments, feature flags, analytics/privacy, observability/crash reporting, performance, security, build/release, and testability.

Use `AI_CONTEXT.md` to select only relevant current documents. Do not create architecture documents automatically. Record unsupported or owner-dependent claims as `Needs verification`. Architecture documents and skills do not authorize implementation changes.

## Documentation impact

Run or apply `documentation-impact-assessment` before finalizing relevant plans and again after implementation. The changed-path classifier is candidate routing, not a semantic decision. Documentation edits require authorization; do not update provenance beyond the review actually performed.

## Protected boundaries

Treat identity/authentication/authorization, secrets, user data and destructive persistence, public/backend contracts, permissions/platform capabilities, signing/certificates/entitlements, production configuration, distribution, and financial/regulated/privacy-sensitive behavior as protected unless this repository narrows or extends the list. Invoke `protected-boundary-preflight` before protected work.

## Testing and verification

- Use the repository's established test stack unless a testing-strategy decision authorizes a change.
- Choose the smallest useful test layer that proves the required contract.
- Report only commands actually run and exact results.
- Do not claim device, backend, accessibility, security, performance, or release behavior from static/unit evidence alone.

## Review and publishing

- Invoke `pr-review` for the coherent task diff before readiness is declared.
- Publishing is two-stage: read-only preparation, then separate explicit approval for remote side effects.
- Never merge, auto-merge, force-push, bypass failed checks, or expose credentials.

## Completion contract

Report: scope, files changed, behavior affected, protected boundaries touched/not touched, tests/checks actually run, documentation-impact classification, architecture-coverage impact when relevant, known blockers, and remaining `Needs verification`.
