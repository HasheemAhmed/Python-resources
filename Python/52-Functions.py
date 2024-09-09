# Functions

# 1 - Functions can be made by - def
# 2 - Functions can also take arguments
# 3 - Functoins can also return values
# 4 - Functions can be calles by name

# simple function

def myfunc():
    print('This is my func')

myfunc()

# Arguments function

def myfunc(name,age):
    print(f"{name} age is {age}")

myfunc('Python',2024)

# return values

def myfunc(Number):
    return f'My number is {Number}'

num = myfunc('0300 - xxxxxxx')
print(num)


# Multiple values arguments

def MultipleArguments(*arg):
    print(f'{arg[0]} is a {arg[1]} Lanhuage ')

MultipleArguments('Python','Good')


# Functions with key value pair

def keyValuePair(arg1,arg2,arg3):
    print(arg1,arg2,arg3,'are printed line by line')

keyValuePair(arg3 = 'Python',arg1='Java', arg2='Javascript')

# Function with the **Asterik

def DictionaryParameter(**name):
    print(name['fname'] , name['lname'], 'is my full name')

DictionaryParameter(fname = 'Java', lname = 'script')

# ** asterik means that we receive a dictionary
# * astril means that we receive a tuple 

# fix arguments value

def FixArgumentsValue(name = 'Python'):
    print(name + 'is the default argument')

FixArgumentsValue()

# passing a list of arguments

def PrintList(lt):
    for x in lt:
        print(x,end = ' ')

lt = ['Apple','Manogo','Banana']

PrintList(lt)

# Return Value

def ReturnValue(fname,Lname):
    fullname = fname + " " + Lname
    return fullname

print('\n' + ReturnValue('Java','Script'))

# pass statement

def PassStatement():
    pass

PassStatement() # doesnt happen , if you want to remain function empty


# Psoitional Arguments

# , /  in parameter used for positional arguments
# its doesnot accept key = value pair 
# it only accept values

def Positional(name,/):
    print(name + ' is a good Language')

 # Positional(name = 'Python') gives error
Positional("Python")

# keyword Only Arguments

# add * before the functions to get the Keyword only arguments

def Keyword(*,name):
    print(name + ' is a bad Language')

# Keyword('Python') gives error
Keyword(name = 'Python')

# Combine positional and keyword

def combine(a,b,/,*,c,d):
    print(a,b,'are Positional and',c,d,' are Keyword Arguments')

# arg before / are positional and after * are keywords

combine(1,2,c = 3,d = 4)

# Recursion

def recursion(value):
    if value == 0:
        return 1
    else:
        return value * recursion(value - 1)
    
print('factorial of 4 is : ',recursion(4))

