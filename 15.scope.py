a = 10 # global variable
print(id(a))
def scope():
    a = 15 # local variable
    x = globals()['a']
    print(x)
    print(id(x))
    print(a) # local given prefernce over global variable inside a function
    globals()['a'] = 36 # global variable value is changed
    print(a) #this is still local variable a
    print(x)
    print(id(x))

scope()
print(a)
print(id(a))