inp_username = "' OR True;--"
inp_password = ""

query = f"SELECT * FROM user WHERE user.username='{inp_username}' AND user.password='{inp_password}';"

with conn:
    print("=>>>>> ", query)
    c.execute(query)
    res = c.fetchall()
    print("Jūsų profilio duomenys yra:", res)