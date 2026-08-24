# Risky/incomplete approach — do not use as production guidance

> Demonstration of a risky/incomplete approach. Do not apply as production guidance.

```swift
Task.detached {
    let profile = await client.fetchProfile()
    self.name = profile.name
    UserDefaults.standard.set(profile.name, forKey: "name")
}
```

It creates unstructured work with an unclear owner, touches UI state without a `MainActor` boundary, and gives no persistence/re-entry contract. The fixture uses a `@MainActor` model, cancellable structured work, atomic local storage, and a scene-active refresh policy.
