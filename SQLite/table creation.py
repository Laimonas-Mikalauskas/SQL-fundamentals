import sqlite3

conn = sqlite3.connect(":memory:")
cur = conn.cursor()

cur.execute("""
CREATE TABLE person (
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    gender TEXT,
    date_of_birth DATE,
    company TEXT
)
""")

