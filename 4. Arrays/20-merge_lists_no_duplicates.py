# Merge two lists without duplicate elements
def merge_no_duplicates(a, b):
    result = []
    for x in a + b:
        if x not in result:
            result.append(x)
    return result

print(merge_no_duplicates([1, 2, 3], [3, 4, 5]))
print(merge_no_duplicates([], []))
