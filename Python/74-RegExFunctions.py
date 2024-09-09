# there are 4 types of function in regex

# findall()  - search()  - split()  - sub()

import re

# findall()

txt = "Pyhton is a good programming language in Ai and ML."
res = re.findall("in",txt) # returns a list of all in 
print(res)

# search()

res = re.search(r"\S*gram\S*",txt) # find word containg gram
if res:
    print(res.span()) # returns the index (17,20)
    print(res.start()) # returns the start index
    print(res.end()) # returns the end index

# split()

res = re.split("\s",txt) # returns a list at each split chracter
print(res)

res = re.split("\s",txt,3) # split only at the 3 occurence
print(res)

# sub()

res = re.sub("Pyhton",'Javascript',txt)
print(res)

res = re.sub("\s",',',txt,2) # replace space with , at 2 occurences
print(res)


res = re.search(r"\b[pP].\w+", txt)
print(res.group()) # returns the that word