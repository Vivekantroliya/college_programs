# 5. Write a program to prompt users to enter their working hours 
# and rate per hour to calculate gross pay. The program should 
# give the employee 1.5 times the hours worked above 30 hours. If 
# Enter Hours is 50 and Enter Rate is 10, then the calculated 
# payment is Pay: 600.0.

WorkHour = float(input("Enter Total Working Hour Of Employee : "))
Wages = float(input("Enter Per Hour Wage Of Employee : "))

if WorkHour<=30 :
    print("Total Salary Of Employee Is ",WorkHour*Wages,".")
else :
    print("Total Salary Of Employee Is ",(30*Wages)+((WorkHour-30)*1.5*Wages),".")
