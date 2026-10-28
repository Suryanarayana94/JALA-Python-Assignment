# Sort a list without using sort() or sorted() (bubble sort)
def manual_sort(lst):
    arr = list(lst)
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(manual_sort([5, 2, 9, 1, 5, 6]))
print(manual_sort([]))
