# Decorators: they add some functionality and returns it. 
# Decorator is a defined function

def make_pretty(func):
    def innerr():
        print("I got decorated")
        func()
    return innerr

#@make_pretty  #it calls the function

def ordinary():
    print("I am ordinary")


#working of decorators
#pretty = make_pretty(ordinary)
#pretty()


# adding the functionality of decorators
# zero gives an error when doing division, the decorator can solve this by making the function smarter
def dividefun(func):
    def inner(a,b):
        print("I'm going to divide {} by {} ".format(a,b))
        if b ==0:
            print("not possilbe to divide zero")
            return
        return func(a,b)
    return inner

@dividefun #called the function in another function
def divide(a,b):
    print(a/b)
divide(10,0)