# Pattern matching using re module
import re
email = "test@example.com"
print("Email valid:", bool(re.match(r"^[\w.+-]+@[\w-]+\.[\w.-]+$", email)))
digits = "12345"
print("Only digits:", bool(re.fullmatch(r"\d+", digits)))
print("Only digits (abc):", bool(re.fullmatch(r"\d+", "abc")))
