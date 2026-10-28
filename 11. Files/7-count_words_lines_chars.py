# Count words, lines, characters
import os
path = os.path.join(os.path.dirname(__file__), "sample.txt")
if not os.path.exists(path):
    with open(path, "w") as f:
        f.write("Hello World\nSecond line here\n")
with open(path, "r") as f:
    content = f.read()
lines = content.count("\n")
if content and not content.endswith("\n"):
    lines += 1
words = len(content.split())
chars = len(content)
print("Lines:", lines, "Words:", words, "Chars:", chars)
