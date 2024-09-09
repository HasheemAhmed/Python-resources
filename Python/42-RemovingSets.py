# remove() , discard()

se = {'Green','Yellow','Blue'}

se.remove("Green")
se.discard("Blue")

print(se)

# pop()

s2 = {'Green','Blue'}
se.update(s2)

se.pop() # removes a random item
 
print(se)

# del - clear()

del s2
se.clear()

# print(type(se)) not a set in del
print(type(se))