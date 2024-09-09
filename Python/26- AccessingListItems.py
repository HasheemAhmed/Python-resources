# We can access list as we access string

mylist = ["Apple", "Banana", "Cherry", "Kiwi", "Mango", "Watermelon"]

print(mylist[0])  # Print Apple
print(mylist[0:2]) # Print 0 and 1 index
print(mylist[-3:]) # print from end of array 

# - 3 minus index print from the last of list

print(mylist[::2]) # print  ['Apple', 'Cherry', 'Mango']


if "apple" in mylist:
    print("Yes, apple is in list")
elif "Apple" in mylist:
    print("Yes, Apple is in list")