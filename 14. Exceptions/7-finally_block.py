# Using finally to close file
import os
path = os.path.join(os.path.dirname(__file__), "finally_test.txt")
with open(path, "w") as f:
    f.write("data")
f = None
try:
    f = open(path, "r")
    print(f.read())
except Exception as e:
    print("Error:", e)
finally:
    if f:
        f.close()
        print("File closed")
os.remove(path)
