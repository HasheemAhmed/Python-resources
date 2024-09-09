# changing list items using indexing

mylist = ["Apple", "Banana", "Cherry", "Kiwi", "Mango", "Watermelon"]

mylist[0] = "Lemon" # Apple changes to this

print(mylist)

mylist[2:3] = ["Peach" , "Strawberry"] # replacing seconf index with these two values

print(mylist)


mylist[-3:] = ["Dates"] # replacing last three indexes

print(mylist)
