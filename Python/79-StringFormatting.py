# string formatting in python

# adding f before string means formatting
txt = f"This is a format string."

# By using formatting you can use variables in string using {}

pop = 6.6
world = f"World population is {pop} Billion."
print(world)

# you can also use decimals length
pop = 6.678910
world = f"World population is {pop:.2f} Billion."
print(world)

# perform operations in the {}
value = 2
result = f"Sum of 2 + 2 is : {value + 2}"
print(result)

# use if else

pop = 7
world = f"Worlds population is {"increasing" if pop > 6 else "decreasing"}"
print(world)

# use functions

def square(num):
    return num * num

squ = f"Square of 2 is : {square(2)}"
print(squ)

# Modifiers

# :, use to put comma in thousands or :_ for undescore
price = 59000000
txt = f"The price is {price:,} dollars" # 59,000,000
print(txt)

# :< left align , :> right align , :^ center aligns
txt = f"The price is {price:<10} dollars" # left align within the given space
print(txt)

# := place signs at the leftmost position
txt = f"The price is {-price:=15} dollars" 
print(txt)

# :+ to indicate the signs eiter + or - , :- for negative only
txt = f"The price is {price:+} dollars" 
print(txt)

# :b to find binary values
txt = f"Binary number of 5 is {5:b}" 
print(txt)

# :d find decimal values 
txt = f"Decimal number of 0b101 is {0b101:d} or 0xe2 hexa is {0xe2:d}" 
print(txt)

# :o for octal and :x for hex like binary or decimal

# :.%
res = f"My percentage is {0.2545454:.2%}"
print(res)