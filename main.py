import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    email TEXT UNIQUE,
    name TEXT NOT NULL,
    age INTEGER CHECK (age >= 18),
    city TEXT DEFAULT 'Vilnius'
)
""")

cursor.execute('INSERT INTO users (email, name, age, city) VALUES (?, ?, ?, ?)', ('jonas@example.com', 'Jonas', 20, 'Kaunas'))
cursor.execute('INSERT INTO users (email, name, age) VALUES (?, ?, ?)', ('jonas@example.com', 'Jonas', 55))
conn.commit()

cursor.execute('SELECT * FROM users')

for row in cursor.fetchall():
    print(row)

