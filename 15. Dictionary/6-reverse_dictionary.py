# Reverse dictionary: name -> id
students = {101: "Alice", 102: "Bob"}
reversed_dict = {v: k for k, v in students.items()}
print(reversed_dict)
