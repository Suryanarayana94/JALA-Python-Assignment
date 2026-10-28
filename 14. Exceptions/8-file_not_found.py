# File not found handling
try:
    with open("no_such_file.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
