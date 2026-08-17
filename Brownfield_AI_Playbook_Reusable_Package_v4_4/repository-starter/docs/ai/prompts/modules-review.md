# Task: Read-only review of MODULES.md

Review only:

`docs/wiki/project/MODULES.md`

Do not edit any file and do not change document status.

Verify material claims against current repository/build evidence. Check:
- missing or invented modules/targets;
- incorrect module responsibilities;
- build-declared dependency direction errors;
- source-set/test topology errors;
- folder-name assumptions presented as ownership facts;
- runtime claims inferred from declarations;
- desired modularization presented as current state;
- missing exceptions, provenance, or Needs verification;
- broken repository-relative paths.

Return exactly these sections:
1. Blocking findings.
2. Non-blocking findings.
3. Smallest revision scope.
4. Promotion recommendation: `Promote`, `Revise`, or `Blocked`.
5. Evidence inspected and commands run.

Recommend `Promote` only when no blocking documentation correction is required.
