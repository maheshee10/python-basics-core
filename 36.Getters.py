# similar to Iterators except it yields in stead of returns
# yields do not terminate function return terminates ahould be at end of code block
# generator give iterator
def topten():
    n = 1
    while n<=10:
        sq = n*n
        yield sq
        n+=1
    yield 5
    # this gives an  iterator object  # keyword converts function as generator


values = topten()
# print(values)

for i in values:
    print(i)

