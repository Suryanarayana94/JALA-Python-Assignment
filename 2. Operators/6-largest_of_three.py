def largest_of_three(a, b, c):
    if a >= b and a >= c:
        print("Largest:", a)
    elif b >= a and b >= c:
        print("Largest:", b)
    else:
        print("Largest:", c)
largest_of_three(4, 9, 2)
largest_of_three(5, 5, 1)
