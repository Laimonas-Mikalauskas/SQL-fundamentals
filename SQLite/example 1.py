import sqlite3


conn = sqlite3.connect('abc123.db')
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS person (
    first_name TEXT,
    last_name TEXT,
    email TEXT,
    gender TEXT,
    date_of_birth DATE,
    company TEXT
)
""")

cur.executemany(
    'INSERT INTO person VALUES (?, ?, ?, ?, ?, ?)',
    [
        ('Jonas', 'Jonaitis', 'jonas@example.com', 'Male', '1985-03-15', 'PyCharm'),
        ('Ona', 'Onute', 'ona@example.com', 'Female', '1991-07-22', 'Amazon'),
        ('Petras', 'Petraitis', 'petras@example.com', 'Male', '1973-02-02', 'IMB'),
        ('Maryte', 'Morkaite', 'maryte@example.com', 'Female', '1995-11-29', 'PyCharm'),
    ]
)

cur.execute('SELECT * FROM person')
rows = cur.fetchall()
for row in rows:
    print(row)

print('-' * 90)

cur.execute('SELECT first_name, gender FROM person')
rows = cur.fetchall()
for row in rows:
    print(row)

print('-' * 90)

cur.execute('SELECT DISTINCT gender FROM person')
rows = cur.fetchall()
for row in rows:
    print(row)
