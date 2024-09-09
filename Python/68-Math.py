# math is a module through which we can perform mathoperations

# min() max() to find minimum and maximum value

x = min(5,6,7,8,9)
y = max(1,2,3)

print('Min : ',x , 'Max :',y)

#abs() - rmeoves  the negative sign

z = abs(-7.65)
print('Abs : ' , z)

#pow(value, power) to find the power

p = pow(4,3)
print('Power : ' , p)

# now its time to use math module

import math

#sqrt() - Square root of the value
s = math.sqrt(64)
print("SQRT : ", s)

# ceil() - floor()

c = math.ceil(1.3) # returns 2
f = math.floor(1.3) # returns 1

print('Ceil : ',c, 'Floor : ', f)

# math.pi

print('Math : ',f"{math.pi:.2f}")

# degrees() convert radians to angles in degrees

print('Degrees : ' , math.degrees(math.pi/4))

# there are a lot of functions in math module to perform operations on the math
