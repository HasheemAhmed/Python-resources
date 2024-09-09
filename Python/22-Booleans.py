# bool datatype

x = True
y = False

print(x,y)

x = 1
y = 0

print(x,y)

# Both can be used


x = "Hello"
y = ""

print(bool(x),bool(y))

# bool() function converts the datatype to bool

# all empty things are false and non empty things are true

x = ["Apple"]
y = list()

print(bool(x),bool(y))

if y:
    print("List has Items")
else:
    print("List is Empty")

# WE can also get bool values by comparison operators

print( 1 == 1) # true
print( 1 > 1) # false
print( 1 <= 1) # true
print( 1 != 1 and 1 == 1) # false
print( 1 != 1 or 1 == 1) # true
print( not 1 == 1) # false

# functions can also return bools 

def boolean(age):
    if age > 20:
        return True
    else:
        return False
    
print(boolean(21)) # true
print(boolean(19)) # false