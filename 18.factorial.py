
def fact(n):
    f = 1
    for e in range(1,n+1):
        f = f * e
    return f


r = fact(5)
print(r)
