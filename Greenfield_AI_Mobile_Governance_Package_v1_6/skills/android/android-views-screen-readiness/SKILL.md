# Android Views Screen Readiness

## Purpose
Review XML/View-based Android screens when an approved decision selects Views or a hybrid boundary.

## Required inputs
- screen contract and design authority
- Activity/Fragment/ViewModel ownership
- navigation and lifecycle plan
- resources, RTL, adaptive, and accessibility requirements

## Checks
- thin Activity/Fragment host and ViewModel ownership
- no repository/provider work in Views or binding adapters
- lifecycle-aware observation
- resource-only strings and start/end semantics
- configuration change and process-death reconstruction
- phone/tablet/resizable layouts, IME, insets, and focus
- TalkBack semantics, traversal, touch targets, keyboard/D-pad
- runtime evidence matrix

## Verdicts
`PASS`, `FAIL`, `BLOCKED`, or `NEEDS VERIFICATION`.

## Post-Mutation and Route-Origin Readiness (v1.6)
For any screen that commits durable state, identify dependent parent/sibling/cross-feature consumers and prove their render state updates from the authoritative source without relying on accidental navigation reload. For reusable screens entered from multiple origins, verify save/cancel/failure semantics per origin, including explicit separation of onboarding/setup completion from normal management.
