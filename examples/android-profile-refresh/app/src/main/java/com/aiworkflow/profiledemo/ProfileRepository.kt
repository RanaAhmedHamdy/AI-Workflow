package com.aiworkflow.profiledemo

import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.withContext

class ProfileRepository(private val database: ProfileDatabase) {
    private val _profile = MutableStateFlow(database.load())
    val profile: StateFlow<Profile> = _profile.asStateFlow()

    suspend fun refresh() = withContext(Dispatchers.IO) {
        // A real app could obtain this from a network client. This fixture stays deterministic.
        val refreshed = database.load().copy(displayName = "Ada Lovelace")
        database.save(refreshed)
        _profile.value = refreshed
    }
}
