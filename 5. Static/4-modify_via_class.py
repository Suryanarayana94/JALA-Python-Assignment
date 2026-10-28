# Modify class variable via class name
class Demo:
    class_var = "Shared"

Demo.class_var = "Updated"
o1 = Demo()
o2 = Demo()
print("Class:", Demo.class_var)
print("o1:", o1.class_var)
print("o2:", o2.class_var)
