def count_digits(num):
    num = abs(num)
    if num == 0: return 1
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count
for test in [0, 5, 123, 9999]:
    print(test, "has", count_digits(test), "digits")
