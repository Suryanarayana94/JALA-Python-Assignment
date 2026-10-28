# else block runs only when no exception
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Division by zero")
else:
    print("No exception, result:", x)
