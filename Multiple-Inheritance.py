
class Foo():
    
    def foo_method(self):
        print("foo method")
    
class Bar():
    def bar_method(self):
        print("bar method")

class FooBar( Foo, Bar):
    def foo_method(self): # it will override the foomethod and call the FooBar, so we will use the super class to call both
       super(FooBar, self).foo_method()
       print("FooBar method")
        


fb = FooBar() 
print(fb.foo_method())