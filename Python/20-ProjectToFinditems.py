# Program to find the items in the string

UserInput = """Python is a Snake, but it is a language.
It can be used to do Artificial Intelligence and Machine Learning"""

check = ['Artificial intelligence', 'Machine Learning' , "Deep Learning", "Python"]

for c in check:
    if UserInput.lower().find(c.lower()) == -1:
        print(c.title()," is not present in string")
    else:
        print(c.title(),f"is Present at index {UserInput.lower().find(c.lower())}.")
