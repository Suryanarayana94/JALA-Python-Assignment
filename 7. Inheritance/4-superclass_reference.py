# Superclass reference behavior (runtime polymorphism)
class A:
    def show(self): print("A.show")

class B(A):
    def show(self): print("B.show")

class C(B):
    def show(self): print("C.show")

ref = A()
ref.show()
ref = B()
ref.show()
ref = C()
ref.show()
