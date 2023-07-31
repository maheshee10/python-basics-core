# technically method ol is not possible in python
from functools import reduce
class Student:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None :
            s = a+b+c
        elif a!=None and b != None :
            s = a+b
        else :
            print("add not possible with one value")
        return s
    def add(self,a,*b):
        sum = 50
        for e in b :
            sum = sum+e

        i = reduce(lambda a,b : a+b,b)

        return sum+i


S = Student(56,65,78)
result = S.sum(4,6)
result1 = S.sum(4,5,6)
result3 = S.add(50,1,2,3,4,5,6,7,8)
print(result,result1,result3)
# if we want three params to add -- cannot because mismatch in params of init and object constructor


class A:
    def show(self):
        print("in A")

class B(A):
    def show(self):
        print("B")

b = B()
b.show() # here B class  is overriding its super class method
# overriding can work only in case of inheritence

class C :
    def show(self):
        print('in C')

c = C()
c.show()