# Advanced function with defaults, *args, **kwargs
def total_price(base, discount=0, *items, **extra):
    total = base
    for item in items:
        total += item
    for key, value in extra.items():
        if key == "tax":
            total += value
    total -= discount
    print("Total:", total)

total_price(100, 10, 20, 30, tax=15)
