# Find the second-largest number in a list
def second_largest(lst):
    if len(lst) < 2:
        return None
    first = second = None
    for x in lst:
        if first is None or x > first:
            second = first
            first = x
        elif second is None or (x > second and x != first):
            second = x
    return second

print(second_largest([1, 2, 3, 4, 5]))
print(second_largest([5, 5, 4]))
print(second_largest([1]))
