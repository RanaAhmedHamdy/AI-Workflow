package com.aiworkflow.profiledemo

import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.activity.viewModels
import androidx.appcompat.app.AppCompatActivity
import androidx.lifecycle.ViewModel
import androidx.lifecycle.ViewModelProvider
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.repeatOnLifecycle
import kotlinx.coroutines.launch

class MainActivity : AppCompatActivity() {
    private val viewModel: ProfileViewModel by viewModels {
        object : ViewModelProvider.Factory {
            @Suppress("UNCHECKED_CAST")
            override fun <T : ViewModel> create(modelClass: Class<T>): T {
                return ProfileViewModel(ProfileRepository(ProfileDatabase(applicationContext))) as T
            }
        }
    }

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        val profileName = findViewById<TextView>(R.id.profileName)
        findViewById<Button>(R.id.refresh).setOnClickListener { viewModel.refresh() }

        lifecycleScope.launch {
            // Collection stops outside STARTED; no Activity/view reference is retained by the flow.
            repeatOnLifecycle(androidx.lifecycle.Lifecycle.State.STARTED) {
                viewModel.profile.collect { profile -> profileName.text = profile.displayName }
            }
        }
    }
}
