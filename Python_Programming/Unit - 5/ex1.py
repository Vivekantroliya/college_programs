# 1.Write a program to display all the records of student table
# (make use of fetchone() method)

import pymysql

conn = pymysql.connect(host='localhost',
                       user='root',
                       password='',
                       db='student')

cur = conn.cursor()

cur.execute('SELECT * FROM stud_table')
while True:
    record = cur.fetchone()
    if record is None:
        break
    print(f"{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}")

conn.close()
