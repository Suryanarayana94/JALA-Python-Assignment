# Computed property: Rectangle area
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    @property
    def area(self):
        return self.length * self.width

r = Rectangle(5, 3)
print("Area:", r.area)
r.length = 10
print("Area after change:", r.area)
