# Protected Boundaries Policy

## 1. Purpose

Protected boundaries require explicit authority, preflight review, fail-closed behavior, and matching evidence. This policy is shared by Android and iOS; platform overlays define platform-specific mechanics.

## 2. Protected categories

Treat as protected unless explicitly narrowed:

- identity, authentication, authorization, account linking, and entitlement;
- secrets, API keys, tokens, certificates, signing material, and production configuration;
- sensitive user data, regulated data, destructive persistence, deletion, backup, and device transfer;
- public APIs, backend contracts, provider schemas, externally visible identifiers, and data exports;
- permissions, capabilities, manifests, entitlements, exported components, app links, universal links, custom schemes, and external entry points;
- background execution, push, notifications, workers, services, receivers, widgets, extensions, and scheduled operations;
- billing, subscriptions, receipts, financial transactions, and entitlement state;
- health, medical, child-safety, legal, and regulated behavior;
- analytics, advertising, tracking, crash reporting, observability, and raw-data logging;
- external AI, provider SDKs, attestation, and server gateways;
- signing, archive/export, store credentials, distribution, rollout, and publication.

## 3. Preflight

Before protected work, run `protected-boundary-preflight` or equivalent.

The preflight must identify:

- exact boundary;
- authority;
- data involved;
- purpose and minimization;
- permission, disclosure, or consent;
- storage, retention, backup, transfer, and deletion;
- network and provider behavior;
- logging and redaction;
- environment separation;
- failure and recovery;
- test and runtime evidence;
- release implications;
- owner decisions still required.

A `Blocked`, `Fail`, or unresolved owner decision stops affected work.

## 4. Fail-closed rule

Missing or invalid protected configuration must result in an explicit:

- unavailable;
- recoverable error;
- queued state;
- degraded local mode;
- owner-approved manual fallback.

Never fall back to fake success, permissive authorization, silent data loss, or simulated provider completion.

## 5. Configuration files

A configuration file, plist, JSON/XML resource, manifest entry, entitlement, dependency, or SDK declaration does not authorize use.

Configuration retained for future features must document:

- repository path;
- source-set or target membership;
- build-phase/package inclusion;
- runtime discovery and automatic initialization;
- linked SDKs;
- network behavior;
- privacy impact;
- active or dormant status;
- authorizing decision;
- removal or activation conditions.

Dormant configuration must not silently activate an out-of-scope service.

## 6. Secrets

- Never commit production secrets.
- Client-visible configuration must be treated as public unless the platform guarantees otherwise.
- Use approved secret stores and CI injection.
- Do not print secrets in logs, evidence, screenshots, test output, or reports.
- Redact tokens, user data, and sensitive identifiers.

## 7. Data handling

Every collected, stored, transferred, logged, or deleted data category requires:

- approved purpose;
- minimization;
- classification;
- storage location;
- protection;
- retention;
- backup and transfer;
- deletion behavior;
- logging rule;
- failure and recovery;
- evidence.

Do not overclaim secure or forensic deletion.

## 8. External services

Before provider or backend integration, define:

- ownership;
- endpoint and environment;
- credentials;
- request/response contracts;
- timeout, retry, cancellation, and idempotency;
- offline behavior;
- attestation;
- privacy and redaction;
- staging and production separation;
- outage and recovery;
- user-visible terminal states.

## 9. Permissions and capabilities

Request only approved permissions and capabilities.

Define:

- trigger;
- rationale;
- denied, restricted, unavailable, and revoked states;
- retry or settings recovery;
- least privilege;
- platform declarations;
- runtime evidence;
- removal behavior.

A framework import does not justify a permission.

## 10. Release and publishing

Production signing, provisioning, entitlements, archive/export, store upload, rollout, and publication require separate release authorization.

Preparation and inspection may be read-only. Remote side effects require explicit approval.
