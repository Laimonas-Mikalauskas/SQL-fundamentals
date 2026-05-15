import sqlite3

# Nuskaitomi visi studentai
with sqlite3.connect("pavyzdys.db") as conn:
    c = conn.cursor()
    for row in c.execute("SELECT * FROM studentai"):
        print(row)