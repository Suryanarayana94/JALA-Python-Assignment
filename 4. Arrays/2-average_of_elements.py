def average_elements(lst):
    if not lst: return 0
    total = 0
    for x in lst: total += x
    return total / len(lst)
print(average_elements([1, 2, 3, 4, 5]))
