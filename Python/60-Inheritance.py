# Inheritance

# used to access the attributes and methods of the another class
# use parent child concept

# creating a paent class

class parent:

    def __init__(attr,fname,lname):
        attr.fname = fname
        attr.lname = lname

    def printname(self):
        print(f'{self.fname} {self.lname}')

objp = parent('Parent','Class')
objp.printname() # Parent Child Class

# creating a child class

class child(parent):
    pass

objc = child('Child','Class')
objc.printname() # print Child Class

# if we create __init__() in child class the parent class init will not be called

# creating __init__()  in child class

class child2(parent):

    def __init__(self,fname,lname):
        parent.__init__(self,fname,lname)
        # we can also use
        #super().__init__(fname,lname)

        # both are use to call the parent constrcutor

objc2 = child2('Child 2','Class')
objc2.printname()


# making the attributes in the child class

class child3(parent):
    
    def __init__(self,fname,lname,age):
        self.age = age
        super().__init__(fname,lname)

    def printinfo(self):
        parent.printname(self)
        # super.printname()
        print(f'age is {self.age}')

objc3 = child3('My',' Sql',50)
objc3.fname = 'Java'
objc3.lname = 'Script'
objc3.printinfo()

