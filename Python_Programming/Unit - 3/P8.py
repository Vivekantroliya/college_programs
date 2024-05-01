# 8.Write a program to create abstract class with one method.

from abc import ABC,abstractmethod

class abstract_demo(ABC):
    @abstractmethod
    def one_m(self):
        pass
    def two_m(self):
        print("Implemented Method")
class child_demo(abstract_demo):
    def one_m(self):
        print("Overridden one_m() method")

a1 = child_demo()
a1.one_m()
a1.two_m()
