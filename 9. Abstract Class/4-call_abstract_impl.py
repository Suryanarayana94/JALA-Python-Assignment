# Call abstract method implementation via child
from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def area(self):
        pass

class Child(Parent):
    def area(self):
        return 42

c = Child()
print("Area:", c.area())
