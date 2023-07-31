from numpy import *
arr = array([5,6,78,89,90])
print(arr)
arr+= 5
print(arr)
arr1 = array([45,67,56])
print(arr1)
arr2 = array([34,45,3])
print(arr2)
arr3 = arr1+arr2 # vectorised addition #shapes(sizes) should match
print(arr3)
# math ops of array
print(sqrt(arr))
print(sum(arr))
print(min(arr))
print(sort(arr))
print(concatenate([arr2, arr1]))
# + adds elements to each other
# concatenate is combine to arrays into one


#copying array
A = array([12,23,34,45,56])
B = A # copies A to B also both will have same adresses
print(A)
print(B)
print(id(A))
print(id(B))

B = A.view() # Shallow copy - copies A to B but different adress - but if you change A will effect B
print(B)
print(id(B))

B = A.copy() # deep copy - coppies  A to B but changes its address and also A change dont effect B
A[2] = 245
print(A[2])
print(B)
print(id(B))
