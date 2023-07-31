# two types of array - single dim and multi dim
# numpy - 3rd party package
# in python we can't use multi dim arrays with array module
# so we use numpy pack for multi dim arrays
# but to use numpy by default numpy is not available in python
# install manually using - 'pip'
# pip - used to install external packages in python
# pip : pip install packages
# go to command prompt - use command -pip3 install numpy
from numpy import *
a = array([12,23,34],int)
print(a)
# in numpy package no need to mention type in array() function
print(a.dtype)
# there are 6 types of arrays creation in numpy
# in array all elements have same type
# in numpy python converts all values implicitly if we dont't give sepcific type
#one way
a = array([1,2,3,4]) # by default array will take type based on values it hold-in this case-int
b = array([1,2,3.4,45]) # all other elements converted to float
print(a,b)
print(a.dtype, b.dtype, sep =" ,")
#second way - linspace()
#takes three param - start stop step
c = linspace(0,15,10) # unlike in range here 15 is included and 10 is the range broken into number of parts
#16 parts into 10 parts gives
print(c)
#if we dont give number of parts-50 is default value

#3rd way
d = arange(1,15,2) # - like range
print(d)
# 4th way
# in linspace gap betwwn parts is fixed and same
e = logspace(1,40,5)
# parts same like linespace but spacing is based on log of that number
print("%0.2f" % e[4])
print(e)

# 5th way
f = zeros(5)
# 6th way
g = ones(5,int)
print(f,g)

