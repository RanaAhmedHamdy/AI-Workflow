# Contributing to AI-Workflow

Contributions are welcome for both the Greenfield and Brownfield packages.

## What makes a good contribution

Useful contributions usually do one of the following:

- fix a concrete routing, platform, governance, or documentation defect;
- add a missing mobile failure mode with a clear trigger and evidence requirement;
- improve a skill without weakening authority or readiness semantics;
- add regression/evaluation cases based on a real failure mode;
- improve installation, examples, validation, or contributor experience;
- improve Android/iOS parity where there is a real capability gap rather than merely a count mismatch.

## Important repository rules

1. Preserve the separation between Greenfield and Brownfield operating models.
2. Preserve explicit human authorization boundaries. A readiness result is not implementation or release authorization.
3. Preserve Android/iOS self-contained packaging. Duplicate cross-cutting skill names across platform folders are intentional so one platform can be installed independently.
4. For dual-platform installations, keep skills under `.agents/skills/android/` and `.agents/skills/ios/`; do not flatten the packs.
5. Do not introduce project-specific facts into reusable skills/templates.
6. Do not add generated macOS archive metadata (`.DS_Store`, `__MACOSX`, `._*`).
7. New or materially changed skills should include/update regression cases in `evals/cases.json` when practical.

## Before opening a pull request

Run:

```bash
python3 tools/validate_repository.py
python3 -m unittest discover -s tests
```

If you changed skill behavior, also review the applicable cases in `evals/cases.json` and, when you have agent outputs, run:

```bash
python3 tools/evaluate_responses.py --responses-dir .eval-results --require-all
```

## Pull request description

Please include:

- problem/failure mode being addressed;
- affected package(s) and platform(s);
- authority or lifecycle impact;
- why the change is safe;
- validation/evidence performed;
- any compatibility or migration concern.

## License for contributions

By contributing to this repository, you agree that your contribution is licensed under the repository's Apache License 2.0, consistent with GitHub's standard inbound=outbound contribution model unless a separate written agreement applies.
