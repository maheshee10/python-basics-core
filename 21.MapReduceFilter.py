# filter
import functools

lst = [2, 34875, 83893, 9202]
evens = list(filter(lambda n: n % 2 == 0, lst))
print(evens)
import math

# map
lst = [4, 56, 67, 35, 673, 2456]
mapping = list(map(lambda n: math.sqrt(n), lst))
print(mapping)

# reduce - reucing output of a functio
lst = [56,34,89,24,9348]
# reduce is function that belongs to 'functools' module
"""    At first step, first two elements of sequence are picked and the result is obtained.
    Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
    This process continues till no more elements are left in the container.
    The final returned result is returned and printed on console."""
from functools import reduce
lstd = [56,34,89,24,9348]
reduced = (reduce(lambda a,b : a if a>b else b, lstd))
print(reduced)
# reduced return only one output
# map and filter returns list output
# all three takes two arguments one is function and other is iterable i.e list / sequence
s = 'mahesh kumar'
import functools
# r = functools.reduce(lambda a : a[:-1],s)
# print(r)
