# Comparison with popular AI engineering workflows

This repository is intentionally narrower than general-purpose AI coding frameworks: it focuses on **native Android and native iOS delivery governance**, including architecture authority, protected platform boundaries, lifecycle correctness, migrations, localization/RTL, adaptive UI/accessibility, runtime evidence, and explicit owner authorization.

The comparison below describes project positioning, not a claim that one framework is universally better. General-purpose systems are often stronger at generic implementation mechanics, while AI-Workflow is designed to be stronger at native-mobile correctness and governance.

## High-level comparison

| Capability | AI-Workflow | Matt Pocock Skills | Superpowers | GitHub Spec Kit |
|---|---|---|---|---|
| Primary scope | Native-mobile governance for greenfield + brownfield | Composable engineering/productivity skills | End-to-end agentic software-development methodology | General spec-driven development toolkit |
| Native Android/iOS platform depth | **Core focus** | General-purpose | General-purpose | General-purpose |
| Architecture authority / decision synchronization | **Strong, explicit** | Skill-dependent | Plan/design oriented | Strong spec/plan workflow |
| Feature contract → plan → tasks traceability | **Explicit mobile lifecycle** | Composable rather than one mandatory lifecycle | Strong implementation workflow | **Core strength** |
| Permissions/privacy/capabilities/entitlements | **Platform-specific gates** | Generic unless a skill is added | Generic unless a skill is added | Generic unless customized |
| Persistence + migration safety | **Platform-specific gates** | Generic | Generic | Generic |
| Lifecycle/re-entry/process-death/background behavior | **Platform-specific** | Generic | Generic | Generic |
| Localization/RTL/adaptive UI/accessibility | **Required mobile readiness concerns** | Generic | Generic | Generic |
| Runtime/device/release evidence | **Explicit evidence gates** | Depends on chosen skills | Strong verification discipline | General verification/checklist support |
| TDD/debugging mechanics | Planned future improvement | **Strong** | **Strong** | Not the central specialization |
| Installation/community maturity | Early | **Mature** | **Mature** | **Mature** |
| Brownfield repository understanding | **Dedicated Brownfield package** | Skills can be composed | Methodology can be applied | Primarily spec-driven project workflow |

## Where AI-Workflow is stronger for native mobile

### 1. Platform correctness is part of the workflow, not an optional afterthought

Greenfield has dedicated readiness procedures for:

- Android coroutines/Flow, Compose and Views, Room/DataStore migrations, permissions, manifest/exposure, process death, WorkManager/background concerns, adaptive UI, RTL, TalkBack, and runtime evidence.
- iOS Swift concurrency, SwiftUI/UIKit, persistence/migrations, privacy manifests, required-reason APIs, capabilities/entitlements, Dynamic Type, VoiceOver, localization/RTL, lifecycle/re-entry, and runtime evidence.

These checks are routed into planning, task authoring, bounded implementation, convergence, and final readiness rather than existing only as a generic checklist.

### 2. Product authority and implementation authority are separated

The Greenfield package distinguishes PRD/product authority, optional approved Design Authority, architecture bootstrap, owner-gated ADR lifecycle decisions, Feature Input, Feature Contract, Architecture Spine/ADRs, Implementation Plan, Implementation Tasks, readiness, explicit implementation authorization, convergence, owner acceptance, and release authorization. Passing one stage does not silently grant authority for the next.

### 3. Mobile evidence is treated as a first-class artifact

Static code inspection or host-side tests are not treated as proof for device-only behavior, accessibility, lifecycle, signing, protected configuration, migration, or release behavior. The package explicitly asks for the evidence appropriate to the risk.

### 4. Greenfield and Brownfield are separate operating modes

The repository does not force a new-project lifecycle onto an existing application. Brownfield starts with discovery, provenance, characterization tests, no-edit audits, architecture coverage, safety-net creation, and bounded change. Greenfield starts by establishing product authority, optional approved external design authority, and a synchronized architecture baseline before bounded feature delivery.

## Where the other projects are currently stronger

AI-Workflow should not pretend to replace strengths that already exist elsewhere:

- **Matt Pocock Skills** has a mature, composable skill ecosystem and strong implementation-oriented skills such as TDD. Official repository: https://github.com/mattpocock/skills
- **Superpowers** has a mature end-to-end methodology with brainstorming, planning, TDD, debugging, review, and execution mechanics. Official repository: https://github.com/obra/superpowers
- **GitHub Spec Kit** has a mature general spec-driven workflow, CLI/integration ecosystem, presets, and extensions. Official repository: https://github.com/github/spec-kit

A practical integration strategy is to keep **AI-Workflow as the repository authority for native-mobile governance** and optionally use compatible generic skills for implementation techniques such as TDD/debugging. Avoid running multiple competing contract/plan/task authorities at the same time.

## Positioning statement

A concise public description is:

> AI-Workflow is a repository-owned governance system for AI-assisted native Android and iOS development. It provides separate Greenfield and Brownfield operating models with architecture synchronization, platform-specific readiness gates, protected-boundary controls, evidence-driven delivery, and explicit human authorization from feature intake through release readiness.

## Sources used for this comparison

This positioning was checked against the current public project documentation in August 2026:

- Matt Pocock Skills: https://github.com/mattpocock/skills
- Superpowers: https://github.com/obra/superpowers
- GitHub Spec Kit: https://github.com/github/spec-kit

Feature sets evolve, so keep this comparison qualitative rather than relying on volatile star counts or exact skill counts.
