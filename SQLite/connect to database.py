import sqlite3

# Prisijungimas prie duomenų bazės
conn = sqlite3.connect("pavyzdys.db")
c = conn.cursor()

# Lentelės sukūrimas
c.execute('''CREATE TABLE IF NOT EXISTS studentai (
                vardas TEXT,
                pavarde TEXT,
                klase INTEGER)''')

conn.commit()
conn.close()