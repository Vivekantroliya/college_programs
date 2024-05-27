# 8.Write a program to enter course and no. of students in each course. 
# Display information using pie graph. The course with maximum students 
# shall be displayed separately as a separate slice of pie graph.

import matplotlib.pyplot as plt
import numpy as np

Course=[]
Student=[]
for i in range(5):
    x=input("Enter the Course :")
    y=int(input("Enter No of Student :"))
    Course.append(x)
    Student.append(y)

print(Course)
print(Student)

ex = []
maximum = max(Student)
for i in Student:
    if i == max(Student):
        ex.append(0.1)
    else:
        ex.append(0)
plt.pie(Student, labels=Course,explode=ex,autopct="%1.1f%%")
plt.show()
