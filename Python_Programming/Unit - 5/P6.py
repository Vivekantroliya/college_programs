# 6.Write a program to delete the details of student in above table.

import mysql.connector as sql

mydb = sql.connect(host='localhost',user='root',password='',db='new_db')

mycur = mydb.cursor()

rollno= input("Enter Roll Number :")

delete_query = "DELETE FROM student WHERE rollno=%s"

mycur.execute(delete_query, (rollno,))

mydb.commit()

print("Student's Details Deleted Successfully.")

mydb.close()
