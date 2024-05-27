#6) Write a program to delete the details of student in above table

import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='student')

cur = conn.cursor()
rollno= input("Enter the Roll number: ")

delete_stmt = "DELETE FROM stud_table WHERE rollno=%s"

cur.execute(delete_stmt, (rollno,))

conn.commit()

print("Student details deleted successfully.")

conn.close()