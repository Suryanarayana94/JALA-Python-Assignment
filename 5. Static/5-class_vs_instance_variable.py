# Class variable vs instance variable
class Demo:
    class_var = "Class-level"
    def __init__(self):
        self.instance_var = "Instance-level"

d = Demo()
print("class_var:", Demo.class_var, "|", d.class_var)
print("instance_var:", d.instance_var)
Demo.class_var = "Class updated"
d.instance_var = "Instance updated"
print("After changes -> class_var:", Demo.class_var, "| instance:", d.class_var)
print("instance_var:", d.instance_var)
