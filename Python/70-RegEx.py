# REg Ex means regular expresions

# there is a module re for dealing with the refular expresssoins

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)
#^ means start
#$ means end
#. means single chracter
#* many chracters

# functions in the re module

# findall() -  returns a list containing all matches
# search() - returns a match object if thery is any match
# split() - returns a list after splitting by matching string
# sub()  - replaces one or matches with a string


# Meta Chracters are the chracters with special meaning

# [] - A set of chracters [a - m]
# \ - signals a special sequence using escape chracters \d
# . - Any chracter except newline chracter he..o
# ^ - start with "^Start"
# $ - end at "end$"
# * - Zero or more occurence he.*o
# + - one or more occurence he.+o
# ? - zero or one occurence he.?o
# {} - exact occurence he.{2}o
# | - either or fall| stays
#() - capture and group


txt = "The rain in Spain"
# find all lower case letter between a and i
se = re.findall("[a-i]",txt)
print("[a-i] : ",se)

txt = "I have 39 dollars."
# find all digits
se = re.findall("\d",txt) 
print("\d : ",se)

# find the spaces
se  = re.findall("\s",txt)
print("\s : ",se)


txt = "Hello!  Python developers."
# find for the single chracter
se = re.findall("He..o",txt)
print("he..o : ",se)

# find all that start with  Hello
se = re.findall("^Hello" , txt)
print("^Hello : " , se)

# find if end with lopers
se = re.findall("lopers.$",txt)
print("lopers$ : ",se)

txt = 'Python is a good language.'

# find for zero or more occurence
se = re.findall("Py.*on",txt)
print("Py.*on : " , se)

# find for one or more occurence
se = re.findall("g.+d",txt)
print("g.+d : " , se)

#find for zero or one occurence

se = re.findall("Pyth.?n",txt)
print("Pyth.?n : ",se)


# find exact number of occurencese
se = re.findall("lan.{4}e",txt)
print("lan.{4}e : " ,se)


# find all with keyword

se = re.findall("good|bad",txt)
print("good|bad : ",se)