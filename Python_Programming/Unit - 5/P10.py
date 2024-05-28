# 10.Write a menu based program to perform following information.
# - Insert Student
# - Update Student
# - Search Student
# - Delete Student
# - List Students
# - Exit

import mysql.connector as sql

def connect_to_db():
    mydb = sql.connect(host='localhost',user='root',password='',db='new_db')
    return mydb

def create_table():
    mydb = connect_to_db()
    mycur = mydb.cursor()
    mycur.execute("CREATE TABLE IF NOT EXISTS student(rollno INT,name VARCHAR(30),gender VARCHAR(30),age INT,email VARCHAR(30),mobile INT,city VARCHAR(30))")
    mydb.commit()
    mydb.close()

def insert_student(rollno,name,gender,age,email,mobile,city):
    mydb = connect_to_db()
    mycur = mydb.cursor()
    insert_query = "INSERT INTO student (rollno,name,gender,age,email,mobile,city) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    mycur.execute(insert_query, (rollno,name,gender,age,email,mobile,city))
    mydb.commit()
    print("Student Added Successfully.")
    mydb.close()


def update_student(rollno,name,gender,age,email,mobile,city):
    mydb = connect_to_db()
    mycur = mydb.cursor()
    mycur.execute("SELECT * FROM student WHERE rollno=%s", (rollno,))
    student = mycur.fetchone()
    if student:
        update_query = "UPDATE student SET name=%s,gender=%s,age=%s,email=%s,mobile=%s,city=%s WHERE rollno=%s"
        mycur.execute(update_query, (name,gender,age,email,mobile,city,rollno))
        mydb.commit()
        print("Student Updated Successfully.")
    else:
        print("Student Not Found.")
    mydb.close()
    

def search_student(rollno):
    mydb = connect_to_db()
    mycur = mydb.cursor()
    mycur.execute('SELECT * FROM student WHERE rollno = %s', (rollno,))
    result = mycur.fetchone()
    mydb.close()
    return result


def delete_student(rollno):
    mydb = connect_to_db()
    mycur = mydb.cursor()
    mycur.execute("SELECT * FROM student WHERE rollno=%s", (rollno,))
    student = mycur.fetchone()
    if student:
        delete_query = "DELETE FROM student WHERE rollno=%s"
        mycur.execute(delete_query, (rollno,))
        mydb.commit()
        print("Student Deleted Successfully.")
    else:
        print("Student Not Found.")
    mydb.close()


def list_students():
    mydb = connect_to_db()
    mycur = mydb.cursor()
    mycur.execute('SELECT * FROM student')
    results = mycur.fetchall()
    mydb.close()
    return results


def main():
    create_table()
    while True:
        print("\nStudent Management System")
        print("1. Insert Student")
        print("2. Update Student")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. List Students")
        print("6. Exit")
        option = int(input("Enter Your Choice :"))
        if option == 1:
            rollno=int(input("Enter Roll Number :"))
            name = input("Enter Student Name :")
            gender=input("Enter Gender :")
            age = int(input("Enter Age :"))
            email=input("Enter Email :")
            mobile=input("Enter Mobile Number :")
            city=input("Enter City :")
            insert_student(rollno,name,gender,age,email,mobile,city)
        elif option == 2:
            rollno=int(input("Enter Roll Number :"))
            name = input("Enter Student Name :")
            gender=input("Enter Gender :")
            age = int(input("Enter Age :"))
            email=input("Enter Email :")
            mobile=input("Enter Mobile Number :")
            city=input("Enter City :")
            update_student(rollno,name,gender,age,email,mobile,city)
        elif option == 3:
            rollno = input("Enter Roll Number :")
            result = search_student(rollno)
            if result is not None:
                print(result)
            else:
                print("Student Not Found.")
        elif option == 4:
            rollno = input("Enter Roll Number Which You Want To Delete :")
            result = delete_student(rollno)
        elif option == 5:
            results =list_students()
            for result in results:
                print(f"{result[0]}\t{result[1]}\t{result[2]}\t{result[3]}\t{result[4]}\t{result[5]}\t{result[6]}")
        elif option == 6:
            print('Exit.')
            break
        else:
            print('Invalid Choice.Please Try Again.')
main()
