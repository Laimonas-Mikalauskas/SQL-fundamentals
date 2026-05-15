import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
)
""")



cursor.executemany(
    f"INSERT INTO users (username, password) VALUES (?, ?)",
    [
        ('admin', 'admin'),
        ('admin2', 'admin2')
    ]
)

conn.commit()

cursor.execute('SELECT * FROM users;')
res = cursor.fetchall()

print(res)

username = input('username: ')
password = input('password: ')

cursor.execute(f"INSERT INTO users (username, password) VALUES (?, ?)", (username, password))

cursor.execute('SELECT * FROM users;')
res = cursor.fetchall()

print(res)
