# v1 exit criteria

AI-Workflow should remain pre-v1 until evidence, rather than calendar time,
supports a stable `1.0.0` boundary. The owner should record links or artifacts
for each item below.

## Required evidence

- At least two external Android evaluations, including one Safety workflow.
- At least two external iOS evaluations, including one Safety workflow.
- At least one dual-platform evaluation.
- No known destructive installer defect; install, update, collision, modified
  file, traversal, symlink, rollback, and uninstall behavior remain covered.
- Profile identifiers and transitions have survived external use without an
  undocumented breaking change.
- Routing fact identifiers and canonical skill paths have survived external use.
- Hosted Linux, macOS, Windows, Android, and iOS jobs are stable across the
  supported matrix, with simulator/device limits documented.
- At least one non-Codex coding-agent evaluation is recorded.
- README, quickstart, package metadata, claims matrix, and release notes agree.
- Any pre-v1 breaking behavior has a migration note and a planned release.

## Decision rule

Promote to `1.0.0` only when all required evidence is present and there is no
open P0/P1 issue involving data loss, unsafe overwrite, misleading release
evidence, credential exposure, or an unresolvable public installation failure.
