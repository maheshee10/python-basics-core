# over loading -- using same method by providing different params in num or type - in java
# in python two types of overload can be acheved - one operator and two method
# method overloading however is not allowed in python but can be achieved by another means
# by default when a operator is used in backgroud it calls a magic function in python
# example + calls -- __add__() function
a = 6
b = 7
print(a+b)
print(int.__add__(a,b))

# above two statements are same + operator calls __add__() magic function of int class and applies on a and b objects
# so we can use method overloading in this way by overloading magic functions whic are in built for operators
# we can overload operators but cannot create new operators
class A:
    def __init__(self,a):
        self.a = a
    def __add__(self, other):
        r = a1.a + other.a
        return r
    def __str__(self):
        return '{}'.format(self.a)



a1 = A(5)
a2 = A(4)
sum = a1+a2 # + operator is calling this way here : A.__add__(a1,a2)
print(sum)

print(a1) # a1 is object calling __str__ maguic function ib background 