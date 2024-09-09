# list in pyhthon is used to create an array

MyList = ["Apple", "Banana","chery"]

print(MyList) #  print ['Apple', 'Banana', 'chery']
print(MyList[0]) # print Apple

# Note :
# 1 - List index start from zero 
# 2 - List is created using Square brackets [] 
# 3 - List items Are changeable like add or remove
# 4 - Allow Duplicate items
# 5 - Check length using Length
# 6 - Can have Multiple Datatype 

# we can add or remove items from list after creating it

print(type(MyList)) # print list


MyList = ["Apple", True, 123] # Can be of any datatype

print(MyList)

# Always use constructor for making list

MyList = list(("Apple", "Banana","Mango"))
print(MyList)


