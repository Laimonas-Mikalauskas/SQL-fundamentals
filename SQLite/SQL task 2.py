import sqlite3

conn = sqlite3.connect("books.db")
c = conn.cursor()

with sqlite3.connect("books.db") as conn:
    c = conn.cursor()
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
              ("Lord Of The Rings: The Fellowship Of The Ring", "Fantasy", 1954, "J.R.R. Tolkien"))
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
              ("Lord Of The Rings: The Two Towers", "Fantasy", 1954, "J.R.R. Tolkien"))
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
              ("Lord Of The Rings: The Return Of The King", "Fantasy", 1955, "J.R.R. Tolkien"))

c.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
          ("Hobit", "Fantasy", 1937, "J.R.R. Tolkien"))
c.execute("INSERT INTO books VALUES (?, ?, ?, ?)",
          ("The Silmarillion", "Fantasy", 1977, "J.R.R. Tolkien"))

conn.commit()
conn.close()