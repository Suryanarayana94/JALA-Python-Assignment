# Reverse a list
def reverse_list(lst):
    result = []
    for i in range(len(lst) - 1, -1, -1):
        result.append(lst[i])
    return result

print(reverse_list([1, 2, 3, 4, 5]))
print(reverse_list([]))
