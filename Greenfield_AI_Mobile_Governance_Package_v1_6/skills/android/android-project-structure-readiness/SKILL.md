---
name: android-project-structure-readiness
description: Validates application namespace, thin Activity, composition root, feature ownership, package/module boundaries, and allowed dependencies before Android code generation.
---
# Android Project Structure Readiness

Check:
- approved namespace/source roots;
- intentionally single-module or approved module tree;
- app/composition-root ownership;
- thin Activity contract;
- feature presentation/domain/data ownership;
- allowed dependency directions and cycle prevention;
- locations for ViewModels, routes, content, navigation, repositories, data sources, workers, design system, resources, tests;
- prohibition on feature code in Activities, root packages, top-level `feature/` outside namespace, or generic `utils` dumping grounds;
- criteria for future module extraction.

Return `Ready for walking skeleton`, `Ready with intentionally single-module structure`, or `Blocked`.
