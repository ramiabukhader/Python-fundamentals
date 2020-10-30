# list Comprehension (LC): it is alternative of a for loop, inline comprehension, single line statments

squares = [x*x for x in (1,2,3,4,5)]
print(squares)


# getting a list upper case from a string

print([s.upper() for s in "uppercase"])

# strip of any comas from the end of the list

#list1 = ['ramy,', 'sami,', 'seba,']
print([a.strip(',') for a in ['ramy,', 'sami,', 'seba,']])

#conditional LC, getting even_numbers

print([x for x in range(20) if x % 2== 0])

#if we want to make this in loop

even_nums = []
for i in range(20):
    if i % 2 == 0:
        even_nums.append(i)
print(even_nums)
# as we see, LC gives only one line of code to solve the problem, less complex, and faster runtime


# Dictionary Comprehension (DC)

print({x: x*x for x in (1,2,3,4,5)}) # we use tuple for dictionary 
