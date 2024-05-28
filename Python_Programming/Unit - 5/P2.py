# 2.Write a program to display all the records of student table.
# (make use of fetchall() method)

import mysql.connector as sql

mydb = sql.connect(host='localhost',user='root',password='',db='new_db')

mycur = mydb.cursor()

mycur.execute('SELECT * FROM student')

records = mycur.fetchall()

for record in records:
    print(f"{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}\t{record[4]}\t{record[5]}\t{record[6]}")

mydb.close()
