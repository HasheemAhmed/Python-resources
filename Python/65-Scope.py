# Scope of variables in python

# A variable create inside a function only available for that function
def func():
    a = 10
    print(a)

# gives error print(a)
# Beacause we cannot acces a outside the scope

# Function inside a fucntion ca access the variable
# but Outer function can't access inner function variable

def outerfunc():
    x = 20

    def innerfunc():
        print(x)
        
    innerfunc()

outerfunc()

# Global Variable

# A variable created outside of a function considered as global
# can be used anywhere

var = 30

def myfunc():
    print(var)

myfunc()

# if there are two variable inside and outside a function 
# than they will treat as a seperate variable

x = 'Global Outside'

def Seperate():
    x = 'Local Inside'
    print(x)

Seperate() # print 2
print(x) # print 1


# if we want to use the x as a global than you can use global

y = 'Global Outside'

def globalfunc():
    global y
    y = 'Local Inside' # it changes the y as y is global
    print(y)

globalfunc()
print(y)


# if else loops doesnot have any scope

if True:
    Value = 100

print(Value) # print 100

for x in [1,2,3]:
    val = 200

print(val) # Print 200

# nonlocal can be used outside a function

def myfunc1():
  o = "Jane"
  def myfunc2():
    nonlocal o
    o = "hello"
  myfunc2()
  return o

print(myfunc1())

# nonlocal link the inside variable to ouside variable
# if ouside is no variable then nonlocal can't be used


# Difference 

# Global                       |    Non Local
# Access Anyehere              |   Access only inside the function
# For Ouside functions         |  For nested Function
# Can be used ouside           |  cannot be used outside the function
# function if declared inside  |  but in outer function