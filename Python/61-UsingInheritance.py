# we make classes to use inheritance

# Parent class

class Vehicle:

    # Constructor
    def __init__(self,VehType,RegNum,Model,Year):
        self.Vehtype = VehType
        self.RegNum = RegNum
        self.Model = Model
        self.Year = Year

    # setter Functions

    def setVehtype(self,VehType):
        self.Vehtype = VehType

    def setRegNum(self,RegNum):
        self.RegNum = RegNum

    def setModel(self,Model):
        self.Model = Model

    def setYear(self,Year):
        self.Year = Year

    # getter functions

    def getVehType(self):
        return self.Vehtype
    
    def getRegNum(self):
        return self.RegNum
    
    def getModel(self):
        return self.Model
    
    def getYear(self):
        return self.Year
    
    # if object is called

    def __str__(self):
        return "This is Vehicle class."
    

# Creating a car class inherited from the vehicle class

class Car(Vehicle):

    # Constructor
    def __init__(self,RegNum,Model,Year,CarType,Door):
        super().__init__('Car',RegNum,Model,Year)
        self.CarType = CarType
        self.Door = Door

    # setter Functions

    def setCarType(self,Type):
        self.CarType = Type

    def setDoor(self,door):
        self.Door = door
    
    # getter functions

    def getCarType(self):
        return self.CarType
    
    def getDoor(self):
        return self.Door
    
    # if object is called

    def __str__(self):
        return "This is Car class inherited from Vehicle class."
    
# creating a truck class inherited from the Vehicle class

class Truck(Vehicle):

    # Constructor
    def __init__(self,RegNum,Model,Year,TruckType,Wheels):
        super().__init__('Truck',RegNum,Model,Year)
        self.TruckType = TruckType
        self.Wheels = Wheels

    # setter Functions

    def setTruckType(self,TruckType):
        self.TruckType = TruckType
    
    def setWheels(self,Wheels):
        self.Wheels = Wheels

    # getter functions
    
    def getTruckType(self):
        return self.TruckType
    
    def getWheels(self):
        return self.Wheels
    
    # if object is called

    def __str__(self):
        return "This is Truck class inherited from Vehicle class."

    
# creating a sedan class inherited from car class

class Sedan(Car):

    # Constructor

    def __init__(self,RegNum,Model,Year,Color,Transmission):
        super().__init__(RegNum,Model,Year,'Sedan',4)

        self.Color = Color
        self.Transmission = Transmission
    
     # setter Functions

    def setColor(self,Color):
        self.Color = Color
    
    def setTransmission(self,Transmission):
        self.Transmission = Transmission

    # getter functions
    
    def getColor(self):
        return self.Color
    
    def getTransmission(self):
        return self.Transmission
    
    # if object is called

    def __str__(self):
        return "This is Sedan class inherited from Car class."
    
# creating an suv class inherited from the car Class

class SUV(Car):
    # Constructor

    def __init__(self,RegNum,Model,Year,Drive,Type):
        super().__init__(RegNum,Model,Year,'SUV',4)

        self.Type = Type
        self.Drive = Drive
    
     # setter Functions

    def setType(self,Type):
        self.Type = Type
    
    def setDrive(self,Drive):
        self.Drive = Drive

    # getter functions
    
    def getType(self):
        return self.Type
    
    def getDrive(self):
        return self.Drive
    
    # if object is called

    def __str__(self):
        return "This is SUV class inherited from Car class."


#                         Vehicle
#                            |
#              --------------------------
#              |                        |
#             Car                     Truck
#             |                               
#        ---------------
#       |              |
#     Sedan           Suv


sedan = list()
truck = list()
suv = list()

def showSedanDetails():
    for car in sedan:
        print('Vehicle : ', car.getVehType())
        print('Car : ', car.getCarType())
        print('Model : ', car.getModel())
        print('RegNum : ', car.getRegNum())
        print('Year : ', car.getYear())
        print('Color : ', car.getColor())
        print('Door : ', car.getDoor())
        print('Transmission : ', car.getTransmission())

def showSUVDetails():
    for car in suv:
        print('Vehicle : ', car.getVehType())
        print('Car : ', car.getCarType())
        print('Model : ', car.getModel())
        print('RegNum : ', car.getRegNum())
        print('Year : ', car.getYear())
        print('Drive : ', car.getDrive())
        print('Door : ', car.getDoor())
        print('Type : ', car.getType())


def showTruckDetails():
    for car in truck:
        print('Vehicle : ', car.getVehType())
        print('Truck : ', car.getTruckType())
        print('Model : ', car.getModel())
        print('RegNum : ', car.getRegNum())
        print('Year : ', car.getYear())
        print('Wheels : ', car.getWheels())

def addSedan():
    model = input('Enter the model : ')
    regnum = input('Enter the registration number : ')
    year = input('Enter the year : ')
    color = input('Enter the color : ')
    trans = input('Enter the tranmission type :')

    obj = Sedan(regnum,model,year,color,trans)
    sedan.append(obj)

def addSUV():
    model = input('Enter the model : ')
    regnum = input('Enter the registration number : ')
    year = input('Enter the year : ')
    drive = input('Enter the wheels drive : ')
    Type = input('Enter the SUV Type : ')

    obj = SUV(regnum,model,year,drive,Type)
    suv.append(obj)

def addTruck():
    model = input('Enter the model : ')
    regnum = input('Enter the registration number : ')
    year = input('Enter the year : ')
    trucktype = input('Enter the trucktype : ')
    wheels = input('Enter the wheels :')

    obj = Truck(regnum,model,year,trucktype,wheels)
    truck.append(obj)


def main():
    while(True):
        print('1. Add sedan.')
        print('2. Add Suv')
        print('3. Add truck')
        print('4. Show sedan Details')
        print('5. Show suv Details')
        print('6. Show truck Details')
        print('7. Exit')

        choice = int(input("Enter your choice :"))

        if choice == 1:
            addSedan()
        elif choice == 2:
            addSUV()
        elif choice == 3:
            addTruck()
        elif choice == 4:
            showSedanDetails()
        elif choice == 5:
            showSUVDetails()
        elif choice == 6:
            showTruckDetails()
        elif choice == 7:
            print('Program Exited Succesfully')
            break
        else:
            print('Invalid Input')


main()



