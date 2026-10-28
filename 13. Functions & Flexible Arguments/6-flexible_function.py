# Flexible function: number or string
def flexible(x):
    if isinstance(x, (int, float)):
        print("Square:", x * x)
    elif isinstance(x, str):
        print("Uppercase:", x.upper())
    else:
        print("Unsupported type")

flexible(5)
flexible("hello")
