import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute('ALTER TABLE employees ADD COLUMN last_name')
cursor.execute('ALTER TABLE employees RENAME COLUMN name TO first_name')
cursor.execute('ALTER TABLE employees RENAME TO super_employees')

cursor.execute("INSERT INTO super_employees (first_name, last_name) VALUES (?, ?)", ('Darius', 'Das'))

conn.commit()

cursor.execute('SELECT first_name, last_name FROM super_employees')

for row in cursor.fetchall():
    print(row)

