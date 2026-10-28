# Password validation system
class PasswordValidator:
    def __init__(self, password):
        self.password = password
    def is_valid(self):
        if len(self.password) < 8:
            return False
        if not any(ch.isdigit() for ch in self.password):
            return False
        return True

for p in ["abc", "abcdefgh", "abcd1234", "short1"]:
    pv = PasswordValidator(p)
    print(p, "->", "Valid" if pv.is_valid() else "Invalid")
