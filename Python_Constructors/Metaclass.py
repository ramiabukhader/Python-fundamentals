# everything in python is a class
# metaclass is the class of the class
class Foo(object):
    pass

bar = Foo()
print(type(bar)) # bar is an object of the class foo

print(type(Foo)) # Foo is a class type

print(type(type)) # type belongs to class type

# creating a metaclass
class Randommetaclass(type):
    def __new__(cls , class_name, class_parents, class_dict):
        print("creating a new class named", class_name)
        new_class = super().__new__(cls, class_name, class_parents, class_dict)
        return new_class

class Spam( metaclass = Randommetaclass):
    def info(self):
        print("inseret some elemetns")

s = Spam()
s.info