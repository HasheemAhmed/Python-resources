# Upper case

#upper() function

x = "Python is a popular language that can be used to do AI , ML , APP  etc"
print(x.upper()) # convert string to uppercase

# lower() function

print(x.lower()) #convert string to lowercase

#strip() function

print(x.strip()) # Removes whitespaces from beginning and end

# Note -- Useful; when you have to take last and start first elements

#replace() function

print(x.replace("Python","Javascript"))

#split()

y = x.split(',') # split make slices of string at the commas

for z in y:
    print(z)

#capatalize()

print(x.capitalize()) # converts first letter to capital letter
