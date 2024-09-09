# How to loop a list in python

mylist = list(("Apple","Mango","Banana"))

# Using for-in loop

for x in mylist:
    print(x)


# using range to make an iteratable

for i in range(len(mylist)):
    print(i , mylist[i])


# using while loop

j = 0
while j < len(mylist):
    print(mylist[j])
    j = j + 1
