---
name: ios-project-structure-readiness
description: Validates or inventories iOS target, module, package, folder, and dependency ownership. Supports evidence-only bootstrap mode without turning existing project settings into owner decisions.
---

# iOS Project Structure Readiness

## Modes

- `EVIDENCE-ONLY / BOOTSTRAP`: inventory verified project facts and unknowns. Do not accept generated defaults or choose new architecture.
- `FEATURE / READINESS`: validate the accepted structure against the planned/implemented feature.

## Inspect

- bundle/module namespace;
- application, extension, widget, watch, vision, and test targets;
- target membership and resource ownership;
- checked-in Xcode project versus project generator;
- Xcode/project-format evidence, Swift language/concurrency settings, and deployment settings when relevant;
- local Swift packages and external package products / `Package.resolved` state;
- schemes, configurations, test plans, and derivable local build/test commands;
- application composition root;
- feature ownership boundaries;
- Presentation/Domain/Data/Platform dependency direction;
- locations for observable state, views, navigation, repositories, clients, persistence, background handlers, intents, widgets, and design-system code;
- test targets and fixtures;
- criteria for one app target versus local package extraction.

Flag generic dumping grounds, feature logic in platform hosts, service locators, circular dependencies, duplicate containers, incorrect target membership, and ceremonial empty packages/targets.

In evidence-only mode return verified facts, contradictions, and `Needs verification` items. Existing settings are implementation evidence, not automatic owner approval.

Verdicts:
- `Evidence gathered — owner decisions still required`
- `Ready`
- `Ready with intentional single-target structure`
- `Blocked`
