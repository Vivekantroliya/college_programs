# 4.Create a module with 4 functions of your choice.
# Import and use thefunctions using module in different ways.

from P4_Module import *

a = int(input("Enter First Numeber :"))
b = int(input("Enter Second Numeber :"))
ope = input("Enter A Arithmetic Operator Out Of + - * / :")

if ope == "+":
    c = sum(a,b)
elif ope == "-":
    c = subtract(a,b)
elif ope == "*":
    c = multiply(a,b)
elif ope == "/":
    c = divide(a,b)
else:
    print("Invalid Operator Entered...")

print("Answer Is",c)