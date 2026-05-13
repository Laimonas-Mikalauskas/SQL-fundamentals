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
    ("Jonas", "Jonaitis", "jonas@example.com", "Male", "1985-03-15", "Google"),
    ("Ona", "Onutė", "ona@example.com", "Female", "1991-07-22", "Amazon"),
    ("Petras", "Petraitis", "petras@example.com", "Male", "1978-11-05", "IBM"),
    ("Marytė", "Morkaitė", "maryte@example.com", "Female", "1995-12-01", "Google"),
])


cur.execute('SELECT * FROM person WHERE date_of_birth > date("1980-01-01") OR gender = "Male"')
rows = cur.fetchall()
for row in rows:
    print(row)










