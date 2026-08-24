package com.aiworkflow.profiledemo

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.launch

class ProfileViewModel(private val repository: ProfileRepository) : ViewModel() {
    val profile = repository.profile

    fun refresh() {
        // The work is owned by the ViewModel rather than a disposable view callback.
        viewModelScope.launch { repository.refresh() }
    }
}
