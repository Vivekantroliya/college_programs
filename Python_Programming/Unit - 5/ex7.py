'''7) Write a program to display only those records who have valid email 
address as their information. Use regular expression here.'''

import pymysql
import re

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='student')
cur = conn.cursor()

select_stmt = "SELECT * FROM stud_table"

cur.execute(select_stmt)

for row in cur:
    email = row[4]
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if re.match(pattern, email):
        print(row)

conn.close()