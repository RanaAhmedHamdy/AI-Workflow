# Testability Roadmap specification

## Checklist coverage

- Testing/testability and runtime evidence
- Cross-map verification gaps
- Device, accessibility, security, performance, build, and release evidence layers

## Discovery question

Which deterministic seams and test layers exist, which material architecture
contracts are covered or uncovered, what infrastructure blocks stronger
evidence, and what is the smallest risk-backed verification sequence?

## Required evidence

- every test source and relevant Gradle test declaration
- reviewed `TESTING_MAP.md`
- all Reviewed Phase 3 architecture maps
- feature-page `Needs verification` and testing gaps
- existing scripts/CI configuration
- latest recorded test execution evidence, without silently rerunning it

## Required content

- current test layer/infrastructure inventory
- contract-to-test evidence matrix
- deterministic seams and fake/provider boundaries
- high-risk uncovered behavior
- production Hilt/DataStore integration gaps
- navigation/Compose/accessibility/adaptive UI gaps
- process-death, backup/migration, error/cancellation/concurrency gaps
- privacy/permission/billing/media/share boundary verification
- performance/resource and build/release evidence gaps
- prerequisite infrastructure versus focused tests
- prioritized roadmap with risk, smallest layer, owner/evidence dependency, and
  completion signal
- `Needs verification` and no-safe-seam classifications

Do not add tests, dependencies, production seams, CI, or arbitrary coverage
targets in this documentation task.
