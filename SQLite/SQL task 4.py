import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

with sqlite3.connect("books.db") as conn:
    c = conn.cursor()
    # c.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
    #           ("Traidenis", "History", 2025, "Arthur Dubonis"))
    c.execute("UPDATE books SET release_year = 2009 WHERE author = 'Arthur Dubonis'")
    for row in c.execute("SELECT * FROM books"):
        print(row)

conn.commit()
conn.close()

