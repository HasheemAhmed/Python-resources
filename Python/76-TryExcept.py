# try except case in python

# there are four terms
# try     - Test a block for errors
# except  - Lets handle the error
# else    - Executes codes when there is no error
# finally - Executes code regardless of the try except

# Error handling

try:
    print(x)       # instead of giving error it runs the except case
except:
    print("An Error occured")

# you can also define many except case for different errors

try:
    print(x)
except NameError:
    print("Variable x is not defined") # print this as x is not defined
except:
    print("Something Else Wrong")


try:
    print(2/0)
except NameError:
    print("Variable x is not defined")
except:
    print("Something Else Wrong") # print this as there is an error


# else 

try:
    print("Assalam-o-Alaikum!")
except NameError:
    print("variable is not defined")
except:
    print("Something Went Wrong.")
else:
    print("Succesfully executed")  # print this as there is no error

# finally 

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# difference between else and finally

# finally               |  else
# runs always           | runs only if there is no error
#                       | don't runin case of error


# you can throw error by raise

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below 0")

# raise TypeError("if type does not match")