# Configuration and Environments map specification

## Checklist coverage

- Build-time and runtime configuration strategy
- Schemes, targets, build configurations, environment/flavor/client separation
- Endpoint, secret-delivery, feature-flag, analytics, remote-config, and provider configuration where present
- Generated/local/ignored configuration boundaries and drift risks

## Discovery question

What Xcode, target, scheme, build-configuration, plist, xcconfig, bundle-setting, resource, environment, endpoint, secret-delivery, feature-flag, analytics, remote-config, and runtime configuration surfaces exist, and which staging/production/rollout capabilities are absent, externally managed, protected, or owner-dependent?

## Required evidence

Inspect only applicable current evidence, including:

- `.xcodeproj`, `project.pbxproj`, `.xcworkspace`, shared schemes, build configurations, user-defined build settings, and `.xcconfig` files
- target `Info.plist`, entitlements, bundle identifiers, product names, URL schemes, associated domains, and target-specific resources where relevant
- configuration selectors or centralized app/flavor/environment objects actually present
- `Podfile`/lockfiles, package manifests, build scripts, generated config, and ignore rules
- Firebase/analytics/crash/remote-config provider files or code references where actually present, without exposing secret values
- searches for endpoints, environment switches, feature flags, kill switches, experiments, analytics, crash reporting, logging, and remote configuration
- reviewed Dependencies, Architecture, Security, Build/Release, and feature documentation

## Required content

- configuration-source inventory and ownership
- targets/schemes/configurations and client/flavor/environment separation
- bundle/product/resource/configuration differences across targets where evidenced
- secret-delivery and local-only configuration boundaries without secret disclosure
- endpoint/network-environment ownership and override behavior
- feature flags, experiments, kill switches, rollout/rollback classification
- analytics, crash reporting, remote config, logging, and telemetry provider presence/absence
- Debug/Release and other configuration differences
- generated/local/ignored file boundaries and configuration-drift risks
- externally managed configuration and accountable-owner dependencies
- `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not expose API keys, tokens, certificates, profiles, secrets, or private configuration values.
- Do not change bundle identifiers, signing teams, endpoints, Firebase files, build settings, flags, environments, or production configuration.
- Do not treat developer AI-tool/MCP/editor configuration as application runtime configuration.
- Do not infer an environment merely from a filename; verify how it is selected and consumed.
