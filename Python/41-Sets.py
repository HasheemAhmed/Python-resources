# Sets 

# 1 - Sets are written in curly Brackets {}
# 2 - Sets are unorderes means they  are unindexed
# 3 - Sets are unchangeable
# 4 - Sets are used to store values in a variable

thisset = {'Apple',"banana",1,True}

print(thisset)
print(len(thisset)) # 3 as 1 and true are duplicates
print(type(thisset)) # print set

# we cant access set by index but wit for loop

for x in thisset:
    if 'Apple' is x:  # to access a specified element
        print(x)


print('banana' in thisset) # returns true

# add() method

myset = {'red','Green','Blue'}

myset.add('Yellow')

print(myset)

# update()

secset = {'White','Magenta'}
myset.update(secset)

print(myset)