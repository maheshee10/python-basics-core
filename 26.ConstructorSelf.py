# heap memory - objects stored -- address can be printed using -- id method
class Computer:
    def __init__(self, a):# self.age = 25 # self.name = 'mkn'
        self.x = a
    def show(self):
        print(self.x)
        return 2 * 2

    def compare(self, c2): # this not an inbuilt function # here self is the one we want to compare with c2
        if self.x == c2.x :
            return True
        else :
            return False




c1 = Computer(456)
c2 = Computer('mahesh')
# print(c1)
# print(c2)
# every time we create two different objects we create two different spaces
# sizes of objects depend upon number of variables
# constructor is responsible for allocating memory
# init() used to initialise variables - everytime we create object using class() - it calls init() function internally - which is a constructor - even if I dont specify
# init gets called in background
# computer is a class but computer() - constructor -- thse constructor decide size of object
m = c1.show()
n = c2.show()
print(m)
print(n)
# print(c1.age)
# print(c1.name)
# print(c1)
# init takes params from class constructor while initialising an object but they can be overriden in init block
# whatever we initialise as variables of particular object using self are its attributes / variables inside
# why self?
# we can call a function using its class
# say a function has multiples objects and depending on object data function behaves differently
# now when we call a function which object it has to operate on decided by using self

# to assign values of our own to object can we assign them in init method
# No because in init method it will be changed for every object that variable value
# how to give our values to object of different objects
# one way is to assign them using object.variable out side class
# or we accept params in init and assign those values as args in constructor

# comparing to objects:
if c1.compare(c2):
    print("same")
else:
    print("not same")


