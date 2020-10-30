#Iterators

""" for i in [1,2,3,4]:
    print(i)
"""
"""
list1 = [1,2,3,4,5]
my_iterator = iter(list1)
print (next(my_iterator)) #1
print (next(my_iterator)) # it prints one step of 1 only in each runtime

print(my_iterator.__next__()) #3
print (next(my_iterator)) # 4
print (next(my_iterator)) # it willthrough an error or exception in here because we passed all elements in the list
"""

my_list = [1,2,3,4]
for element in my_list:
    pass

iter_obj = iter(my_list)

while True:
    try: #try check if there is any exceptions or not
        element = next(iter_obj)
        pass
    except StopIteration:
        break
# here we created an iterator object, and we are taking each element from that list using next, it will keep going through the list until the last elemetn and give us the stop iteration error

