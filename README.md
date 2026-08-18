# AI-Workflow

Repository-owned governance and reusable agent skills for **AI-assisted native mobile development**, with separate operating models for new applications and existing codebases.

This repository contains both packages:

| Package | Use it when | Current package version |
|---|---|---|
| [`Greenfield_AI_Mobile_Governance_Package_v1_9_1/`](Greenfield_AI_Mobile_Governance_Package_v1_9_1/) | Starting or establishing architecture/governance for a native Android or iOS application | 1.9.1 |
| [`Brownfield_AI_Playbook_Reusable_Package_v4_4/`](Brownfield_AI_Playbook_Reusable_Package_v4_4/) | Understanding, stabilizing, refactoring, or extending an existing repository | 4.4 |

The packages are complementary but intentionally **not merged into one lifecycle**. Greenfield begins from approved product authority and synchronized architecture. Brownfield begins from repository discovery, provenance, characterization, architecture coverage, and a safe change boundary.

## Why this exists

General AI coding frameworks are good at specs, plans, coding technique, TDD, debugging, or agent orchestration. Native mobile development adds failure modes that are easy for a generic workflow to under-specify: process/lifecycle restoration, platform concurrency, permissions/privacy/capabilities, durable migrations, adaptive layouts, accessibility, localization/RTL, protected configuration, device-only behavior, and release evidence.

AI-Workflow makes those concerns explicit parts of the delivery lifecycle instead of optional reminders.

### Greenfield lifecycle

```text
Approved product authority
→ Architecture Spine + ADRs
→ architecture coverage/readiness
→ Feature Input
→ complexity classification
→ Feature Contract + independent review + owner approval
→ Implementation Plan + independent review + owner approval
→ Implementation Tasks + independent review + owner approval
→ implementation-readiness audit
→ explicit owner implementation authorization
→ bounded implementation + task evidence
→ feature convergence
→ final readiness + independent readiness review
→ owner acceptance
→ separate release authorization
```

### Brownfield lifecycle

```text
Safe setup
→ repository discovery/provenance
→ characterization tests
→ feature + architecture understanding
→ architecture coverage / no-edit audit
→ accountable decisions
→ testing safety net
→ bounded refactor / feature / defect work
→ independent review
→ documentation impact
→ explicit publish authorization
→ CI/runtime/release verification
```

## Native-mobile specialization

The Greenfield package includes dedicated Android/iOS procedures for architecture, project structure, UI frameworks, concurrency, localization/RTL, accessibility/adaptation, persistence/migrations, protected platform capabilities, runtime evidence, bounded implementation, convergence, readiness, documentation, and review.

Android and iOS skill counts are intentionally not identical. The current difference is mostly packaging aliases and a few specialist operational skills, **not missing core iOS coverage**. See [`docs/MOBILE_COVERAGE_MATRIX.md`](docs/MOBILE_COVERAGE_MATRIX.md).

Cross-cutting skills are intentionally duplicated inside the Android and iOS packs so a team can install **only Android** or **only iOS** and still get a complete platform workflow. For a dual-platform repository, keep them namespaced by path:

```text
.agents/skills/android/...
.agents/skills/ios/...
```

Do not flatten both platform packs into one directory.

## Comparison with Matt Pocock Skills, Superpowers, and Spec Kit

AI-Workflow is not positioned as universally better than those projects. Its advantage is narrower: **native-mobile governance depth**.

| Project | Best-known strength | AI-Workflow distinction |
|---|---|---|
| Matt Pocock Skills | Composable engineering/productivity skills and mature installation | AI-Workflow owns a mobile-specific authority/readiness lifecycle instead of only composing generic skills |
| Superpowers | Mature end-to-end methodology, TDD/debugging/review/execution mechanics | AI-Workflow goes deeper on Android/iOS architecture, platform boundaries, lifecycle, migrations, accessibility/RTL, and release evidence |
| GitHub Spec Kit | Mature general spec-driven workflow with CLI, presets, extensions, and agent integrations | AI-Workflow adds native-mobile Architecture Spine/ADR synchronization, platform readiness gates, evidence classes, and explicit owner/release authorization boundaries |

