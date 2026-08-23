---
name: android-project-structure-readiness
description: Inventories or validates Android namespace, Gradle/module/source structure, thin Activity ownership, composition, and dependency direction. Supports evidence-only bootstrap mode without treating generated defaults as owner decisions.
---

# Android Project Structure Readiness

## Modes

- `EVIDENCE-ONLY / BOOTSTRAP`: inventory verified repository/project facts and unknowns. Do not choose a new module tree, namespace, SDK baseline, DI system, or dependency structure.
- `FEATURE / READINESS`: validate the accepted structure against the planned/implemented feature.

## Inspect

- namespace/application ID/source roots;
- Gradle/project structure and intentionally single-module or approved module tree;
- compile/min SDK and language/toolchain settings as evidence where relevant;
- build variants/flavors, test modules/source sets, dependencies/version catalogs/lock state;
- app/composition-root ownership;
- thin Activity contract;
- feature presentation/domain/data ownership;
- allowed dependency directions and cycle prevention;
- locations for ViewModels, routes, content, navigation, repositories, data sources, workers, design system, resources, tests;
- derivable local build/test commands;
- criteria for future module extraction.

Flag feature code in Activities/root packages, top-level feature code outside approved namespace, generic `utils` dumping grounds, circular dependencies, duplicate composition paths, and ceremonial modules.

In evidence-only mode return verified facts, contradictions, and `Needs verification` items. Existing settings are implementation evidence, not automatic owner approval.

Verdicts:
- `Evidence gathered — owner decisions still required`
- `Ready for walking skeleton`
- `Ready with intentionally single-module structure`
- `Blocked`
