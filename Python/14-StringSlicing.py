# string slicing using [:]

x = "Python is a Popular Language"

# index start from 0
print("x[1] : " ,x[1]) #prints y


# prints string from start to index 10
print("x[:10] : " ,x[:10]) 

# prints from 2 to index 12
print("x[2:12] : " ,x[2:12]) 


# prints from 2 to index 12 taking 0 as last index: slice from end
print("x[-12:-5] : " ,x[-12: -2]) 

# prints from 12 slice to end
print("x[-12:] : " ,x[-12:]) 