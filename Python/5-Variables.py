# variables

# No command for creating variable
# variable created when a value is assigned

x = 5 # integer
name = "Hasheem" # String
y = 2.3 #Float

print(type(x))
print(type(name))
print(type(y))

# type can be changed after declaration

z = 4
print(type(z))
z = "hasheem"
print(type(z))

# Type Casting

a = str(3) # a will become string
b = int(3) # b will become int
c = float(3) # c will become float

#str(), int(), float() used to convert the types

x = '123'
x = int(x)

print(x)

# String will Become int if it is valid

r = 'hasheem'
r = "Hasheem"

#Both are same 

s = 4
S = "pyhton"

# Case sensetive both are different variables

# --- Variables Name

# Start with a letter or underscore
# Cannot start by a number
# Variable can be alpha - numeric
# Variables are case sensitive
# Can't be a python keyword
# Cannot be include spaces

_var = 12
var = 3
Var = 4
VAR  = 4

# Camel Case
# Each word, except the first, starts with a capital letter

myVariableName = "Camel Case"

#Pascal Case
#Each word starts with a capital letter:

MyVariableName = "Pascal Case"

# Snake Case
#Each word is separated by an underscore character

my_variable_name = "Snake Case"


# --- Assigning Multiple Variables

# Pyhton allows us to assign multiple values in one line

q , r ,s = "Python", 3.4 , 2
print(q,r,s)

q = r = s = "Python"
print(q,r,s)

# unpacking Lists

friuts = ["Apple", "Banana","Cherry"]
m,n,o= friuts

print(m,n,o)



# Output variables 

# Print Function print()

u = "Python"
v = "is"
w = 'Awesome'

print(u,v,w)
print(u + v + w) # + operator is used for same types

# comma is used for multiple datatypes


# Global Variables

# variables created outside of funtion
# can be used inside or outside a function
glb = "Awesome"

def myfunc():
    global glb
    glb = "Amazing"
    print("Python is " + glb)

myfunc()

print(glb)


