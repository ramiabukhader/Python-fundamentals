# Generators

def generator():
    n = 1
    print("This is the first iteration usin generator")
    yield n # yield is a return function, but it returns as many as u need

    n += 1 
    print("the next iteration")
    yield n

    n += 1
    print("last iteration")
    yield n

a = generator()
print (next(a))
print (next(a))
print (next(a))

def rev_str(my_str):
    length = len(my_str)
    for i in range(length-1, -1, -1): #[4,3,2,1] reverse loop
        yield my_str[i]

for char in rev_str("Rami"):
    print(char)


# Generator expression
print("Generator expression")
new_list = [1,3,6,9,12]
print([x**2 for x in new_list])

a = ((x**2 for x in new_list))
print(next(a))
print(next(a))
print(next(a))