# Identify duplicate values in a list
def find_duplicates(lst):
    seen = []
    dup = []
    for x in lst:
        if x in seen and x not in dup:
            dup.append(x)
        seen.append(x)
    return dup

print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))
print(find_duplicates([1, 2, 3]))
