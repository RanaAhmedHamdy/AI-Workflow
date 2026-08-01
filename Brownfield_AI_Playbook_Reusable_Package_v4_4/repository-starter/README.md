# Brownfield repository starter kit

This directory contains the repository-owned prompt-routing and documentation workflow described in the v4.4 brownfield playbook.

## Copy as a baseline

Copy `scripts/` and `docs/ai/prompts/` when the receiving repository will use the same directory contract. Review every path, command, model invocation, allowed-change rule, and status parser before execution.

`docs/ai/GRAPHIFY_USAGE.md` may be copied as a policy baseline, but update the Graphify version and known parser limitations for the receiving project.

## Adapt before use

The files under `docs/ai/architecture-specs/` demonstrate focused scope specifications. Their structure is reusable, but their evidence paths, feature terminology, platform assumptions, and required content must be adapted to the new repository.

## Examples only — do not copy as project truth

`docs/ai/examples/` contains real project-shaped examples of manifests, routing, Graphify overrides, and checkpoint state. Regenerate or edit them from the receiving repository’s evidence. Never reuse revisions, source paths, feature order, test counts, owner decisions, or completion state as facts.

## Expected repository locations

After adaptation, the runners expect files such as:

- `docs/ai/DOCUMENTATION_CHECKPOINT.md`
- `docs/ai/feature-docs.tsv`
- `docs/ai/architecture-docs.tsv`
- `docs/ai/GRAPHIFY_USAGE.md`
- `docs/ai/graphify-context-overrides.tsv`
- `docs/ai/prompts/`
- `docs/ai/architecture-specs/`
- `scripts/run-doc-phase.sh`
- `scripts/generate-feature-docs.sh`
- `scripts/run-architecture-doc.sh`

Start with dry runs. Keep creation, independent review, and promotion as separate tasks. Stop using an external prompt-writing intermediary once repository policy, reviewed context, a single-task checkpoint, reviewed decisions, the Phase 3.6 audit, and an approved plan are available.
