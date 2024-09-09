dic = dict(name = 'Hasheem', age = 20)

# print the keys name
for x in dic:
    print(x)

# print the values
for x in dic:
    print(dic[x])


# making copy of dictionaries

dic2 = dict(dic)

dic3 = dic2.copy()

print(dic3)