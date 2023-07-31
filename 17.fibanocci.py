# 1,1,2,3,5,7...
def fib(n):
    a = 0
    b = 1
    print(b)

    for i in range(1, n):
        c = a + b
        a = b
        b = c

        print(c)



fib(5)
