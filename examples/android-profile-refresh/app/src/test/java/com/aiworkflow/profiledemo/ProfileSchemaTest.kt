package com.aiworkflow.profiledemo

import org.junit.Assert.assertEquals
import org.junit.Test

class ProfileSchemaTest {
    @Test
    fun legacy_row_without_display_name_gets_explicit_fallback() {
        assertEquals(ProfileSchema.DEFAULT_DISPLAY_NAME, ProfileSchema.displayNameForLegacyRow(null))
        assertEquals(ProfileSchema.DEFAULT_DISPLAY_NAME, ProfileSchema.displayNameForLegacyRow(""))
    }

    @Test
    fun migrated_row_preserves_existing_display_name() {
        assertEquals("Ada", ProfileSchema.displayNameForLegacyRow("Ada"))
    }
}
