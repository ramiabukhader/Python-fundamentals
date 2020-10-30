from functools import partial

# partial creates a partial application for another function and evaluate it partilay

def f(a, b, c, x):
    return 1000*a + 100*b + 10*c + x

g = partial(f, 1, 1, 1) # by using partial, we can set a value for all elements except x, and the program will perform normally
# because of partial, we can evaluate any parameters without setting a value to others
print(g(2)) # two is the value of X

print('-----')

import functools
import locale

print(sorted(["A", "S", "D", "F"], key= functools.cmp_to_key(locale.strcoll)))

listt = [1, 3, 22, 5, 3, 33]
#using reduce to compute something
print("The sum of the list is:")
print(functools.reduce(lambda a, b: a+b, listt))
print("-------")

print(functools.reduce(lambda a, b: a if a>b else b, listt))
