def is_prime(num):
    if num <= 1: return False
    if num == 2: return True
    if num % 2 == 0: return False
    i = 3
    while i * i <= num:
        if num % i == 0: return False
        i += 2
    return True
for test in [2, 3, 4, 17, 20, 1]:
    print(test, "is prime" if is_prime(test) else "is not prime")
