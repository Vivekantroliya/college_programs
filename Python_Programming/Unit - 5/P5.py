# 5.Write a program to update the details of student in above table.

import mysql.connector as sql

mydb = sql.connect(host='localhost',user='root',password='',db='new_db')

mycur = mydb.cursor()

rollno=int(input("Enter Roll Number :"))
name = input("Enter Student Name :")
gender=input("Enter Gender :")
age = int(input("Enter Age :"))
email=input("Enter Email :")
mobile=input("Enter Mobile Number :")
city=input("Enter City :")

update_query = "UPDATE student SET name=%s,gender=%s,age=%s,email=%s,mobile=%s,city=%s WHERE rollno=%s"

mycur.execute(update_query, (name,gender,age,email,mobile,city,rollno))

mydb.commit()

print("Student's Detail Updated Successfully.")

mydb.close()
