# to print multiple hashes
i = 1
n = int(input("enter a val:"))
while i<=n:
    j = 1
    while j<=n:
        print("hash", end =" ")
        j+=1
    i+=1
    print()
print("while loop end")
for i in range(0,n+1):
    for j in range(0,n):
        print("hash", end = " ")
    print()
print("for loop end")
#  to print low triangular matrix

for i in range(n):
    for j in range(i):
        print("#", end =" ")
    print()

#  to print low triangular matrix

for i in range(n):
    for j in range(n-i):
        print("#", end =" ")
    print()