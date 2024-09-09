# adding and removing function to add items to list

# -- append() 
# Add item to last of the list

mylist = list(("Apple", "Banana", "Cherry"))
mylist.append("Orange")

print(mylist)

# -- insert()
# Add item to a specific index

mylist.insert(0,"Dates")
print(mylist)

# -- extend()
# to add items from another list

secondList = ['Peach',"Guava", "Strawberry"]
mylist.extend(secondList)

print(mylist)

# extend function also extend tuples,sets, or dictionaries

print("\nRemoving from list functions : \n")

# ---- removing list items

newlist = ["Apple", "Banana", "Mango", "Banana", "Cherry","Dates","Peach"]

# -- remove() function

newlist.remove("Dates") # case sensitive
print(newlist)

# -- pop() function

newlist.pop(1) # if duplicates remove only first occurence
print(newlist)

# if index is not given remove from the last

newlist.pop()
print(newlist)

# using del keyword

del newlist[1]
print(newlist)

# -- Clear() function

newlist.clear() # deletes all items but not loses datatype
print(newlist)

newlist.append("Apple")
newlist.append("Banana")

# delete the whole list and its datatype 
del newlist
