# IndexError handling
try:
    lst = [1, 2, 3]
    print(lst[10])
except IndexError:
    print("IndexError: list index out of range")
