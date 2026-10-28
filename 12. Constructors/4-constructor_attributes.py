# Constructor initializes instance attributes
class Demo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

d = Demo(1, 2)
print("a:", d.a, "b:", d.b)
print("vars:", vars(d))
