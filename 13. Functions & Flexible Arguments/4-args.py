# Using *args
def sum_all(*args):
    total = 0
    for n in args:
        total += n
    return total

print(sum_all(1, 2, 3, 4))
print(sum_all())
