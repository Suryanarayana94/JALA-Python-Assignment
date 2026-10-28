# Multiple abstract methods
from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def method1(self): pass
    @abstractmethod
    def method2(self): pass

class Child(Parent):
    def method1(self): print("method1 implemented")
    def method2(self): print("method2 implemented")

c = Child()
c.method1()
c.method2()
