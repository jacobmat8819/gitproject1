class family:
    def __init__(self,grandfather,grandmother):
        self.grandfather = grandfather
        self.grandmother = grandmother 
        
    def __str__(self):
        return f"My Father is {self.grandfather} & my Mother is {self.grandmother}"

    def allfamily(self):
        print(self.grandfather,'&',self.grandmother)


family1 = family('Mathew Jacob','Mariamma Mathew')


class myfamily(family):
    def __init__(self,myself,mywife,myson):
        family.__init__(self, grandfather='Mathew Jacob',grandmother= 'Mariamma Mathew')
        self.myself = myself
        self.mywife = mywife
        self.myson = myson
    
    def __str__(self):
        return f"I am {self.myself} my Wife is {self.mywife} and my Son is {self.myson}"

    def myfamily_func(self):
        print(self.myself,self.mywife,self.myson)

myfamily1 = myfamily('Jacob','Shalini','Roshan')
print(family1)
print(myfamily1)


#-------------------------------------------------------


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"

    def dues(self):
        x = int(input("Enter your Emp ID:"))
        if x == 101:
            return f"Welcome {self.fname},your Dues is 20 Lakh Rupees"
        else:
            return f"Sorry i Dont Recognize you!!!"
            
class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname, lname)
        self.fname = fname
        self.lname = lname
        self.year = year
    
    def __str__(self):
        return f"{self.fname} \n{self.lname} \n{self.year}"

    def dues(self):
        x = int(input("Enter your Emp ID:"))
        if x == 201:
            return f"Welcome back {self.fname},your Dues is 20 Lakh Rupees,you have to pay by July {self.year}"
        else:
            return f"Sorry i Dont Recognize you!!!"

    
x = Person("Mike", "Olsen")
y = Student("Jacob","Mathew",2024)
print(x.dues())
print(y.dues())




