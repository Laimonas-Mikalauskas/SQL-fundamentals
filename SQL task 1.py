import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

with sqlite3.connect("books.db") as conn:
    c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS books (
                title TEXT,
                genre TEXT,
                release_year INTEGER,
                author TEXT)''')

conn.commit()
conn.close()

