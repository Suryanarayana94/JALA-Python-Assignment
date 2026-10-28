# Simulating access levels
class Demo:
    def __init__(self):
        self.public = "public"
        self._protected = "protected"
        self.__private = "private"

d = Demo()
print("public:", d.public)
print("protected:", d._protected)
try:
    print("private:", d.__private)
except AttributeError as e:
    print("private access error:", e)
print("name-mangled:", d._Demo__private)
