

class Person:
    # Attributes
    #species = "homo sapiens"
    # method

    def __init__(self, name, hair_color, species = "Homo"): # a constructor takes a value and operate it in the object you call
        self.name = name
        self.species = species
        self.hair_color = hair_color

    def info(self): # the function turns to method when its inside the class
        print("{} can walk".format(self.name))

    def sleep(self):
        print("{} is sleeping".format(self.name))
    
    def rename(self, new_name): # here we can maipulate the object
        self.name = new_name
        print("my name changed to {}".format(self.name))

# make an objects if you want to use the class
# Rami = Person("Rami", "Black")

# Sami = Person('Sami' , 'Red')

# Rami.info()
# print( "Rami's hair colour is " + Rami.hair_color)

# Rami.rename("Khader")


# Bound, Unbound and static methods
class A:

    @classmethod
    def fan(self, x):
        print(2  *x) 
    @staticmethod
    def g( name): # no self, in static methods because you don't call it from otger functions
        print("hello, %s" %name)

A.fan(4)
#a = A()
#a.g("Remi")  
#print(A.f) # this will save a function stored in a location , Static method
A.g("Remi")