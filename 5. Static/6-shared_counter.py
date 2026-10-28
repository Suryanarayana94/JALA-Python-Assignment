# Shared counter for Student objects
class Student:
    count = 0
    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("A")
s2 = Student("B")
s3 = Student("C")
print("Total students:", Student.count)
print(s1.name, s2.name, s3.name)
