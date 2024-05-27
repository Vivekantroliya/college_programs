'''Write a program to load all the records from table and display only those 
details where names start with “N” and has length of 5 characters.''' 
import pymysql

conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='student'
    )
cursor = conn.cursor()
    
query = "SELECT * FROM stud_table WHERE name LIKE 'a__' AND LENGTH(name) = 5"
cursor.execute(query)

records = cursor.fetchall()
for record in records:
    print(record)
    
conn.close()
