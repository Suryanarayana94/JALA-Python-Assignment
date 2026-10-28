# Simple Student class with name and age, setters/getters
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_age(self, age): self.age = age
    def get_age(self): return self.age

s = Student("Alice", 20)
print(s.get_name(), s.get_age())
s.set_name("Bob"); s.set_age(21)
print(s.get_name(), s.get_age())
