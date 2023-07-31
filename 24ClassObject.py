class Computer:
    # Attributes - Variables - data
    # Behavior - action - Methods(aka functions)
    def configuration(self):
        print("note pro laptop")


obj1 = Computer()
print(type(obj1)) # -- gives <class '__main__.Computer'> here two : one module name - main.Computer and type class
# module belongs to class type and this obj belongs to computer of class
a = '5'
print(type(a)) # gives -- <class 'str'>
# str is in built class Computer is user defined class
b = 5;
print(type(b))
# int also a class --> b is a object of class int here
# everything in python is a object
# if functions written in a class we cannot call them directly

# to call functions in a class we have to use the class it belongs to
Computer.configuration(obj1)
# a class can have multiple objects
# function of a class operates different for every objects -- changes behavior based on objects using
obj2 = Computer()
# now when i called function config() which object it belongs to?
# we have to give which object we calling in function param place
Computer.configuration(obj2)

# therefore self is the object we are passing in function during calling using its class
# object is created using its Class name
# functions called using its class name
# objects passed in the functions param place

#  another way to call functions :
# using objects
obj1.configuration()
obj2.configuration()
# here no need to pass object as param -- becasuse obj1 and configuration() both belong to same class\
# and in background function takes the object as its self which is calling it
# example
a = 5 # a is an object of in built class int and it will have some functions in it
a.bit_length() # by def this function takes self as param but when called with object of its clss it accepts that obj as self
