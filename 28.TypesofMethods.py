# types - 3 types of methods
# Instance methods - Class methods - Static Methods
# variables thrre types - Instance belong to method/init - Class and static are same - inside a class outside init

class Student:
    name = 'mkn'

    def __init__(self, sub, marks, best):
        self.sub = sub
        self.marks = marks
        self.best = 98
        self.value = 'val'

    def avg(self): # instance method
        return (self.marks+self.best)/2
    def set_grade(self,value): #settters and getters in instance methods
        self.value = value
    def get_grade(self):
        return self.value

    @classmethod
    def get_schoolname(cls):
        cls.name = 'SSS'
        return cls.name

    @staticmethod
    def get_info():
        print("this is code for types of methods and this in static metho of module ",__name__)

# this is instance method -- why - because - it is passing self i.e object as its parameter
# so to call this method we use objects

s1 = Student('math', 65, 95)
s2 = Student("sci", 66, 95)
print(s1.avg())
print(s2.avg())

# two types of instances - one : Accesor methods Second : Mutator methods # tehse are also called as setters and getters

# we can assign values to variables either in constructor of class or using method
# but firt we have to initialse default values in init method
# we can get values of variables / instance variable by using object.variable or by using get method() inside class


# Accesor method - used only fetching instance variable values
# mutator method - used to modify instance variable we use mutator
s1.set_grade('A')
s2.set_grade('B')

print(s1.get_grade())
print(s2.get_grade())


# class methods
# methods that deal with class variables are class methods
# we have to use cls as param here instead of self
# we have to use a decorator @classmethod before defingn the method
print(Student.get_schoolname()) # if u dont mention @classmethod -- this line get_schoolname asks cls as param

# static method
# methods that dont deal with any instance variable or class variables are called as static methods
# use decorator - @staticmethod
# no param
print(Student.get_info())

