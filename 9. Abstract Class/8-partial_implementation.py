# Partial implementation: cannot instantiate
from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def method1(self): pass
    @abstractmethod
    def method2(self): pass

class Partial(Parent):
    def method1(self):
        print("method1 implemented")
    # method2 not implemented

try:
    p = Partial()
    print("Created partial")
except TypeError as e:
    print("Error:", e)
