# 9.Write a program to create a list with 3 columns for name,
# data type and size. Create table as per the information entered.
# Consider following example
# name varchar 20
# qualification varchar 20
# post varchar 20
# salary int 6
# Once above information is stored in list, program shall
# create a table from above information.

import mysql.connector as sql

mydb = sql.connect(host='localhost',user='root',password='',db='new_db')

mycur = mydb.cursor()

mycur.execute("CREATE TABLE employee (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(20), qualification VARCHAR(20), post VARCHAR(20), salary INT(6))")

print("Table Created.")

mydb.close()

