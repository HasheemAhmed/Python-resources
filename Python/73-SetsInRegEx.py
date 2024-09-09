# A set is set of chracters within the []

import re

txt = "Python is a good language,but it is sometimes bad."

# returns a match if a , r, n is present in the word
res = re.findall("[arn]",txt)
print(res)

# returns a match lowercase chracters between a - n is present in the word
res = re.findall("[a-n]",txt)
print(res)

# returns a match except a r n is present in the word
res = re.findall("[^arn]",txt)
print(res)

# returns a match for all uppercase and lowercase is present in the word
res = re.findall("[a-zA-z]",txt)
print(res)