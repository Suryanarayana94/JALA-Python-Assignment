# Abstract and non-abstract methods
from abc import ABC, abstractmethod

class AbstractDemo(ABC):
    @abstractmethod
    def abstract_method(self):
        pass
    def normal_method(self):
        print("Normal method from abstract class")

# child implements it
class Child(AbstractDemo):
    def abstract_method(self):
        print("Implemented abstract method")

c = Child()
c.normal_method()
c.abstract_method()
