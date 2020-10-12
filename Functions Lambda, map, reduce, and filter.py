s = lambda x : x * x 
print(s(2))


length = map(len, ['Rami', 'Sami'])
print(list(length))
# map basicly takes a function, global function can be imported easily takes two functions. it creates one empty collection(empty list for example)


# Reduce Function

from functools import reduce
# takes a fucntion into a collection, have to arguments, it returns a value created by combined items, it reduce tasks
# combine function into less time

total = reduce(lambda a, v: a + v, [1,2,3,4])
print(total)

# fliter function
# it also takes two functions

array1 = [1,2,3,4,43,2,2]
for i in filter(lambda q: q >= 4, array1):
    print(i)

