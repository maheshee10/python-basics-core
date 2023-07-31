# prime - one and itself are its factors
n = int(input("enter a val:"))
for i in range(2,n):
    for j in (2,i):
        if i%j != 0 :
            print(i, end = " ")
print()
for i in range(2,n):
    if n%i == 0:
        print("not prime")
        break
else:
    print("prime")
