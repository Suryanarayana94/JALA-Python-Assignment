# Calling parent constructor with super()
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

c = Child("Alice", 20)
print(c.name, c.age)
