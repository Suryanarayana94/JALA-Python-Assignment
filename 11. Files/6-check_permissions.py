# Check file permissions using os.access
import os
path = os.path.join(os.path.dirname(__file__), "sample.txt")
if not os.path.exists(path):
    with open(path, "w") as f:
        f.write("test")
print("Readable:", os.access(path, os.R_OK))
print("Writable:", os.access(path, os.W_OK))
