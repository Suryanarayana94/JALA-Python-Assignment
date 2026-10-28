# Relative import demonstration inside package
from .class_one import ClassOne

def use_class_one():
    obj = ClassOne(10)
    obj.show()
    return obj
