# Count frequency of each element in a list
def frequency_count(lst):
    freq = {}
    for x in lst:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

print(frequency_count([1, 2, 2, 3, 3, 3]))
print(frequency_count([]))
