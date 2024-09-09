# Dictionaries

# 1 - Dictionaries are Written in {}
# 2 - Dicstionary are written in key : value pairss
# 3 - Dicionaries does not have duplicates
# 4 - Items are changeable

# how dictionary is created

thisdic = {'name' : 'Hasheem',
           'age' : 23}

print(thisdic)
print(type(thisdic)) # print dict

dictionary = dict(name = 'hasheem',age = 23)

print(dictionary)

# first item is key and second item is value

# Accessing dictionaries

name = thisdic['name']
age = thisdic['age']
print(name) # print Hasheem
print(age)

# get() method

print(thisdic.get('name'))

# get the key names - keys()

print(thisdic.keys())

# adding new item to dictoinary

thisdic['gender'] = 'Male'

print(thisdic)

# getting the values - values()

print(thisdic.values()) # get values as list

# get the all values pair in dict - items() 

y = thisdic.items() 

for x in y:
    print(x[0].capitalize() + ' :',x[1])

# checking a key in dicy

if 'age' in thisdic:
    print('Yes, age is present in the dictionary')