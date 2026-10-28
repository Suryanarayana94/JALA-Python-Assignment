# Class hierarchy A -> B -> C
class A:
    pass

class B(A):
    pass

class C(B):
    pass

print("A is superclass of B:", issubclass(B, A))
print("B is superclass of C:", issubclass(C, B))
print("A is superclass of C:", issubclass(C, A))
