def find_index(lst, value):
    for i in range(len(lst)):
        if lst[i] == value: return i
    return -1
lst = [10, 20, 30, 40]
print(find_index(lst, 30))
print(find_index(lst, 99))
