def contains(lst, value):
    for x in lst:
        if x == value: return True
    return False
print(contains([1, 2, 3], 2))
print(contains([1, 2, 3], 5))
