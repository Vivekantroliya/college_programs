# 9.Write a program to do student operations using menu as follows
#   a) Add Student
#   b) Search Student
#   c) List All Students
#   d) Update Student
#   e) Delete Student
#   f) Exit

import csv

def addStudent(Roll_No, Student_Name, City):
    with open('student.csv','r+',newline='') as std:
        if std.readline() == "Roll_No,Student_Name,City\n":
            pass
        else:
            std.write("Roll_No,Student_Name,City\n")
    with open('student.csv','a',newline='') as std:
        csv_writer = csv.writer(std,delimiter=",")
        csv_writer.writerow([Roll_No,Student_Name,City])

def searchStudent():
    Search_Student_Name = input("Enter Name Of Which Student's Details You Want:")
    with open('student.csv','r',newline='') as search:
        csv_read = csv.reader(search)
        for row in csv_read:
            if row[1] == Search_Student_Name :
                print(row)

def listAllStudent():
    with open('student.csv','r',newline='') as list_all:
        list_student = csv.reader(list_all)
        for row in list_student:
            Roll_No,Student_Name,City = row
            print(Roll_No,Student_Name,City)

def updateStudent():
    with open('student.csv','r',newline='') as student:
        student = csv.reader(student)
        lst = []
        Roll = input("Enter Roll Number Of Student For Update City:")
        found = False
        for row in student:
            if row[0] == Roll:
                found = True
                City = input("Enter New City :")
                row[2]=City
            lst.append(row)
    
    if found == False:
        print("Student Record Not Found.")
    else:
        with open('student.csv','w+',newline='') as update:
            update1 = csv.writer(update,delimiter=",")
            update1.writerows(lst)
            update.seek(0)
            read1 = csv.reader(update)
            for row in read1:
                Roll_No,Student_Name,City = row
                print(Roll_No,Student_Name,City)

def deleteStudent():
    with open('student.csv','r',newline='') as student:
        student = csv.reader(student)
        lst = []
        Roll = input("Enter Roll Number Of Student For Delete Record :")
        found = False
        for row in student:
            if row[0] == Roll:
                found = True
            else:
                lst.append(row)
    
    if found == False:
        print("Student Record Not Found.")
    else:
        with open('student.csv','w+',newline='') as update:
            update1 = csv.writer(update,delimiter=",")
            update1.writerows(lst)
            update.seek(0)
            read1 = csv.reader(update)
            for row in read1:
                Roll_No,Student_Name,City = row
                print(Roll_No,Student_Name,City)

while True:
    print("---------------------------------------------------------")
    print("Press 1 For Add Student Record")
    print("Press 2 For Search Student Record")
    print("Press 3 For Display All Records")
    print("Press 4 For Update Student Record")
    print("Press 5 For Delete Student Record")
    print("Press 6 For Exit")
    choice=input("Enter Your Choice :")
    print("---------------------------------------------------------")

    if choice == "1":
        Num = int(input("Enter How Many Record You Want To Enter :"))
        for i in range(Num):
            Roll_No = int(input("Enter Roll Number :"))
            Student_Name = input("Enter Student Name :")
            City = input("Enter Student's City :")
            addStudent(Roll_No,Student_Name,City)
    elif choice == "2":
        searchStudent()
    elif choice == "3":
        listAllStudent()
    elif choice == "4":
        updateStudent()
    elif choice == "5":
        deleteStudent()
    elif choice == "6":
        break
    else:
        print("Entered Choice Is Invalid.")