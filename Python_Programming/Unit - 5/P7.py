# 7.Write a program to display only those records who have valid
# email address as their information. Use regular expression here.

import mysql.connector as sql
import re

mydb = sql.connect(host='localhost',user='root',password='',db='new_db')

mycur = mydb.cursor()

select_query = "SELECT * FROM student"

mycur.execute(select_query)

for row in mycur:
    email = row[4]
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        print(row)

mydb.close()
