# two types - Instance and Class(Static)
class Car:
    wheels = 4
    def __init__(self,a):
        self.mil = a
        self.company = 'bmw' # instance values
        # instances because - as object changes - thse values changes

c1 = Car(45)
c2 = Car(10)
c3 = Car(60)
c3.mil = 55
print(c1.mil,c1.wheels) # calling with object
print(c2.mil, Car.wheels) # calling with class because it belongs to class
print(c3.mil,c3.wheels)
c2.mil = 38
# instance variables are different for different objects and can be changed differently without effecting other
# varibales defined outside init and inside class are - class/static variables
# namespace - area you create and store object/variable
# two types of namespace
# class namespace - class variables
# instance namespace - instance variaBLES
# if you change class variable - it changes for all objects
# to change class varibale
Car.wheels = 5 # because its a class variable
