# Random access reading using seek()
import os
path = os.path.join(os.path.dirname(__file__), "sample.txt")
if not os.path.exists(path):
    with open(path, "w") as f:
        f.write("Hello World")
with open(path, "r") as f:
    f.seek(6)
    print("From index 6:", f.read())
