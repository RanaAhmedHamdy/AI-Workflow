# Security Boundaries map specification

## Checklist coverage

- Security and sensitive-data boundaries
- Permissions and platform capabilities
- Analytics, consent, and privacy boundaries
- Background execution, notifications, and platform integrations
- Persistence and backup security cross-links

## Discovery question

What data, permission, manifest, intent, persistence, backup, billing, media,
sharing, network, logging, child-safety, and platform-capability boundaries are
implemented, prohibited, deferred, or unverified?

## Required evidence

- `AGENTS.md` and product privacy/safety requirements
- Android manifest and backup/data-extraction rules
- repository persistence code and key/value content
- navigation/external entry points
- notebook photo, Share Success, unlock/billing, guest/account, and parent-data
  feature pages and source
- build/dependency searches for network, billing, media, permissions,
  notifications, background work, analytics, and logging
- reviewed Data Flow, Persistence, Configuration, Error Handling, and Testing pages

## Required content

- data classification and storage boundaries
- permissions declared/requested and no-permission evidence
- intents, deep links, exported components, and external-entry boundaries
- backup/device-transfer uncertainty
- login/account/child-profile absence
- camera/media/photo placeholder boundary
- platform sharing/public upload boundary
- billing/financial boundary
- network/cloud/analytics/telemetry/logging boundaries
- background work/notifications/platform integrations classification
- destructive data controls and parent-guided safety
- static evidence versus runtime/security/release evidence

Do not create a threat model unsupported by scope or claim `Not applicable`
solely because an implementation was not found.
