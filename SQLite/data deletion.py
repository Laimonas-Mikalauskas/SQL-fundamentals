import sqlite3

# Ištrinamas studentas pagal vardą
with sqlite3.connect("pavyzdys.db") as conn:
    c = conn.cursor()
    c.execute("DELETE FROM studentai WHERE vardas = 'Jonas'")

# Patikriname trynimą
with sqlite3.connect("pavyzdys.db") as conn:
    c = conn.cursor()
    for row in c.execute("SELECT * FROM studentai"):
        print(row)