class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"your name is : {self.name} and your age is :{self.age}"

    def myfunc(self):
        print("Hello my name is:",self.name)
        print("My age is :",self.age)

p1 = person('Jacob',36)
p1.myfunc()

print(p1)
