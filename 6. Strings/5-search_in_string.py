# Search in string using find() and index()
s = "Hello World"
print("find('World'):", s.find("World"))
print("find('Python'):", s.find("Python"))
try:
    print("index('World'):", s.index("World"))
except ValueError:
    print("index: not found")
try:
    print("index('Python'):", s.index("Python"))
except ValueError:
    print("index('Python'): not found")
