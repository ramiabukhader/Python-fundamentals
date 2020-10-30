import heapq

# Heap is a tree in whic all the nodes of the tree are in a specific order, root node is the highest number


numbers = [1, 5, 3, 2, 100, 150, 190, 13, 35, 9, 5]

print(heapq.nlargest(2, numbers))
print(heapq.nsmallest(3, numbers))

print("----------")

heapq.heapify(numbers) # take the smalest elemetn to the first position
print(numbers)
print('----------')
# heap[0] is the smallest number in the array
people = [{'firstname': 'Jhon', 'Lastname' : 'RAmi', 'age' : 25},
          {'firstname': 'sami', 'Lastname' : 'said', 'age' : 24},
          {'firstname': 'reema', 'Lastname' : 'said', 'age' : 28},
          {'firstname': 'Jhon', 'Lastname' : 'Dora', 'age' : 18},
          {'firstname': 'Rana', 'Lastname' : 'Nadia', 'age' : 16}]

oldest = heapq.nlargest(2, people, key = lambda x: x['age'])
print(oldest)