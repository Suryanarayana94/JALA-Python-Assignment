# Read from a specific index a fixed number of chars
import os
path = os.path.join(os.path.dirname(__file__), "sample.txt")
if not os.path.exists(path):
    with open(path, "w") as f:
        f.write("Hello World")
with open(path, "r") as f:
    f.seek(2)
    print("3 chars from index 2:", f.read(3))
