# Read-only property: Employee id
class Employee:
    def __init__(self, eid, name):
        self._id = eid
        self.name = name
    @property
    def id(self):
        return self._id

e = Employee(101, "Alice")
print("ID:", e.id)
try:
    e.id = 202
except AttributeError as ex:
    print("Cannot modify id:", ex)
