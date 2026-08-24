# Intended v1 support policy

AI-Workflow remains pre-v1. This document states the compatibility boundary intended for a future v1; it is not a promise of an immediate 1.0.0 release.

## Intended stable concepts

- Public CLI command names and documented options.
- Manifest lifecycle semantics: no silent overwrite of recipient-owned or modified managed files.
- Profile identifiers: `skills`, `safety`, `feature`, and `full`.
- Canonical skill identifiers and installed path namespaces.
- Routing fact identifiers in `routing/routes.json`.
- The meaning of installer ownership, update, dry-run, and uninstall results.

## Intentionally evolving material

- Wording and examples inside specialist procedures.
- Template detail that does not change a documented output contract.
- Route recommendations when a safety improvement is backward-compatible and documented.
- Demo implementation details, build tooling, and test coverage.

## Breaking changes

A change is breaking when it removes or changes the meaning of a documented CLI option, profile, fact identifier, canonical installed path, manifest format, ownership protection, or required safety/authority state without a supported migration. It requires a major version after v1 and a migration note.

Adding an optional procedure, route, profile content, or template section is normally non-breaking. Correcting unsafe wording or a false public claim is treated as a patch unless users must migrate automation.

## Support window

The project does not promise indefinite support. Each public release will state its supported Python range, known Android/Xcode fixture matrix, and migration notes. Security reports follow [SECURITY.md](../SECURITY.md), not public issue comments.
