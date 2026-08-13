# Changelog

## 1.8

- Split implementation plan/task templates into iOS/iPadOS and Android variants.
- Kept Feature Input, Feature Contract, readiness audit, and readiness report shared/mobile.
- Neutralized Android-specific wording in the shared Feature Contract.
- Added verification timing (`TASK-CLOSURE`, `FEATURE-CONVERGENCE`, `FINAL-READINESS`) and blocking scope/cost classification.
- Added evidence reuse: one valid artifact may satisfy multiple verification rows.
- Added convergence blocker taxonomy so CI/evidence/docs/repository-state blockers are not mislabeled as implementation defects.
- Preserved default-to-COMPLEX behavior when platform complexity classification is not executed or is missing/invalid/stale.
