i = 1
while i<=5:
    print(i," hi",end = " ")
    i+=1
    j = 1
    while j<=5 :
        print("mahesh", end =" ")
        j+=1
        break
    print()

m = 1
while m<=5 :
    print('mahesh','nmk\'s','mnk\'s',sep =" ,")
    m+=1
    if m==4:
        print('continue block executed here')
        continue
a = input('enter string').split(" ")
print(a)