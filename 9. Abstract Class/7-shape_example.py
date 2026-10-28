# Real-world: abstract Shape with Circle and Rectangle
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self): pass
    def display(self):
        print("This is a shape")

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h

for s in (Circle(3), Rectangle(4, 5)):
    s.display()
    print("Area:", s.area())
