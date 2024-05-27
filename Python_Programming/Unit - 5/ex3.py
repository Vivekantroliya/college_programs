'''3) Write a program to search for particular student and display the details of student. If student is not found, related message shall be displayed'''

import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='student')

cur = conn.cursor()

roll_no = input("Enter the student roll number: ")
cur.execute('SELECT * FROM stud_table WHERE rollno = %s', (roll_no,))

record = cur.fetchone()

if record is not None:
    print(record)
else:
    print("Student not found.")

conn.close()