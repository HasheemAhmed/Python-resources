# joining lists in python


# Using + operator
list1 = ["Apple", "Banana"]
list2 = [1,2]

list3 = list1 + list2

print(list3)

# Using extend()

list1.extend(list2)

print(list1)

# using for loop apppend()


for x in list1:
    list2.append(x)


print(list2)