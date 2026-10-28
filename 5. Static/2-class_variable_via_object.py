# Access class variable via object
class Demo:
    class_var = "Shared"

obj = Demo()
print("Via object:", obj.class_var)
