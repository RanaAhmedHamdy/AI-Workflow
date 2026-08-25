# Versioning and compatibility

AI-Workflow is currently **pre-v1 and under active validation**. The visible
numbers in this repository describe different things; they are not all release
versions of the same product.

## Current version map

| Thing | Current value | Meaning |
|---|---:|---|
| Project release | `0.9.0` | Current pre-v1 external-evaluation candidate identity. |
| Python distribution and CLI | `0.9.0` | Candidate version published by package metadata and the installed `ai-workflow` command. |
| Greenfield content | `1.10.0` | Content revision retained in the existing Greenfield package paths and documents. |
| Brownfield content | `4.4` | Content revision retained in the existing Brownfield package paths and playbook. |
| Greenfield pipeline document | `1.3` | Independent document revision, not the project release. |
| Greenfield current playbook document | `2.3` | Independent document revision, not the project release. |
| Historical Greenfield playbook | `2.2` | Historical reference only. |
| Brownfield iOS overlay | `1.4` | Overlay document revision retained for traceability. |
| Template policy/schema revisions | e.g. `1.1` | Per-document revision where a template declares one. |

The machine-readable companion is [`release-manifest.json`](../release-manifest.json).
It records the present values without pretending that the repository is a public
v1 release.

## Compatibility policy

Until v1, compatibility is best-effort and changes are explicitly documented.
The installer must never silently replace user-owned or user-modified files.
`--force` is not a supported public workflow while the transactional ownership
model is being implemented.

For this candidate, the project release, Python distribution, CLI,
Git tag, and release notes will share one SemVer version. Content component
revisions may remain in the manifest only when they are independently useful
for migration or historical interpretation.

A breaking release changes a documented CLI command or option, installed path,
installer-manifest format, routed skill path/output contract, required safety
gate, or the meaning of an authority/evidence state without a supported
migration. New optional skills, profiles, or template sections are minor
changes; corrections to unsafe wording or false claims are patches unless they
require users to migrate automation.

## Simplified future model

The preferred v1 model is one project SemVer version with a single root
changelog and release manifest. Version-bearing package directory names and
duplicate `VERSION` files will be retired only as part of a planned migration,
not rewritten during this P0 correction.

## Release-candidate recommendation

The appropriate next public candidate is **`0.9.0`**, not `1.0.0-rc.1`.
The installer, profiles, routing, clean artifacts, and native fixtures have matured enough for outside evaluation, but the project has no established public compatibility history or release tags and still needs real external feedback. `0.9.0` truthfully communicates a substantial pre-v1 candidate without prematurely committing the intended v1 stability boundary. Do not change the distribution version until the release-candidate publication decision and tag are approved.
