# Create a child class implementing abstract method
from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def task(self):
        pass

class Child(Parent):
    def task(self):
        print("Child implemented task")

c = Child()
c.task()
