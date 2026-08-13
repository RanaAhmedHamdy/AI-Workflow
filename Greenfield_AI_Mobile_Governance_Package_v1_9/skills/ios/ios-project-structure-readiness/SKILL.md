---
name: ios-project-structure-readiness
description: Validates iOS target, module, package, folder, and dependency ownership before implementation.
---

# iOS Project Structure Readiness

Verify:

- bundle/module namespace;
- application, extension, widget, watch, vision, and test targets;
- target membership and resource ownership;
- checked-in Xcode project versus project generator;
- local Swift packages and external package products;
- application composition root;
- feature ownership boundaries;
- Presentation/Domain/Data/Platform dependency direction;
- locations for observable state, views, navigation, repositories, clients, persistence, background handlers, intents, widgets, and design-system code;
- test targets and fixtures;
- criteria for one app target versus local package extraction.

Flag:

- feature logic in `App`, AppDelegate, SceneDelegate, or root controllers;
- global service locators;
- generic `Utils` dumping grounds;
- circular target/package dependencies;
- duplicate dependency containers;
- files added without correct target membership;
- empty packages/targets created only for template compliance.

Return `Ready`, `Ready with intentional single-target structure`, or `Blocked`.
