# Object creation and method calls
class A:
    def a1(self): print("A.a1")
    def a2(self): print("A.a2")
    def show(self): print("A.show")

class B(A):
    def b1(self): print("B.b1")
    def b2(self): print("B.b2")
    def show(self): print("B.show")

class C(B):
    def c1(self): print("C.c1")
    def c2(self): print("C.c2")
    def show(self): print("C.show")

for cls in (A, B, C):
    obj = cls()
    print("---", cls.__name__, "---")
    if cls is A:
        obj.a1(); obj.a2()
    elif cls is B:
        obj.a1(); obj.a2(); obj.b1(); obj.b2()
    else:
        obj.a1(); obj.a2(); obj.b1(); obj.b2(); obj.c1(); obj.c2()
    obj.show()
