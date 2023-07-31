# # calling a function from itself
# import sys
#
# sys.setrecursionlimit(200)
# print(sys.getrecursionlimit())
#
#
# def greet():
#     i = 0
#     print("hello", i)
#     i += 1
#     greet()
#
#
# greet()


# fact using recursion
def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)



r = fact(5)
print(r)
