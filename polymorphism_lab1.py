class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()


  #---------------------------------------------------------

class Mammals:
    def __init__(self,species,habitat):
        self.species = species
        self.habitat = habitat
    
    def properties(self):
        return f"The {self.species} species give birth to babies and the live {self.habitat}"

class reptiles:
    def __init__(self,species,habitat):
        self.species = species
        self.habitat = habitat
    
    def properties(self):
        return f"The {self.species} Lay Eggs and the live in the {self.habitat}"

class seacreatures:
    def __init__(self,species,habitat):
        self.species = species
        self.habitat = habitat
    
    def properties(self):
        return f"The {self.species} give birth to babies and they live under {self.habitat}"


x = Mammals('dogs','worldwide')
y = reptiles('snakes','whole world except in New Zealand')
z = seacreatures('whale','Water')

for i in (x,y,z):
    print(i.properties())