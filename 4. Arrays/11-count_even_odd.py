# Count even and odd numbers in a list
def count_even_odd(lst):
    even = 0
    odd = 0
    for x in lst:
        if x % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

print(count_even_odd([1, 2, 3, 4, 5, 6]))
