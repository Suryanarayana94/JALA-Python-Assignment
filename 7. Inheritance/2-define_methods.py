# Define methods: two specific + one common overridden
class A:
    def method_a1(self): print("A method_a1")
    def method_a2(self): print("A method_a2")
    def common(self): print("A common")

class B(A):
    def method_b1(self): print("B method_b1")
    def method_b2(self): print("B method_b2")
    def common(self): print("B common")

class C(B):
    def method_c1(self): print("C method_c1")
    def method_c2(self): print("C method_c2")
    def common(self): print("C common")

a = A(); b = B(); c = C()
for obj in (a, b, c):
    obj.common()
a.method_a1(); a.method_a2()
b.method_b1(); b.method_b2()
c.method_c1(); c.method_c2()
