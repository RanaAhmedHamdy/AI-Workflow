# Build and Release map specification

## Checklist coverage

- Xcode build graph, schemes, configurations, targets, dependency resolution, and toolchain
- Signing, provisioning, entitlements, archive/export, distribution, and rollback boundaries
- CI/shared verification presence or absence
- dSYM/symbol, crash-reporting, artifact, and release-evidence handling
- Simulator/device/release verification matrix

## Discovery question

How is the native iOS application currently built, versioned, dependency-resolved, signed, tested, archived, and prepared for distribution, and what CI, artifact, symbol, credential, rollout, rollback, and release evidence is absent, protected, externally managed, or still `Needs verification`?

## Required evidence

Inspect only applicable current evidence, including:

- `.xcodeproj`, `project.pbxproj`, `.xcworkspace`, shared schemes, test plans, build configurations, and `.xcconfig` files
- target build settings, deployment targets, supported platforms, product/bundle/version settings, target dependencies, and generated build phases
- `Info.plist`, entitlements, capabilities, and target-specific resources/configuration
- `Podfile`/`Podfile.lock`, Swift Package manifests/resolution files, Carthage files, or other dependency-manager evidence actually present
- `Gemfile`/`Gemfile.lock`, Fastlane files, shell scripts, Makefiles, or repository build/release tooling actually present
- repository CI/workflow configuration and shared validation scripts
- signing/provisioning references without reading, printing, decoding, or exposing credentials or private material
- reviewed `DEPENDENCIES.md`, `TESTING_MAP.md`, configuration/security maps, and recorded test/build evidence

## Required content

- workspace/project/target/scheme/configuration build graph
- Xcode/Swift/deployment-target/toolchain evidence and compatibility gaps
- version/build-number ownership and target-specific differences
- dependency resolution and lock/resolution artifacts
- Debug/Release and other configuration differences actually observed
- build, test, archive, export, and validation commands supported by repository evidence, distinguishing commands actually run from candidate commands
- signing/provisioning/entitlement/certificate/profile boundaries without secret disclosure
- archive, dSYM/symbol, crash-symbol upload, artifact-retention, and distribution evidence
- CI/MR/release pipeline classification and externally managed gaps
- TestFlight/App Store/enterprise/ad-hoc or other distribution channels only when evidenced
- rollout, rollback, telemetry, and release-verification gaps
- protected release actions, accountable approvals, and `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not change signing, provisioning, entitlements, bundle identifiers, deployment targets, schemes, configurations, dependency versions, or release settings.
- Do not run archive/export/distribution or mutate App Store Connect/TestFlight unless separately authorized.
- Do not infer release readiness from a local build or infer a CI pipeline from local scripts.
- Do not expose credentials, provisioning contents, private keys, tokens, or secret configuration values.
- Do not prescribe migration to Swift Package Manager, a project generator, newer Xcode settings, Swift 6 mode, or another build system.
