# Difference between largest and smallest elements
def diff_max_min(lst):
    if not lst:
        return 0
    mn = mx = lst[0]
    for x in lst:
        if x < mn: mn = x
        if x > mx: mx = x
    return mx - mn

print(diff_max_min([1, 2, 3, 4, 5]))
print(diff_max_min([]))
