# State Management map specification

## Checklist coverage

- State ownership, concurrency, lifecycle, and restoration
- Dependency boundaries that affect state lifetime
- Project-specific separation of persisted, derived, and UI-local state

## Discovery question

Which objects own application, navigation, ViewModel, repository, persisted,
derived, and Compose-local state, and what are their lifecycle, concurrency,
restoration, and one-off-event boundaries?

## Required evidence

- all feature ViewModels and shared `UiState` declarations
- repository `StateFlow` implementations and application coroutine scope
- manual navigation stack
- `remember`/`rememberSaveable` use in screens and shell
- Route collection and selection behavior
- guided index, notebook draft, settings action, progress, and completion state
- reviewed Data Flow and feature pages
- ViewModel, repository, selector, guided, and route tests

## Required content

- state ownership inventory by lifetime
- persisted versus derived versus transient state
- flow construction, sharing policy, dispatcher/scope, and cancellation
- Route/Screen state boundary
- one-off messages and action-in-progress state
- navigation and process-restoration limits
- configuration-change, process-death, rapid-action, and concurrent-edit gaps
- error visibility in state models
- test seams and runtime evidence limits

Do not prescribe SavedStateHandle, lifecycle-aware collection, or a navigation
migration as if already approved.
