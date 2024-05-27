import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="mydatabase"
    )

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE emp (id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(25), qualification VARCHAR(25), post VARCHAR(25), salary INT(25))")

print("Table created..!")

#Program 10 INSERT

# sql_query = "INSERT INTO employee (name, qualification, post, salary) VALUES (%s, %s, %s, %s)"
# values = ("Tisha", "Mtech", "Software Engineer", 80000)
# mycursor.execute(sql_query, values)
# mydb.commit()

# #Program 10 UPDATE

# sql = "UPDATE employee SET qualification=%s, post=%s, salary=%s WHERE name=%s"
# values = ("Mtech", "Software Engineer", 85000, "Tisha")
# mycursor.execute(sql, values)
# mydb.commit()
# print(f"{mycursor.rowcount} row(s) affected")


mydb.close()

