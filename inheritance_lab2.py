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

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname, lname)
        self.fname = fname
        self.lname = lname
        self.year = year
    
    def __str__(self):
        return f"{self.fname} \n{self.lname} \n{self.year}"

x = Person("Mike", "Olsen")
y = Student("Jacob","Mathew",2024)
print(x)
print(y)
print(y.lname)


