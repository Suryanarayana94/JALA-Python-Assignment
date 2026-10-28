# Copy elements from one list to another
def copy_list(src):
    dst = []
    for x in src:
        dst.append(x)
    return dst

a = [1, 2, 3]
b = copy_list(a)
print("Original:", a)
print("Copy:", b)
b.append(4)
print("After modifying copy, original:", a)
