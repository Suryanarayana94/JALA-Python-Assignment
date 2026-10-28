# Instance variables with same name in A, B, C
class A:
    def __init__(self):
        self.value = "A-value"

class B(A):
    def __init__(self):
        super().__init__()
        self.value = "B-value"

class C(B):
    def __init__(self):
        super().__init__()
        self.value = "C-value"

a, b, c = A(), B(), C()
print("a.value:", a.value)
print("b.value:", b.value)
print("c.value:", c.value)
ref = a
ref = b
print("ref (B).value:", ref.value)
ref = c
print("ref (C).value:", ref.value)
