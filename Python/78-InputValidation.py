# userinput validation

# int validation

while True:
    try:
        user = input("Enter a Number : ")
        userinput = int(user)
    except ValueError:
        print("Please enter a number : ")
    else:
        print("Number : ",userinput)
        break


# float validation

while True:
    try:
        user = input("Enter a Number or decimal value : ")
        userinput = float(user)
    except ValueError:
        print("Please enter a number or a decimal : ")
    else:
        print("Number : ",userinput)
        break

# Also check for email id
import re

while True:
    user = input("Enter a valid email id : ")
    userinput = re.search(r"\b[a-zA-Z.+_0-9\-]+@[a-zA-z]+\.[a-zA-z.]+\b",user)

    if userinput:
        print("Email : ",userinput.group())
    else:
        print("Please enter a email id : ")