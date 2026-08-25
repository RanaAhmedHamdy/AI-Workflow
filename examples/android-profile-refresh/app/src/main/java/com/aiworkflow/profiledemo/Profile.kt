package com.aiworkflow.profiledemo

data class Profile(
    val id: String,
    val displayName: String,
)

/**
 * Version-two migration policy: existing rows receive an explicit safe fallback.
 * A generic agent often adds a non-null column but forgets that version-one rows exist.
 */
internal object ProfileSchema {
    const val VERSION = 2
    const val DEFAULT_DISPLAY_NAME = "Unnamed profile"

    fun displayNameForLegacyRow(value: String?): String = value?.takeIf { it.isNotBlank() } ?: DEFAULT_DISPLAY_NAME
}
