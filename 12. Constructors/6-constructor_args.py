# Constructor with *args
class Demo:
    def __init__(self, *args):
        self.args = args
    def show(self):
        print("Stored args:", self.args)

Demo(1, 2, 3).show()
Demo("a", "b").show()
