#repr tells python what the string representation of the class should be, it returns a string
class Employee:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

john = Employee('John')

#print(john)

#class methods - functions that are defined as a part of the class
class Dog:
    def bark(self):
        print("dog sound")


#instantiate - before use
class Car:
    pass
ferrari = Car()

#class variables
#a class is a template for a data type(a blueprint)

#dir() returns all the attributes in the curret scope of that specific class
#print(dir(Employee))

#super() function allows a subclass to invoke its parent's version of an overridden method

class ParentClass:
    def print_test(self):
        print("parent method")

class ChildClass(ParentClass):
    def print_test(self):
        print("Child method")
        super().print_test()

child_instance = ChildClass()
child_instance.print_test()


#user defined exceptions

class CustomError(Exception):
    pass

#polymorphism is when 2 python classes offer the same set of methods with different implementation

class ParentClasspoly:
    def print_self(self):
        print('A')

class ChidlClasspoly(ParentClasspoly):
    def print_self(self):
        print('b')

obj_A = ParentClasspoly()
obj_B = ChidlClasspoly()

obj_A.print_self()
obj_B.print_self()


#dunder methods: double underscores:
#__init__, __add__, __len__, __iter__

#issubclass

print(issubclass(ChidlClasspoly,ParentClasspoly))


#inheritance  - share attributes between classes

class Animal:
    def __init__(self, name, legs):
        self.name = name
        self.legs = legs

class Dog(Animal):
    def sound(self):
        print("Wooof!!")

D1 = Dog("Happy", 4)
print(D1.name)
D1.sound()