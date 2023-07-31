# iterator - something that can be iterable
# iterator and iterable both are different
# say a list is iterable but not iterator
# iterator knows its state remembers its memory state
# for loop in background uses this iterator concept
# iterator takes a iterable and works on every object in it
# iterator will have two one is iterator() and other is next()
# both are dunder methods - iter() returns itself and next() returns next item
# __iter__() and __next__()
# nums = [4, 5, 6, 7, 8]
# for e in nums:
#     print(e)

# here nums is converted into an iterator first by using iter() or __iter__ on nums
# and return itself first and next is used to go for next value
# this is repeated until limit reached where it raisies an StopRaise exception
# it = iter(nums)  # converting iterable into iterator
# print(it)  # gives list_iterator obj address -- list_iterator means list converted into iterator
# # iterator gives one value at atime
# print(iter(nums))  # -- # object adress output
# print(it.__next__())  # next gives iterators next values and it has a state means it remembers -- here 4
# print(next(it))  # gives next of iterator where it remebers 4 -- 5 is output
# print(next(it))  # gives next of 5 in iterator it
# print(next(it))
# print(next(it))


# print(next(it))
# print(next(it))
# print(next(it)) # its stopping at 8 irrespective of repetitions -- error - StopIteration

# we need two methods to do our own iterator - iter() - gives the self value - to help store the state of it
# and second is next() which gives the next value / state of what iter() remebered

# class Iter:
#
#     # def __init__(self, lst):  # initialising object with variable -- here list is given to object self
#     #     pass
#     #          # self.a = lst
#
#     def __iter__(self):  # iter() returns iterate of given iterable
#         i = 0
#         self.a = lst[i] # initialising first value of the iterate
#         i+=1
#         return lst[i] # returning the iterate
#
#     def __next__(self):  # returns next value of iterate and stores next state of iter()
#         val = self.a # storing current value of iterate
#         self.a += 1 # incrementing and storing nexrt value of itearate for next iteration
#         return val # returning current value of iterate
#
#
# lst = [3, 4, 5, 6]
#
# it = Iter()
# # print(it.__next__())
# # print(it.__iter__())
# i = it.__iter__()
# print(i)
# n = it.__next__()
# print(n)
# print(n)
#
#
class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

sequence = [6,7,8,9,56]
s = SequenceIterator(sequence)
r = s.__iter__()
r1 = s.__next__()
print(r)
print(r1)
print(s.__next__())
print(next(r))