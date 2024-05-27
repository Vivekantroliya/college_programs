'''10) Write a menu based program to perform following information.
- Insert Student
- Update Student
- Search Student
- Delete Student
- List Students
- Exit'''

import pymysql

def connect_to_db():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='student'
    )
    return conn

def create_table():
    conn=connect_to_db()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS stud_table(
                                                            rollno INT AUTO_INCREMENT PRIMARY KEY,
                                                            name VARCHAR(20),
                                                            gender varchar(20),
                                                            age INT,
                                                            email varchar(20),
                                                            city varchar(20)
                                                         );
                """)
    conn.commit()
    conn.close()

def insert_student(rollno,name,gender,age,email,mobile,city):
    """Insert a new student into the database."""
    conn = connect_to_db()
    cur = conn.cursor()
    insert_stmt = "INSERT INTO stud_table (rollno,name,gender,age,email,mobile,city) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cur.execute(insert_stmt, (rollno,name,gender,age,email,mobile,city))
    conn.commit()
    conn.close()


def update_student(rollno,name,gender,age,email,mobile,city):
    """Update a student in the database."""
    conn = connect_to_db()
    cur = conn.cursor()

    # Check if the student exists in the database
    cur.execute("SELECT * FROM stud_table WHERE rollno=%s", (rollno,))
    student = cur.fetchone()

    if student:
        update_stmt = "UPDATE stud_table SET name=%s,gender=%s,age=%s,email=%s,mobile=%s,city=%s WHERE rollno=%s"
        cur.execute(update_stmt, (name,gender,age,email,mobile,city,rollno))
        conn.commit()
        print("Student updated successfully.")
    else:
        print("Student not found.")

    conn.close()
    

def search_student(rollno):
    """Search for a student in the database."""
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM stud_table WHERE rollno = %s', (rollno,))
    result = cur.fetchone()
    conn.close()
    return result


def delete_student(rollno):
    """Delete a student from the database."""
    conn = connect_to_db()
    cur = conn.cursor()

    # Check if the student exists in the database
    cur.execute("SELECT * FROM stud_table WHERE rollno=%s", (rollno,))
    student = cur.fetchone()

    if student:
        delete_stmt = "DELETE FROM stud_table WHERE rollno=%s"
        cur.execute(delete_stmt, (rollno,))
        conn.commit()
        print("Student deleted successfully.")
    else:
        print("Student not found.")

    conn.close()


def list_students():
    """List all students in the database."""
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM stud_table')
    results = cur.fetchall()
    conn.close()
    return results


def main():
    """Main function to run the menu-based program."""
    create_table()
    while True:
        print("\nStudent Management System")
        print("1. Insert Student")
        print("2. Update Student")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. List Students")
        print("6. Exit")
        option = int(input("Enter your option: "))
        if option == 1:
            rollno=int(input("Enter Roll numbder:"))
            name = input("Enter the student name: ")
            gender=input("Enter Gender:")
            age = int(input("Enter the student age: "))
            email=input("Enter Email :")
            mobile=input("Enter Mobile number :")
            city=input("Enter city :")
            insert_student(rollno,name,gender,age,email,mobile,city)
            print("Student added successfully.")
        elif option == 2:
            rollno=int(input("Enter Roll numbder to Update:"))
            name = input("Enter the student name: ")
            gender=input("Enter Gender:")
            age = int(input("Enter the student age: "))
            email=input("Enter Email :")
            mobile=input("Enter Mobile number :")
            city=input("Enter city :")
            update_student(rollno,name,gender,age,email,mobile,city)
            #print("Student updated successfully.")
        elif option == 3:
            rollno = input("Enter the student roll number: ")
            result = search_student(rollno)
            if result is not None:
                print(result)
            else:
                print("Student not found.")
        elif option == 4:
            rollno = input("Enter the student roll number which you want to delete: ")
            result = delete_student(rollno)
            #print("Student details deleted successfully.")
        elif option == 5:
            results =list_students()
            for result in results:
                print(f"{result[0]}\t{result[1]}\t{result[2]}\t{result[3]}\t{result[4]}\t{result[5]}\t{result[6]}")
        elif option == 6:
            print('Exiting program...')
            break
        else:
            print('Invalid choice. Please try again.')


main()