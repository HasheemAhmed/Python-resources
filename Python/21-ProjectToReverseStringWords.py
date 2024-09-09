# Project to reverse the all words in a string

UserInput = """Python is a Snake, but it is a language.
It can be used to do Artificial Intelligence and Machine Learning"""

def reverse(str1):
    str2 = ""
    l = len(str1) -1
    for x in str1:
        str2 += str1[l]
        l -= 1
    return str2

# first method

start = 0
end = 0
reverseString = ""

for sr in UserInput:
    end += 1
    if end == len(UserInput):
        reverseString += ' ' + reverse(UserInput[start:end])
    elif sr == ' ' :
        reverseString += reverse(UserInput[start:end])
        start = end
    

print("Reversed String is : " , reverseString)

# second method

string = UserInput.split()
reverseString = ""
lt = list()
for s in string:
    lt.insert(0,reverse(s))

lt.reverse()
for s in lt:
    reverseString += s + ' '
    
print("Reversed String is : " , reverseString)