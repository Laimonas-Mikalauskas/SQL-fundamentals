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

cur.executemany("""
INSERT INTO person VALUES (?, ?, ?, ?, ?, ?)
""", [
    ("John", "Johnson", "john@example.com", "Male", "1985-03-15", "Google"),
    ("Jane", "Wilson", "jane@example.com", "Female", "1991-07-22", "Amazon"),
    ("Peter", "Peterson", "peter@example.com", "Male", "1978-11-05", "IBM"),
    ("Marry", "Montgomery", "marry@example.com", "Female", "1995-12-01", "Google"),
])
