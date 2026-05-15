import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT
)""")

cursor.execute("""
CREATE TABLE courses (
    id INTEGER PRIMARY KEY,
    title TEXT
)""")

cursor.execute("""
CREATE TABLE student_courses (
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
)
""")

cursor.execute('INSERT INTO students (name) VALUES (?)', ('Jonas', ))
cursor.execute('INSERT INTO courses (title) VALUES (?)', ('Matematika', ))
cursor.execute('INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)', (1, 1))

conn.commit()

cursor.execute("""
SELECT students.name, courses.title
FROM student_courses
JOIN students ON student_courses.student_id = students.id
JOIN courses ON student_courses.course_id = courses.id
""")

for row in cursor.fetchall():
    print(row)
