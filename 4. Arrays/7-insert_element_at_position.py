# Insert an element at a specified index
def insert_at(lst, index, value):
    result = []
    for i in range(len(lst)):
        if i == index:
            result.append(value)
        result.append(lst[i])
    if index >= len(lst):
        result.append(value)
    return result

print(insert_at([1, 2, 3], 1, 99))
print(insert_at([1, 2, 3], 5, 99))
