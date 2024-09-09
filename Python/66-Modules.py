# A module is a file containing a set of funcitons you want to include in your application

# write code and save it with .py extension
# myModule.py

import MyModules as M

M.greeting()

# you can also use variables describrd in thre module

[print(x) for x in M.lt]

print(M.Var)

# you can also access classes

obj = M.Student('Python', 5)
obj.printname()

obj.name = 'Javascript'
obj.rollno = 6
obj.printname()

# There are also the built in modules 

import platform
# platform is a module through which we can get the our system information

print(platform.system()) # print the OS Name - Windows
print(platform.machine()) # print the machine name - AMD64
print(platform.processor()) # print processor info - Intel64 Family 6 Model 78 Stepping 3, GenuineIntel
print(platform.architecture()) # print windows bit ('64bit', 'WindowsPE')
print(platform.platform()) # print Windows 10

# to see al =l the functions in module use dir()

func = dir(platform)
[print(x) for x in func]

# dir( cannot be used for user defined functions

# you can also import a part from module

from MyModules import lt

for x in lt:
    print(x) 

# When using import we dont have to write MyModule.lt , use direct lt
# we can also import a class from module

# Note - Module name always start from the alphabets

