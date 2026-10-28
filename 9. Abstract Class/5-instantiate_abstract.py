# Attempt to instantiate abstract class
from abc import ABC, abstractmethod

class AbstractDemo(ABC):
    @abstractmethod
    def task(self):
        pass

try:
    obj = AbstractDemo()
    print("Created object")
except TypeError as e:
    print("Error:", e)
# Cannot instantiate abstract class with abstract method.
