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
    name TEXT PRIMARY KEY
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

conn.commit()
conn.close()

print("✅ Fresh database created.")
