class StudentInfo:

    # Constructor

    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.count = 0

    # print function

    def printinfo(self):
        print(f'Name : {self.name} Roll no : {self.rollno}')

    # you want to perform operation on rollno for every object created

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count < 10:
            self.count += 1
        else:
            raise StopIteration

totalStudents = StudentInfo(None,None)
myiter = iter(totalStudents)

obj1 = StudentInfo('Python',1)
next(myiter)
obj2 = StudentInfo('C',2)
next(myiter)
obj3 = StudentInfo('R',3)
next(myiter)

obj1.printinfo()
obj2.printinfo()
obj3.printinfo()

print(totalStudents.count)
