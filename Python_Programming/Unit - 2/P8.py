# 8.Write a program to read file which has marks entry of student and 
# display details with total, percentage and grade (Consider a file which has 
# comma separated data with RollNo, Student Name, Mark1, Mark2, Mark3 and Mark4)

import csv

with open("studentdata.csv",newline='') as std:
    reader = list(csv.reader(std))
    for head in reader[:1]:
        for i in head:
            print(i,end = " ")
    print("Total","Percentage","Grade")        
    for row in reader[1:]:
        Roll_No,Student_Name,Mark1,Mark2,Mark3,Mark4 = row
        row[2],row[3],row[4],row[5]=int(row[2]),int(row[3]),int(row[4]),int(row[5])
        Total = row[2]+row[3]+row[4]+row[5]
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
        print(Roll_No,Student_Name,Mark1,Mark2,Mark3,Mark4,Total,Percentage,Grade)