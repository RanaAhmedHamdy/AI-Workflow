# AI-Workflow 0.9.0 owner release checklist

This is an owner-executed checklist. Checking a box means evidence exists; it
does not authorize publication by an automated job.

## Before merge

- [ ] Candidate changes are reviewed and the working tree is clean.
- [ ] `python tools/validate_repository.py` passes.
- [ ] `python -m unittest discover -s tests` passes.
- [ ] Hosted Linux, macOS, Windows, Android, and iOS jobs pass.
- [ ] Public claims, README commands, metadata, and release notes agree.
- [ ] Android and iOS fixture evidence is current for the candidate commit.

## Candidate commit

- [ ] Project, distribution, CLI, and release-manifest version are `0.9.0`.
- [ ] `python tools/version_check.py` passes.
- [ ] `python tools/release_check.py` passes with the documented build environment.
- [ ] Exact approved commit SHA is recorded.
- [ ] Candidate source ZIP, wheel, and sdist are clean and share that SHA.

## Public visibility smoke test

- [ ] Owner changes the repository to Public.
- [ ] Anonymous browser can open the repository, README, tags, Actions, Issues,
      Releases, and referenced security/support pages.
- [ ] The default branch and tag `v0.9.0` resolve anonymously.
- [ ] README remote quickstart works without credentials.
- [ ] Hosted CI status is visible and green for the candidate/tag.

## PyPI setup

- [ ] `ai-workflow` namespace is still available and name confusion is accepted.
- [ ] PyPI Trusted Publisher is configured for this repository and this exact
      workflow filename.
- [ ] GitHub environment `pypi` exists and requires maintainer approval.
- [ ] No pull-request workflow has publishing credentials or `id-token: write`.
- [ ] TestPyPI validation is complete, or the owner records why it is unnecessary.

## Tag and release

- [ ] Owner creates and pushes `v0.9.0` from the approved commit.
- [ ] Release workflow rejects any tag/version mismatch.
- [ ] GitHub Release is a prerelease with the approved notes and checksums.
- [ ] PyPI receives the exact validated wheel and sdist.
- [ ] PyPI attestations/provenance are visible where supported by the publishing path.
- [ ] `uvx --from ai-workflow==0.9.0 ai-workflow profiles` works anonymously.

## After release

- [ ] GitHub-tag and PyPI quickstart commands both work.
- [ ] External feedback issue is opened and monitored.
- [ ] Installation, routing, profile, native-CI, and documentation feedback is logged.
- [ ] A serious defect is yanked where appropriate and fixed in `0.9.1`; the
      original file is never silently replaced.

## Response rule

If `0.9.0` is materially broken, stop announcements, document the issue, yank
the release when appropriate, publish a corrected version, and update the
GitHub Release. Do not delete and silently replace a published file.
