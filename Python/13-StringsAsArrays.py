# Strings in python are composed of array of bytes

# index start from 0
a = "Python"
print("a[1] : " ,a[1]) #prints y


# prints string from start to index 2
print("a[:3] : " ,a[:3]) 

# prints from 2 to index 4
print("a[2:5] : " ,a[2:5]) 

# using loop to prints this

for x in a:
    print(x)

#len() functions

print(len(a)) # print 6 for python

# checking string using in

x = "Python is a snake"
print("snake" in x) # returns true

# -- Note this serah is case sensitive