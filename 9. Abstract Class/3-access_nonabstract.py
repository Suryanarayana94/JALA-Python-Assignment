# Access non-abstract method via child object
from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def task(self):
        pass
    def normal(self):
        print("Inherited normal method")

class Child(Parent):
    def task(self):
        print("Child task")

c = Child()
c.normal()
