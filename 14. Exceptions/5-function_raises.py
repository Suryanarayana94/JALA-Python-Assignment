# Function that always raises; call without handling then handle
def always_raises():
    raise RuntimeError("Always fails")

# Unhandled call would crash; demonstrate handling instead
try:
    always_raises()
except RuntimeError as e:
    print("Handled:", e)
print("Continued after handling")
