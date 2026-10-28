# Real-world Employee class
class Employee:
    def __init__(self, name, eid, salary):
        self.name = name
        self.id = eid
        self.salary = salary
    def __str__(self):
        return f"Employee(name={self.name}, id={self.id}, salary={self.salary})"

e1 = Employee("Alice", 101, 50000)
e2 = Employee("Bob", 102, 60000)
print(e1)
print(e2)
