
class Foo():
    
    def foo_method(self):
        print("foo method")
    
class Bar():
    def bar_method(self):
        print("bar method")

class FooBar( Foo, Bar):
    def foo_method(self):
       super(FooBar, self).foo_method()
       print("FooBar method")
        


fb = FooBar()
print(fb.foo_method())