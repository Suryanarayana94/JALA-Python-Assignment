# Remove a specific element from a list
def remove_element(lst, value):
    result = []
    for x in lst:
        if x != value:
            result.append(x)
    return result

print(remove_element([1, 2, 3, 2, 4], 2))
print(remove_element([1, 2, 3], 9))
