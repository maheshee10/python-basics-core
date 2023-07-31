print(__name__) # prints the name of the the module - in this case - it is __main__ because
# python running directly in this file - every file accts as module
# say I import another module here
import math
print("math module name : {}".format(math.__name__))
print(__name__)
# math module begins with its __name__ as main
# not stated explicitly but staring point for execution of math is main() - function
# now when I import a module say example math module all the functions and all the statements in it in it are also imported
# every module will have __main__ as its __name__ when operating it
# so to avoid importing of all functions we use if __name__ == __main__ in every module

# this allows it nor import all its functions whichh arein main
# only required functions will be imported
# the file we are operating will have main as it name variable modules will have their module names as name variable