For the detailed, deliberately balanced comparison, see [`docs/COMPARISON.md`](docs/COMPARISON.md).

## Installation and repository bootstrap

The repository installer now performs the **full reusable bootstrap by default**, not only skill copying. The package documentation remains the authority for the lifecycle and for which project-specific artifacts must be created from real evidence and owner decisions.

Greenfield iOS:

```bash
python3 tools/install.py greenfield --platform ios --target /path/to/your/repository
```

Greenfield Android:

```bash
python3 tools/install.py greenfield --platform android --target /path/to/your/repository
```

A Greenfield bootstrap installs the root `AGENTS.md`, applicable `.agents/policies/`, the selected platform skill pack, governance/architecture/mobile templates, a seeded `AI_CONTEXT.md`, and `docs/decisions/DECISION_REGISTER.md`. It intentionally does **not** fabricate the Architecture Spine, ADRs, feature contracts, plans, tasks, readiness artifacts, runtime evidence, or release records; those depend on the receiving project's approved product authority and explicit decisions.

Brownfield Android or iOS:

```bash
python3 tools/install.py brownfield --platform android --target /path/to/your/repository
python3 tools/install.py brownfield --platform ios --target /path/to/your/repository
```

Brownfield installs the reusable repository-starter prompts/specifications, a composed common + platform `AGENTS.md`, the reusable checklist/template material, the applicable reusable skills, and the Markdown playbook as `AI_PLAYBOOK.md`. It leaves project-specific manifests, checkpoints, Graphify overrides, repository facts, and `AI_CONTEXT.md` to be created/adapted from the receiving repository rather than copying example state as truth.

If you intentionally want only the skill pack, retain the narrower behavior with `--skills-only`:

```bash
python3 tools/install.py greenfield --platform ios --target /path/to/your/repository --skills-only
```

Use `--dry-run` to preview the complete install plan. The installer refuses to overwrite existing destination paths unless `--force` is supplied. `tools/install_skills.py` remains as a backward-compatible entry point, but it now has the same full-bootstrap default; pass `--skills-only` for its historical behavior.

## Executable repository validation and evaluation corpus

The repository now includes deterministic checks so public contributions can be tested instead of relying only on review of Markdown files.

Run locally:

```bash
python3 tools/validate_repository.py
python3 -m unittest discover -s tests
```

The validator checks skill frontmatter/name consistency, stale iOS routing paths, likely cross-platform copy/paste leaks, macOS/archive metadata, public repository files, and the regression-case corpus. GitHub Actions runs the same checks on pushes and pull requests.

`evals/cases.json` contains cross-package behavioral smoke cases for authorization, protected boundaries, migrations, concurrency, accessibility/RTL, convergence/release separation, characterization tests, and publishing. See [`evals/README.md`](evals/README.md) for running them against saved outputs from any coding agent.

## Public contributions

Contributions are welcome. Start with [`CONTRIBUTING.md`](CONTRIBUTING.md), run the repository validation before opening a pull request, and preserve the distinction between Greenfield and Brownfield authority models.

This repository is licensed under **Apache License 2.0**. See [`LICENSE`](LICENSE) and [`NOTICE`](NOTICE). Citation metadata is provided in [`CITATION.cff`](CITATION.cff) so GitHub can expose a standard repository citation for research, articles, talks, and derivative work.

## Repository links

- Greenfield start-here: [`Greenfield_AI_Mobile_Governance_Package_v1_9_1/README.md`](Greenfield_AI_Mobile_Governance_Package_v1_9_1/README.md)
- Brownfield start-here: [`Brownfield_AI_Playbook_Reusable_Package_v4_4/README.md`](Brownfield_AI_Playbook_Reusable_Package_v4_4/README.md)
- Mobile coverage/parity: [`docs/MOBILE_COVERAGE_MATRIX.md`](docs/MOBILE_COVERAGE_MATRIX.md)
- Comparison/positioning: [`docs/COMPARISON.md`](docs/COMPARISON.md)
- Contribution guide: [`CONTRIBUTING.md`](CONTRIBUTING.md)
