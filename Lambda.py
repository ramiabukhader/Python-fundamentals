
"""
def greeting():
    return 'Retrun'
print(greeting())

greet_lambda = lambda: "HEy you"
print(greet_lambda())
"""
"""def result(s):
    print(s.strip().upper())
"""
# as we notice, lambda can take arguments same as functions but faster when having small operations
result = lambda s: s.strip().upper()
print(result("                Hallo               "))


def result(*args):
    for i in args:
        print(i)

print(result(1,2,3,4,5))

examp = lambda x, *args, **kwargs: print(x, args, kwargs)
print(examp("Test", 'test2', test3 = 'argument'))