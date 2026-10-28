# Append data with timestamp
import os
from datetime import datetime
path = os.path.join(os.path.dirname(__file__), "log_test.txt")
with open(path, "a") as f:
    f.write(f"{datetime.now()} - appended entry\n")
with open(path, "r") as f:
    print(f.read())
os.remove(path)
