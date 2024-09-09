# Polymorphism means same forms but different functions

# same name different functions

# for example len() used to find any length list,dict,string

# Polymorphism is used in classes methods with sam emethod name

class Vehicle:

    def __init__(self,Model,Brand):
        self.Model = Model
        self.Brand = Brand

    def move(self):
        print('Move!')

class car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print('Sail!')


objcar = car('Camry',"Toyota")
objboat = Boat('Ibiza',"Touring 20")

for x in (objcar,objboat):
    print(x.Brand,x.Model)
    x.move()

# this is the benefit of the polymorphism

