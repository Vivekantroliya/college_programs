# 3.Write a program to search for particular student and
# display the details of student. If student is not found,
# related message shall be displayed.

import mysql.connector as sql

mydb = sql.connect(host='localhost',user='root',password='',db='new_db')

mycur = mydb.cursor()

rollno = input("Enter Student Roll Number :")

mycur.execute('SELECT * FROM student WHERE rollno = %s', (rollno,))

record = mycur.fetchone()

if record is not None:
    print(record)
else:
    print("Student Not Found.")

mydb.close()
