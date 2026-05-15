import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE departments (
    id INTEGER PRIMARY KEY,
    name TEXT
)
""")

cursor.execute("""
CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    name TEXT,
    employee_id INTEGER,
    FOREIGN KEY (employee_id) REFERENCES departments(id) 
)
""")

cursor.execute('INSERT INTO departments (name) VALUES (?)', ('IT skyrius', ))
cursor.execute('INSERT INTO employees (name, department_id) VALUES (?, ?)', ('Jonas', 1))
cursor.execute('INSERT INTO employees (name, department_id) VALUES (?, ?)', ('Ona', 1))
cursor.execute('INSERT INTO employees (name, department_id) VALUES (?, ?)', ('Petras', 1))
conn.commit()
