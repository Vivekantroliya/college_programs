# 9.Write a program to create interface and utilize the same in other class.

from abc import ABC,abstractmethod

class interface(ABC):
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def show(self):
        pass

class child_class(interface):
    def display(self):
        print("This is child_class display method.")
    def show(self):
        print("This is child_class show method.")

c = child_class()
c.display()
c.show()
