import sqlite3


def init_db():
    conn = sqlite3.connect('mokykla.py')
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS mokiniai (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vardas TEXT,
            pavarde TEXT,
            klase TEXT,
            vidurkis FLOAT
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS mokytojai (
            vardas TEXT,
            pavarde TEXT,
            dalykas TEXT        )
    """)
    conn.commit()
    conn.close()


class Asmuo:
    def __init__(self, vardas, pavarde):
        self.vardas = vardas
        self.pavarde = pavarde


class Mokinys(Asmuo):
    def __init__(self, vardas, pavarde, klase, vidurkis):
        Asmuo.__init__(self, vardas, pavarde)
        self.klase = klase
        self.vidurkis = vidurkis


class Mokytojas(Asmuo):
    def __init__(self, vardas, pavarde, dalykas):
        Asmuo.__init__(self, vardas, pavarde)
        self.dalykas = dalykas


def log_operacija(func):
    def wrapper(*args, **kwargs):
        print('Vykdoma operacija: ', func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log_operacija
def prideti_mokini(mokinys):
    try:
        conn = sqlite3.connect('mokykla.py')
        c = conn.cursor()
        c.execute(
            'INSERT INTO mokiniai (vardas, pavarde, klase, vidurkis) VALUES (?, ?, ?, ?)',
            (mokinys.vardas, mokinys.pavarde, mokinys.klase, mokinys.vidurkis)
        )
        conn.commit()
        conn.close()
        print('Mokinys pridetas')
    except Exception as e:
        print(f'Klaida pridedant mokini: {e}')

@log_operacija
def parodyti_visus_mokinius():
    conn = sqlite3.connect('mokykla.py')
    c = conn.cursor()
    c.execute('SELECT * FROM mokiniai')
    visi = c.fetchall()
    conn.close()
    if not visi:
        print('Nera mokiniu.')
    for m in visi:
        print(m)

@log_operacija
def ieskoti_mokinio(tekstas):
    conn = sqlite3.connect('mokykla.py')
    c = conn.cursor()
    c.execute('SELECT * FROM mokiniai')
    visi = c.fetchall()
    conn.close()
    rasta = []
    for m in visi:
        if tekstas.lower() in m[1].lower() or tekstas.lower() in m[2].lower():
            rasta.append(m)
    if not rasta:
        print('Nera mokiniu.')
    for m in rasta:
        print(m)

@log_operacija
def atnaujinti_klase(mokinio_id, nauja_klase):
    conn = sqlite3.connect('mokykla.py')
    c = conn.cursor()
    c.execute('SELECT * FROM mokiniai')
    visi = c.fetchall()
    rastas = False
    for m in visi:
        if m[0] == mokinio_id:
            c.execute('UPDATE mokiniai SET klase = ? WHERE id = ?', (nauja_klase, mokinio_id))
            conn.commit()
            print('Klase atnaujinta.')
            rastas = True
            break
    if not rastas:
        print('Nera tokio mokinio.')
    conn.close()

@log_operacija
def istrinti_mokini(mokinio_id):
    conn = sqlite3.connect('mokykla.py')
    c = conn.cursor()
    c.execute('SELECT * FROM mokiniai')
    visi = c.fetchall()
    rastas = False
    for m in visi:
        if m[0] == mokinio_id:
            c.execute('DELETE FROM mokiniai WHERE id = ?', (mokinio_id, ))
            conn.commit()
            print('Mokinis pasalintas.')
            rastas = True
            break
    if not rastas:
        print('Nera tokio mokinio.')
    conn.close()


def pagrindinis_meniu():
    while True:
        print('\n=== Mokyklos sistema ===')
        print('1. Prideti mokinį')
        print('2. Rodyti visus mokinius')
        print('3. Ieskoti mokinio')
        print('4. Atnaujinti mokinio klase')
        print('5. Istrinti mokini')
        print('0. Iseiti')

        pasirinkimas = input('Pasirinkite veiksmą: ')

        try:
            if pasirinkimas == '1':
                vardas = input('Vardas: ')
                pavarde = input('Pavarde: ')
                klase = input('Klase: ')
                vidurkis = input('Vidurki: ')
                mokinys = Mokinys(vardas, pavarde, klase, vidurkis)
                prideti_mokini(mokinys)
            elif pasirinkimas == '2':
                parodyti_visus_mokinius()
            elif pasirinkimas == '3':
                tekstas = input('Vardas arba pavarde: ')
                ieskoti_mokinio(tekstas)
            elif pasirinkimas == '4':
                mok_id = int(input('Mokinio ID: '))
                nauja_klase = input('Nauja klase: ')
                atnaujinti_klase(mok_id, nauja_klase)
            elif pasirinkimas == '5':
                mok_id = int(input('Mokinio ID: '))
                istrinti_mokini(mok_id)
            elif pasirinkimas == '0':
                break
            else:
                print('Neteisingas pasirinkimas.')
        except ValueError:
            print('Neteisinga ivestis (pvz. tiketasi skaiciaus).')
        except Exception as e:
            print(f'Klaida: {e}')

init_db()
pagrindinis_meniu()
