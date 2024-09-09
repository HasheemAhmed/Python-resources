# A samll type of function

# lambda arguments : expressions

x = lambda a : a + 15
print(x(5))

x = lambda a , b: print(a + b)
x(5,5)

# lamda can have multiple expressions but only have one expression

# using the lambda funtion in another function

def myfunc(value):
    return lambda a : a * value

myvalue = myfunc(2) # myfunc retruns lambda a : a * 2
                    # so when we pass value to myvalue we actually pass to lambda function

print(myvalue(4))




fullname = lambda firstname,lastname: firstname + ' ' + lastname

print(fullname('Java', 'Script'))

# we can use the lamda function for the samll task or in the other function
