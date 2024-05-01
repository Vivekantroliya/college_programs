# 4.Write a program to make use of inner class.

class outer:
    def __init__(self):
        self.inn = self.inner(10,"Vivek")
        print("This is outer class constructor.")
    def display(self):
        self.inn.display()
        print("This is outer class display method.")
        print("Id :",self.inn.id,"\nName :",self.inn.name)

    class inner:
        def __init__(self,id,name):
            print("This is inner class constructor.")
            self.id = id
            self.name  = name
        def display(self):
            print("This is inner class display method.")
            print("Id :",self.id,"\nName :",self.name)

out = outer()
out.display()
