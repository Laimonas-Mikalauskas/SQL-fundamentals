import sqlite3

# Įterpiamas mokytojas su saugia parametrizuota užklausa
with sqlite3.connect("pavyzdys.db") as conn:
    c = conn.cursor()
    c.execute("INSERT INTO mokytojai (vardas, pavarde, dalykas) VALUES (?, ?, ?)",
              ("Tomas", "Tomaitis", "Matematika"))