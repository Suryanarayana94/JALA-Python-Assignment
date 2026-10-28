# Multiple except blocks
try:
    a = int(input("Enter numerator: ")) if False else 10
    b = int(input("Enter denominator: ")) if False else 0
    print(a / b)
except ZeroDivisionError:
    print("Division by zero")
except ValueError:
    print("Invalid input")
# Sample: numerator 10, denominator 0 -> Division by zero
