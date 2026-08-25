# Public claims matrix

Use this matrix before adding release notes, README copy, badges, or presentations. A claim is only as strong as the listed evidence.

| Claim | Evidence | Status | Allowed wording |
| --- | --- | --- | --- |
| Supports native Android and iOS workflows | Namespaced packs, profile matrix, route registry | VERIFIED | “Supports Android and iOS workflow packs.” |
| Supports new and existing repositories | Greenfield/Brownfield packages and installer tests | VERIFIED | “Offers separate paths for new apps and existing repositories.” |
| Four adoption profiles | `routing/routes.json`, installer tests | VERIFIED | “Choose Skills, Safety, Feature, or Full; Safety is recommended.” |
| Safe install, update, and uninstall | Manifest ownership tests and lifecycle documentation | VERIFIED | “Refuses unmanaged overwrites and preserves modified managed files.” |
| Dual-platform composition | Installer composition tests | VERIFIED | “Can compose Android and iOS packs under separate namespaces.” |
| Deterministic routing | `routing/routes.json`, routing corpus, CLI tests | VERIFIED | “Routes stated observable facts deterministically.” |
| 71 specialist procedures | `AUDIT/19_PRODUCT_UX_ROUTING_REPORT.md`, coverage matrix | VERIFIED | “Provides about 71 canonical specialist procedures.” |
| Android demo is a maintained native fixture | `examples/android-profile-refresh` and its verification record | VERIFIED | “Includes a maintained Android fixture.” |
| iOS demo is a maintained native fixture | `examples/ios-profile-refresh` and its verification record | VERIFIED | “Includes a maintained iOS fixture.” |
| Android demo builds/tests | `examples/android-profile-refresh/VERIFICATION.md` | VERIFIED | “Android unit tests and debug build ran locally.” |
| iOS demo builds/tests | `examples/ios-profile-refresh/VERIFICATION.md` | VERIFIED | “iOS simulator build and XCTest ran locally.” |
| Works with Codex | Repository Markdown instructions and this maintained review process | PARTIALLY VERIFIED | “Repository-owned Markdown instructions were manually reviewed with Codex.” |
| Works with Claude Code | A maintained end-to-end harness result | NOT YET VERIFIED | “The Markdown format is architecturally portable; Claude Code has not been verified here.” |
| Works with GitHub Copilot coding agents | A maintained end-to-end harness result | NOT YET VERIFIED | “The Markdown format is architecturally portable; Copilot coding-agent workflows have not been verified here.” |
| Production safe / bug-free | No evidence can support a universal claim | NOT APPLICABLE | Never claim this. |

## Evidence status meanings

- **VERIFIED** — a repository artifact plus an executable test or direct inspection supports the claim.
- **PARTIALLY VERIFIED** — one aspect is demonstrated, but the public claim must name its limit.
- **DESIGN CLAIM** — the project is designed for this behavior; it is not runtime proof.
- **NOT YET VERIFIED** — do not present as a fact.
