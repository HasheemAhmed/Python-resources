# Making a class for student info
# we can use any word instead of self
class Student:

    # Constructor 
    def __init__(self): 
        self.name = None
        self.Id  = None # i want to initialize it latter

    # setter methods
    def setName(self,name):
        self.name = name

    def setId(self,Id):
        self.Id = Id

    # getter methods 
    def getName(self):
        return self.name
    
    def getId(self):
        return self.Id
    
    # if only object is called than it used to print some string like print(obj)
    def __str__(self):
        return f'Name : {self.name}   Id : {self.Id}'
    
obj1 = Student()
obj1.setId(123)
obj1.setName('Python')
print('Name :',obj1.getName(), 'Id : ',obj1.getId())




    