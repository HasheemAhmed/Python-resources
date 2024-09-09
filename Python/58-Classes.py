# Python is object oriented progrmamming

# Almost everything in python is object oriented programming

# class is used to create a class
# we called the attributes in python as property

# creating class

class MyClass:
    x = 5

# creating object of the MyClass

obj = MyClass()
print(obj.x)

# __init__() Function
# this function always executed when an object is created
# this function is like parameterized construtor

class AnotherClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

objA = AnotherClass('Python',24)

print(objA.name,objA.age)

# __str__() Function
# this function is used to return vaues if only object is called

print(objA) # print <__main__.AnotherClass object at 0x0000018CFB88B350>

# with __str__() function

class StringClass:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} -- {self.age}'
    
objs = StringClass('Javascript',23)
print(objs) # print Javascript -- 23


# class methods

class classmethods:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def printname(self):
        print('My name is',self.name, ' and age is',self.age)

objc = classmethods('C++', 20)
objc.printname()

objc1 = classmethods('Java',30)
objc1.name = 'Sql'
objc1.printname()

# del obj

# deletes the age property fro the objc1 object

del objc1.age
print(objc1.name)       


# del objc1

del objc1


# class

class Student:
    name = ''
    ids = 0

    def __init__(self,name,ids):
        self.name = name
        self.ids = ids

    def __str__(self):
        return f'{self.name} -- {self.ids}'
    
    def printstudent(self):
        print(self.name,self.ids)

objStu = Student()
objStu.name = 'Django'
objStu.ids = '1234'
objStu.printstudent()

# Note - If you use __init__() then you have to must pass parameters

