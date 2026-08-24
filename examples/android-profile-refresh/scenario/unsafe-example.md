# Risky/incomplete approach — do not use as production guidance

> Demonstration of a risky/incomplete approach. Do not apply as production guidance.

```kotlin
// Adds a non-null field to the model and updates a TextView directly.
data class Profile(val id: String, val displayName: String)

fun refresh(button: View) {
    GlobalScope.launch {
        val profile = api.fetchProfile()
        textView.text = profile.displayName
    }
}
```

It looks small, but it has no v1-to-v2 data migration for existing rows, lets work outlive the screen, and mutates UI from an unowned coroutine. The safe fixture instead has an explicit migration fallback, ViewModel-owned work, and lifecycle-aware Flow collection.
