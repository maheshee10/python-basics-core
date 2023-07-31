av = 6
x = int(input("how many candies you want:"))
i=1
"""while i<=x:
    if i > av:
        print("out of stock")
        break
    print("candy",i)
    i+=1"""

"""while i<=x:
    print(i)
    if i == 6:
        i += 1
        continue

    print("candy", i)
    i+=1"""
for i in range(1,25):
    if i%3==0 or i%5==0:
        continue
    print(i, end =" ")

print()
print('bye')

# pass - to ignore that part
