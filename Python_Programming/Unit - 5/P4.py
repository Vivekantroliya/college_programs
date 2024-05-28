# 4.Write a program to insert the details of student in above table.

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

insert_query = "INSERT INTO student (rollno,name,gender,age,email,mobile,city) VALUES (%s, %s, %s, %s, %s, %s, %s)"

mycur.execute(insert_query, (rollno,name,gender,age,email,mobile,city))

mydb.commit()

print("Student's Detail Inserted Successfully.")

mydb.close()
