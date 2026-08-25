package com.aiworkflow.profiledemo

import android.content.Context
import android.database.sqlite.SQLiteDatabase
import android.database.sqlite.SQLiteOpenHelper

/** Local-only persistence whose v1 -> v2 migration is intentionally small and testable. */
class ProfileDatabase(context: Context) : SQLiteOpenHelper(context, "profile.db", null, ProfileSchema.VERSION) {
    override fun onCreate(db: SQLiteDatabase) {
        db.execSQL("CREATE TABLE profile (id TEXT PRIMARY KEY, display_name TEXT NOT NULL)")
    }

    override fun onUpgrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {
        if (oldVersion < 2) {
            db.execSQL("ALTER TABLE profile ADD COLUMN display_name TEXT")
            db.execSQL("UPDATE profile SET display_name = ? WHERE display_name IS NULL OR display_name = ''", arrayOf(ProfileSchema.DEFAULT_DISPLAY_NAME))
        }
    }

    fun load(): Profile {
        readableDatabase.rawQuery("SELECT id, display_name FROM profile LIMIT 1", null).use { cursor ->
            return if (cursor.moveToFirst()) {
                Profile(cursor.getString(0), ProfileSchema.displayNameForLegacyRow(cursor.getString(1)))
            } else {
                Profile("local", ProfileSchema.DEFAULT_DISPLAY_NAME)
            }
        }
    }

    fun save(profile: Profile) {
        writableDatabase.execSQL(
            "INSERT OR REPLACE INTO profile (id, display_name) VALUES (?, ?)",
            arrayOf(profile.id, profile.displayName),
        )
    }
}
