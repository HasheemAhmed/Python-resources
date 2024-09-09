# Tuples

# 1- Tuples are written in round brackets
# 2 - Orderd
# 3- unchangeables once it is created but you can join two tuples
# 4 - Allow Duplicates Values
# 5 - Start From 0
# 6 - Can be of any datatype


mytuple = ('Cherry', 123, 'Apple')

print(len(mytuple))

# For creating 1 item tuple we have to add a comma

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Using tuple constructor

tup  = tuple(('Apple', 'Banana','Cherry'))
print(type(tup))
