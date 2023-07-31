# # Functions
# # define and call
# # once defined can be called multiple times
# # must be called to get executed
# # fun have one name and two a block of statements
# # syntax: def fun_name() : - enter - write a block - exit block - call func-name
# def greet():
#     print("hai gm")
#     print("bye")
#
#
# greet()
#
#
# # add without params/arguments
# def add():
#     x = int(input("enter a val:"))
#     y = int(input("enter another val:"))
#     z = x + y
#     print(z)
#
#
# add()
#
#
# # add with return
# def add(x, y):
#     z = x + y
#     return z
#
#
# r = add(4, 8)
# print(r)
#
#
# #  returning multiple values
# def add_sub(x, y):
#     z = x + y
#     s = x - y
#     m = (x + y) * (x - y)
#     return z, s, m
#
#
# r1, r2, r3 = add_sub(6, 7)
# print(r1,r2,r3)
# # Arguments of a function
# """in general we have pass by value and pass by refernce concepts
# pass by value means passing only value of a variable to another variable as argument here changing
# the argument varibale doent effect original variable
# pass by reference mean passing address of the value it holds as argument variable
# here if you change arg variable the original variables value also changes becasue the address is main
# """
# # but in Python no such concept of pass by value or reference ias there
# def update(x):
#     print("x id before update",id(x))
#     x = 8
#     print(x, "x")
#     print("x id after update", id(x))
# a = 10
# print("id of a ",id(a))
# print(a, "a")
# update(a)
# l = [3,4]
# print("list l id",id(l))
# update(l)
# lst = list([4,5,67])
# print("lst id", id(lst))
# update(lst)
# print()
# print("list l id",id(l))
# print("lst id", id(lst))
# update(id(lst))
# # types of arguments
# positional, keyword, default, arbitrary(arbitraty pos, arbitrary kewyword)
# poasitional first, kewyword next, arbitrary pos next, arb keyword next
# positional
def add(a, b):
    print(a, b, "a,b")  # takes a as 5 and b as 6


add(5, 6)


def person(name, age):  # takes name as 23 and age as mb
    print(name, age, "name, age")


person(23, "mb")


# to solve positional problem use keywords

def person1(name, age):
    print(name, age, "name, age")


person1(name="mahesh", age=30)  # keyword arguments


# position must follow keyword but not keyword after position

def person4(id, name, age):
    print(id, name, age)


person4(1, age=30, name="mkn")


# default - can be given in dife -
def default_det(id, age, fav="mb,dhoni", name_per="mkn"):
    print(id, age, fav, "id,name,age,fav")
    print(id, age, name_per, fav, "id,name,age,fav")


default_det(2, age=33)  # mix of pos, keyword, default

# arbitrary
# position
# def info_per(*det):
#     print(det)
#     for i in det:
#         print(i)


details = tuple([2, 3, "mahesh"])


# info_per(details)

def info_per1(a, *det):
    for i in det:
        print(a, i)


info_per1("yn66", details)
info_per1("mahesh", 1, 2, 3, 4, 5, 6, 7, 8)


def information(a, *rno, subject, college='BEC', **data):
    for i in rno:
        for key, value in data.items():
            print(college, a, subject, ':', i, ':', key, value)
            break


# dat = dict({'mahesh': 56, 'rajesj': 56})
information("EEE", 1, 2, 3, 4, 5, 6, 7, 8, subject="EMF", mahesh=67, kiran=34, sai=99)
# information("EEE", 1, 2, 3, 4, 5, 6, 7, 8, subject="EMF", **dat)
