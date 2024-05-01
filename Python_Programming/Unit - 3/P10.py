# 10.Write a program to overload addition (+) and subtraction (-)
# (Use appropriate methods to overload the same).

class vector:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
    def __add__(self,other):
        return vector(self.x+other.x,self.y+other.y)
    def __sub__(self,other):
        return vector(self.x-other.x,self.y-other.y)
    def __str__(self):
        return "({0},{1})".format(self.x,self.y)

v1 = vector(10,12)
v2 = vector(5,6)

print(v1+v2)
print(v1-v2)
