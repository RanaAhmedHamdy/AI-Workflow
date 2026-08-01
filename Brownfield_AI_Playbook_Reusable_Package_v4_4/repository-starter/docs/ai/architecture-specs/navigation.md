# Navigation map specification

## Checklist coverage

- Navigation, deep links, and external entry points
- Argument transport and fallback behavior
- Navigation-related state restoration and UI adaptation ownership

## Discovery question

How do route constants, builders, parsing, the manual stack, main-tab
replacement, detail pushes, completion routes, back behavior, and screen
callbacks work, and what external-entry/restoration behavior is absent?

## Required evidence

- `navigation/Routes.kt`
- `navigation/StemCampNavHost.kt`
- `navigation/StemCampNavViewModel.kt`
- all Route composables and navigation callbacks
- MainActivity and manifest entry points
- route and navigation-related ViewModel tests
- reviewed Navigation and all flow-adjacent feature pages
- reviewed State Management and project Architecture pages

## Required content

- route grammar and destination model
- parser fallbacks and malformed/unknown arguments
- stack mutation rules for main and detail destinations
- Activity Completion, Lesson Completed, Share Success, and notebook transitions
- bottom-navigation visibility/selection and system-back ownership
- external entry points, intents, and deep-link classification
- argument identity and data lookup boundaries
- restoration, duplicate-tap, configuration-change, and process-death limits
- compact/expanded navigation adaptation ownership
- tested parsing versus untested stack/runtime behavior

Do not present Navigation Compose, deep links, or SavedStateHandle as current.
