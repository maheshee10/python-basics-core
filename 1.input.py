import sys
# using input function taking input
# by default input function takes string value
# to convert string to other types we use type conversion method which is to write (data type) in front of input

# x = input("enter value :")[0]
# y = input("enter a vlaue :")
# z = eval(input("entaer a val:"))
# print(x,y,z)
# another way is to take input using arg values
# arg starts with 1 because zero takes filename
x = sys.argv[1]
y = sys.argv[2]
z = sys.argv[3]
print(x)
print(y)
print(z)
print(x,y,z)
# argv takes command line values as input to be taken in command prompt
print("argument list :", list(sys.argv))

