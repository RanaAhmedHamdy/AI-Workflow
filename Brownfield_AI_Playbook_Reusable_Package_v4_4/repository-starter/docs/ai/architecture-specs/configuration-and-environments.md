# Configuration and Environments map specification

## Checklist coverage

- Configuration and environment strategy
- Feature flags, experiments, rollout, and rollback
- Secrets delivery and build-time/runtime configuration
- Analytics/observability provider configuration where present

## Discovery question

What Gradle, manifest, resource, build-type, environment, secret, endpoint,
feature-flag, analytics, and runtime configuration surfaces exist, and which
staging/production/rollout capabilities are absent or owner-dependent?

## Required evidence

- root and app Gradle files
- version catalog, Gradle properties, settings, wrapper, and local ignore rules
- manifest and resource configuration files
- build types, application ID/namespace, SDK levels, and packaging rules
- AI-client configuration only as tooling configuration, clearly separated from
  Android runtime configuration
- repository searches for endpoints, BuildConfig, flags, analytics, crash,
  remote config, and secrets
- reviewed Dependencies, Architecture, Security-related feature boundaries, and
  Testing pages

## Required content

- configuration-source inventory and ownership
- build types/flavors and environment separation
- secrets and local-only configuration boundaries
- endpoint/network configuration classification
- feature flags/experiments/kill switches/rollout/rollback classification
- analytics/crash/remote-config provider presence or absence
- debug/release differences and verification gaps
- generated/local/ignored file boundaries
- owner decisions and `Needs verification`

Do not expose secret values or treat developer AI-tool configuration as
application production configuration.
