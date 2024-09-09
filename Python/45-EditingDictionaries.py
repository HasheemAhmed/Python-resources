dic = {'name':'Hasheem',
       'age' : 23}

dic['age'] = 22

print(dic)

# update()  method

dic.update({'age':20})
print(dic)

#using these methods we can also add item to dictionary

dic.update({'gender':'Male'})
print(dic)

# removing items
# Pop() method

dic.pop('gender')
print(dic)

#popitem()

dic.popitem() # removes last element
print(dic)

# using del

del dic['name']
print(dic)

# clear()

dic.clear() # clear whole dictionary
print(dic)