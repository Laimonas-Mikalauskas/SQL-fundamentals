import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()

query = """CREATE TABLE IF NOT EXISTS user(
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);
"""

with conn:
    c.execute(query)

with conn:
    c.execute("INSERT INTO user VALUES(NULL, 'adomas', '123456', 'adas@gmail.com');")
    c.execute("INSERT INTO user(username, password, email) VALUES('tomas', 'asdfgh', 'tomas@gmail.com');")
    c.execute("INSERT INTO user(username, password, email) VALUES('romas', '987654', 'romas@gmail.com');")