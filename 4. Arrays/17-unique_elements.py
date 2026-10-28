# Return a list containing only unique elements (no duplicates)
def unique_elements(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

print(unique_elements([1, 2, 2, 3, 3, 4]))
print(unique_elements([]))
