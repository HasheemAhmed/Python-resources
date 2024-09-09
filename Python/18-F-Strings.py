# String formatting methods

#age = 23
#name = "My Age is : " + age

# we cannot combine int string using + operator

# -----Using str() method
age = 20
name = "My age is : " + str(age)

print(name)

# ----- using string formatting - String litteralls

# Using f"" and {} for variables

age = 20
name = f"My age is : {age + 10}"

print(name)

# using :.2f

age = 20.123
name = f"My age is : {age:.2f}" # for decimals 

print(name)