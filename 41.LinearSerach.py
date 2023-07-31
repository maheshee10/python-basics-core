# linear search is searching for an elemnt in a given sequnece
# we take a list as input and number n to be found
# search for number through the list

pos = -1


def ser(lst, n):
    for e in lst:
        if e == n:
            globals()['pos'] = lst.index(e)
            return True
# once you write rtuen statement it terminates the code in which it is written

def linearsearch(lst, n):
    i = 0
    while i < len(lst):
        if lst[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    else:
        return False


def search(lst, n):
    i = 0
    for i in range(len(lst)):
        if lst[i] == n:
            globals()['pos'] = i

            return True
        i += 1


lst = [4, 5, 6, 7, 7, 4, 34, 345, 34, 5, 54, 5, 32]
n = 345
if ser(lst,n):
    print("found",pos)
else:
    print("not found")

if search(lst, n):
    print("found using search for loop", pos)

else:
    print("not found")

s = linearsearch(lst, n)
if s:
    print("found at {} using while loop".format(pos))
else:
    print("not found")
