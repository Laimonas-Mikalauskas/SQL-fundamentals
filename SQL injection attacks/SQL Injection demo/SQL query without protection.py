inp_username = input("Įveskite username: ")
inp_password = input("Įveskite slaptažodį: ")

query = f"SELECT * FROM user WHERE user.username='{inp_username}' AND user.password='{inp_password}';"

with conn:
    c.execute(query)
    res = c.fetchall()
    if res:
        print("Jūsų profilio duomenys yra:")
        print(res)
    else:
        print(f"Vartotojas {inp_username} neegzistuoja arba neteisingas slaptažodis")