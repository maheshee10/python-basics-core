from array import *
arr = array('i',[])
n = int(input("enter length of array:"))
for a in range(n):
    x = int(input("enter array values:"))
    arr.append(x)
print(arr)
s = int(input("enter value to search:"))
k = 0
for a in arr:
    if a == s:
        print(arr.index(a))
        print(k)
        break
    k+=1
else :
    print("input value not found:")
print(arr.index(s))