# Sorting in list

numeric = [1 , 9 , 5 , 7,  8 , 3, 4, 2 ,6]
alpha = ["Banana", "Mango","Dates","apple","orange","Grapes","Strawberry"]
alphanumeric = [ 1 , "Carot", 9 , "Cabbage" , "Chilli", 4 , "Garlic"]

# -- sort() function

numeric.sort()
alpha.sort()


print(numeric)
print(alpha)

# cant sort alpha numeric

# desending sort

numeric.sort(reverse=True)
alpha.sort(reverse=True)

print(numeric)
print(alpha)

# Customized sort 
def myfunc(s):
    return abs(s - 5)

numeric.sort(key= myfunc) # sort elements nearest to 5

print(numeric)

# Solves case sensitive sorting issue

alpha.sort(key = str.lower)

print(alpha)

# -- reverse function () 
# reverse all the list 

alpha.reverse()

print(alpha)