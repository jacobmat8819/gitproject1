mytuple = ('Apple','Bananna','Cherry')
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


class mynumbers:
    def __init__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = mynumbers()
myiter = iter(myclass)


for x in myiter:
    print(x)