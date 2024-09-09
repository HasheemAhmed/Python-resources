# Copying a list from another list

# -- Using copy() function

list1 = ["Apple", "Banana"]
list2 = list1.copy()

print(list1)
print(list2)

# -- Using list() function

list3 = ["Python", "C++"]
list4 = list(list3)


print(list3)
print(list4)

# Important note - Not Use This

list5 = ["SQL","Mongodb"]
list6 = list5

list6.append("Azure") # changing in list 6 also takes place in list 5

print(list5)
print(list6)