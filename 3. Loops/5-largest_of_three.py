def largest_of_three(a, b, c):
    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= a and b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)
largest_of_three(12, 45, 7)
largest_of_three(3, 3, 3)
