# Installer lifecycle

AI-Workflow records every installed file in `<target>/.ai-workflow/manifest.json`.
The manifest is installer metadata, not application code. It records the schema,
workflow, selected platforms, profile, package version, file path, source identity,
and installed SHA-256 for each package-owned file.

## Ownership rules

- A package-owned file is in the manifest and still has its recorded hash.
- A modified managed file is in the manifest but has a different hash. It is always
  preserved by update and uninstall.
- An unmanaged file is not in the manifest. Installation and update never overwrite
  it.
- Directories are never recursively removed. Empty installer metadata directories may
  be removed after a complete uninstall; recipient directories remain intact.
- A file removed by a newer package is deleted only when it still matches its recorded
  hash. A modified copy is retained and recorded as residual state.

## Commands

```bash
ai-workflow greenfield --platform android --profile safety --dry-run
ai-workflow profiles
ai-workflow route --workflow greenfield --platform android --fact persistence --fact concurrency
ai-workflow greenfield --platform android --platform ios
ai-workflow status --target /path/to/repository
ai-workflow update --target /path/to/repository --profile feature --dry-run
ai-workflow update --target /path/to/repository --platform ios
ai-workflow uninstall --target /path/to/repository --dry-run
ai-workflow uninstall --target /path/to/repository
```

Use `update --platform ios` to add iOS to an existing Android installation (and
vice versa). Use `update --profile skills|safety|feature|full` for an explicit profile transition; unchanged managed files may be removed on a downgrade, while modified managed files and unmanaged files are preserved. `--platform both` is equivalent on a fresh install. Re-running an
install into a manifest-backed target is rejected; use `update` so the ownership
analysis is visible. Platform removal is not implemented in this release; use a
full uninstall only after reviewing its dry run.

`status --json` provides the same ownership summary for agents and automation,
including the canonical installed profile. `--skills-only` is a deprecated compatibility alias for `--profile skills`.
It reports missing/modified managed files and whether an update can proceed without
local conflicts.

## Safety and recovery

The installer preflights every destination, rejects absolute/traversal paths,
rejects symlinked targets and destination parents, stages file contents outside the
recipient tree, verifies staged hashes, then commits file-level changes. Existing
unmodified managed files are backed up before replacement/removal. A commit failure
rolls back changed files. The manifest is written only as part of a successful
commit. Read-only or file/directory conflicts fail without claiming success.

No command follows a symlink out of the target, overwrites recipient-owned files,
or offers a destructive `--force` mode. The retained compatibility flag exits with
migration guidance and is scheduled for removal in the next breaking CLI release.
