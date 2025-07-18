
import sqlite3
import os

# ✅ Clean old DB
if os.path.exists('database.db'):
    os.remove('database.db')
    print("🧹 Old database removed.")

# ✅ Create new DB
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create tables
c.execute("""
CREATE TABLE teams (
    name TEXT PRIMARY KEY,
    password TEXT,
    site_id INTEGER DEFAULT 1
)
""")

c.execute("""
CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    score INTEGER,
    duration INTEGER,
    site_id INTEGER
)
""")

# Insert example teams for testing (as mentioned in requirements)
c.execute("INSERT INTO teams (name, password, site_id) VALUES (?, ?, ?)", ("TeamAlpha", "alpha123", 1))
c.execute("INSERT INTO teams (name, password, site_id) VALUES (?, ?, ?)", ("BugSquashers", "squash404", 2))
c.execute("INSERT INTO teams (name, password, site_id) VALUES (?, ?, ?)", ("ErrorHunters", "error007", 3))
c.execute("INSERT INTO teams (name, password, site_id) VALUES (?, ?, ?)", ("NullPointers", "nullnull", 4))

# Keep original test teams too
c.execute("INSERT INTO teams (name, password, site_id) VALUES (?, ?, ?)", ("alpha", "bug123", 5))
c.execute("INSERT INTO teams (name, password, site_id) VALUES (?, ?, ?)", ("beta", "fix456", 1))
c.execute("INSERT INTO teams (name, password, site_id) VALUES (?, ?, ?)", ("gamma", "patch789", 2))

conn.commit()
conn.close()

print("✅ Fresh database created with example teams.")
