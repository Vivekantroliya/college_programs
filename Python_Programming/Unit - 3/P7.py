# 7.Use appropriate functions for each class.
# Write a program to display MRO using multiple inheritance.
# Multiple inheritance can be done as per your choice.

class Demo_A:
    def __init__(self,a):
        self.a = a
    def display(self):
        print("A = ",self.a)
        
class Demo_B:
    def __init__(self,b):
        self.b = b
    def display(self):
        print("B = ",self.b)
        
class Demo_C(Demo_A,Demo_B):
    def __init__(self,c):
        self.c = c
    def display(self):
        print("C = ",self.c)

print(Demo_C.__mro__)
c = Demo_C(10)
c.display()
