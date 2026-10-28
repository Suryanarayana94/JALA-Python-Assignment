# Internal variables prefixed with _
class Demo:
    def __init__(self):
        self._internal = "internal value"

d = Demo()
print("Accessing _internal:", d._internal)
# Convention: single underscore means internal use; still accessible.
