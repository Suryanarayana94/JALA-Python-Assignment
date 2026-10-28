# Validation: age must be > 0
class Student:
    def __init__(self, name, age):
        self.name = name
        self.set_age(age)
    def set_age(self, age):
        if age > 0:
            self.age = age
        else:
            print("Error: age must be greater than zero")
    def get_age(self):
        return self.age

s = Student("Alice", 20)
print(s.get_age())
s.set_age(-5)
print(s.get_age())
