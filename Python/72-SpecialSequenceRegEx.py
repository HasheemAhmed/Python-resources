# Special Sequence is a \ followed by a letter

import re

txt = "The rain is raining in the lahore."

# \A returns a match if specified chracter is at the start of (string)
res = re.findall("\AThe",txt)
print(r"\AThe : ",res)

# \b return if specified sequence is at the start or at the end of (word)
# useful when dealing with words
res = re.findall(r"\brai",txt)
print(r"\brai : ",res)

res = re.findall(r"he\b",txt)
print(r"he\b : ",res)

# \B return if specific chracter is not at the end or at the start
res = re.findall(r"rai\B",txt)  # sequence not be at the end
print(r"rai\B : ",res)

res = re.findall(r"\Bhe",txt)  # sequence not be at the start
print(r"\Bhe : ",res)

txt = "My number is 123-456-789"
#\d return when string contains digits 0 -9 (Chracter)
res = re.findall(r"\d",txt)
print(res)

#\D return when string does not contains digits 0 -9 (Chracter)
res = re.findall(r"\D",txt)
print(res)

#\s return where there is a whitespace (Chracter)

txt = "The rain is raining in the lahore."
res = re.findall(r"\s",txt)
print(r"\s :",res)


#\s return where there is a no  whitespace (Chracter)

txt = "The rain is raining #@%$#^%^ in the Lahore."
res = re.findall(r"\S",txt)
print(r"\S : ",res)

#\w returns the string where the string contains any word conatining alphabet,0-9,_ (Chracter)
res = re.findall(r"\w",txt)
print(r"\w : ",res)

#\w returns the string where the string does not contains any word conatining alphabet,0-9,_ (Chracter)
# for special chracters and spaces
res = re.findall(r"\W",txt)
print(r"\W :",res)

# \Z return if at the end of string
res = re.findall(r"Lahore.\Z",txt)
print(r"Lahore.\Z :",res)

