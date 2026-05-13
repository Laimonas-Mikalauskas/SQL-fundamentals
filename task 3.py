import sqlite3

conn = sqlite3.connect('db.db')
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE studies (
    id = INTEGER PRIMARY KEY,
    title = TEXT
)
""")

cursor.execute("""
CREATE TABLE student_courses (
    id = INTEGER PRIMARY KEY, 
    student_id = INTEGER,
    course_id = INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)

    )
""")












