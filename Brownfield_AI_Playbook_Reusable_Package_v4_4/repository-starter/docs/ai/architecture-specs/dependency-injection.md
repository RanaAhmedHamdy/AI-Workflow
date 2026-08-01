# Dependency Injection map specification

## Checklist coverage

- Dependency injection and service location
- Dependency direction, cycles, isolation, scopes, and test seams
- Module/domain ownership where DI establishes a boundary

## Discovery question

How are application scope, DataStores, repositories, ViewModels, Routes, fakes,
and preview/test seams constructed, scoped, qualified, and consumed, and what
runtime Hilt behavior remains unverified?

## Required evidence

- application and activity Hilt annotations
- `di/RepositoryModule.kt` and `di/Qualifiers.kt`
- all repository interfaces and implementations
- all `@HiltViewModel` constructors
- Route composable `hiltViewModel()` access
- preview/test construction and fake repositories
- Gradle Hilt/KSP/kapt declarations as applicable
- reviewed Data Flow, Modules, Dependencies, Architecture, and Testing pages

## Required content

- provider/binding inventory and dependency direction
- singleton/application/ViewModel/UI-local lifetimes
- qualifier separation
- manual construction and fake seams
- Route versus Screen access rules
- placeholder purchase/settings bindings and consumers
- potential service-location or interface-delegation exceptions
- static declaration versus generated/runtime graph evidence
- cycle/isolation/testability observations

Do not infer successful runtime component creation solely from annotations and
provider declarations.
