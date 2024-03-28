# 3.Write a program to generate arithmetic exception and log the exception in system.

try:
    a = 10
    b = 0
    c = a/b
except ArithmeticError as e:
    print("You Have Just Got An ArrithmeticError.")   