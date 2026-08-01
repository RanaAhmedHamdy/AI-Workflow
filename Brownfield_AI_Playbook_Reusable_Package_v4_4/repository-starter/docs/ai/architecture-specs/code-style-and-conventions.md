# Code Style and Conventions map specification

## Checklist coverage

- Code style and conventions
- Dependency/layering conventions that affect maintainability
- Generated-source, resource, test, and documentation conventions

## Discovery question

What naming, package, file organization, Compose, Route/Screen, ViewModel,
repository, Flow/coroutine, DI, resource, test, formatting, and generated-source
conventions are consistently observed, and what exceptions exist?

## Required evidence

- representative source from every major package
- Gradle formatting/lint configuration and scripts
- Route/Screen/ViewModel/repository patterns
- theme/components/resources
- test packages, fakes, naming, and coroutine-test patterns
- generated/build exclusions and Graphify boundaries
- reviewed Modules, Architecture, Dependency Injection, Design System, State,
  Testing, and feature pages

## Required content

- package/file/type/function naming
- layer and dependency conventions
- Compose state/callback/preview conventions
- ViewModel/Flow/coroutine conventions
- repository/fake/DataStore conventions
- Hilt/qualifier/provider conventions
- resources, strings, icons, illustrations, and accessibility conventions
- test organization and assertion boundaries
- formatting/lint/tool availability
- comments, generated sources, documentation, and Graphify-output rules
- observed exceptions and `Needs verification`

Describe observed and mandatory conventions separately. Do not turn preferences
into established policy without evidence.
