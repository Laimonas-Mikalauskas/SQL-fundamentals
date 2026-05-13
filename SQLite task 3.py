import sqlite3

conn = sqlite3.connect("employees.db")
c = conn.cursor()

# Drop the employees table if it exists
c.execute('DROP TABLE IF EXISTS employees')

# Create the employees table with the correct schema
c.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        name TEXT,
        surname TEXT,
        role TEXT,
        salary INTEGER,
        experience TEXT
    )
''')

# Add a row with integer salary
c.execute('''
    INSERT INTO employees (name, surname, role, salary, experience)
    VALUES (?, ?, ?, ?, ?)
''', ('Tom', 'Gordon', 'Python developer', '2000', '2 years'))

conn.commit()
conn.close()