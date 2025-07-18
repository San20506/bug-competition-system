
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
    password TEXT
)
""")

c.execute("""
CREATE TABLE scores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    score INTEGER,
    duration INTEGER
)
""")

# Insert example teams for testing (as mentioned in requirements)
c.execute("INSERT INTO teams (name, password) VALUES (?, ?)", ("TeamAlpha", "alpha123"))
c.execute("INSERT INTO teams (name, password) VALUES (?, ?)", ("BugSquashers", "squash404"))
c.execute("INSERT INTO teams (name, password) VALUES (?, ?)", ("ErrorHunters", "error007"))
c.execute("INSERT INTO teams (name, password) VALUES (?, ?)", ("NullPointers", "nullnull"))

# Keep original test teams too
c.execute("INSERT INTO teams (name, password) VALUES (?, ?)", ("alpha", "bug123"))
c.execute("INSERT INTO teams (name, password) VALUES (?, ?)", ("beta", "fix456"))
c.execute("INSERT INTO teams (name, password) VALUES (?, ?)", ("gamma", "patch789"))

conn.commit()
conn.close()

print("✅ Fresh database created with example teams.")
