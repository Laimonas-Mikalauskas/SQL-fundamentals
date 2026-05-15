import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

with sqlite3.connect("books.db") as conn:
    c = conn.cursor()
    # c.execute("INSERT INTO Books VALUES (?, ?, ?, ?)",
    #           ("Lord Of The Rings: The Fellowship Of The Ring", "Fantasy", 1954, "J.R.R. Tolkien"))
    for row in c.execute("SELECT * FROM books"):
        print(row)

conn.commit()
conn.close()