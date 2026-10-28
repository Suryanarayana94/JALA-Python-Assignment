def is_palindrome(num):
    s = str(num)
    return s == s[::-1]
for test in [121, 123, 1221, 10]:
    print(test, "is palindrome" if is_palindrome(test) else "is not palindrome")
