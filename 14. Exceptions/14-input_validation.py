# Input validation system (simulated inputs)
def get_valid_number():
    attempts = ["abc", "0", "5"]
    for val in attempts:
        try:
            n = int(val)
            if n <= 0:
                raise ValueError("must be positive")
            print("Valid number:", n)
            return n
        except ValueError as e:
            print(f"Invalid input '{val}': {e}")
    return None

get_valid_number()
