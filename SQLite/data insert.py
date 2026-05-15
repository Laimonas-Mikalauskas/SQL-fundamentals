import sqlite3

# Įterpiamas naujas studentas
with sqlite3.connect("pavyzdys.db") as conn:
    c = conn.cursor()
    c.execute("INSERT INTO studentai (vardas, pavarde, klase) VALUES (?, ?, ?)",
              ("Jonas", "Jonaitis", 10))