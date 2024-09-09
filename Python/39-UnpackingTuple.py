# unpacking the tuple 

# get values int o variables

color = ('White','Black','Yellow')

(white,black,yellow ) = color

print(white)
print(black)
print(yellow)

# if there are extra words then use * it places all extra words in last variable

color = ('White','Black','Yellow','Mahroon','green')

(white,black,*yellow ) = color

print(white)
print(black)
print(yellow)
print(type(yellow)) # stores as list