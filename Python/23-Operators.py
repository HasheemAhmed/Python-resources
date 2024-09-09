# operators

# --- Arthimetic Operators

# ADD operator +

a = 20 + 5 + 6
print("Sum Is : ",a)

# Minus operator -
m = 40 - 20 - 30
print("Minus is : ", m ) 

# Multiply operator *

m = 2 * 2 * 2
print("Multiplication is :",m)

# Division Operatot /

d = 5/2
print("Division is : " , d)

# Note : d = 5/ 0 gives error for infinity

# Modulus operatot %

M = 5%2
print("Modulus is : ",M)

M = 2.123 % 1 # Extract the decimal part
print("Modulus By 1:", f"{M:.3f}") 

M = 3 % 1 # Gives zero
print("Modulus by 1 : " , M)

# Note : 5 % 0 Gives  error

# Exponentian Operator **

e = 5 ** 2
print("Exponent is : ", e)

# Floor Division operator //

f = 7 // 2 # gets the integer
print("Floor Division is : " , f)

# Altenative

f = int(7/2)
print("Alternative Division is : ",f)


# --- Assignment operators

# Equal operator

x = 3
y = "Python"

# += operator

x = 0
x += 3 # x = x + 3
print("x += 3 : ", x)

# -= operator

x = 0
x -= 3 # x = x - 3
print("x -= 3 : ", x)

# *= operator

x =  2
x *= 3 # x = x * 3
print("x *= 3 : ", x)

# /= operator

x = 7
x /= 3 # x = x / 3
print("x /= 3 : ", x)

# //= operator

x = 7
x //= 3 # x = x // 3
print("x //= 3 : ", x)

# **= operator

x = 7
x **= 2 # x = x ** 2
print("x **= 2 : ", x)

# := operator

print("P := 3 : " ,p := 3) # p = 3 and print(p)
print("Using p := 3 : ", p)


# --- Camparision operator

print( 1 == 1) # Equal 
print( 2 != 1) # Not Equal
print( 2 > 1) # Greater Than
print( 1 < 2) # Less Than
print( 1 <= 1) # Less Than And Equal Too
print( 2 >= 1) # Greater than and equal too

#  --- Logical operator

print( True and True) # And
print( False or True) # Or
print( not False) # Not

# --- Identity Operators

x = 2
y = 2
a = 5
z = "Python"
print( x is y) # Same value - true
print( x is a) # Different value - false
print( x is  z) # Different datatype - Fasle

print( x is not z) # x and z are not same - true

# " is " like " == "
# " is not " like " != "


# --- Bitwise Operator

# & AND Operator
print( "2 & 4 : " ,2 & 4)

""" AND
    0000 0010 = 2
    0000 0100 = 4
    ---------
    0000 0000 = 0"""

# | OR Operator
print("2 | 4 : " , 2 | 4)

""" OR
    0000 0010 = 2
    0000 0100 = 4
    ---------
    0000 0110 = 6"""

# ~ not Operator
print("~2 : ", ~4)

""" OR
    0000 0001 = 1
    ---------
    1111 1110 = -2"""

# ^ XOR Operator

print("2 ^ 4 : ", 2 ^ 4 )

""" XOR
    0000 0010 = 2
    0000 0100 = 4
    ---------
    0000 0110 = 6"""

# left shit

print("3 << 2 : ", 3 << 2 )

"""
The << operator inserts the specified number of 0's (in this case 2) 
from the right and let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 0000 0011
becomes
12 = 0000 1100"""

# right shift

print("8 >> 2 : ", 8 >> 2 )

"""
The >> operator moves each bit the specified number of times to the right.
Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 0000 1000
becomes
 2 = 0000 0010"""

# Python Membership Operator

x = "Apple"

print("App" in x)  # True -Check if the sequence is present in the String or not
print("APple" in x)  # False
print("Ban" not in x)  # True

# Note : Case Sensetive