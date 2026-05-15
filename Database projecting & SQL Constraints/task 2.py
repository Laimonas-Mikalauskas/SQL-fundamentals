import sqlite3

conn = sqlite3.connect('const.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER CHECK(age >= 18 AND age <= 120),
    country TEXT DEFAULT 'USA'
)
""")

cursor.execute('INSERT INTO clients (full_name, email, age, country) VALUES (?, ?, ?, ?)',
               ('John Peterson', 'john@example.com', 30, None))
cursor.execute('INSERT INTO clients (full_name, email, age, country) VALUES (?, ?, ?, ?)',
               ('Olivia Wilson', 'olivia@example.com', 35, 'USA'))
cursor.execute('INSERT INTO clients (full_name, email, age, country) VALUES (?, ?, ?, ?)',
               ('Mark Anderson', 'mark@example.com', 20, 'Latvia'))


# cursor.execute('INSERT INTO clients (full_name, email, age, country) VALUES (?, ?, ?, ?)',
#                ('John Peterson', 'john@example.com', 30, None))
# cursor.execute('INSERT INTO clients (full_name, email, age, country) VALUES (?, ?, ?, ?)',
#                (None, 'olivia@example.com', 35, 'USA'))
# cursor.execute('INSERT INTO clients (full_name, email, age, country) VALUES (?, ?, ?, ?)',
#                ('Mark', 'mark@example.com', 5, 'Canada'))


    
    
    
    
    
