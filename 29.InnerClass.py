# sometime when a class is used for particcular class we can create an inner class for it

# inner objects can be created either inside its outer class or outside outerclass
# if created in inner class it can be created in init() with refering to obj it is being called.. that is
# that is... self.obj (here obj is objectof innerclass) = self.Constructor(constructor is constructor of inner class)
# to call it we use self/obj of outercalss.objectofinnercalls.variables or methods
# we can also create objects for inner class using outer class objects outside thae class

# if obj of inner class created outised outer class then its created this way:
# objofinnerclass = outerClass.innerClassConstructor()
class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.l1 = self.Laptop('azure', 'single')  # object of inner class Laptop

    def show(self):
        return (self.name, self.roll,self.l1.brand,self.l1.core)

    class Laptop:

        def __init__(self, brand, core):
            self.brand = brand
            self.core = core

        def show(self):
            return (self.brand, self.core)


s1 = Student('mkn', 5)
s2 = Student('nmk', 6)
print(s1, s2)
print(s1.name, s1.roll, s2.name, s2.roll, sep="      ")

s1.l1.brand = 'mi'
s2.l1.core = 'dual'

print(s1.l1.brand)
print(s2.l1.core)

print(s2.show())

lap1 = Student.Laptop('videocon','octa') # object of Laptop class using Student class
lap2 = s1.Laptop('samsung','dualocta') # object of Laptop class using object of Student class

print(lap1.brand,lap1.core,lap1.show())
