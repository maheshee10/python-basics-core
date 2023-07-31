from numpy import *
# arr = array([1,2,3])
# print(arr)
# print(arr.dtype)
# print(arr.ndim)
# print(arr.shape)
# print(arr.size)
# print(arr.flatten())
# arr1 = array([1,2,3,4,5,6,7,8,9],(float,4))
# print(arr1)
# rint(arr1.dtype)
# print(arr1.ndim)
# print(arr1.shape)
# print(arr1.size)
# print(arr1.flatten())
#
# #
a = array([[1,2,3],[4,5.0,6],[7,8,9]])
print(a)
print(a.dtype)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.flatten()) # converts / reduces dimension from 2 d to one d
# b = array([[[],[]],[[],[]]])
# c = array([[],[]])
# n = int(input("enter outer array count val:"))
# m = int(input("enter inner array count"))
# o = int(input("enter elements length:"))
# for i in range(n):
#     for j in range(m):
#         for k in range(o):
#             x = int(input("enter elements:"))
#
#
# b = a.reshape(3,4)

# print(b)
x = array([[1,2,3],[4,5,6]])
print(x)
y=x.flatten()
print(y)
z = y.reshape(2,3)
print(z)
m = z.reshape(3,2)
print(m)
n = m.reshape(2,3,1)
print(n)
o = m[:,:,newaxis]
print(o)
newA = array([[[1,2,3,4],[5,6,7,8]]])
print(newA)
print(newA.shape)
print(newA.reshape(4,1,2))
m = matrix(newA)
name = 'python'
mat = matrix('1 2 3;4 5 6;7 8 9')
print(mat)
