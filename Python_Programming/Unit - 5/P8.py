# 8.Write a program to load all the records from table and display only those 
# details where names start with “N” and has length of 5 characters.''' 

import mysql.connector as sql

mydb = sql.connect(host='localhost',user='root',password='',db='new_db')

mycur = mydb.cursor()
    
select_query = " SELECT * FROM student WHERE name LIKE 'V____' "

mycur.execute(select_query)

records = mycur.fetchall()

for record in records:
    print(record)
    
mydb.close()
