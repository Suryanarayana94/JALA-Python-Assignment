# Handle exception with try/except
try:
    print("Result:", 10 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
