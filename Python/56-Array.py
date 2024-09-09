# Arrays in python

# Creating Arrays of the values

cars = ['Toyota','Volvo','BMW']

# Accessing arrays

print(cars[0],cars[1],cars[2])

# Modify the array elements

cars[1] = 'Honda'

print(cars[1])

# length of array

print(len(cars))

# adding elements to array

cars.append('Mercedes')

print(cars)

# pop()

cars.pop() # removes element from the last
print(cars)

cars.pop(1) # remove the first element
print(cars)


# extends()
truck = ['Mazda','Loader']

cars.extend(truck)
print(cars)

# remove()

cars.remove('Mazda')
print(cars)

