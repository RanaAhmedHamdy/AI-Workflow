# Navigation map specification

## Checklist coverage

- App/session entry, navigation ownership, stacks/tabs/modals, and feature routing
- Storyboard/XIB/code/SwiftUI destination construction where observed
- Deep links, URL schemes, universal links, notifications, and other external entry points
- Argument transport, fallback behavior, restoration, and form-factor navigation differences

## Discovery question

How does the current iOS application enter and move between screens/features, who owns navigation decisions and destination construction, how are arguments/deep links/external entries transported and validated, and what restoration or runtime behavior remains unverified?

## Required evidence

Inspect current evidence where applicable:

- app/scene delegates, root-controller setup, launch/session entry, and composition roots
- storyboards/XIBs, storyboard identifiers, segues, navigation controllers, tab bar controllers, split views, modal presentation, and programmatic transitions
- routers/coordinators/navigation helpers and feature builders actually present
- SwiftUI `NavigationStack`/`NavigationSplitView` only if actually present
- URL schemes, associated domains, universal links, notification taps, custom URL handling, and other external entry points
- argument/identifier transport and destination lookup
- target/flavor-specific storyboard/root/navigation selection
- navigation-related tests and Reviewed feature pages
- reviewed State Management, Architecture, Configuration, Security, and UI Adaptation maps

## Required content

- entry/root/session navigation model
- destination inventory at the appropriate cross-feature level
- stack/tab/modal/root replacement rules and navigation owner
- storyboard/XIB/programmatic/SwiftUI construction boundaries where observed
- router/coordinator responsibilities and callbacks
- argument identity, parsing/validation, and data-lookup boundaries
- deep-link/external-entry classification and protected boundaries
- target/flavor navigation divergence
- system-back equivalents, dismissal/pop behavior, duplicate-action risks, and reentrancy where evidenced
- scene/restoration/process-relaunch limits
- iPhone/iPad/split-view/multitasking navigation differences where evidenced
- tests versus unverified runtime behavior
- `Needs verification`

## Evidence limits

- Static source and project configuration prove only the inspected implementation.
- Unit tests prove only their executed assertions.
- Runtime, device, accessibility, backend, security, signing, archive, distribution, and production claims require matching evidence.
- Graphify or another graph tool may route discovery, but material relationships must be verified against current source, tests, or project configuration. Missing graph edges are not evidence of absence.
- Reviewed foundation and feature documents are orientation evidence; current source/configuration wins when they conflict.
- Unresolved material claims remain `Needs verification`.

## Explicit non-goals

- Do not introduce a coordinator, router, `NavigationStack`, `NavigationSplitView`, or new navigation architecture.
- Do not infer deep-link support from URL schemes alone; trace actual handling.
- Do not claim restoration, notification routing, or universal-link behavior without matching runtime/platform evidence.
- Do not modify storyboard identifiers, segues, target membership, or root composition.
