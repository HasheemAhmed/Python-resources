# Editing Tuple

# Updating tuple

mytuple = ('Apple','Banana','Cherry')
x = list(mytuple)
x[1] = 'kiwi'
y = tuple(x)

print(x)

# we can also add , remove or replace item by converting
# item from tuple to list and then to tulpe

# Joining two tuples

tup1 = ('Apple','Banana','Cherry')
tup2 = ('Mushrooms','Dates','PineApple')

joines = tup1 + tup2
print(joines)