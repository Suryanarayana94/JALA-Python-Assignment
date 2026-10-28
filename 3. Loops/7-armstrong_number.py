def is_armstrong(num):
    digits = str(num)
    n = len(digits)
    total = sum(int(d) ** n for d in digits)
    return total == num
for test in [153, 370, 371, 9474, 123]:
    print(test, "is Armstrong" if is_armstrong(test) else "is not Armstrong")
