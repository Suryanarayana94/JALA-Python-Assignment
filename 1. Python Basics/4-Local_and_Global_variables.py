name = "Python"  # Global variable

def display():
    global name
    name = "Java"  # Modifies the global variable
    age = 22       # Local variable
    print("Inside function:", name)
    print("Age:", age)

display()
print("Outside function:", name)