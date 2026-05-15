import sqlite3

conn = sqlite3.connect(':memory:')
c = conn.cursor()

inp_username = input("Enter username: ")
inp_password = input("Enter password: ")

with conn:
    c.execute("SELECT * FROM user WHERE user.username=? AND user.password=?;", (inp_username, inp_password))
    res = c.fetchall()
    if res:
        print("Jūsų profilio duomenys yra:")
        print(res)
    else:
        print(f"Vartotojas {inp_username} neegzistuoja arba neteisingas slaptažodis")