# Property decorator with age validation
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            print("Error: age must be greater than zero")

s = Student("Alice", 20)
print(s.age)
s.age = 22
print(s.age)
s.age = -3
print(s.age)
