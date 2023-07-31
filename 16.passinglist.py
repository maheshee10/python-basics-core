lst1 = [1, 2, 3, 4, 5, 6, 7, 78, 9]
# lst = []
# length = int(input("enter list length:"))
# for i in range(length):
#     x = int(input("enter a val:"))
#     lst.append(x)
# print(lst)


def count(lst):
    even = 0
    odd = 0
    for e in lst:
        if e % 2 == 0:
            even += 1
        else:
            odd += 1
    return even,odd


# even,odd = count(lst)
# print(even,odd)
e,o = count(lst1)
print("even :",{e} ,"odd :",{o})
print("even : {} and  odd {}".format(e,o))
