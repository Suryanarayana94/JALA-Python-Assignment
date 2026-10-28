# Read file using read(), readline(), readlines()
import os
path = os.path.join(os.path.dirname(__file__), "sample.txt")
if not os.path.exists(path):
    with open(path, "w") as f:
        f.write("Line one\nLine two\nLine three\n")
with open(path, "r") as f:
    print("read():", repr(f.read()))
with open(path, "r") as f:
    print("readline():", repr(f.readline()))
with open(path, "r") as f:
    print("readlines():", f.readlines())
