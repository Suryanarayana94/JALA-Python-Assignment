# Find minimum and maximum values in a list
def min_max(lst):
    if not lst:
        return None, None
    mn = lst[0]
    mx = lst[0]
    for x in lst:
        if x < mn:
            mn = x
        if x > mx:
            mx = x
    return mn, mx

print(min_max([3, 1, 4, 1, 5, 9, 2]))
print(min_max([]))
