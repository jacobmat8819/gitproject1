class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()



class family:
    def __init__(self,Father,Mother):
        self.Father = Father
        self.Mother = Mother

    def myfamily(abc):
        print(f"{abc.Father} \n{abc.Mother}")

    def __str__(self):
        return f"{self.Father} & {self.Mother}"

instance1 = family('Jacob','Shalini')
instance2 = family('Anumpam','Sakshi')
instance1.myfamily()



#-----Child class uses Parent Class

class newfamily(family):
    def __init__(self,city,pincode):
        self.city = city
        self.pincode = pincode

    def newfamily_func(add):
        print(add.city,add.pincode)

    def __str__(self):
        return f"{self.city} {self.pincode}" 

inst3 = newfamily('Bhilai',490001)
print(instance1,"address is",inst3)


