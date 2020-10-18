# inheritance in oop, basic and multiple inheritcane

# class Base:
#     def walk(self):
#         print("I am walking")

# class DerivedClass(Base):
#     pass

# d = DerivedClass()
# d.walk()



class Rectangle():
    
    def __init__(self, w, h):
            self.w = w
            self.h = h

    def area(self):
        return self.w * self.h 

    def parameter(self):
        return 2* (self.w + self.h)
        

class Square(Rectangle):
    def __init__(self, s):
        super(Square, self).__init__(s,s) # the super method will take us to the rectangle class
        self.s = s

s = Square(3)
print(s.area())
print(s.parameter())



# Monkey Patching: if you forget to add a function in the class, and you want to use later, monkey patching help

class A:
    def __init__(self,num1):
        self.num1 = num1

    def add(self, num2):
        print(self.num1 + num2)

def get_num(self): # monkey patching
    return self.num1


foo = A(42)
A.get_num = get_num  # monkey patching 

print(foo.get_num())
bar = A(6)
print(bar.get_num())
