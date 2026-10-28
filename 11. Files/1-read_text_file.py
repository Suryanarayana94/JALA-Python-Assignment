# Read a text file
import os
path = os.path.join(os.path.dirname(__file__), "sample.txt")
if not os.path.exists(path):
    with open(path, "w") as f:
        f.write("Hello World\nSecond line\n")
with open(path, "r") as f:
    print(f.read())
