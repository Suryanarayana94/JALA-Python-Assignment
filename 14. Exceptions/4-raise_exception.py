# Raise exception manually for age < 18
def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    print("Age accepted:", age)

try:
    check_age(15)
except ValueError as e:
    print("Error:", e)
check_age(20)
