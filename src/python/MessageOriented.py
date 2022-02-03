class Foo:
    # Method called if attribute is unknown
    def __getattr__(self, attribute):
        return lambda: print(f"Method {attribute} not found")

class Bar(Foo):
    def f(self): print("Bar:f")

class Baz(Foo):
    def g(self): print("Baz:g")

def test(anything):
    print(anything.__class__)
    anything.f()
    anything.g()

if __name__ == '__main__':
    test(Bar())
    test(Baz())

# Output:
# <class '__main__.Bar'>
# Bar:f
# Method g not found
# <class '__main__.Baz'>
# Method f not found
# Baz:g
