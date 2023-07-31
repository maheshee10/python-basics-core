def decorator_fun(original_fun):
    def inner_fun():
        return original_fun()
    return inner_fun

def display():
    print("decorator test")

my_decorator = decorator_fun(display)
my_decorator()