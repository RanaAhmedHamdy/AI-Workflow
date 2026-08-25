# Changelog

All notable public-facing changes are recorded here. The repository has no established public release tags, so this file does not invent historical release dates.

## 0.9.0

First pre-v1 external-evaluation candidate. This is not a v1 compatibility
promise.

### Added

- Manifest-backed safe install/update/status/uninstall lifecycle with dual-platform composition.
- Four adoption profiles: `skills`, `safety`, `feature`, and `full`; Safety is the recommended default.
- Deterministic fact-based routing across 13 concern routes.
- Android and iOS profile-refresh fixtures with deliberately isolated risky examples and route evidence.
- Public quickstart, claims matrix, v1 support-policy draft, support/community templates, and release-artifact policy.

### Changed

- Root README is now a concise product landing page with a five-minute route-first trial and links to detailed documentation.
- iOS plan/review procedures were expanded for concurrency, scene, persistence, target/configuration, privacy, and accessibility safeguards.

### Fixed

- Installer ownership protection, rollback, profile transitions, and source/wheel/sdist release validation were established during pre-public remediation.

### Removed

- Retired the duplicate Android aliases `adaptive-compose`, `localization-rtl-readiness`, and `runtime-evidence-readiness` in favor of their canonical procedures. See [docs/SKILL_ALIASES.md](docs/SKILL_ALIASES.md).

### Security

- The installer rejects unmanaged overwrites, traversal, symlinked destinations, malformed manifests, and modified managed-file replacement.
