# Five-minute quickstart

AI-Workflow installs repository-owned Markdown instructions. It does not modify application source code, create product decisions, or claim native runtime evidence.

## Choose a path

| Your starting point | Command family | Recommended profile |
| --- | --- | --- |
| Existing Android app | `brownfield --platform android` | `safety` |
| Existing iOS app | `brownfield --platform ios` | `safety` |
| New Android app | `greenfield --platform android` | `feature` |
| New iOS app | `greenfield --platform ios` | `feature` |
| Android + iOS repository | `--platform both` or add the second platform with `update` | `safety` |

`safety` is the light default: specialist procedures, fact routing, protected-boundary checks, and evidence guidance. Choose `feature` when you want SMALL/STANDARD/COMPLEX delivery templates. `full` adds the deep Architecture Spine/ADR/design/readiness lifecycle. `skills` installs procedures and the router only.

## Safe disposable trial

Prerequisite: install [uv](https://docs.astral.sh/uv/getting-started/installation/) so `uvx --version` works.

```bash
mkdir ai-workflow-trial
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow brownfield --platform android --profile safety --target ai-workflow-trial --dry-run
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow brownfield --platform android --profile safety --target ai-workflow-trial
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow status --target ai-workflow-trial
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow route --workflow brownfield --platform android --profile safety --fact persistence --fact schema_migration --fact concurrency --fact lifecycle
```

The install writes one canonical `AGENTS.md`, a thin `CLAUDE.md` adapter, an `AI_CONTEXT.md` inventory, `.agents/skills/android/`, Claude-compatible `.claude/skills/` symlinks, `.agents/routing/routes.json`, and `.ai-workflow/manifest.json`. It refuses recipient-owned collisions.

The final route command prints this real checked-in classification:

```text
Task classification: brownfield / android / safety
Detected concerns: concurrency, lifecycle, persistence, schema_migration
Recommended tier: COMPLEX
Required checks:
- android-persistence-migration-readiness: because detected persistence, schema_migration
- kotlin-coroutines-readiness: because detected concurrency
- protected-lifecycle-transaction-review: because detected lifecycle
- android-runtime-evidence-readiness: because detected lifecycle
Escalation: required — schema_migration
```

Then ask your coding agent: "Read `AGENTS.md`, `AI_CONTEXT.md`, and `FIRST_SAFE_CHANGE.md`. For this request, state observable facts, run the router, explain each selected check, and stop if an unresolved fact changes safety." Claude Code will load `CLAUDE.md` and discover the `.claude/skills/` aliases automatically; other clients can use the same canonical Markdown paths.

For frequent use, install the CLI once permanently:

```bash
uv tool install git+https://github.com/RanaAhmedHamdy/AI-Workflow.git
```

Then call `ai-workflow` directly from any directory.

## Platform examples

### Existing Android app

```bash
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow brownfield --platform android --profile safety --target /path/to/existing-android-app
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow route --workflow brownfield --platform android --profile safety --fact persistence --fact concurrency
```

### Existing iOS app

```bash
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow brownfield --platform ios --profile safety --target /path/to/existing-ios-app
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow route --workflow brownfield --platform ios --profile safety --fact persistence --fact concurrency --fact lifecycle
```

### New Android or iOS app

```bash
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow greenfield --platform android --profile feature --target /path/to/new-android-app
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow greenfield --platform ios --profile feature --target /path/to/new-ios-app
```

`feature` installs `.templates/mobile/mobile/SMALL_FEATURE_RECORD_TEMPLATE.md`; use it only after the facts show a confirmed SMALL change. Persistence, meaningful concurrency, lifecycle, permissions/privacy/capabilities, protected configuration, architecture boundaries, or unknown behavior require at least STANDARD. Schema migration requires COMPLEX.

### Android + iOS repository

```bash
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow brownfield --platform both --profile safety --target /path/to/mobile-repository
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow update --platform ios --target /path/to/mobile-repository --dry-run
```

The first form composes namespaced `.agents/skills/android/` and `.agents/skills/ios/` from a clean target. The update form is how an existing single-platform installation adds the other platform.

## Preview, inspect, update, and uninstall

```bash
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow profiles
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow status --target /path/to/mobile-repository
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow update --target /path/to/mobile-repository --profile feature --dry-run
uvx --from git+https://github.com/RanaAhmedHamdy/AI-Workflow.git ai-workflow uninstall --target /path/to/mobile-repository --dry-run
```

Read [Installer lifecycle](INSTALLER_LIFECYCLE.md) before a real update or uninstall. Unchanged managed files can change or be removed; modified managed files and all recipient-owned files are retained. The tool never offers a destructive overwrite mode.

## What the trial proves

It proves a safe install/dry-run/status/route flow and shows how stated task facts select specialist procedures. It does not classify natural language automatically, inspect your source code, authorize a change, or prove runtime behavior. See the maintained [native examples](../examples/README.md) for bounded Android and iOS implementation evidence.
