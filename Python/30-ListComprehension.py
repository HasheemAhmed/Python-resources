# Using List Comprehension methods for looping string

#newlist = [expression for item in iterable if condition == True]

# 1 - List Comprehensions are written in []
# 2 - Expression is the statement that executes when loop runs
# 3 - If condition is true than the statement executes

mylist = ["Apple", "Banana", "Cherry", "Kiwi", "Mango", "Watermelon"]

[print(x) for x in mylist] # print the list

# print those which has letter a

newList = [x for x in mylist if 'a' in x] 

[print(x) for x in newList]

# if else in the List comprehension


newlist = [x if x not in  ["Apple","Mango"]  else "Orange" for x in mylist ]

[print(x) for x in newlist]