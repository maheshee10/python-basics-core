class Computer:
    # special method __init__ -- similar to special variable __name__
    def __init__(self,a,b): # like constructor in java - loads when class obj is created here also
        self.cpu = a
        self.ram = b
        print("in init")

    # not needed to call this fun/method it executes self
    # used to initialise the variables in a class # attributes # sim to constructor in java

    def config(self):  # methods / functions
        print("pro laptop")
        print(self.cpu,self.ram)


# class wont iniated unless object is created
obj1 = Computer('mkn',23) # the moment object is created class is initiated and execute init fun/method -- just like constructor in java
# for every obj init gets called oncce
# params of init  and obj args must match
obj2 = Computer('ram',25)
# it accepts three args - self which is object arg, string and int values
# this means the object here will have to values in it and self is used to fetch values in it whenever it wants

# the args that we pass here will be accepted by __init__() as params
obj2.config()


