# Security Boundaries map specification

## Checklist coverage

- Authentication/authorization/session and sensitive-data boundaries
- Keychain/files/preferences/database/network transport boundaries
- Permissions, entitlements, capabilities, deep links, external inputs, and platform integrations
- Privacy/analytics/logging/background/release-sensitive boundaries

## Discovery question

What identity, authorization, user-data, storage, transport, permission, entitlement, capability, external-entry, logging/analytics, background, financial, privacy, and release-sensitive boundaries exist in the current iOS app, and which guarantees remain runtime/backend/security/release `Needs verification`?

## Required evidence

Inspect current evidence only as needed and without exposing secrets, including:

- `AGENTS.md`, approved security/privacy/product decisions, and Reviewed feature pages
- authentication/session/token/cookie code and backend-contract evidence available in the repository
- Keychain, `UserDefaults`, files, caches, database, and deletion/logout behavior
- `Info.plist` usage descriptions, ATS configuration, URL schemes, associated domains, and other security-relevant declarations
- entitlements such as App Groups, iCloud, push, keychain sharing, associated domains, or other capabilities actually present
- certificate pinning/custom trust/network-security code if present
- push/background/notification, camera/microphone/photos/location/biometric or other permissioned framework code if present
- analytics/crash/logging/advertising/tracking/privacy manifests and required-reason API declarations where present
- StoreKit/payment/subscription code only if present
- build/dependency searches for security-sensitive integrations
- reviewed Data Flow, Persistence, Configuration, Error Handling, Build/Release, Testing, and feature pages

## Required content

- sensitive-data and trust-boundary inventory
- authentication/session/token/cookie storage and lifecycle boundaries within available evidence
- authorization decisions performed client-side versus backend-dependent contracts
- at-rest storage boundaries and deletion/logout behavior
- network transport/ATS/pinning/custom-trust boundaries
- permissions declared/requested, denial/degraded paths, and capability ownership
- URL schemes, universal links, notification payloads, external inputs, exported/shared data, and validation boundaries
- entitlements/App Groups/iCloud/push/background capability boundaries
- analytics/logging/crash/privacy/PII handling evidence
- financial/StoreKit or other regulated boundaries where present
- protected release/signing configuration cross-links
- static evidence versus runtime/backend/security/release evidence
- `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not create an unsupported threat model or claim a security guarantee from static source alone.
- Do not print secrets, tokens, profiles, certificates, keys, Firebase secrets, user data, or private configuration.
- Do not change ATS, pinning, auth/session policy, Keychain access, entitlements, permissions, privacy manifests, analytics, signing, or backend contracts.
- Do not classify a concern `Not applicable` merely because no implementation was found.
