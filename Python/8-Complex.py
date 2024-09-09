# Complex datatype 

# j is used to represent complex numbers

cmp = 2 + 4j

# 2 is real part 4j is imaginary part

print("Type Of cmp : " ,type(cmp))

# accessing real and imaginary part

real = cmp.real
imaginary = cmp.imag

print("Type Of real : " ,type(real))
print("Type Of imaginary: " ,type(imaginary))

# Calculations

cmp1 = 2 + 2j
cmp2 = 3 + 3j
result = cmp1 + cmp2

print("Result is : " , result)

# rsult will be ( 5 + 5j)

# complex function
# default value is 0
# 1 parameter = real number
# 2 parameter = imaginary number

x  = complex() # 0 + 0j
y = complex(1) # 1 + 0j
z = complex(2, -3) # 2 - 3j

print(x,y,z)


