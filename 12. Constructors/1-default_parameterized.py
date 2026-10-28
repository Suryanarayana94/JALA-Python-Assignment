# Default and parameterized constructors simulated
class Demo:
    def __init__(self, a=None, b=None):
        if a is None and b is None:
            self.x = 0
            self.y = 0
        elif b is None:
            self.x = a
            self.y = 0
        else:
            self.x = a
            self.y = b
    def show(self):
        print("x =", self.x, "y =", self.y)

Demo().show()
Demo(5).show()
Demo(5, 10).show()
