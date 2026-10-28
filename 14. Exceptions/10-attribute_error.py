# AttributeError handling
try:
    obj = "hello"
    obj.nonexistent()
except AttributeError:
    print("AttributeError: attribute not found")
