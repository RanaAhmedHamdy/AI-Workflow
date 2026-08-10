# Changelog

## 1.4

- Added platform-specific `bounded-feature-implementation` skills for iOS and Android.
- Defined implementation as an explicitly authorized production-mutation procedure with task-local verification and evidence closure.
- Kept `feature-implementation-convergence` independent and whole-feature in scope; implementation does not duplicate its broad post-implementation audit or create `READINESS_REPORT.md`.
- Updated the canonical lifecycle, modular policies, platform procedure routing, task template, package README, governance pipeline, and agent-native playbook.
- Retained earlier playbook editions unchanged.

## 1.3

- Removed broken hook configuration.
- Removed macOS metadata.
- Updated package README.
- Retained both playbooks; updated v2.0 agent-native lifecycle and canonical filenames.
- Added pre-implementation readiness audit distinction.
- Normalized Android and iOS skill directories while keeping platform-specific same-named skills separate.
- Added missing Android coroutine, persistence/migration, permission/capability, and Views readiness procedures.
- Moved reusable feature templates outside skill folders.
- Moved architecture and readiness templates under `templates/architecture/`.
- Moved superseded policies to `historical/policies/`.
- Added AI context, decision register, feature input, and implementation readiness audit templates.
- Updated iOS installation/routing documentation away from old AGENTS and Spec Kit references.
