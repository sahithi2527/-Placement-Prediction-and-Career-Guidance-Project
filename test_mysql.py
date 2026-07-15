import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Root@123",
    database="placement_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

conn.close()