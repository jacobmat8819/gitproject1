class person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname,self.lastname)
    
x = person('Jacob',36)
x.printname()

class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year
        self.firstname = fname
        self.lastname = lname
    
    def welcome(self):
        print("Welcome",self.firstname,self.lastname,'to the Class of',self.graduationyear)


y = student('Abraham','Mathew',2024)
y.welcome()



