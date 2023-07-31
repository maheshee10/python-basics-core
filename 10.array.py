# import array or import array as arr -- module
# arr here is amodule with function array()
# so we have to use arr.array() everytime we use array function or
# we can simply import function instead of module i.e from array import array()
#from array import array() or from array import * -- * imports all functions of array module
from array import *
# for arrays we have to mention type also first and next the values
# becaus earrays accept all same type of data
# depending on type of datat type we specify memory will have that type of size in arrays
# unsigned int - starts with zero and infinity and signed int takes all neg and pos values

values = array('i',[1,2,3,4,5]) # i is signed int data type takes alla neg qand pios
print(values)
print(values.buffer_info()) # gives a tuple of two ele-- first is address and second is size
print(values.append(45), values)
for i in values:
    print(i)
for i in range(len(values)):
    print(values[i], sep = ",",end ="")
ar = array('u',['m','h','e','s','h']) # u is code for char type data
for e in ar:
    print(e)
print()
newA = array(values.typecode,(a for a in values))
# values.type code is used when you dont know which type of value we give
# when you dont type values and copy from some list or array use: s for s in vals
# here s taking for every s element in vals array
print(newA)
newA2 = array(newA.typecode, (a*a for a in newA))
print(newA2)