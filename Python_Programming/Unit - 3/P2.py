# 2.Write a program to create a class for student with RollNo, Name, Age, Gender
# and methods named AddStudent() and DisplayStudent().

class Student():
    
    lst = []
    
    def __init__(self):
        Student.lst.append(self)
        
    def addStudent(self):
        self.RollNo = int(input("Enter Roll No :"))
        self.Name = input("Enter Name :")
        self.Age = int(input("Enter Age :"))
        self.Gender = input("Enter Gender :")
        print("Student Added.")
        
    def displayStudent(self):
        print(f"Student Displayed. \nRoll No : {self.RollNo} \nName : {self.Name} \nAge : {self.Age} \nGender : {self.Gender}")

    def add(obj):
        obj = Student()
        obj.addStudent()

    def display():
        for i in Student.lst:
            i.displayStudent()

while True:
    print("--------------------------------------------------------------------")
    print("Press 1 For Add Student")
    print("Press 2 For Display Student")
    print("Press 3 For Exit")
    choice = int(input("Enter Your Choice :"))
    print("--------------------------------------------------------------------")

    if choice == 1:
        time = int(input("Enter How Many Record You Want To Enter :"))
        for obj in range(time):
            Student.add(obj)

    elif choice == 2:
        Student.display()

    elif choice == 3:
        break

    else:
        print("Invalid Choice...")
