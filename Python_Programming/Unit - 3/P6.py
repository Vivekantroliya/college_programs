# 6.Write a Python Program that creates a class and inherit into another class.
# (Base Class : Student with rollno, name, gender, age)
# (Derived Class : Course with coursename, duration, fee)

class student:
    def setdata(self,roll_no,name,age,gender):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender
    def display(self):
        print("Roll No : ",self.roll_no)
        print("Name : ",self.name)
        print("Gender : ",self.gender)
        print("Age : ",self.age)

class course(student):
    def __init__(self,course_name,duration,fee):
        self.course_name = course_name
        self.duration = duration
        self.fee = fee
    def display_course(self):
        print("Course Name : ",self.course_name)
        print("Duration : ",self.duration)
        print("Fee : ",self.fee)

c = course("MCA","2 Years",200000)
c.setdata(4028,"Vivek",22,"Male")
c.display()
c.display_course()
