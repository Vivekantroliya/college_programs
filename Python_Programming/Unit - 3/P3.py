# 3.Write a program to make use of class method and instance method.

class UseMethod:
    name = "Vivek"

    @classmethod
    def class_method(cls):
        print(cls.name)

    #instancemethod
    def instance_method(self):
        self.name = "Om"
        print(self.name)

u1 = UseMethod()
UseMethod.class_method()
u1.instance_method()
