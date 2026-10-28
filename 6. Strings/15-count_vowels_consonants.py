# Count vowels and consonants
def count_vc(s):
    vowels = 0
    consonants = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants

v, c = count_vc("Hello World")
print("Vowels:", v, "Consonants:", c)
