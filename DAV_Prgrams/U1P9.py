# 9. Write a program to prompt users to enter a year;
# then find whether it’s a leap year.
# A year is considered a leap year if it’s 
# divisible by 4 and 100 and 400. If it’s divisible 
# by 4 and 100 but not by 400, it’s not a leap year. 
# Display a proper message.

year = int(input("Enter A Year :"))

if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"Is A Leap Year.")
else:
    print(year,"Is Not A Leap Year.")
