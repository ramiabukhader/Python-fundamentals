# Excetpions handling: errors detected during execution are called exceptions.
# To handle exceptions, we use try, catch, finally and else

# def divide(a, b):
#     print(a/b)

# divide(2,0)

# print("other part working")
# print()

""" execpting the error by giving the code a tries
try:
    x = 3 / 2
    #print(x)
except ZeroDivisionError as e:
    print("Division by zero! the execption was", e)
    #handle exceptions
    # x = 0
    pass
finally:
    print("the end")


print("other part of code")
"""
# try:
#     x = 5 / 0
#     print(x)
# except ZeroDivisionError as e:
#     print("I got an error")
#     raise # this for debug, raise the exception for the debugging purpose
# finally:
#     print("The End")

# print("code runing perfectly")

try:
    d = {}
    a = d[1]
    b = d.jrgeugnsa
except (KeyError, AttributeError) as e: # or you can use the keyword: Exception
    print("A keyError and attribute error exception was caught!")
    raise