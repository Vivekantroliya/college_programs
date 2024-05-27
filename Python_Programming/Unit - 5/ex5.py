#5) Write a program to update the details of student in above table

import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='student')
cur = conn.cursor()

rollno=int(input("Enter Rool numbder:"))
name = input("Enter the student name: ")
gender=input("Enter Gender:")
age = int(input("Enter the student age: "))
email=input("Enter Email :")
mobile=input("Enter Mobile number :")
city=input("Enter city :")

update_stmt = "UPDATE stud_table SET name=%s,gender=%s,age=%s,email=%s,mobile=%s,city=%s WHERE rollno=%s"

cur.execute(update_stmt, (name,gender,age,email,mobile,city,rollno))

conn.commit()

print("Student details updated successfully.")

conn.close()