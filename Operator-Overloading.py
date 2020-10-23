#Operator overlading is the extanding operator of such a +, - or any other operators, it used for extanding of one operator
# to enable it, we can define a magice methods such as __add__, ___sub___, and etc.
# class A:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

        

#     def __add__(self, other):
#         return self.a + other.a, self.b + other.b

#     def __sub__(self, other):
#         return self.a - other.a, self.b - other.b
    
# # obj1 = A(2)
# # obj2 = A(3)

# obj1 = A(1,2)
# obj2 = A(2,4)
# print( obj1 + obj2)

## another example

class B: 
    def __init__(self, a):
        self.a = a

    def __lt__(self, other):
        if(self.a < other.a):
            return "obj1 is less than obj1"
        else:
            return "obj2 is less than obj1"
        
    def __eq__(self, other):
        if(self.a == other.a):
            return "they're equal"

        else:
            return"they are not equal"

        


obj1 = B(2)
obj2 = B(3)
# self.a = 2, other.a = 3
print(obj1 == obj2)