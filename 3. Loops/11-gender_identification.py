def gender_identify(g):
    g = g.strip().upper()
    if g == "M": print("Male")
    elif g == "F": print("Female")
    else: print("Invalid Input")
gender_identify("M")
gender_identify("F")
gender_identify("X")
