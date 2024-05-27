#4) Write a program to insert the details of student in above table

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

insert_stmt = "INSERT INTO stud_table (rollno,name,gender,age,email,mobile,city) VALUES (%s, %s, %s, %s, %s, %s, %s)"

cur.execute(insert_stmt, (rollno,name,gender,age,email,mobile,city))

conn.commit()

print("Student details inserted successfully.")

conn.close()