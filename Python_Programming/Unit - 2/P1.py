# 1.Write a program to display basic exception handling in python.

a = 10
b = 0
try:
    c = a/b
    print(c)
except ZeroDivisionError as e:
    print(e)