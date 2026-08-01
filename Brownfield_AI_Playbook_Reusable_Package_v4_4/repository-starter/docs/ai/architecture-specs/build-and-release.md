# Build and Release map specification

## Checklist coverage

- Build, signing, release, distribution, and rollback
- Crash symbols/mappings and operational artifact handling
- CI/shared verification presence or absence
- Release/device verification matrix

## Discovery question

How is the Android app built, versioned, packaged, signed, tested, and prepared
for distribution, and what CI, release-channel, artifact, symbol, credential,
rollback, and store evidence is absent or protected?

## Required evidence

- settings, root/app Gradle files, wrapper, version catalog, and properties
- manifest, resource, ProGuard/R8, packaging, and build-type configuration
- repository CI/workflow files and scripts
- signing references without reading or exposing credentials
- test tasks and reviewed Testing Map
- product roadmap publishing scope and reviewed Dependencies/Configuration/Security pages

## Required content

- module/build graph and toolchain
- SDK/application/version configuration
- debug/release differences
- dependency resolution and generated artifacts
- signing/provisioning/credential boundaries
- lint/test/package tasks and actual evidence
- CI/MR/release pipeline classification
- mapping/symbol/crash artifact handling
- distribution channels, store readiness, rollout, rollback, and telemetry gaps
- protected release actions and owner approvals
- local/static versus clean-environment/artifact/device/release evidence

Do not inspect or print secrets, infer a release pipeline from local Gradle
tasks, or claim store readiness without matching evidence.
