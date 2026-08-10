# Android Permission and Capability Readiness

## Purpose
Review Android permissions, manifests, exported components, external entry points, background capabilities, and protected configuration.

## Required inputs
- manifests and merger output
- permission/capability decisions
- feature contract, plan, and tasks
- provider/SDK configuration
- privacy and runtime evidence

## Checks
- least privilege and approved trigger/rationale
- denied/restricted/revoked recovery
- exported Activities/Services/Receivers/Providers
- app links, deep links, intent filters, and schemes
- foreground services, alarms, WorkManager, boot behavior
- dormant future configuration and runtime initialization
- release manifest/APK/AAB inspection

## Verdicts
`PASS`, `FAIL`, `BLOCKED`, or `NEEDS OWNER DECISION`.
