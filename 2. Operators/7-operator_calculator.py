def calculator(a, b, op):
    if op == "+":
        print("Result:", a + b)
    elif op == "-":
        print("Result:", a - b)
    elif op == "*":
        print("Result:", a * b)
    elif op == "/":
        if b == 0:
            print("Error: division by zero")
        else:
            print("Result:", a / b)
    else:
        print("Invalid operator:", op)
calculator(10, 2, "+")
calculator(10, 2, "/")
calculator(10, 0, "/")
calculator(10, 2, "%")
