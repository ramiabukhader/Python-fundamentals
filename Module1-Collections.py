import collections

counts = collections.Counter([1,1,3])
print(counts)

# letter counter
# the counter will count the words
print(collections.Counter('Task scheduling'))

print("\n")

# Implementing dequeue
from collections import deque
d = deque('happy') # will convert the string into a list
for element in d:
    print(element.upper())

d.append('You')
print(d)
d.appendleft('How')
print(d)

print(d.pop())
print(d)
print(d[-1])