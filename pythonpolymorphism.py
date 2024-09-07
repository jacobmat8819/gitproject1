class vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")


class car(vehicle):
    #def __init__(self,brand,model):
     #   self.brand = brand
      #  self.model = model
    
    #def move(self):
     #   print("Drive")
    pass
class boat(vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class plane(vehicle):
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = car('Ford','Mustang')
boat1 = boat('Ibiza','Touring20')
plane1 = plane('Boeing','747')

car1.move()
boat1.move()
plane1.move()




for x in (car1,boat1,plane1):
    x.move()