# __str__ for better output
class Demo:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Demo(name={self.name}, age={self.age})"

print(Demo("Alice", 20))
