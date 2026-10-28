# Modify class variable via instance demonstrates instance attribute creation
class Demo:
    class_var = "Shared"

obj = Demo()
obj.class_var = "Instance value"
print("Instance:", obj.class_var)
print("Class:", Demo.class_var)
