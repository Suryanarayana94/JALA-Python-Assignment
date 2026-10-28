# Remove duplicate elements and return a new list
def remove_duplicates(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))
print(remove_duplicates([]))
