# Write and append to a text file
import os
path = os.path.join(os.path.dirname(__file__), "write_test.txt")
with open(path, "w") as f:
    f.write("First write\n")
with open(path, "a") as f:
    f.write("Appended line\n")
with open(path, "r") as f:
    print(f.read())
os.remove(path)
