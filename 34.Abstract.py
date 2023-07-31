# Python directly dont support Abstract classes
# we use ABC - Abstract Base Classes module and use @abstractmethod
# abstract class must have one abstract method atleast
# abstract method - declared but not defined that means no body
# abstrct class cannot have object

from abc import ABC, abstractmethod


class A(ABC):

    def __init__(self):
        pass

    def m1(self):
        pass

    @abstractmethod
    def run(self):
        pass


# m = A() this error - because one abstract class enough to calla a class abstract and abstratc classes canot have objects

# if any class inheriting this abstarct class it must define the abstract method it inherits else it also turn abstract

class B(A):
    def run(self):
        print("running")

b = B()
b.run()
b.m1()