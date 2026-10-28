# Copy file content
import os
src = os.path.join(os.path.dirname(__file__), "sample.txt")
dst = os.path.join(os.path.dirname(__file__), "copy_test.txt")
if not os.path.exists(src):
    with open(src, "w") as f:
        f.write("Copy me\n")
with open(src, "r") as f:
    data = f.read()
with open(dst, "w") as f:
    f.write(data)
print("Copied. Destination content:")
with open(dst, "r") as f:
    print(f.read())
os.remove(dst)
