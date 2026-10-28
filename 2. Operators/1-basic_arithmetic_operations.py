def arithmetic_operations(a, b):
    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)
    if b != 0:
        print("Division:", a / b)
    else:
        print("Division: cannot divide by zero")
arithmetic_operations(10, 2)
arithmetic_operations(7, 0)
