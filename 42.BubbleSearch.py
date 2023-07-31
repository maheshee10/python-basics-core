# in bubble search instead of checking every value we use midpoint chechking
# take two bounds - lower and upper and midle = l+u//2 integer divison
# compare n number to be searched with midlle value if n > middle => change l to middle else change Upper to miccle
# repeat this until middle matches wwith n
# binary search works only with sorted list

pos = -1
def bubble(li,n):
    l = 0
    u = len(li)
    i = 0
    while i<len(li):
        m = (l+u)//2
        if li[m] == n:
            globals()['pos'] = m
            return True
        else:
            if n > li[m]:
                l = m
            else:
                u = m
        i+=1

def bsearch(lst,n):
    l = 0
    u = len(lst)
    for i in range(len(lst)):
        m = (u+l)//2
        if lst[m] == n:
            globals()['pos'] = m
            return True
        else:
            if n>lst[m]:
                l = m
            else:
                u =m



lst = [34,5,67,34,56,546,34,2345,56,546,435,5,52,5,623]
n = 34
li=lst.sort()
print(li)


if bsearch(lst,n):
    print("found using dor loop",pos)
else:
    print("not found")



if bubble(lst,n):
    print("found at {}".format(pos))
else:
    print("not found")