# Poly means multiple, morph means form
# it is the ability of object to take multiple forms

class Dog:
    def bark(self):
        print("whoaaa")
    
    def feathers(self):
        print("The dog has brown feathers")
        
class Man:
    def bark(self):
        print("the man can imitate the dog")

    def feathers(self):
        print("the person takes a feather from the ground and takes it")

    def name(self):
        print("Rami Airi")


def in_the_forest(obj):
    obj.bark()
    obj.feathers()

milo = Dog()
rami = Man()

in_the_forest(milo)

print("---------------------------")

in_the_forest(rami)