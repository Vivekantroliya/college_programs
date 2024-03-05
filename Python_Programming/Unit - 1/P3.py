# 3.write a program to enter marks of 4 subjects and display result(result shall include total,percentage and grade).

Android = float(input("Enter Android Subject Marks : "))
Python = float(input("Enter Python Subject Marks : "))
DAV = float(input("Enter DAV Subject Marks : "))
CN = float(input("Enter Computer Network Subject Marks : "))

Total = Android+Python+DAV+CN

Percentage = Total/4

if Percentage>60 and Percentage<69.99 :
    Grade = "D"

elif Percentage>70 and Percentage<79.99 :
    Grade = "C"

elif Percentage>80 and Percentage<89.99 :
    Grade = "B"

elif Percentage>90 and Percentage<100 :
    Grade = "A"

else :
    Grade = "E"

print("Android Subject Marks :",Android)
print("Python Subject Marks :",Python)
print("DAV Subject Marks :",DAV)
print("Computer Network Subject Marks :",CN)
print("Total Marks : ",Total)
print("Pecentage : ",Percentage,"%")
print("Grade : ",Grade)

