# Verify whether a list contains both 12 and 23
def contains_both(lst):
    has12 = False
    has23 = False
    for x in lst:
        if x == 12: has12 = True
        if x == 23: has23 = True
    return has12 and has23

print(contains_both([1, 12, 5, 23]))
print(contains_both([12, 5]))
