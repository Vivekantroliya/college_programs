# 1.write a program to input p,r,n and find out interest using simple input output statement.

p = int(input("Enter The Principle Amount : "))
r = float(input("Enter The Rate Of Interest : "))
n = float(input("Enter Number Of Years : "))

Interest = p*r*n/100

print("Total Interest Is ",Interest," Rs.")
