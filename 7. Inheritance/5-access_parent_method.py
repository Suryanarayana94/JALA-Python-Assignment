# Access parent method using super()
class A:
    def show(self): print("A.show")

class B(A):
    def show(self):
        super().show()
        print("B.show")

class C(B):
    def show(self):
        super().show()
        print("C.show")

C().show()
