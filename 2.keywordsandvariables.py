# keywords are reserved words
import keyword

kw = keyword.kwlist
print(kw)
# variable
''' variables are containers with data -- name and value -- python takes data type of variable by defaul dependon 
on the value it holds -- value can be changed -- mul var can point to same address - var with no data is none data type
unused value is taken by garbage collector -- cannot be keywords -- cannot start with nums only alpha or _
unlike java no need to declare datatype'''
a = 10
b = a
# a and b will point to same address
print(id(a))
print(id(b))
a = 12
print(id(a))
print(id(b))
# b will still point same 10 value address
#swapping two var
x = 34
y = 'mahesh'
x,y = y,x
print(x,y)
#assigning multiple ways
m = n = p = 78
m,n,p = 'pqr'
print(m,n,p)
m,n,p = 4,5,67
print(m,n,p)
x,y = [89,'d']
print(x,y)
# python liner by line execution so if there is error in line 4 it executes output till there
x,y = (67,89)
print(x,y)
x,*y = 'mahesh'
print(x,y)
# functions
# python wiil have num of in built function which can be used to perform various types of tasks
# type() gives type of class/data type
# input() takes in put we give at command line -- by default it takes string class type
# print() give the output
# also modules like math and we can use them by using 'import' also import required - from math import
# string takes single or double quotes no char separate part of string only
# string concatenate and mul can be done
# str + for concatenate and constant*str for mul - no str*str option
# none - num: int bool float complex - collections : str, list, tuple, range non sequence  : set and dict
# str sequence immutable have some functions str.
# list sequence mutable - slicing- indexing - all types accept
# tuple - immutable - seq- indexing - slicing - tuple. - accepts all type
# set - unordered - unique - doent keep inserting order - no indexing - no slicing - accepts int float str but not list
# dict  - key value pairs - functions - unordered - inserting order preserved - list no - indexing no - slicing no -
# dict. -
# dups not allowed in set and dict
# to keep raw input we use r in print
# by default python takes \n as end param so \n is new line but if we specify end with something else
# output can be changed accordingly
# by default separate is <space> in python we can alter by changeiong sep param
# sep="," end = " "
# /t gives tab that is apace
# insert and append differe on list
# insert - inserts in index before the specified index
# append replces on the specified index
help()