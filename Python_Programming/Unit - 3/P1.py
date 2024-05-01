# 1.Write a program to create a simple class with 2 methods and execute both methods.

class simple:
    def assign(self):
        self.id = 1
        self.name = 'Vivek'
        print("Values Assigned.")
    def display(self):
        print("Values Displayed.")
        print(f"Id is {self.id}. \nName is {self.name}.")
        

s1 = simple()
s1.assign()
s1.display()
