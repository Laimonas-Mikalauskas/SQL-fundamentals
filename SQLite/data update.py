import sqlite3

# Atnaujinamas studento klasės lygis
with sqlite3.connect("pavyzdys.db") as conn:
    c = conn.cursor()
    c.execute("UPDATE studentai SET klase = 11 WHERE vardas = 'Jonas'")

# Patikriname atnaujinimą
with sqlite3.connect("pavyzdys.db") as conn:
    c = conn.cursor()
    for row in c.execute("SELECT * FROM studentai"):
        print(row)